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
"""

import numpy as np
import pandas as pd

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
) -> pd.DataFrame:
    """
    Identify road segments with insufficient charging coverage.

    For each road segment, find the nearest existing fast charger (≥50 kW).
    If that distance exceeds the segment's applicable AFIR spacing threshold,
    the segment is flagged as a coverage gap.

    Parameters
    ----------
    road_segments_df : pd.DataFrame or gpd.GeoDataFrame
        Interurban road segments. Must have: 'Carretera', 'is_tent', optionally
        'tent_tier' and 'geometry'. Lat/lon centroid columns used if no geometry.
    existing_stations_df : pd.DataFrame
        NAP charging stations. Must have: 'latitude', 'longitude', 'max_power_kw'.
    spacing_km : float, optional
        Override spacing threshold for all segments. If None, uses tiered AFIR
        thresholds (60 / 100 / 120 km) per segment.

    Returns
    -------
    pd.DataFrame
        Subset of road_segments_df rows that are coverage gaps, with an added
        'gap_spacing_threshold_km' column indicating the applicable threshold.
    """
    from sklearn.neighbors import BallTree

    # Filter to highway-grade fast chargers only (C4)
    fast = existing_stations_df[
        existing_stations_df['max_power_kw'] >= MIN_EXISTING_CHARGER_POWER_KW
    ].copy()

    if len(fast) == 0:
        road_segments_df = road_segments_df.copy()
        road_segments_df['gap_spacing_threshold_km'] = road_segments_df.apply(
            _get_spacing_threshold, axis=1
        )
        return road_segments_df

    # Build BallTree on fast charger coordinates
    charger_coords = np.radians(fast[['latitude', 'longitude']].values)
    tree = BallTree(charger_coords, metric='haversine')

    # Compute segment midpoints
    seg = road_segments_df.copy()

    if hasattr(seg, 'geometry') and seg.geometry is not None:
        # GeoDataFrame: reproject to UTM for centroid accuracy, then back
        try:
            seg_utm = seg.to_crs('EPSG:25830')
            centroids = seg_utm.geometry.centroid.to_crs('EPSG:4326')
            seg['_mid_lat'] = centroids.y
            seg['_mid_lon'] = centroids.x
        except Exception:
            seg['_mid_lat'] = seg.geometry.centroid.y
            seg['_mid_lon'] = seg.geometry.centroid.x
    else:
        # DataFrame without geometry: attempt lat/lon columns
        seg['_mid_lat'] = seg.get('latitude', seg.get('lat', None))
        seg['_mid_lon'] = seg.get('longitude', seg.get('lon', None))

    # Drop rows with missing midpoints
    valid_mask = seg['_mid_lat'].notna() & seg['_mid_lon'].notna()
    seg_valid = seg[valid_mask].copy()

    seg_coords = np.radians(seg_valid[['_mid_lat', '_mid_lon']].values)
    dist_rad, _ = tree.query(seg_coords, k=1)
    dist_km = dist_rad[:, 0] * 6371  # Earth radius in km

    seg_valid['_nearest_charger_km'] = dist_km
    seg_valid['gap_spacing_threshold_km'] = seg_valid.apply(_get_spacing_threshold, axis=1)

    if spacing_km is not None:
        seg_valid['gap_spacing_threshold_km'] = spacing_km

    gap_mask = seg_valid['_nearest_charger_km'] > seg_valid['gap_spacing_threshold_km']
    gaps = seg_valid[gap_mask].drop(columns=['_mid_lat', '_mid_lon', '_nearest_charger_km'])

    return gaps.reset_index(drop=True)


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

    # --- Compute midpoints for gap segments ---
    gaps = gap_segments_df.copy()
    if hasattr(gaps, 'geometry') and gaps.geometry is not None:
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
            length_km = float(row.get('length_km', row.get('Longitud', 5000)) or 5000)
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

        # Mark all gap segments within spacing_thresh of this station as covered.
        # Correct radius is spacing_thresh (not /2): a station at point A covers
        # all segments within the AFIR threshold distance, so any gap segment
        # whose midpoint is ≤ spacing_thresh km from A is now AFIR-compliant
        # (it has a station within the legally mandated spacing).
        # Using spacing_thresh/2 was too conservative and over-placed stations.
        station_coord = np.radians([[cand_lat, cand_lon]])
        dists_rad, _ = BallTree(gap_mid_coords, metric='haversine').query(
            station_coord, k=len(gaps)
        )
        dists_km = dists_rad[0] * 6371
        close_positions = np.where(dists_km <= spacing_thresh)[0]
        covered_indices.update(gaps.index[close_positions].tolist())
        # Always mark the selected segment itself
        covered_indices.add(best_idx)

    return pd.DataFrame(stations)
