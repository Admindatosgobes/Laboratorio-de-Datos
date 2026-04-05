# Task Board

**Last updated:** 2026-04-05
**Updated by:** Claude agent (Phase 0 foundation refresh)

---

## 🔄 In Progress

*(none — Phase 0 just completed; next session picks up from "Ready" below)*

---

## 📋 To Do — Ready (unblocked)

### Phase 1 — Source-code stubs & NB re-execution

| Task | Priority | Est. Hours | Blocks | Notes |
|---|---|---|---|---|
| Re-execute NB 03 (roads) with visible outputs | **High** | 1h | Modelling | Brief §5.1 DQ criterion |
| Re-execute NB 04 (chargers baseline) with visible outputs | **High** | 1h | Modelling | Brief §5.1 DQ criterion |
| Re-execute NB 05 (grid consolidation) with visible outputs | **High** | 1h | NB 08 | Brief §5.1 DQ criterion |
| Implement `src/geo_utils.py` — `find_nearest_substation` (BallTree + haversine) | **High** | 2h | NB 07, 08 | scipy BallTree with haversine metric |
| Implement `src/geo_utils.py` — `snap_point_to_road`, `get_road_segment_id` | **High** | 2h | NB 07 | shapely `nearest_points` |
| Implement `src/optimization.py` — `compute_coverage_gaps` (greedy) | **High** | 3h | NB 07 | Greedy interval covering baseline |
| Implement `src/optimization.py` — `place_stations_greedy` | **High** | 2h | NB 07 | Fallback for MILP |

---

## 📋 To Do — Blocked (waiting on Phase 1)

### Phase 2 — Demand modelling (parallel tracks)

| Task | Priority | Est. Hours | Blocked By | Notes |
|---|---|---|---|---|
| NB 06a — deterministic demand (Track A) | **High** | 6h | Phase 1 done | IMD × BEV share × charging prob → demand per segment |
| NB 06b — ABM calibration (Track B) | Medium | 8h | Phase 1 done | Tune trip gen to IMD; Mesa or numpy |
| NB 06c — ABM demand simulation (Track B) | Medium | 10h | 06b | ~5–10k agents, 15-min ticks, 1 day |
| NB 06d — deterministic/ABM reconciliation | Medium | 4h | 06a + 06c | Report-centrepiece notebook |

### Phase 3 — Optimisation & validation

| Task | Priority | Est. Hours | Blocked By | Notes |
|---|---|---|---|---|
| NB 07 — MILP Set Cover (PuLP) | **High** | 10h | 06d | Tiered AFIR 60/100/120 km spacing |
| NB 07 — greedy benchmark comparison | Medium | 2h | 07 | "MILP found X, greedy Y, gap Z%" for report |
| NB 07b — ABM validation re-run | Medium | 6h | 07 + 06c | Utilisation + queue KPIs, pitch visual |

### Phase 4 — Grid integration & deliverables

| Task | Priority | Est. Hours | Blocked By | Notes |
|---|---|---|---|---|
| NB 08 — grid viability & friction points | **High** | 6h | 07 | Spatial join stations↔substations |
| NB 09 — File_1/2/3.csv generation + schema validation | **High** | 4h | 08 | Schema compliance = DQ critical |
| NB 10 — Folium self-contained map | **High** | 6h | 09 | Single .html, green/yellow/red |
| Analytical report (3–5 pp) | **High** | 10h | 09 | 50% of grade |
| Pitch deck (≤5 min) | **High** | 8h | Report | Lead with 87% grid saturation insight |

---

## ✅ Completed

| Task | Completed | Notes |
|---|---|---|
| Phase 0 — sync `src/constants.py` with `references/assumptions.md` | 2026-04-05 | All values now reflect approved research |
| Phase 0 — refresh memory files to match reality | 2026-04-05 | state, task_board, blockers all current |
| Phase 0 — remove `notebooks/test.ipynb` | 2026-04-05 | Submission hygiene |
| Data acquisition — all mandatory + additional sources | pre-2026-04-05 | See `references/sources.md` |
| NB 01 — data ingestion & cleaning | pre-2026-04-05 | 14 files in `data/processed/` |
| NB 02 — EV projection fork (mandatory) | pre-2026-04-05 | Output: 2,498,159 EVs |
| Assumptions research (25+ entries) | 2026-03-16 | `references/assumptions.md` |
| GitHub roadmap, glossary, data-gap audit | 2026-03-17 | `references/` folder |

---

## Team Assignment Suggestions (mentor's "divide and conquer")

| Track | Owner(s) | Scope |
|---|---|---|
| **Track A — Deterministic + critical path** | TBD | NB 06a, NB 07 (MILP), NB 09 (outputs), schema validation |
| **Track B — ABM + differentiator** | TBD | NB 06b, 06c, 07b; digital-twin pitch visual |
| **Track C — Grid + viz** | TBD | NB 08, NB 10 (Folium map) |
| **Track D — Communication** | TBD | Analytical report, pitch deck |

Tracks A + C + D are the minimum viable submission. Track B is upside.
