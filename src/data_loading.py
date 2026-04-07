"""
Reusable functions for loading each dataset.
"""

import pandas as pd
import geopandas as gpd
from pathlib import Path
from pyproj import Transformer
from shapely import wkb

DATA_RAW = Path(__file__).parent.parent / 'data' / 'raw'
DATA_PROCESSED = Path(__file__).parent.parent / 'data' / 'processed'

# INE province code → province name mapping (for Endesa files)
INE_PROVINCE_CODES = {
    1: 'Araba/Álava', 2: 'Albacete', 3: 'Alicante/Alacant', 4: 'Almería',
    5: 'Ávila', 6: 'Badajoz', 7: 'Balears, Illes', 8: 'Barcelona',
    9: 'Burgos', 10: 'Cáceres', 11: 'Cádiz', 12: 'Castellón/Castelló',
    13: 'Ciudad Real', 14: 'Córdoba', 15: 'Coruña, A', 16: 'Cuenca',
    17: 'Girona', 18: 'Granada', 19: 'Guadalajara', 20: 'Gipuzkoa',
    21: 'Huelva', 22: 'Huesca', 23: 'Jaén', 24: 'León',
    25: 'Lleida', 26: 'Rioja, La', 27: 'Lugo', 28: 'Madrid',
    29: 'Málaga', 30: 'Murcia', 31: 'Navarra', 32: 'Ourense',
    33: 'Asturias', 34: 'Palencia', 35: 'Palmas, Las', 36: 'Pontevedra',
    37: 'Salamanca', 38: 'Santa Cruz de Tenerife', 39: 'Cantabria',
    40: 'Segovia', 41: 'Sevilla', 42: 'Soria', 43: 'Tarragona',
    44: 'Teruel', 45: 'Toledo', 46: 'Valencia/València', 47: 'Valladolid',
    48: 'Bizkaia', 49: 'Zamora', 50: 'Zaragoza', 51: 'Ceuta', 52: 'Melilla',
}

# UTM Zone 30N (ETRS89) → WGS84 transformer
_transformer = Transformer.from_crs("EPSG:25830", "EPSG:4326", always_xy=True)


def _parse_spanish_float(value):
    """Parse a Spanish-formatted number string (comma decimal, optional dot thousands)."""
    if pd.isna(value) or str(value).strip() == '':
        return None
    s = str(value).strip()
    # If it has both dots and commas, dots are thousands separators
    if '.' in s and ',' in s:
        s = s.replace('.', '').replace(',', '.')
    elif ',' in s:
        s = s.replace(',', '.')
    try:
        return float(s)
    except ValueError:
        return None


def _utm_to_wgs84(utm_x, utm_y):
    """Convert UTM ETRS89 Zone 30N coordinates to WGS84 lat/lon."""
    if utm_x is None or utm_y is None:
        return None, None
    try:
        lon, lat = _transformer.transform(utm_x, utm_y)
        # Sanity check: must be within Spain
        if 35.0 <= lat <= 44.0 and -10.0 <= lon <= 5.0:
            return lat, lon
        return None, None
    except Exception:
        return None, None


def load_road_network(filepath=None):
    """Load Ministry of Transport road network GeoJSON."""
    if filepath is None:
        filepath = DATA_RAW / 'ministry_roads' / 'hermes_roads.parquet'
    return load_geo_parquet_compat(filepath)


def load_geo_parquet_compat(filepath):
    """
    Load a GeoParquet file with a compatibility fallback for the project's road
    datasets, which can fail under pyarrow/geopandas with
    `Repetition level histogram size mismatch`.
    """
    path = Path(filepath)

    try:
        gdf = gpd.read_parquet(path)
        if gdf.crs is None:
            gdf = gdf.set_crs(epsg=4326)
        return gdf
    except OSError as err:
        if 'Repetition level histogram size mismatch' not in str(err):
            raise

    df = pd.read_parquet(path, engine='fastparquet')
    if 'geometry' not in df.columns:
        raise ValueError(f"{path} does not contain a geometry column")

    geometry = df['geometry'].apply(
        lambda value: None if value is None or (isinstance(value, bytes) and value == b'') else wkb.loads(value)
    )
    return gpd.GeoDataFrame(df.drop(columns=['geometry']), geometry=geometry, crs='EPSG:4326')


