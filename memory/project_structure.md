# Project Structure

**Last updated:** 2026-03-17  

---

## Repository Layout

```
iberdrola-ev-network/
├── CLAUDE.md                    # Agent coordination (auto-loaded)
├── README.md                    # Project overview
├── requirements.txt             # Python dependencies
├── .venv/                       # Virtual environment
├── .gitignore                   # Git exclusions
│
├── notebooks/                   # Analysis pipeline (sequential execution)
│   ├── 00_environment_setup.ipynb
│   ├── 01_data_ingestion_and_cleaning.ipynb      # ✅ Complete
│   ├── 02_ev_projection_fork.ipynb               # 🔄 Partially run  
│   ├── 03_road_network_analysis.ipynb            # 📝 Written, not executed
│   ├── 04_existing_chargers_baseline.ipynb       # 📝 Written, not executed
│   ├── 05_grid_capacity_consolidation.ipynb      # 📝 Written, not executed
│   ├── 06_demand_modeling.ipynb                  # 📝 Stub only
│   ├── 07_network_optimization.ipynb             # 📝 Stub only
│   ├── 08_grid_viability_friction.ipynb          # 📝 Stub only
│   ├── 09_output_generation.ipynb                # 📝 Stub only
│   ├── 10_visualization_export.ipynb             # 📝 Stub only
│   └── test.ipynb                                # Development sandbox
│
├── src/                         # Shared utilities
│   ├── __init__.py
│   ├── constants.py             # ⚠️ OUTDATED - needs assumptions.md sync
│   ├── data_loading.py          # ✅ Complete
│   ├── grid_analysis.py         # ✅ Complete  
│   ├── geo_utils.py             # ⚠️ 3/4 functions NotImplemented
│   └── optimization.py          # ⚠️ 2/3 functions NotImplemented
│
├── scripts/                     # Standalone execution scripts
│   └── download_rutas.py        # 📝 Planned (issue #4)
│
├── data/                        # Data pipeline
│   ├── raw/                     # Original downloads (92 MB)
│   │   ├── datos_gob_ev_forecast/           # EV registrations 2015-2026
│   │   ├── dgt_registrations/               # Vehicle registrations
│   │   ├── grid_capacity/                   # i-DE, Endesa, Viesgo substations
│   │   ├── ministry_roads/                  # Hermes road network
│   │   ├── nap_charging_points/             # National charging registry
│   │   ├── trips_people_overnight_pyspainmobility/  # Jan 2022 OD matrix
│   │   └── additional/                      # Tourism, gas stations, boundaries
│   └── processed/               # Cleaned, ready-to-use (smaller files)
│       ├── ev_projection_2027.csv           # SARIMA output
│       ├── roads_clean.geojson              # Filtered road network
│       ├── chargers_clean.csv               # NAP processed
│       ├── grid_capacity_unified.csv        # All DSOs combined
│       ├── imd_traffic_clean.geojson        # Traffic stations
│       └── [others]
│
├── output/                      # Final deliverables
│   ├── File_1.csv              # 📝 Placeholder (global KPIs)
│   ├── File_2.csv              # 📝 Placeholder (proposed stations)
│   ├── File_3.csv              # 📝 Placeholder (friction points)
│   ├── visualization/          # Interactive map
│   ├── report/                 # Analytical report (3-5 pages)
│   └── presentation/           # Pitch deck (5 min max)
│
├── references/                  # Documentation & research
│   ├── assumptions.md          # ✅ 20 assumptions researched & approved
│   ├── glossary.md             # ✅ 49 acronyms defined
│   ├── github_roadmap.md       # ✅ 39 issues across 4 milestones  
│   ├── sources.md              # Data source inventory
│   ├── data_gap_audit.md       # Data availability assessment
│   ├── brief.pdf               # Original datathon brief
│   └── articles/               # Research papers (Wu et al., Liao et al.)
│
├── memory/                     # Agent coordination (shared state)
│   ├── project_state.md        # ✅ Current status dashboard
│   ├── task_board.md           # ✅ Kanban-style task tracking  
│   ├── decisions_log.md        # ✅ Key decisions with rationale
│   ├── blockers.md             # ✅ Current issues & resolution
│   ├── lessons_learned.md      # ✅ What worked, what didn't
│   └── project_structure.md    # ✅ This file
│
└── .claude/                    # Agent configuration
    └── rules/                  # 📝 Planned
        ├── code_standards.md   # Python style, docstrings
        ├── data_conventions.md # File formats, naming
        └── notebook_rules.md   # Cell execution, output standards
```

