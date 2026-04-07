# Task Board

**Last updated:** 2026-04-07 (rev 2)

## Done

- [x] Analyze competitor ABM/sequential papers and apply methodology to our scenario
- [x] Merge `origin/main` (Theo's refactor) with `--allow-unrelated-histories`. Kept our `constants.py`, took Theo's everything else.
- [x] Restore 23 missing constants in `src/constants.py` so all modules import cleanly
- [x] Create `src/abm_demand.py` — parsimonious ABM behavioral demand module
- [x] Update `src/optimization.py` — implement `compute_coverage_gaps()` + `place_stations_greedy()`
- [x] Implement `src/geo_utils.py` stubs — `find_nearest_substation()` + `snap_point_to_road()`
- [x] Run NB03 — interurban roads filtered, IMD attached, TEN-T tagged
- [x] Run NB04 — existing chargers baseline (6,065 stations)
- [x] **Fix NB04 coverage gap detection** — replaced broken centroid-distance logic with linear-referencing approach. 39 gaps now detected (was 0).
- [x] Draft NB06 — Demand Modeling (ABM notebook content present)
- [x] Draft NB07 — Network Optimization notebook content present
- [x] Draft NB08 — Grid Viability & Friction Points notebook content present
- [x] Draft NB09 — Output Generation notebook content present
- [x] Draft NB10 — Visualization Export notebook content present
- [x] Add auxiliary split-track notebooks `06a`–`06d` and `07b`
- [x] Run NB05 — Grid Capacity Consolidation ✅
- [x] Run NB06 — Demand Modeling ✅
- [x] Implement 06a — Deterministic demand baseline (annual average, lower bound)
- [x] Implement 06b — ABM calibration & sensitivity analysis (B1, SOC, seasonal)
- [x] Implement 06c — Monte Carlo ABM simulation (2,000 agents/segment, stochastic cross-check)
- [x] Implement 06d — Demand reconciliation (three-way comparison, NB06 designated authoritative)
- [x] Create memory/ infrastructure

## In Progress

_(none)_

## Pending — critical path

- [ ] Run NB07 — Network Optimization (needs NB04 ✅ + NB06 ✅)
- [ ] Run NB08 — Grid Viability & Friction Points (needs NB05 ✅ + NB07)
- [ ] Run NB09 — Output Generation (needs NB08)
- [ ] Run NB10 — Visualization Export (needs NB09)

## Pending — deliverables

- [ ] Write `report/analytical_report.pdf` (3–5 page executive summary)
- [ ] Create `presentation/pitch.pdf` (max 5-min pitch deck)
- [ ] Decide whether to keep or remove `notebooks/test.ipynb` exploratory notebook