def load_nap_charging_points(filepath=None):
    """
    Parse NAP EV charging station XML (DATEX II v3) or load parquet.
    Returns a DataFrame with one row per charging site.
    Populates missing province information via spatial join if needed.
    """
    if filepath is None:
        filepath = DATA_RAW / 'nap_charging_points' / 'nap_ev_charging_points.parquet'

    # 1. Load Data
    if str(filepath).endswith('.parquet'):
        df = pd.read_parquet(filepath)
    else:
        # If not parquet, parse XML (logic kept below)
        from lxml import etree

        NS = {
            'egi': 'http://datex2.eu/schema/3/energyInfrastructure',
            'fac': 'http://datex2.eu/schema/3/facilities',
            'loc': 'http://datex2.eu/schema/3/locationReferencing',
            'locx': 'http://datex2.eu/schema/3/locationExtension',
            'com': 'http://datex2.eu/schema/3/common',
        }

        tag = f'{{{NS["egi"]}}}energyInfrastructureSite'
        records = []

        for event, elem in etree.iterparse(str(filepath), events=('end',), tag=tag):
            site_id = elem.get('id', '')

            # Name
            name_el = elem.find('.//fac:name/com:values/com:value', NS)
            name = name_el.text if name_el is not None else None

            # Coordinates
            lat_el = elem.find('.//loc:coordinatesForDisplay/loc:latitude', NS)
            lon_el = elem.find('.//loc:coordinatesForDisplay/loc:longitude', NS)
            lat = float(lat_el.text) if lat_el is not None and lat_el.text else None
            lon = float(lon_el.text) if lon_el is not None and lon_el.text else None

            # Address fields
            postcode_el = elem.find('.//locx:postcode', NS)
            postcode = postcode_el.text if postcode_el is not None else None

            municipality = None
            province = None
            address = None
            for addr_line in elem.findall('.//locx:addressLine', NS):
                order = addr_line.get('order', '')
                text_el = addr_line.find('.//com:value', NS)
                if text_el is not None and text_el.text:
                    txt = text_el.text
                    if order == '1' and 'Dirección:' in txt:
                        address = txt.replace('Dirección:', '').strip()
                    elif order == '2' and 'Municipio:' in txt:
                        municipality = txt.replace('Municipio:', '').strip()
                    elif order == '3' and 'Provincia:' in txt:
                        province = txt.replace('Provincia:', '').strip()

            # Connectors: count and max power
            connectors = elem.findall('.//egi:connector', NS)
            n_connectors = len(connectors)
            max_power_kw = 0.0
            for conn in connectors:
                power_el = conn.find('egi:maxPowerAtSocket', NS)
                if power_el is not None and power_el.text:
                    try:
                        power_w = float(power_el.text)
                        max_power_kw = max(max_power_kw, power_w / 1000.0)
                    except ValueError:
                        pass

            records.append({
                'site_id': site_id,
                'name': name,
                'latitude': lat,
                'longitude': lon,
                'address': address,
                'municipality': municipality,
                'province': province,
                'postcode': postcode,
                'n_connectors': n_connectors,
                'max_power_kw': max_power_kw,
            })

            elem.clear()

        df = pd.DataFrame(records)

    # 2. Normalize and Clean
    # Handle older parquet schema if present
    rename_cols = {
        'num_connectors': 'n_connectors',
        'address_postcode': 'postcode',
        'address_addressLine': 'address'
    }
    df = df.rename(columns={k: v for k, v in rename_cols.items() if k in df.columns})

    # Drop rows without coordinates
    df = df.dropna(subset=['latitude', 'longitude'])

    # 3. Add Province Feature if missing/null (Spatial Join)
    if 'province' not in df.columns or df['province'].isna().all():
        try:
            provinces_gdf = load_provinces()
            # Convert chargers to GeoDataFrame
            points_gdf = gpd.GeoDataFrame(
                df,
                geometry=gpd.points_from_xy(df.longitude, df.latitude),
                crs="EPSG:4326"
            )
            # Spatial join to get 'name' from provinces
            joined = gpd.sjoin(points_gdf, provinces_gdf[['name', 'geometry']], how='left', predicate='within')
            df['province'] = joined['name_right']
        except Exception as e:
            print(f"Warning: Could not populate provinces via spatial join: {e}")
            if 'province' not in df.columns:
                df['province'] = None

    return df


