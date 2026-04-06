# Project State

**Last updated:** 2026-04-06  
**Status:** Core `src/` modules are implemented, but notebook/output state is mixed. Repo is not yet in a clean "pipeline fully executed" state.

## What is done

| Component | Status | Notes |
|---|---|---|
| `src/constants.py` | ✅ Done | 8 values corrected, 15 ABM/AFIR constants added |
| `src/abm_demand.py` | ✅ Done | New ABM behavioral demand module |
| `src/optimization.py` | ✅ Done | `compute_coverage_gaps` + `place_stations_greedy` implemented |
| `src/geo_utils.py` | ✅ Done | `find_nearest_substation` + `snap_point_to_road` implemented |
| Notebook / constants compatibility | ❌ Broken | Several notebooks still import stale constant names removed during the constants refactor |
| `01_data_ingestion_and_cleaning.ipynb` | ✅ Executed | Only notebook with populated execution counts |
| `03_road_network_analysis.ipynb` | ❌ Broken | Malformed JSON; notebook does not parse cleanly |
| `04_existing_chargers_baseline.ipynb` | ⚠️ Present | Notebook exists, but not executed |
| `05_grid_capacity_consolidation.ipynb` | ⚠️ Present | Notebook exists, but not executed |
| `06_demand_modeling.ipynb` | ⚠️ Drafted | Notebook content exists, but not executed |
| `07_network_optimization.ipynb` | ⚠️ Drafted | Notebook content exists, but not executed |
| `08_grid_viability_friction.ipynb` | ⚠️ Drafted | Notebook content exists, but not executed |
| `09_output_generation.ipynb` | ⚠️ Drafted | Notebook content exists, but not executed |
| `10_visualization_export.ipynb` | ⚠️ Drafted | Notebook content exists, but not executed |
| Auxiliary notebooks `06a`–`06d`, `07b` | ⚠️ Planning scaffolds | Added for parallel work; intentionally TODO-based |
| `output/File_1`–`File_3` | ⚠️ Placeholder only | Files currently contain headers only |
| `visualization/bi_map.html` | ❌ Missing | Visualization has not yet been generated |

## What still needs to happen

1. **Run the pipeline end-to-end** (NB06 → NB10) to produce actual output files
2. **Repair `notebooks/03_road_network_analysis.ipynb`** so the notebook set is valid
3. **Write analytical report** (`report/analytical_report.pdf`) — 3–5 page executive summary
4. **Build pitch deck** (`presentation/pitch.pdf`) — max 5-minute pitch

## Key output files (after running pipeline)

- `data/processed/demand_per_segment.csv` — ABM demand output
- `data/processed/proposed_stations.csv` — Sequential greedy station placement
- `data/processed/stations_with_grid_status.csv` — Stations + grid classification
- `data/processed/friction_points.csv` — Moderate + Congested only
- `output/File_1.csv`, `output/File_2.csv`, `output/File_3.csv` — Submission deliverables; currently header-only placeholders
- `visualization/bi_map.html` — Interactive Folium map; not yet present