---

## Data Flow Pipeline

```
                          INPUTS                                 PROCESSING                               OUTPUTS
                                                                                                  
┌─────────────────────┐   ┌──────────────────────────────┐   ┌─────────────────────────────────────┐   ┌──────────────────┐
│ Rutas por Carretera │──▶│ NB 06: Demand Model          │──▶│ demand_per_segment.parquet          │──▶│ File_2.csv       │
│ (3 reference dates) │   │ - Segment flows              │   │ - daily_ev_trips per road segment  │   │ (proposed        │
└─────────────────────┘   │ - EV scaling (5.7% × 60%)   │   │ - n_chargers_needed                 │   │  stations)       │
                          │ - Seasonal correction        │   └─────────────────────────────────────┘   │                  │
┌─────────────────────┐   └──────────────────────────────┘                                               │                  │
│ Service Areas +     │                                        ┌─────────────────────────────────────┐   │                  │
│ Gas Stations +      │──────────────────────────────────────▶│ NB 07: Network Optimization        │──▶│                  │
│ Existing Chargers   │                                        │ - Candidate locations              │   │                  │
└─────────────────────┘                                        │ - Set Cover LP (60/100/120km)      │   │                  │
                                                               │ - Station sizing                   │   │                  │
┌─────────────────────┐   ┌──────────────────────────────┐   │ - Gap filling                      │   │                  │
│ Grid Substations    │──▶│ NB 08: Grid Viability        │──▶│                                     │──▶│                  │
│ (i-DE+Endesa+Viesgo)│   │ - BallTree nearest neighbor  │   └─────────────────────────────────────┘   └──────────────────┘
└─────────────────────┘   │ - Distance classification    │                                              
                          │ - Sufficient/Moderate/       │   ┌─────────────────────────────────────┐   ┌──────────────────┐
┌─────────────────────┐   │   Congested                  │──▶│ Grid-enriched proposed stations     │──▶│ File_3.csv       │
│ EV Projection       │   └──────────────────────────────┘   └─────────────────────────────────────┘   │ (friction points)│
│ (SARIMA 2027)       │                                                                                  └──────────────────┘
└─────────────────────┘                                        ┌─────────────────────────────────────┐   
                                                               │ NB 09: Output Generation           │   ┌──────────────────┐
                          ┌──────────────────────────────┐   │ - Aggregate KPIs                   │──▶│ File_1.csv       │
                          │ NB 10: Visualization         │──▶│ - Schema validation                 │   │ (global KPIs)    │
                          │ - Folium interactive map     │   └─────────────────────────────────────┘   └──────────────────┘
                          │ - Station markers            │                                              
                          │ - Grid status colors         │   ┌─────────────────────────────────────┐   ┌──────────────────┐
                          │ - TEN-T corridors            │──▶│ Interactive Map                     │──▶│ bi_map.html      │
                          │ - Traffic heatmaps           │   └─────────────────────────────────────┘   └──────────────────┘
                          └──────────────────────────────┘   
```

---

## Key Dependencies

**Critical Path (cannot slip):**
1. `scripts/download_rutas.py` → all modeling work
2. Update `src/constants.py` → NB 06-08 execution  
3. NB 06 demand model → NB 07 optimization
4. NB 07 optimization → NB 08 grid analysis
5. NB 08 grid analysis → NB 09 outputs

**Parallel Work (can happen simultaneously):**
- Additional data acquisition (elevation, weather) 
- Analytical report writing (methodology sections)
- Code utilities implementation (`geo_utils.py`, `optimization.py`)
- Pipeline execution (NB 02-05)

---

## File Conventions

### Naming
- **Notebooks:** `NN_descriptive_name.ipynb` (sequential numbering)
- **Data raw:** `source_dataset_YYYY-MM-DD.ext` 
- **Data processed:** `descriptive_name_clean.ext`
- **Scripts:** `verb_noun.py` (e.g., `download_rutas.py`)

### Formats
- **Working data:** Parquet (columnar, compressed, fast)
- **Geospatial:** GeoParquet for working, GeoJSON for final outputs
- **Configs:** YAML where possible, JSON for compatibility
- **Output:** CSV for datathon submission (required format)

### Git
- **Commit notebooks:** With outputs visible (crucial for handoffs)
- **Branch naming:** `feat/task-description`, `fix/issue-description` 
- **No commits:** Large raw data files, virtual environments
- **Do commit:** Processed data <10MB, documentation, configuration