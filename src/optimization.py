"""
Network optimization for EV charging station placement.

Objective: place the minimum number of new stations such that no gap on any
interurban road segment exceeds the AFIR-mandated spacing threshold:
  - TEN-T Core:          60 km  (legal requirement)
  - TEN-T Comprehensive: 100 km
  - General interurban:  120 km

Algorithm: sequential greedy set-cover — each candidate location is scored by
demand × coverage_km. The highest-scoring uncovered candidate is selected,
covered segments are marked, and residual demand is recalculated until all
AFIR gaps are closed.

Distance methodology: all coverage gap detection and station placement use
road-following (linear referencing) distances, not birds-eye haversine.
AFIR spacing rules are defined along the route, so coverage must be measured
the same way.
"""

import numpy as np
import pandas as pd
import geopandas as gpd
from shapely.ops import linemerge, unary_union, substring

from src.constants import (
    MAX_STATION_SPACING_KM,
    MAX_STATION_SPACING_TENT_CORE_KM,
    MAX_STATION_SPACING_TENT_COMP_KM,
    CHARGING_PROBABILITY,
    AVG_CHARGE_DURATION_HOURS,
    EFFECTIVE_OPERATING_HOURS,
    MIN_CHARGERS_TENT,
    MIN_CHARGERS_STANDARD,
    MAX_CHARGERS_HIGH_TRAFFIC,
    MAX_CHARGERS_STANDARD,
    HIGH_TRAFFIC_IMD_THRESHOLD,
    MIN_EXISTING_CHARGER_POWER_KW,
)


def calculate_chargers_needed(
    daily_ev_traffic: float,
    charging_probability: float = CHARGING_PROBABILITY,
    avg_charge_hours: float = AVG_CHARGE_DURATION_HOURS,
    operating_hours: float = EFFECTIVE_OPERATING_HOURS,
    is_tent: bool = False,
    imd_total: float = 0.0,
) -> int:
    """
    Calculate number of 150 kW chargers needed for a given daily BEV flow.

    Parameters
    ----------
    daily_ev_traffic : float
        Daily BEV count passing through the station location (already scaled
        from IMD × EV_penetration × BEV_fraction by the caller).
    charging_probability : float
        Fraction of passing BEVs that stop to charge (default 0.12, B1).
    avg_charge_hours : float
        Average session duration in hours (default 0.37 = 22 min, B2).
    operating_hours : float
        Effective daily availability (default 20 hrs, B3).
    is_tent : bool
        True if location is on a TEN-T corridor (enforces 4-charger minimum).
    imd_total : float
        Raw IMD total used to select high-traffic vs standard charger cap.

    Returns
    -------
    int
        Number of chargers, clamped to [min_chargers, max_chargers].
    """
    daily_demand_hours = daily_ev_traffic * charging_probability * avg_charge_hours
    n_chargers = int(np.ceil(daily_demand_hours / operating_hours))

    min_c = MIN_CHARGERS_TENT if is_tent else MIN_CHARGERS_STANDARD
    max_c = (
        MAX_CHARGERS_HIGH_TRAFFIC
        if imd_total > HIGH_TRAFFIC_IMD_THRESHOLD
        else MAX_CHARGERS_STANDARD
    )
    return max(min_c, min(n_chargers, max_c))


def _get_spacing_threshold(row) -> float:
    """Return the applicable AFIR spacing threshold (km) for a road segment row."""
    tent_tier = str(row.get('tent_tier', '')).lower()
    is_tent = bool(row.get('is_tent', False))
    if tent_tier == 'core' or (is_tent and tent_tier not in ('comprehensive', 'none', '')):
        return MAX_STATION_SPACING_TENT_CORE_KM    # 60 km
    if tent_tier == 'comprehensive':
        return MAX_STATION_SPACING_TENT_COMP_KM    # 100 km
    return MAX_STATION_SPACING_KM                  # 120 km


def _segment_midpoint(row) -> tuple:
    """Return (lat, lon) midpoint of a road segment from geometry or centroid."""
    geom = row.get('geometry')
    if geom is not None:
        pt = geom.interpolate(0.5, normalized=True)
        return pt.y, pt.x
    # Fall back to None — caller must handle
    return None, None