def _load_ide(filepath=None):
    """Load i-DE (Iberdrola) grid capacity CSV."""
    if filepath is None:
        filepath = DATA_RAW / 'grid_capacity' / 'ide_iberdrola' / '2026_03_05_R1-001_Demanda.csv'
    df = pd.read_csv(filepath, sep=';', encoding='utf-8-sig')
    df['distributor_network'] = 'i-DE'
    df['available_capacity_mw'] = df['Capacidad firme disponible (MW)'].apply(_parse_spanish_float)
    df['utm_x'] = df['Coordenada UTM X'].apply(_parse_spanish_float)
    df['utm_y'] = df['Coordenada UTM Y'].apply(_parse_spanish_float)
    df['voltage_kv'] = df['Nivel de Tensión (kV)'].apply(_parse_spanish_float)
    df['substation_name'] = df['Subestación'].astype(str).str.strip()
    df['provincia'] = df['Provincia'].astype(str).str.strip()
    df['municipio'] = df['Municipio'].astype(str).str.strip()
    return df[['substation_name', 'provincia', 'municipio', 'utm_x', 'utm_y',
               'available_capacity_mw', 'voltage_kv', 'distributor_network']]


def _load_endesa(filepaths=None):
    """Load Endesa (e-distribución) grid capacity CSVs."""
    if filepaths is None:
        base = DATA_RAW / 'grid_capacity' / 'endesa'
        filepaths = list(base.glob('*.csv'))
    frames = []
    for fp in filepaths:
        df = pd.read_csv(fp, sep=';', encoding='utf-8-sig')
        df['distributor_network'] = 'Endesa'
        df['available_capacity_mw'] = df['Capacidad disponible (MW)'].apply(_parse_spanish_float)
        df['utm_x'] = df['Coordenada UTM X'].apply(_parse_spanish_float)
        df['utm_y'] = df['Coordenada UTM Y'].apply(_parse_spanish_float)
        df['voltage_kv'] = df['Nivel de Tensión (kV)'].apply(_parse_spanish_float)
        df['substation_name'] = df['Nombre Subestación'].astype(str).str.strip()
        # Province: numeric INE code in first 'Provincia' column
        provincia_col = df.columns[df.columns.str.strip() == 'Provincia'][0]
        df['provincia'] = df[provincia_col].apply(
            lambda x: INE_PROVINCE_CODES.get(int(float(x)), str(x)) if pd.notna(x) else None
        )
        municipio_cols = df.columns[df.columns.str.strip() == 'Municipio']
        if len(municipio_cols) > 1:
            df['municipio'] = df[municipio_cols[-1]].astype(str).str.strip()
        else:
            df['municipio'] = df[municipio_cols[0]].astype(str).str.strip()
        frames.append(df[['substation_name', 'provincia', 'municipio', 'utm_x', 'utm_y',
                          'available_capacity_mw', 'voltage_kv', 'distributor_network']])
    return pd.concat(frames, ignore_index=True)


