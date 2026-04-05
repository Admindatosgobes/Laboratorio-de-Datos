# Project State Dashboard

**Last updated:** 2026-04-05
**Updated by:** Claude agent (Phase 0 foundation refresh)

## Current Status: Data acquired, pipeline in build-out (M1 → M2)

**Overall progress:** Data ingestion done, demand/optimisation notebooks not yet built.

---

## Completed ✅

### Research & Planning
- Assumptions research (25+ entries) approved and documented in `references/assumptions.md`
- Glossary (62 terms), sources, data-gap audit, GitHub roadmap all committed under `references/`
- Core strategic insight confirmed from data: **86.2% of 4,990 substations show 0 MW available capacity** (i-DE 92%, Endesa 81%, Viesgo 64%) — this is the central friction-point narrative.

### Data Acquisition
- All mandatory raw datasets downloaded: Ministry roads, NAP chargers, i-DE / Endesa / Viesgo grid capacity, DGT monthly registrations (2014–2026), datos.gob.es EV projection fork.
- Additional sources acquired: DGT IMD traffic, INE population + tourism seasonal, REE demand profiles + grid, OSM service areas, TEN-T corridor geometries, gas stations.

### Data Pipeline
- **NB 01** (ingestion & cleaning): implemented and executed — produces 14 processed files under `data/processed/`.
- **NB 02** (EV projection fork): implemented, partially executed — `ev_projection_2027.csv` generated, mandatory output `total_ev_projected_2027 = 2,498,159`.
- **NB 03, 04, 05** (roads, chargers baseline, grid consolidation): implemented in code, outputs exist in `data/processed/`, **execution counts are null in the .ipynb — need re-run with visible outputs to comply with brief §5.1**.

### Foundation (Phase 0 — 2026-04-05)
- `src/constants.py` **synced with `references/assumptions.md`** — all approved values now reflected (range 340 km, effective 255 km, tiered spacing 60/100/120 km, charging probability 12%, operating hours 20, AFIR min-chargers 4, CAPEX bands, etc.). Backwards-compat aliases kept for `MAX_STATION_SPACING_KM` and `AFIR_SPACING_KM`.
- Memory files refreshed to match reality.
- `notebooks/test.ipynb` removed.

---

## In Progress 🔄

*(nothing actively in progress at time of write — next session picks up from "To Do" below)*

---

## To Do 📋

### Phase 1 — Source-code stubs (blocking modelling work)
- [ ] Implement `src/geo_utils.py` stubs: `find_nearest_substation` (BallTree + haversine), `snap_point_to_road`, `get_road_segment_id`.
- [ ] Implement `src/optimization.py` stubs: `compute_coverage_gaps`, `place_stations_greedy` (greedy baseline before MILP).
- [ ] Re-execute NB 03, 04, 05 top-to-bottom so all cells have visible outputs (brief §5.1 DQ criterion).

### Phase 2 — Demand modelling (parallel: two tracks)
- **Track A (deterministic, critical-path):**
  - [ ] NB 06a — deterministic demand per segment from IMD × BEV share × charging prob.
- **Track B (ABM, differentiator):**
  - [ ] NB 06b — ABM calibration (tune trip generation rates against IMD ground truth).
  - [ ] NB 06c — ABM demand simulation (stochastic charging events per segment).
- [ ] NB 06d — reconciliation (compare deterministic vs ABM, pick primary for NB 07).

### Phase 3 — Optimisation & validation
- [ ] NB 07 — MILP Set Cover (PuLP / OR-Tools) + greedy baseline + tiered AFIR spacing.
- [ ] NB 07b — ABM re-run against proposed network → utilisation / queueing KPIs.

### Phase 4 — Grid integration & deliverables
- [ ] NB 08 — spatial join stations ↔ substations, grid_status classification, friction points.
- [ ] NB 09 — generate File_1.csv, File_2.csv, File_3.csv in exact mandated schema + validation.
- [ ] NB 10 — Folium self-contained interactive map.
- [ ] Analytical report (3–5 pp).
- [ ] Pitch deck (≤5 min).

---

## Key Files Status

| Component | Status | Location | Notes |
|---|---|---|---|
| Raw data | ✅ Complete | `data/raw/` | All mandatory + additional sources |
| Processed data | ✅ Complete | `data/processed/` | 14 clean files incl. `roads_clean.parquet`, `grid_capacity_unified.csv` |
| NB 01 ingestion | ✅ Executed | `notebooks/01_*.ipynb` | |
| NB 02 EV projection | ✅ Executed (partial) | `notebooks/02_*.ipynb` | Output: 2,498,159 |
| NB 03–05 | ⚠️ Code written, execution counts null | `notebooks/03_*.ipynb`, `04_*.ipynb`, `05_*.ipynb` | Re-run needed |
| NB 06–10 | ❌ Stubs only | `notebooks/06_*.ipynb` … `10_*.ipynb` | Empty |
| `src/constants.py` | ✅ Synced with assumptions | `src/constants.py` | Refreshed 2026-04-05 |
| `src/geo_utils.py` | ❌ NotImplementedError stubs | `src/geo_utils.py` | Blocks NB 07, 08 |
| `src/optimization.py` | ❌ NotImplementedError stubs | `src/optimization.py` | Blocks NB 07 |
| `src/grid_analysis.py` | ✅ Implemented | `src/grid_analysis.py` | `classify_grid_status` works |
| `src/data_loading.py` | ✅ Implemented | `src/data_loading.py` | 393 lines, Spanish-locale handling |
| File_1/2/3.csv | ❌ Headers only | `output/` | Awaiting NB 09 |

---

## Next Priority Actions

1. Re-execute NB 03, 04, 05 with visible outputs committed.
2. Implement `src/geo_utils.py` and `src/optimization.py` stubs (greedy first).
3. Split team into deterministic (Track A) and ABM (Track B) pairs for NB 06.
4. Build MILP formulation for NB 07.

---

## Risk Watch 🚨

- **Execution-count hygiene** — brief §5.1 disqualifies teams without fully visible notebook outputs.
- **ABM time-box** — hard deadline (~3 days) for MVP; if not producing segment demand, fall back to deterministic alone.
- **File_3 scope rule** — `grid_status = 'Sufficient'` in File_3 is an automatic DQ. Add validation to NB 09.
- **150 kW fixed** — `estimated_demand_kw = n_chargers × 150` is a DQ criterion. Use only `POWER_PER_CHARGER_KW` from constants.
- **Communication weight** — report + pitch = 50% of grade. Reserve final 2 days.
