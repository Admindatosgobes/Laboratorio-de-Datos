# Project Structure

```
iberdrola-ev-network/
├── notebooks/                  # Main pipeline — execute 00 → 10 sequentially
│   ├── 00_environment_setup.ipynb
│   ├── 01_data_ingestion.ipynb       ✅ fully implemented
│   ├── 02_ev_projection.ipynb        ✅ fully implemented (SARIMA → 2,498,159)
│   ├── 03_road_network_analysis.ipynb ✅ fully implemented
│   ├── 04_existing_chargers_baseline.ipynb ✅ fully implemented
│   ├── 05_grid_capacity.ipynb        ✅ fully implemented
│   ├── 06_demand_modeling.ipynb      ✅ ABM demand (IMD × penetration × BEV)
│   ├── 07_network_optimization.ipynb ✅ Sequential greedy placement
│   ├── 08_grid_viability_friction.ipynb ✅ BallTree substation matching
│   ├── 09_output_generation.ipynb    ✅ File_1/2/3 + compliance checks
│   └── 10_visualization_export.ipynb ✅ Folium map → visualization/bi_map.html
│
├── src/                        # Shared Python modules
│   ├── constants.py            ✅ Single source of truth (all params corrected)
│   ├── abm_demand.py           ✅ ABM behavioral demand model (NEW)
│   ├── optimization.py         ✅ Coverage gaps + greedy placement (implemented)
│   ├── geo_utils.py            ✅ Substation matching + road snapping (implemented)
│   ├── grid_analysis.py        ✅ Grid status classification (pre-existing)
│   └── data_loading.py         ✅ Spanish locale CSV loading (pre-existing)
│
├── data/
│   ├── raw/                    # Original downloads (never modify)
│   └── processed/              # Pipeline outputs
│       ├── interurban_roads.parquet
│       ├── interurban_chargers_baseline.csv
│       ├── grid_capacity_unified.csv
│       ├── ev_projection_2027.csv
│       ├── demand_per_segment.csv        ← NB06 output
│       ├── proposed_stations.csv         ← NB07 output
│       ├── stations_with_grid_status.csv ← NB08 output
│       └── friction_points.csv           ← NB08 output
│
├── output/                     # Submission deliverables
│   ├── File_1.csv              ← NB09 output (1 row: global KPIs)
│   ├── File_2.csv              ← NB09 output (all proposed stations)
│   └── File_3.csv              ← NB09 output (friction points only)
│
├── visualization/
│   └── bi_map.html             ← NB10 output (interactive Folium map)
│
├── references/
│   ├── assumptions.md          # 25+ assumptions — source of truth
│   ├── glossary.md             # 62 domain terms
│   ├── sources.md              # All data sources
│   └── data_gap_audit.md       # Known gaps + mitigations
│
├── memory/                     # Agent memory (this directory)
│   ├── project_state.md
│   ├── task_board.md
│   ├── decisions_log.md
│   ├── blockers.md
│   ├── lessons_learned.md
│   └── project_structure.md    ← this file
│
├── CLAUDE.md                   # Project intelligence for Claude Code
└── requirements.txt
```

## Data Flow

```
NB01-05 (data prep)
    ↓
NB06: demand_per_segment.csv  (IMD → BEV flow → charger count)
    ↓
NB07: proposed_stations.csv   (AFIR gap detection → greedy placement)
    ↓
NB08: stations_with_grid_status.csv + friction_points.csv
    ↓
NB09: File_1.csv + File_2.csv + File_3.csv
    ↓
NB10: visualization/bi_map.html
```
