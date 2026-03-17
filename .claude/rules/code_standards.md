# Code Standards

**Purpose:** Ensure consistent, maintainable code across all team members and agents.

---

## Python Style

### General
- **PEP 8 compliance** — use `black` formatter if available
- **Line length:** 88 characters (black default)
- **Imports:** standard library, third-party, local (separated by blank lines)
- **Naming:** snake_case for functions/variables, PascalCase for classes

### Functions
```python
def calculate_chargers_needed(
    daily_ev_trips: float, 
    charging_probability: float = 0.12,
    session_duration_hours: float = 0.37,
    operating_hours: float = 20.0
) -> int:
    """
    Calculate number of chargers needed for a road segment.
    
    Args:
        daily_ev_trips: Daily BEV traffic through segment
        charging_probability: Fraction of passing EVs that charge (0-1)
        session_duration_hours: Average charging session duration
        operating_hours: Station daily operating hours
        
    Returns:
        Number of 150kW chargers needed (integer, minimum 2)
        
    Example:
        >>> calculate_chargers_needed(1000, 0.12, 0.37, 20)
        3
    """
    raw_demand = daily_ev_trips * charging_probability * session_duration_hours
    chargers_needed = math.ceil(raw_demand / operating_hours)
    return max(chargers_needed, 2)  # Minimum 2 chargers per station
```

### Error Handling
```python
# Prefer specific exceptions over generic
try:
    result = process_data(filepath)
except FileNotFoundError:
    logger.error(f"Data file not found: {filepath}")
    return None
except pd.errors.EmptyDataError:
    logger.warning(f"Empty data file: {filepath}")
    return pd.DataFrame()
```

### Constants
```python
# Use constants.py for all shared parameters
from src.constants import MAX_SPACING_KM, CHARGER_POWER_KW

# Not: magic numbers in code
charger_load = n_chargers * 150  # Bad
charger_load = n_chargers * CHARGER_POWER_KW  # Good
```

---

## Data Handling

### File I/O
```python
# Always use pathlib for paths
from pathlib import Path

def load_rutas_data(date_str: str) -> pd.DataFrame:
    """Load Rutas informacion_tramo for specific date."""
    data_path = Path("data/raw/rutas_por_carretera")
    file_path = data_path / f"{date_str}_Tramos_info_odmatrix.csv.gz"
    
    if not file_path.exists():
        raise FileNotFoundError(f"Rutas data not found: {file_path}")
    
    return pd.read_csv(file_path, sep=";", compression="gzip")
```

### DataFrame Operations
```python
# Chain operations for readability
result = (
    df
    .query("road_type in ['AP', 'A', 'N']")
    .groupby("tramo_id")["largo"]
    .sum()
    .reset_index()
)

# Use explicit column names
df.rename(columns={"total": "total_trips", "largo": "long_trips"}, inplace=True)

# Always validate data after major operations
assert not result.isna().any().any(), "NaN values found in result"
assert len(result) > 0, "Empty result dataframe"
```

### Geospatial
```python
import geopandas as gpd
from sklearn.neighbors import BallTree

# Use consistent CRS (EPSG:4326 for lat/lon, EPSG:25830 for Spain UTM)
gdf = gpd.read_file("roads.geojson")
assert gdf.crs == "EPSG:4326", f"Expected EPSG:4326, got {gdf.crs}"

# Use BallTree for nearest neighbor searches
coords = np.radians(gdf[["longitude", "latitude"]].values)
tree = BallTree(coords, metric="haversine")
```

---

## Notebook Standards

### Cell Organization
```python
# Cell 1: Imports and setup
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from pathlib import Path
import sys
sys.path.append('../src')
from constants import *

# Cell 2: Load data
# Cell 3: Exploration and validation  
# Cell 4: Main processing
# Cell 5: Output and export
# Cell 6: Visualization
```

### Output Management
```python
# Always save intermediate results
processed_data.to_parquet("data/processed/demand_per_segment.parquet")
print(f"✅ Saved {len(processed_data)} segments to demand_per_segment.parquet")

# Clear, informative print statements
print(f"📊 Loaded {len(df)} road segments")
print(f"🔍 Filtered to {len(interurban_df)} interurban roads")
print(f"⚡ Total daily EV trips: {daily_ev_trips.sum():,.0f}")
```