def compute_coverage_gaps(
    road_segments_df,
    existing_stations_df,
    spacing_km: float = None,
) -> 'gpd.GeoDataFrame':
    """
    Identify coverage gaps on interurban routes using road-following linear referencing.

    For each route (Carretera), merges all segments into a continuous line, projects
    fast chargers (≥50 kW) onto the line using shapely linear referencing (.project()),
    walks consecutive charger positions, and flags any stretch longer than the AFIR
    spacing threshold as a coverage gap. Gaps are measured *along the route*, not as
    birds-eye distances — this is the methodologically correct interpretation of AFIR.

    Parameters
    ----------
    road_segments_df : gpd.GeoDataFrame
        Interurban road segments with geometry. Must have: 'Carretera', 'is_tent'.
        Optional: 'tent_tier', 'segment_id'.
    existing_stations_df : pd.DataFrame
        NAP charging stations. Must have: 'latitude', 'longitude', 'max_power_kw'.
    spacing_km : float, optional
        Override AFIR threshold for all routes. If None, uses tiered thresholds
        (60 / 100 / 120 km) per route from is_tent / tent_tier.

    Returns
    -------
    gpd.GeoDataFrame
        One row per contiguous uncovered stretch with columns:
        Carretera, gap_start_km, gap_end_km, gap_length_km,
        gap_mid_lat, gap_mid_lon, is_tent, tent_tier,
        gap_spacing_threshold_km, n_chargers_on_route,
        segment_id (representative nearest segment), geometry (EPSG:4326).
    """
    _EMPTY_COLS = [
        'Carretera', 'gap_start_km', 'gap_end_km', 'gap_length_km',
        'gap_mid_lat', 'gap_mid_lon', 'is_tent', 'tent_tier',
        'gap_spacing_threshold_km', 'n_chargers_on_route', 'segment_id', 'geometry',
    ]

    if not hasattr(road_segments_df, 'geometry') or road_segments_df is None:
        return gpd.GeoDataFrame(columns=_EMPTY_COLS, crs='EPSG:4326')

    # Filter to fast chargers only (C4: ≥50 kW count toward AFIR coverage)
    fast = existing_stations_df[
        existing_stations_df['max_power_kw'] >= MIN_EXISTING_CHARGER_POWER_KW
    ].copy()

    # Reproject roads to UTM for accurate metric distance measurements
    roads_utm = road_segments_df.to_crs('EPSG:25830')

    # Build fast charger GeoDataFrame in UTM
    if len(fast) > 0:
        fast_gdf = gpd.GeoDataFrame(
            fast,
            geometry=gpd.points_from_xy(fast['longitude'], fast['latitude']),
            crs='EPSG:4326',
        ).to_crs('EPSG:25830').reset_index(drop=True)
    else:
        fast_gdf = gpd.GeoDataFrame(geometry=gpd.array.GeometryArray([]), crs='EPSG:25830')

    gap_records = []

    for carretera, road_group in roads_utm.groupby('Carretera'):
        # Merge all segments of this route into one continuous line
        try:
            merged = linemerge(unary_union(road_group.geometry.values))
        except Exception:
            merged = unary_union(road_group.geometry.values)

        # If the route is discontinuous, take the longest contiguous piece
        if merged.geom_type == 'MultiLineString':
            merged = max(merged.geoms, key=lambda g: g.length)

        route_length_km = merged.length / 1000
        if route_length_km < 5:
            continue  # skip very short routes

        # Determine AFIR tier for this route
        is_tent = bool(road_group['is_tent'].any())
        if 'tent_tier' in road_group.columns:
            tier_vals = road_group['tent_tier'].fillna('none').astype(str).str.lower()
            if (tier_vals == 'core').any():
                tent_tier = 'core'
            elif (tier_vals == 'comprehensive').any():
                tent_tier = 'comprehensive'
            elif is_tent:
                tent_tier = 'core'  # default TEN-T to core when tier unknown
            else:
                tent_tier = 'none'
        else:
            tent_tier = 'core' if is_tent else 'none'

        if spacing_km is not None:
            threshold_km = spacing_km
        elif tent_tier == 'core':
            threshold_km = MAX_STATION_SPACING_TENT_CORE_KM
        elif tent_tier == 'comprehensive':
            threshold_km = MAX_STATION_SPACING_TENT_COMP_KM
        else:
            threshold_km = MAX_STATION_SPACING_KM
        threshold_m = threshold_km * 1000

        # Find fast chargers within 2 km of this route
        if len(fast_gdf) > 0:
            route_buffer = merged.buffer(2000)
            nearby = fast_gdf[fast_gdf.geometry.within(route_buffer)].copy()
        else:
            nearby = fast_gdf.iloc[:0].copy()

        if len(nearby) == 0:
            positions = [0.0, merged.length]
        else:
            # Project each charger onto the route line (linear referencing)
            nearby = nearby.copy()
            nearby['along_m'] = nearby.geometry.apply(lambda p: merged.project(p))
            nearby = nearby.sort_values('along_m').reset_index(drop=True)
            positions = [0.0] + nearby['along_m'].tolist() + [merged.length]

        n_chargers = len(nearby)

        for i in range(len(positions) - 1):
            gap_m = positions[i + 1] - positions[i]
            if gap_m > threshold_m:
                try:
                    gap_geom = substring(merged, positions[i], positions[i + 1])
                except Exception:
                    gap_geom = None

                # Midpoint at 50% along the gap geometry (road-following midpoint)
                if gap_geom is not None and not gap_geom.is_empty:
                    mid_pt_utm = gap_geom.interpolate(0.5, normalized=True)
                    mid_wgs = gpd.GeoDataFrame(
                        geometry=[mid_pt_utm], crs='EPSG:25830'
                    ).to_crs('EPSG:4326')
                    gap_mid_lon = float(mid_wgs.geometry.iloc[0].x)
                    gap_mid_lat = float(mid_wgs.geometry.iloc[0].y)
                else:
                    gap_mid_lat = None
                    gap_mid_lon = None

                gap_records.append({
                    'Carretera': carretera,
                    'gap_start_km': round(positions[i] / 1000, 2),
                    'gap_end_km': round(positions[i + 1] / 1000, 2),
                    'gap_length_km': round(gap_m / 1000, 2),
                    'gap_mid_lat': gap_mid_lat,
                    'gap_mid_lon': gap_mid_lon,
                    'is_tent': is_tent,
                    'tent_tier': tent_tier,
                    'gap_spacing_threshold_km': threshold_km,
                    'n_chargers_on_route': n_chargers,
                    'segment_id': None,  # filled below
                    'geometry': gap_geom,
                })

    if len(gap_records) == 0:
        return gpd.GeoDataFrame(columns=_EMPTY_COLS, crs='EPSG:4326')

    # Build GeoDataFrame in UTM, convert gap geometries to WGS84
    gaps_gdf = gpd.GeoDataFrame(
        gap_records, geometry='geometry', crs='EPSG:25830'
    ).to_crs('EPSG:4326')

    # Attach representative segment_id (nearest original segment to each gap midpoint)
    valid_mid = gaps_gdf['gap_mid_lat'].notna() & gaps_gdf['gap_mid_lon'].notna()
    if valid_mid.any() and 'segment_id' in road_segments_df.columns:
        mid_pts = gpd.GeoDataFrame(
            geometry=gpd.points_from_xy(
                gaps_gdf.loc[valid_mid, 'gap_mid_lon'],
                gaps_gdf.loc[valid_mid, 'gap_mid_lat'],
            ),
            crs='EPSG:4326',
            index=gaps_gdf.index[valid_mid],
        ).to_crs('EPSG:25830')

        roads_for_join = road_segments_df[['segment_id', 'geometry']].to_crs('EPSG:25830')
        joined = gpd.sjoin_nearest(
            mid_pts[['geometry']],
            roads_for_join[['segment_id', 'geometry']],
            how='left',
        ).drop_duplicates(keep='first')
        gaps_gdf.loc[valid_mid, 'segment_id'] = joined['segment_id'].values

    return gaps_gdf.reset_index(drop=True)


