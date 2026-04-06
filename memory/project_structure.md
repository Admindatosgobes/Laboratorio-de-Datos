# Project Structure

```
iberdrola-ev-network/
├── notebooks/                  # Main pipeline notebooks + auxiliary split-track notebooks
│   ├── 01_data_ingestion_and_cleaning.ipynb   ✅ executed
│   ├── 03_road_network_analysis.ipynb         ❌ malformed JSON
│   ├── 04_existing_chargers_baseline.ipynb    ⚠️ present, not executed
│   ├── 05_grid_capacity_consolidation.ipynb   ⚠️ present, not executed
│   ├── 06_demand_modeling.ipynb               ⚠️ drafted, not executed
│   ├── 06a_demand_deterministic.ipynb         ⚠️ auxiliary scaffold
│   ├── 06b_abm_calibration.ipynb              ⚠️ auxiliary scaffold
│   ├── 06c_abm_demand_simulation.ipynb        ⚠️ auxiliary scaffold
│   ├── 06d_demand_reconciliation.ipynb        ⚠️ auxiliary scaffold
│   ├── 07_network_optimization.ipynb          ⚠️ drafted, not executed
│   ├── 07b_abm_validation.ipynb               ⚠️ auxiliary scaffold
│   ├── 08_grid_viability_friction.ipynb       ⚠️ drafted, not executed
│   ├── 09_output_generation.ipynb             ⚠️ drafted, not executed
│   ├── 10_visualization_export.ipynb          ⚠️ drafted, not executed
│   └── test.ipynb                             ⚠️ exploratory notebook, decision pending
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
│   └── processed/              # Available processed datasets
│       ├── interurban_roads.parquet
│       ├── interurban_chargers_baseline.csv
│       ├── grid_capacity_unified.csv
│       ├── ev_projection_2027.csv
│       ├── roads_clean.parquet
│       ├── imd_traffic_clean.geojson
│       ├── service_areas_clean.geojson
│       ├── population_municipal.csv
│       └── tourism_seasonal.csv
│
├── output/                     # Submission deliverables
│   ├── File_1.csv              ← currently header-only placeholder
│   ├── File_2.csv              ← currently header-only placeholder
│   └── File_3.csv              ← currently header-only placeholder
│
├── visualization/
│   └── (empty)                 # `bi_map.html` not yet generated
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
NB01 / 03 / 04 / 05 (data prep)
    ↓
NB06: demand_per_segment.csv  (planned: IMD → BEV flow → charger count)
    ↓
NB07: proposed_stations.csv   (planned: AFIR gap detection → greedy placement)
    ↓
NB08: stations_with_grid_status.csv + friction_points.csv  (planned)
    ↓
NB09: File_1.csv + File_2.csv + File_3.csv  (planned)
    ↓
NB10: visualization/bi_map.html  (planned)
```