### Documentation
```markdown
# Cell documentation using markdown cells before major processing blocks:

## Step 3: Scale to 2027 EV Demand

Apply the approved assumptions:
- EV penetration rate: 5.7% (2M EVs / 35M total vehicles)  
- BEV fraction: 60% (only BEVs need DC fast charging)
- Long-trip probability: Use `largo` trips only (>50km)

Formula: `daily_ev_trips = largo_trips × 0.057 × 0.60`
```

---

## Git & Collaboration

### Commit Messages
```bash
# Good commit messages
git commit -m "feat(demand): implement segment-level EV trip scaling"
git commit -m "fix(optimization): handle edge case when no candidates found"
git commit -m "docs(assumptions): update charging probability to 12% per IEA data"

# Prefixes: feat, fix, docs, refactor, test, data
```

### Branch Strategy
```bash
# Feature branches from main
git checkout -b feat/demand-model
git checkout -b fix/constants-sync
git checkout -b data/download-rutas

# Keep branches focused and short-lived
```

### Code Review
```python
# Include type hints for complex functions
def solve_set_cover_lp(
    candidates: gpd.GeoDataFrame,
    demand_points: gpd.GeoDataFrame, 
    coverage_matrix: np.ndarray,
    max_spacing_km: float
) -> Tuple[List[int], float]:
    """Solve Set Cover LP to minimize station count."""
    # Implementation
    pass

# Document non-obvious business logic
# Why 2.1 safety factor? Because...
safety_factor = 2.1  # Conservative: drivers charge at 50% SoC to avoid anxiety
max_spacing = effective_range_km / safety_factor
```

---

## Testing & Validation

### Data Validation
```python
def validate_demand_model_output(df: pd.DataFrame) -> None:
    """Validate demand model output meets expectations."""
    # Schema validation
    required_cols = ["tramo_id", "daily_ev_trips", "n_chargers_needed"]
    missing_cols = set(required_cols) - set(df.columns)
    assert not missing_cols, f"Missing columns: {missing_cols}"
    
    # Range validation
    assert df["daily_ev_trips"].min() >= 0, "Negative EV trips found"
    assert df["n_chargers_needed"].between(2, 12).all(), "Charger count out of range"
    
    # Business logic validation
    total_chargers = df["n_chargers_needed"].sum()
    assert 1000 <= total_chargers <= 5000, f"Total chargers {total_chargers} seems unrealistic"
```

### Integration Tests
```python
# Test end-to-end workflow with small data
def test_demand_model_pipeline():
    """Test demand model with synthetic data."""
    # Create test data
    test_segments = create_test_segments()
    
    # Run pipeline
    result = run_demand_model(test_segments)
    
    # Validate result
    assert len(result) == len(test_segments)
    assert result["daily_ev_trips"].sum() > 0
```

---

## Performance

### Memory Management
```python
# Use chunked processing for large files
chunk_size = 10000
for chunk in pd.read_csv("large_file.csv", chunksize=chunk_size):
    process_chunk(chunk)

# Clean up intermediate variables
del large_dataframe
gc.collect()
```

### Optimization
```python
# Use vectorized operations over loops
# Bad
for idx, row in df.iterrows():
    df.loc[idx, "result"] = calculate_something(row["value"])

# Good  
df["result"] = df["value"].apply(calculate_something)

# Best (if possible)
df["result"] = df["value"] * 1.5  # Vectorized operation
```

---

## Error Handling for Agents

### Graceful Degradation
```python
def download_with_fallback(url: str, backup_url: str = None) -> Optional[bytes]:
    """Download with fallback for agent resilience."""
    try:
        return download_file(url)
    except (requests.RequestException, TimeoutError) as e:
        logger.warning(f"Primary download failed: {e}")
        if backup_url:
            try:
                return download_file(backup_url)
            except Exception as e2:
                logger.error(f"Backup download also failed: {e2}")
        return None
```

### Agent Handoff
```python
# Always save state before complex operations
checkpoint_data = {
    "processed_segments": len(df),
    "timestamp": datetime.now().isoformat(),
    "next_step": "optimization"
}
with open("memory/checkpoint.json", "w") as f:
    json.dump(checkpoint_data, f)
```