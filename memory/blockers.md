# Current Blockers

**Last updated:** 2026-04-05
**Updated by:** Claude agent (Phase 0 foundation refresh)

---

## 🚨 High Priority

### Blocker #1: `src/geo_utils.py` stubs
**Issue:** `find_nearest_substation`, `snap_point_to_road`, `get_road_segment_id` raise `NotImplementedError`.
**Impact:** NB 07 and NB 08 cannot run.
**Resolution:** Implement using `sklearn.neighbors.BallTree` with haversine metric (approved per assumption G3).
**Est. fix time:** 4h.

### Blocker #2: `src/optimization.py` stubs
**Issue:** `compute_coverage_gaps`, `place_stations_greedy` raise `NotImplementedError`.
**Impact:** NB 07 (optimisation) cannot run. Greedy baseline needed as MILP fallback.
**Resolution:** Implement greedy interval covering first; add MILP (PuLP) in NB 07 itself.
**Est. fix time:** 5h.

### Blocker #3: NB 03, 04, 05 execution counts null
**Issue:** Code is written and processed outputs exist in `data/processed/`, but notebook cells show no execution counts. Brief §5.1 disqualifies submissions whose cell outputs are not fully visible.
**Impact:** Eligibility risk on submission day.
**Resolution:** Open each notebook, Restart & Run All, commit the executed `.ipynb` with all outputs embedded.
**Est. fix time:** 3h total.

---

## 🔶 Medium Priority

### Blocker #4: ABM framework choice not locked in
**Issue:** Mesa vs vectorised numpy not decided. Mesa is more explainable to judges; numpy is faster to iterate.
**Impact:** Track B cannot start NB 06b.
**Resolution:** Team call — recommend Mesa for MVP (explainability > speed at this stage).
**Est. fix time:** 30 min decision + spike.

### Blocker #5: OD pair source for ABM
**Issue:** ABM needs origin-destination trip pairs. No real OD matrix in repo.
**Impact:** Track B must synthesise OD from province populations + tourism seasonality.
**Resolution:** Sample OD weighted by INE `population_municipal.csv` × `tourism_seasonal.csv`. Document as assumption in report ("data gap → synthetic OD, proposed survey partnership to close").
**Est. fix time:** 3h.

---

## 🟢 Resolved

| Blocker | Resolved | How |
|---|---|---|
| Constants drift (constants.py ↔ assumptions.md) | 2026-04-05 | Phase 0 — constants.py rewritten, all assumption IDs cited |
| Rutas por Carretera download | pre-2026-04-05 | Data now in `data/raw/` |
| Grid capacity consolidation | pre-2026-04-05 | `data/processed/grid_capacity_unified.csv` exists |
| Data structure understanding | 2026-03-17 | Ministry API + file formats confirmed |
| Assumption uncertainty | 2026-03-16 | 25+ assumptions researched with citations |

---

## Escalation Path

- Technical implementation blockers (#1, #2): unblock by pairing on src/ stubs before starting NB 06.
- Execution-count hygiene (#3): allocate a single owner, batch all three re-runs in one session.
- Modelling decisions (#4, #5): team sync, document choice in `decisions_log.md`.
