# Data Conventions

**Purpose:** Standardize data formats, naming, and storage across all team members and agents.

---

## File Formats by Usage

### Working Data (Internal)
| Format | Use Case | Why |
|--------|----------|-----|
| **Parquet** | Structured tabular data | Columnar storage, fast reads, type-safe, compressed |
| **GeoParquet** | Geospatial working files | Parquet + geometry, fast spatial queries |
| **JSON** | Configuration, metadata | Human-readable, universal compatibility |
| **CSV.gz** | Raw downloads | Space-efficient for transport, pandas-readable |

### Final Outputs (Submission)
| Format | Use Case | Requirement |
|--------|----------|-------------|
| **CSV** | File_1, File_2, File_3 | **Mandated by datathon** |
| **HTML** | Interactive map | **Required: bi_map.html** |
| **PDF** | Analytical report | **Required: 3-5 pages** |
| **PDF** | Pitch deck | **Required: 5 min max** |

### Legacy/Archive
| Format | Use Case | Notes |
|--------|----------|-------|
| **GeoJSON** | Final geospatial outputs | For visualization, larger file size |
| **Shapefile** | Ministry downloads | Keep as-is for provenance |
| **XML** | NAP charging data | Original format, convert to CSV for analysis |

---

## Directory Structure Conventions

```
data/
├── raw/                        # Original downloads, never modified
│   ├── source_name/            # Group by data provider
│   │   ├── YYYY-MM-DD_dataset.ext    # Date-prefixed files
│   │   └── metadata.json      # Source URL, download date, description
│   └── rutas_por_carretera/    # ← New addition
│       ├── 20240824_Tramos_info_odmatrix.csv.gz
│       ├── 20240824_OD_rutas.csv.gz  
│       └── geometria/
│           └── Geometria_tramos.shp
│
├── processed/                  # Cleaned, analysis-ready
│   ├── segments_demand_2027.parquet      # Core demand model output
│   ├── proposed_stations.parquet         # Optimization result  
│   ├── grid_friction_analysis.parquet    # Grid viability
│   └── validation/                       # Cross-checks, QA outputs
│       ├── imd_vs_rutas_comparison.csv
│       └── existing_vs_proposed.csv
│
└── temp/                       # Intermediate files, .gitignored
    ├── download_progress.json
    └── optimization_checkpoints/
```

---

## File Naming Conventions

### Raw Data
```
# Pattern: YYYY-MM-DD_source_dataset_version.ext
2024-08-24_mitma_tramos_info.csv.gz
2024-10-16_mitma_od_rutas.csv.gz  
2026-03-05_ide_grid_capacity.csv
2025-12-01_dgt_ev_registrations.xlsx
```

### Processed Data
```
# Pattern: descriptive_name_processing_status.ext
roads_interurban_filtered.parquet
chargers_highway_grade_only.parquet
demand_per_segment_summer_peak.parquet
stations_proposed_optimized.parquet
```

### Outputs
```
# Pattern: FileN.csv (exact datathon requirement)
File_1.csv    # Global KPIs
File_2.csv    # Proposed stations  
File_3.csv    # Friction points
```

### Scripts
```
# Pattern: verb_noun.py
download_rutas.py
validate_outputs.py
export_deliverables.py
```

---

## Column Naming Standards

### General Rules
- **snake_case** for all column names
- **Explicit units** in name: `distance_km`, `capacity_mw`, `duration_hours`
- **No abbreviations** unless universally clear: `id` OK, `trm` not OK
- **Consistent prefixes**: `n_` for counts, `is_` for booleans, `avg_` for averages

### Standard Column Names

#### Geographic
```python
# Coordinates (always decimal degrees, EPSG:4326)
latitude          # Decimal degrees North
longitude         # Decimal degrees East
geometry          # GeoPandas geometry column

# Administrative
province_code     # INE province code (01-52)
ccaa_code         # INE autonomous community code  
municipality_code # INE municipality code (01001, 28079, etc.)
```

#### Infrastructure
```python
# Road network
road_name         # "A-3", "AP-7", "N-II"  
road_type         # "AP", "A", "N"
tramo_id          # Unique segment identifier
segment_length_km # Length of road segment

# Charging stations
station_id        # Unique station identifier
n_chargers        # Number of charging points
charger_power_kw  # Power per charger (150 for our project)
operator_name     # "Iberdrola", "Endesa", "Tesla"
is_existing       # Boolean: existing vs proposed
```

#### Demand & Traffic
```python
# Traffic flows  
daily_trips       # Vehicles per day (all types)
daily_ev_trips    # BEV trips per day
largo_trips       # Long-distance trips (>50km)
n_chargers_needed # Required chargers for demand

# Grid
available_capacity_mw    # MW capacity at substation
distributor_network      # "i-DE", "Endesa", "Viesgo"  
grid_status              # "Sufficient", "Moderate", "Congested"
connection_distance_km   # Distance to nearest substation
```

#### Dates & Times
```python
# Always ISO format
date              # YYYY-MM-DD
timestamp         # YYYY-MM-DDTHH:MM:SS
last_updated      # ISO timestamp

# Relative  
season            # "winter", "spring", "summer", "autumn"
month_num         # 1-12
hour              # 0-23
```

---

## Data Types & Validation

