"""
Spatial operations: nearest substation, point-on-road, haversine distance.
"""

import numpy as np
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point

from src.constants import (
    MAX_SUBSTATION_SEARCH_RADIUS_KM,
    SUBSTATION_DIST_OPTIMAL_KM,
    SUBSTATION_DIST_FEASIBLE_KM,
    SUBSTATION_DIST_HIGH_COST_KM,
    DEFAULT_STATUS_IF_NO_SUBSTATION,
)


def haversine_distance(lat1, lon1, lat2, lon2):
    """Calculate haversine distance in km between two lat/lon points."""
    R = 6371  # Earth radius in km
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
    return 2 * R * np.arcsin(np.sqrt(a))


def find_nearest_substation(
    station_lat: float,
    station_lon: float,
    substations_df: pd.DataFrame,
    max_radius_km: float = MAX_SUBSTATION_SEARCH_RADIUS_KM,
) -> dict:
    """
    Find nearest electricity substation to a proposed charging station.

    Uses sklearn BallTree with haversine metric for O(log n) lookups,
    consistent with the G3 spatial matching assumption.

    NOTE: haversine (straight-line) distance is intentional here. Grid cable
    connections do not follow road paths — they run via overhead lines or
    underground cables that can cross any terrain. Road-following distance
    would be incorrect for grid infrastructure matching.

    Connection distance tiers (D4):
      'optimal'    : ≤5 km  — direct LV/MV connection
      'feasible'   : 5–15 km — MV line extension (~€100–300K CAPEX)
      'high_cost'  : 15–25 km — requires feasibility study
      (>25 km classified as Congested by default, per D5)

    Parameters
    ----------
    station_lat, station_lon : float
        WGS84 coordinates of the proposed charging station.
    substations_df : pd.DataFrame
        Grid capacity data. Must have: 'latitude', 'longitude',
        'available_capacity_mw', 'distributor_network'.
        Optional: 'substation_id' or 'substation_name'.
    max_radius_km : float
        Maximum matching radius. Default 25 km (D4).

    Returns
    -------
    dict or None
        Keys: substation_id, distance_km, available_capacity_mw,
              distributor_network, connection_tier.
        Returns None if no substation found within max_radius_km.
    """
    from sklearn.neighbors import BallTree

    df = substations_df.dropna(subset=['latitude', 'longitude']).reset_index(drop=True)
    if len(df) == 0:
        return None

    coords = np.radians(df[['latitude', 'longitude']].values)
    tree = BallTree(coords, metric='haversine')

    query = np.radians([[station_lat, station_lon]])
    dist_rad, idx = tree.query(query, k=1)
    dist_km = float(dist_rad[0][0]) * 6371

    if dist_km > max_radius_km:
        return None

    row = df.iloc[int(idx[0][0])]

    # Determine substation identifier
    if 'substation_id' in df.columns and pd.notna(row.get('substation_id')):
        sub_id = str(row['substation_id'])
    elif 'substation_name' in df.columns and pd.notna(row.get('substation_name')):
        sub_id = str(row['substation_name'])
    else:
        sub_id = str(int(idx[0][0]))

    # Assign connection tier (D4)
    if dist_km <= SUBSTATION_DIST_OPTIMAL_KM:
        tier = 'optimal'
    elif dist_km <= SUBSTATION_DIST_FEASIBLE_KM:
        tier = 'feasible'
    else:
        tier = 'high_cost'

    return {
        'substation_id': sub_id,
        'distance_km': round(dist_km, 3),
        'available_capacity_mw': float(row.get('available_capacity_mw', 0) or 0),
        'distributor_network': str(row.get('distributor_network', 'Unknown')),
        'connection_tier': tier,
    }


def snap_point_to_road(
    lat: float,
    lon: float,
    roads_gdf: gpd.GeoDataFrame,
    max_distance_km: float = 2.0,
):
    """
    Snap a lat/lon point to the nearest interurban road segment.

    Reprojects to UTM EPSG:25830 for metric distance accuracy, then finds
    the nearest road geometry. Returns None if no road is within max_distance_km.

    Parameters
    ----------
    lat, lon : float
        WGS84 coordinates of the point to snap.
    roads_gdf : gpd.GeoDataFrame
        Interurban road network in EPSG:4326.
    max_distance_km : float
        Maximum snap distance in km. Default 2 km (C4 rule).

    Returns
    -------
    pandas.Series or None
        The nearest road segment row, or None if beyond max_distance_km.
    """
    if roads_gdf is None or len(roads_gdf) == 0:
        return None

    point_wgs84 = gpd.GeoDataFrame(
        geometry=[Point(lon, lat)], crs='EPSG:4326'
    )
    point_utm = point_wgs84.to_crs('EPSG:25830').geometry.iloc[0]

    roads_utm = roads_gdf.to_crs('EPSG:25830')
    distances = roads_utm.geometry.distance(point_utm)
    min_idx = distances.idxmin()
    min_dist_m = distances[min_idx]

    if min_dist_m > max_distance_km * 1000:
        return None

    return roads_gdf.loc[min_idx]


def get_road_segment_id(
    lat: float,
    lon: float,
    roads_gdf: gpd.GeoDataFrame,
) -> str:
    """
    Return the route segment identifier (Carretera) for the nearest road.

    Parameters
    ----------
    lat, lon : float
        WGS84 coordinates.
    roads_gdf : gpd.GeoDataFrame
        Interurban road network with 'Carretera' column.

    Returns
    -------
    str
        Road name (e.g. 'A-3', 'AP-7'), or 'Unknown' if no road found.
    """
    row = snap_point_to_road(lat, lon, roads_gdf, max_distance_km=5.0)
    if row is None:
        return 'Unknown'
    return str(row.get('Carretera', row.get('route_segment', 'Unknown')))
