# Task Board

**Last updated:** 2026-04-06

## Done

- [x] Analyze competitor ABM/sequential papers and apply methodology to our scenario
- [x] Fix `src/constants.py` — 8 corrections + 15 new constants aligned with `references/assumptions.md`
- [x] Create `src/abm_demand.py` — parsimonious ABM behavioral demand module
- [x] Update `src/optimization.py` — implement `compute_coverage_gaps()` + `place_stations_greedy()`
- [x] Implement `src/geo_utils.py` stubs — `find_nearest_substation()` + `snap_point_to_road()`
- [x] Draft NB06 — Demand Modeling (ABM notebook content present)
- [x] Draft NB07 — Network Optimization notebook content present
- [x] Draft NB08 — Grid Viability & Friction Points notebook content present
- [x] Draft NB09 — Output Generation notebook content present
- [x] Draft NB10 — Visualization Export notebook content present
- [x] Add auxiliary split-track notebooks `06a`–`06d` and `07b`
- [x] Create memory/ infrastructure

## In Progress

_(none)_

## Pending

- [ ] Fix notebook/module imports that still reference stale `src.constants.py` names after the constants refactor
- [ ] Repair `notebooks/03_road_network_analysis.ipynb` — file is malformed JSON
- [ ] Run NB04–NB10 and verify outputs are populated instead of header-only placeholders
- [ ] Decide whether to keep or remove `notebooks/test.ipynb` exploratory notebook
- [ ] Run NB06–NB10 end-to-end and verify all output files
- [ ] Write `report/analytical_report.pdf` (3–5 page executive summary)
- [ ] Create `presentation/pitch.pdf` (max 5-min pitch deck)