### Pandas dtypes
```python
# Use explicit dtypes for clarity and performance
COLUMN_TYPES = {
    "tramo_id": "string",
    "latitude": "float64", 
    "longitude": "float64",
    "daily_ev_trips": "float64",
    "n_chargers_needed": "int64",
    "grid_status": "category",
    "is_existing": "boolean",
    "date": "datetime64[ns]"
}

df = pd.read_csv("file.csv", dtype=COLUMN_TYPES)
```

### Validation Rules
```python
def validate_station_data(df: pd.DataFrame) -> None:
    """Validate proposed station data."""
    # Geographic bounds (Spain mainland + islands)
    assert df["latitude"].between(35.0, 44.0).all(), "Latitude out of Spain range"
    assert df["longitude"].between(-10.0, 5.0).all(), "Longitude out of Spain range"
    
    # Business logic
    assert df["n_chargers_needed"].between(2, 12).all(), "Charger count unrealistic"
    assert df["grid_status"].isin(["Sufficient", "Moderate", "Congested"]).all()
    
    # Data completeness
    assert not df["station_id"].isna().any(), "Missing station IDs"
    assert df["station_id"].is_unique, "Duplicate station IDs"
```

---

## Coordinate Reference Systems

### Standard CRS Usage
| CRS | EPSG | Usage | Why |
|-----|------|-------|-----|
| **WGS84** | 4326 | All input/output data | Universal compatibility, GPS standard |
| **UTM Zone 30N** | 25830 | Distance calculations | Accurate for Spain, preserves distances |
| **UTM Zone 31N** | 25831 | Eastern Spain calculations | More accurate for Valencia/Catalonia |

### CRS Handling
```python
import geopandas as gpd

# Always validate CRS on load
roads = gpd.read_file("roads.geojson")
assert roads.crs == "EPSG:4326", f"Expected WGS84, got {roads.crs}"

# Transform only when needed for distance calculations  
roads_utm = roads.to_crs("EPSG:25830")  # For Spain-wide analysis
distance_km = roads_utm.geometry.length / 1000

# Transform back to WGS84 for output
output_gdf = results_utm.to_crs("EPSG:4326")
```

---

## Configuration Management

### Constants in Code
```python
# src/constants.py structure
class VehicleAssumptions:
    EV_RANGE_KM = 340                    # A1: Average WLTP range
    EFFECTIVE_RANGE_FACTOR = 0.75        # A2: Highway usability  
    EFFECTIVE_RANGE_KM = EV_RANGE_KM * EFFECTIVE_RANGE_FACTOR  # 255 km

class ChargingBehavior:
    CHARGING_PROBABILITY = 0.12          # B1: Interurban charging rate
    SESSION_DURATION_HOURS = 0.37        # B2: 22 minutes average
    OPERATING_HOURS_PER_DAY = 20         # B3: Station availability

class NetworkConstraints:
    MAX_SPACING_TENT_CORE_KM = 60        # C2: AFIR TEN-T Core
    MAX_SPACING_TENT_COMP_KM = 100       # C3: AFIR TEN-T Comprehensive  
    MAX_SPACING_GENERAL_KM = 120         # C1: General interurban
```

### External Configuration
```json
// config/data_sources.json
{
  "rutas_por_carretera": {
    "base_url": "https://movilidad-opendata.mitma.es",
    "target_dates": ["20240824", "20241016", "20240331"],
    "file_types": ["informacion_tramo", "od_rutas", "calidad"],
    "geometry_folder": "estudios_rutas/geometria/Geometria_tramos_2023_2024"
  }
}
```

---

## Data Quality Standards

### Completeness Thresholds
```python
# Acceptable missing data rates by dataset type
COMPLETENESS_REQUIREMENTS = {
    "core_infrastructure": 0.99,    # Roads, stations: <1% missing
    "traffic_data": 0.95,           # IMD, Rutas: <5% missing  
    "grid_capacity": 0.90,          # DSO data: <10% missing
    "tourism_seasonal": 0.85        # INE data: <15% missing
}
```

### Data Freshness
```python
from datetime import datetime, timedelta

def validate_data_freshness(file_path: Path, max_age_days: int) -> bool:
    """Check if data file is recent enough."""
    file_age = datetime.now() - datetime.fromtimestamp(file_path.stat().st_mtime)
    return file_age.days <= max_age_days

# Apply different freshness requirements
FRESHNESS_REQUIREMENTS = {
    "grid_capacity": 30,      # Grid data changes monthly
    "ev_registrations": 60,   # Registration data quarterly  
    "road_network": 365,      # Road network changes slowly
    "assumptions": 7          # Assumptions should be recent
}
```

---

## Backup & Recovery

### Critical Data Protection
```python
# Always backup before major transformations
def backup_dataframe(df: pd.DataFrame, operation_name: str) -> Path:
    """Create timestamped backup before risky operation."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = Path(f"data/temp/backup_{operation_name}_{timestamp}.parquet")
    df.to_parquet(backup_path)
    return backup_path

# Usage
backup_path = backup_dataframe(stations_df, "optimization_results")
# ... perform risky operation ...
if validation_failed:
    stations_df = pd.read_parquet(backup_path)  # Restore
```

### Version Control Strategy
```bash
# Track processed data <10MB, metadata always
git add data/processed/*.parquet
git add data/**/metadata.json
git add config/

# Never track raw downloads, temp files
# (Already in .gitignore)
git rm --cached data/raw/large_file.csv
```