def _load_viesgo(filepath=None):
    """Load Viesgo grid capacity CSV."""
    if filepath is None:
        filepath = DATA_RAW / 'grid_capacity' / 'viesgo' / '2026_03_05_R1005_demanda.csv'
    df = pd.read_csv(filepath, sep=';', encoding='latin-1')
    df['distributor_network'] = 'Viesgo'
    df['available_capacity_mw'] = df['Capacidad firme disponible (MW)'].apply(_parse_spanish_float)
    df['utm_x'] = df['Coordenada UTM X'].apply(_parse_spanish_float)
    df['utm_y'] = df['Coordenada UTM Y'].apply(_parse_spanish_float)
    # Viesgo has 'Nivel de tensión (kV)' with lowercase t
    tension_col = [c for c in df.columns if 'tensi' in c.lower()][0]
    df['voltage_kv'] = df[tension_col].apply(_parse_spanish_float)
    # Viesgo has 'Subestación ' with trailing space and 'Nombre subestación'
    sub_col = [c for c in df.columns if 'Nombre' in c and 'subestaci' in c.lower()]
    if sub_col:
        df['substation_name'] = df[sub_col[0]].astype(str).str.strip()
    else:
        sub_col2 = [c for c in df.columns if 'Subestaci' in c]
        df['substation_name'] = df[sub_col2[0]].astype(str).str.strip()
    df['provincia'] = df['Provincia'].astype(str).str.strip()
    df['municipio'] = df['Municipio'].astype(str).str.strip()
    return df[['substation_name', 'provincia', 'municipio', 'utm_x', 'utm_y',
               'available_capacity_mw', 'voltage_kv', 'distributor_network']]


def load_grid_capacity(distributor='all'):
    """
    Load grid capacity data for i-DE, Endesa, and/or Viesgo.
    Converts UTM to WGS84 and returns a unified DataFrame.
    """
    loaders = {
        'i-DE': _load_ide,
        'Endesa': _load_endesa,
        'Viesgo': _load_viesgo,
    }

    if distributor == 'all':
        frames = [loader() for loader in loaders.values()]
        df = pd.concat(frames, ignore_index=True)
    elif distributor in loaders:
        df = loaders[distributor]()
    else:
        raise ValueError(f"Unknown distributor: {distributor}. Use 'all', 'i-DE', 'Endesa', or 'Viesgo'.")

    # Convert UTM to WGS84
    coords = df.apply(lambda row: _utm_to_wgs84(row['utm_x'], row['utm_y']), axis=1)
    df['latitude'] = [c[0] for c in coords]
    df['longitude'] = [c[1] for c in coords]

    # Drop rows where conversion failed
    df = df.dropna(subset=['latitude', 'longitude'])

    return df


def load_ev_forecast(filepath=None):
    """
    Load EV registration parquet files and aggregate to monthly BEV+PHEV counts.
    Returns a DataFrame with columns: year_month, ev_registrations
    """
    if filepath is None:
        filepath = DATA_RAW / 'datos_gob_ev_forecast'

    path_obj = Path(filepath)
    parquet_files = sorted(path_obj.glob('*.parquet'))

    if not parquet_files:
        # Fallback: load from already-processed monthly registrations CSV
        fallback = DATA_PROCESSED / 'ev_monthly_registrations.csv'
        if fallback.exists():
            print(f"Warning: No .parquet files in {path_obj.name}/. Loading from processed CSV fallback.")
            df = pd.read_csv(fallback, parse_dates=['date'])
            if 'year_month' not in df.columns:
                df['year_month'] = df['date'].dt.strftime('%Y_%m')
            return df[['year_month', 'ev_registrations', 'date']]
        print(f"Warning: No .parquet files found in {path_obj.absolute()}")
        return pd.DataFrame(columns=['year_month', 'ev_registrations', 'date'])

    records = []
    for pf in parquet_files:
        # Extract year_month from filename (e.g., 2023_01.parquet)
        year_month = pf.stem  # e.g., '2023_01'
        try:
            df = pd.read_parquet(pf)

            # Filter to new registrations only
            if 'CLAVE_TRAMITE' in df.columns:
                df = df[df['CLAVE_TRAMITE'] == '1']

            # Filter to plug-in EVs (BEV + PHEV)
            if 'CATEGORÍA_VEHÍCULO_ELÉCTRICO' in df.columns:
                ev_count = df[df['CATEGORÍA_VEHÍCULO_ELÉCTRICO'].isin(['BEV', 'PHEV'])].shape[0]
            else:
                ev_count = 0

            records.append({
                'year_month': year_month,
                'ev_registrations': ev_count,
            })
        except Exception as e:
            print(f"Error reading {pf}: {e}")

    result = pd.DataFrame(records)
    if result.empty:
        return pd.DataFrame(columns=['year_month', 'ev_registrations', 'date'])

    # Parse year_month to datetime for time series
    result['date'] = pd.to_datetime(result['year_month'], format='%Y_%m')
    result = result.sort_values('date').reset_index(drop=True)
    return result


