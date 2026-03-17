# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

IE Sustainability Datathon (March 2026) — **Team Greenlabs**. Optimal placement of EV charging stations along Spain's interurban road network for 2027, incorporating grid capacity constraints from three DSOs: i-DE (Iberdrola), Endesa, and Viesgo.

## Running the Project

```bash
pip install -r requirements.txt
jupyter notebook notebooks/
# Execute notebooks 00 through 10 in sequential order
```

No build system, Makefile, or CI pipeline exists. Python 3.10+.

## Architecture

**Jupyter notebook pipeline** (`notebooks/00` → `10`) with shared Python utilities in `src/`.

### Data Flow
```
00 Environment Setup
01 Data Ingestion & Cleaning    → data/processed/*.csv, *.parquet, *.geojson
02 EV Projection (SARIMA fork)  → ev_projection_2027.csv (mandatory: 2,498,159 EVs)
03 Road Network Analysis        → interurban roads filtered to AP-, A-, N- types
04 Existing Chargers Baseline   → NAP dataset filtered to ≥50 kW
05 Grid Capacity Consolidation  → unified substation capacity from 3 DSOs
06 Demand Modeling              → daily EV demand per road segment
07 Network Optimization         → Set Cover LP: minimize stations with spacing constraints
08 Grid Viability & Friction    → station↔substation matching, grid status classification
09 Output Generation            → File_1.csv, File_2.csv, File_3.csv
10 Visualization Export         → Folium interactive map → visualization/bi_map.html
```

Notebooks 06–10 are stubs awaiting implementation. Notebooks 01–05 are fully implemented.

### Source Modules (`src/`)
- **`constants.py`** — Single source of truth for all thresholds, spacing rules, output schemas
- **`data_loading.py`** — Dataset loaders handling Spanish locale (`;` delimiters, `,` decimals), UTM→WGS84 transforms, DATEX II XML parsing
- **`geo_utils.py`** — Spatial helpers (`haversine_distance`; `find_nearest_substation` and `snap_point_to_road` are TODO stubs)
- **`grid_analysis.py`** — `classify_grid_status()`: Sufficient (≥5 MW), Moderate (1–5 MW), Congested (<1 MW)
- **`optimization.py`** — `calculate_chargers_needed()` implemented; placement algorithms are TODO stubs

### Data Conventions
- `data/raw/` — Unprocessed source files (various encodings: UTF-8-sig, Latin-1)
- `data/processed/` — Cleaned outputs ready for analysis
- `.parquet` for large geospatial data, `.geojson` for geographic features, `.csv` for smaller tables
- Grid capacity CSVs use Spanish locale: semicolon delimiters, comma decimals — use `_parse_spanish_float()` from `data_loading.py`
- UTM coordinates (EPSG:25830) must be converted to WGS84 (EPSG:4326) via `_utm_to_wgs84()`

## Critical Domain Knowledge

**Grid saturation is real, not a data error:** 86.2% of 4,990 substations show 0 MW available capacity. By DSO: i-DE 92%, Endesa 81%, Viesgo 64%. This is the central strategic insight.

**AFIR spacing rules (legally binding):**
- TEN-T Core corridors → 60 km max spacing
- TEN-T Comprehensive → 100 km max spacing
- Other interurban → 120 km max spacing (project assumption)

**Mandatory datathon constraints:**
- `total_ev_projected_2027 = 2,498,159` (non-negotiable SARIMA output)
- `POWER_PER_CHARGER_KW = 150` (fixed across all teams)
- Only AP-, A-, N- road types (interurban filter)
- File_3 (friction points) must contain only Moderate + Congested, never Sufficient

## Output Schemas

- **File_1.csv** (1 row): `total_proposed_stations, total_existing_stations_baseline, total_friction_points, total_ev_projected_2027`
- **File_2.csv**: `location_id, latitude, longitude, route_segment, n_chargers_proposed, grid_status`
- **File_3.csv**: `bottleneck_id, latitude, longitude, route_segment, distributor_network, estimated_demand_kw, grid_status`

## Key References

- `references/assumptions.md` — 25+ assumptions with research citations and justifications
- `references/glossary.md` — 62 domain-specific terms (AFIR, TEN-T, DSO, IMD, NAP, etc.)
- `references/sources.md` — All data sources with URLs and local file paths
- `references/data_gap_audit.md` — Known data gaps and mitigation strategies