def place_stations_greedy(
    gap_segments_df: pd.DataFrame,
    demand_df: pd.DataFrame,
    service_areas_gdf=None,
) -> pd.DataFrame:
    """
    Sequential greedy station placement.

    Algorithm (from the sequential investment methodology):
      1. For each uncovered gap segment, generate a candidate location at its midpoint
         (or nearest service area if available — preferred for land/utilities).
      2. Score each candidate: V_i = n_chargers_needed × gap_length_km
         (maximises demand served per station placed).
      3. Select highest-score candidate, mark all segments within its spacing
         threshold as covered, update residual gaps.
      4. Repeat until no gaps remain.

    Parameters
    ----------
    gap_segments_df : pd.DataFrame
        Output of compute_coverage_gaps(). Must have: 'Carretera', 'is_tent',
        'gap_spacing_threshold_km', 'geometry' or midpoint lat/lon,
        and 'length_km'.
    demand_df : pd.DataFrame
        Output of NB06 demand_per_segment.csv. Must have: 'segment_id',
        'n_chargers_needed', 'daily_bev_traffic_2027'.
    service_areas_gdf : gpd.GeoDataFrame, optional
        Motorway service areas from service_areas_clean.geojson. When a gap
        midpoint is near a service area (<5 km), the service area coordinates
        are preferred as the candidate location.

    Returns
    -------
    pd.DataFrame
        Proposed stations with columns:
        location_id, latitude, longitude, route_segment, n_chargers_proposed
    """
    from sklearn.neighbors import BallTree

    if len(gap_segments_df) == 0:
        return pd.DataFrame(columns=[
            'location_id', 'latitude', 'longitude',
            'route_segment', 'n_chargers_proposed'
        ])

    # --- Build demand lookup ---
    demand_lookup = {}
    if demand_df is not None and len(demand_df) > 0:
        for _, row in demand_df.iterrows():
            sid = row.get('segment_id')
            if sid is not None:
                demand_lookup[sid] = {
                    'n_chargers': int(row.get('n_chargers_needed', MIN_CHARGERS_STANDARD)),
                    'bev_flow': float(row.get('daily_bev_traffic_2027', 0)),
                    'is_tent': bool(row.get('is_tent', False)),
                }

    # --- Use pre-computed road-following midpoints from compute_coverage_gaps() ---
    gaps = gap_segments_df.copy()
    if 'gap_mid_lat' in gaps.columns and 'gap_mid_lon' in gaps.columns:
        gaps['_mid_lat'] = gaps['gap_mid_lat']
        gaps['_mid_lon'] = gaps['gap_mid_lon']
    elif hasattr(gaps, 'geometry') and gaps.geometry is not None:
        # Fallback for legacy input without pre-computed midpoints
        try:
            gaps_utm = gaps.to_crs('EPSG:25830')
            centroids = gaps_utm.geometry.centroid.to_crs('EPSG:4326')
            gaps['_mid_lat'] = centroids.y
            gaps['_mid_lon'] = centroids.x
        except Exception:
            gaps['_mid_lat'] = gaps.geometry.centroid.y
            gaps['_mid_lon'] = gaps.geometry.centroid.x
    else:
        gaps['_mid_lat'] = gaps.get('latitude', None)
        gaps['_mid_lon'] = gaps.get('longitude', None)

    gaps = gaps[gaps['_mid_lat'].notna() & gaps['_mid_lon'].notna()].copy()

    # --- Build service area BallTree (optional, for preferred siting) ---
    sa_tree = None
    sa_coords_deg = None
    if service_areas_gdf is not None and len(service_areas_gdf) > 0:
        sa_pts = service_areas_gdf.copy()
        if hasattr(sa_pts, 'geometry'):
            sa_pts['_sa_lat'] = sa_pts.geometry.centroid.y
            sa_pts['_sa_lon'] = sa_pts.geometry.centroid.x
        sa_pts = sa_pts[sa_pts['_sa_lat'].notna()].reset_index(drop=True)
        if len(sa_pts) > 0:
            sa_coords_deg = sa_pts[['_sa_lat', '_sa_lon']].values
            sa_tree = BallTree(np.radians(sa_coords_deg), metric='haversine')

    # --- Greedy sequential selection ---
    covered_indices = set()
    stations = []
    loc_counter = 1

    # Build a BallTree of gap segment midpoints for coverage radius checks
    gap_mid_coords = np.radians(gaps[['_mid_lat', '_mid_lon']].values)

    while True:
        remaining_mask = ~gaps.index.isin(covered_indices)
        remaining = gaps[remaining_mask]
        if len(remaining) == 0:
            break

        # Score remaining candidates
        scores = []
        for i, (idx, row) in enumerate(remaining.iterrows()):
            seg_id = row.get('segment_id', idx)
            demand_info = demand_lookup.get(seg_id, {})
            n_chargers = demand_info.get('n_chargers', MIN_CHARGERS_STANDARD)
            is_tent = bool(row.get('is_tent', demand_info.get('is_tent', False)))
            if is_tent:
                n_chargers = max(n_chargers, MIN_CHARGERS_TENT)
            length_km = float(
                row.get('gap_length_km', row.get('length_km', row.get('Longitud', 5000))) or 5000
            )
            if length_km > 1000:
                length_km = length_km / 1000  # Convert m to km if needed
            score = n_chargers * length_km
            scores.append((score, idx, row, n_chargers))

        # Select highest-score candidate
        scores.sort(key=lambda x: x[0], reverse=True)
        _, best_idx, best_row, best_n_chargers = scores[0]

        # Determine station coordinates
        cand_lat = best_row['_mid_lat']
        cand_lon = best_row['_mid_lon']
        spacing_thresh = float(best_row.get('gap_spacing_threshold_km', MAX_STATION_SPACING_KM))

        # Prefer nearby service area if within 5 km
        if sa_tree is not None:
            query = np.radians([[cand_lat, cand_lon]])
            dist_rad, sa_idx = sa_tree.query(query, k=1)
            dist_km = dist_rad[0][0] * 6371
            if dist_km <= 5.0:
                sa_row = sa_coords_deg[sa_idx[0][0]]
                cand_lat, cand_lon = sa_row[0], sa_row[1]

        road_name = str(best_row.get('Carretera', best_row.get('route_segment', 'Unknown')))

        stations.append({
            'location_id': f'STA_{loc_counter:04d}',
            'latitude': round(cand_lat, 6),
            'longitude': round(cand_lon, 6),
            'route_segment': road_name,
            'n_chargers_proposed': best_n_chargers,
        })
        loc_counter += 1

        # --- Road-following coverage marking ---
        # Primary: along-route distance for gaps on the same Carretera.
        # A station at position P covers all gap stretches [start, end] on
        # the same road where any part of the gap is within spacing_thresh km.
        if 'gap_start_km' in gaps.columns and 'gap_end_km' in gaps.columns:
            station_pos_km = (
                float(best_row.get('gap_start_km', 0))
                + float(best_row.get('gap_end_km', 0))
            ) / 2
            same_route = gaps['Carretera'] == road_name
            within_reach = (
                same_route
                & (gaps['gap_start_km'] < station_pos_km + spacing_thresh)
                & (gaps['gap_end_km'] > station_pos_km - spacing_thresh)
            )
            covered_indices.update(gaps.index[within_reach].tolist())

        # Secondary: 2 km haversine proximity for cross-route coverage at
        # road intersections (a single interchange may serve two routes).
        station_coord = np.radians([[cand_lat, cand_lon]])
        dists_rad, _ = BallTree(gap_mid_coords, metric='haversine').query(
            station_coord, k=len(gaps)
        )
        dists_km = dists_rad[0] * 6371
        covered_indices.update(gaps.index[np.where(dists_km <= 2.0)[0]].tolist())

        # Always mark the selected gap itself
        covered_indices.add(best_idx)

    return pd.DataFrame(stations)