def load_imd_traffic(filepath=None):
    """Load DGT Intensidad Media Diaria traffic count stations GeoJSON."""
    if filepath is None:
        filepath = DATA_RAW / 'additional' / 'dgt_imd_traffic' / 'hermes_traffic_count_stations.geojson'
    gdf = gpd.read_file(filepath)
    if gdf.crs is None:
        gdf = gdf.set_crs(epsg=4326)
    return gdf


def load_dgt_registrations(filepath=None):
    """Load DGT monthly vehicle registration data (fixed-width TXT files).
    Optional — the parquet files in datos_gob_ev_forecast are sufficient for SARIMA.
    """
    if filepath is None:
        filepath = DATA_RAW / 'dgt_registrations'
    raise NotImplementedError("DGT TXT parsing not implemented. Use load_ev_forecast() instead.")


# === Additional dataset loaders ===

def load_gas_stations(filepath=None):
    """Load MITECO gas stations dataset."""
    if filepath is None:
        filepath = DATA_RAW / 'additional' / 'miteco_gas_stations' / 'miteco_gas_stations.csv'
    return pd.read_csv(filepath)


def load_population(filepath=None):
    """Load INE municipal population data."""
    if filepath is None:
        filepath = DATA_RAW / 'additional' / 'ine_population' / 'ine_population_municipal_2025.csv'
    return pd.read_csv(filepath)


def load_tourism_seasonal(filepath=None):
    """Load INE hotel occupancy / tourism seasonality data."""
    if filepath is None:
        filepath = DATA_RAW / 'additional' / 'ine_population' / 'ine_hotel_occupancy_provinces_2024_raw.csv'
    df = pd.read_csv(filepath, sep='\t', encoding='utf-8-sig')
    # Parse Spanish decimal format in 'Total' column
    if 'Total' in df.columns:
        df['Total'] = df['Total'].astype(str).str.replace('.', '', regex=False).str.replace(',', '.', regex=False)
        df['Total'] = pd.to_numeric(df['Total'], errors='coerce')
    return df


def load_service_areas(filepath=None):
    """Load OSM/Hermes service areas on motorways."""
    if filepath is None:
        filepath = DATA_RAW / 'additional' / 'osm_rest_areas' / 'hermes_service_areas.geojson'
    gdf = gpd.read_file(filepath)
    if gdf.crs is None:
        gdf = gdf.set_crs(epsg=4326)
    return gdf


def load_tent_corridors(filepath=None):
    """Load EU TEN-T corridor designations."""
    if filepath is None:
        filepath = DATA_RAW / 'additional' / 'tent_corridors' / 'hermes_tent_roads_2024.geojson'
    gdf = gpd.read_file(filepath)
    if gdf.crs is None:
        gdf = gdf.set_crs(epsg=4326)
    return gdf


def load_provinces(filepath=None):
    """Load Spain province boundaries."""
    if filepath is None:
        filepath = DATA_RAW / 'additional' / 'ign_boundaries' / 'spain_provinces.geojson'
    return gpd.read_file(filepath)


def load_ccaa(filepath=None):
    """Load Spain autonomous community boundaries."""
    if filepath is None:
        filepath = DATA_RAW / 'additional' / 'ign_boundaries' / 'spain_ccaa.geojson'
    return gpd.read_file(filepath)
