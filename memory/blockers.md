# Blockers

## Active Blockers

_(none — pipeline is unblocked, NB05 onwards ready to execute)_

---

## Resolved Blockers

### [RESOLVED 2026-04-07] NB04 coverage gap detection broken (centroid-distance logic)

**Issue:** Original NB04 cell 8 measured distance from each road segment's centroid to the nearest charger, marking the segment as a gap if `dist > max_spacing_km`. This always returned **0 gaps / 1,295 segments** because (a) the road network is split into many short segments (~10–20 km each), so every centroid is within a few km of some charger, and (b) the method asks the wrong question — it tests whether *some* charger is near the centroid, not whether there is a long *inter-charger stretch* along the route.

**Example of failure:** N-435 has only 2 fast chargers, both clustered in the first 48 km of a 200 km route. The remaining 149 km has zero coverage but the old method passed it because every short segment's centroid was "near" one of those 2 chargers.

**Fix:** Rewrote cell 8 to use linear referencing per route:
1. Filter chargers to ≥50 kW (only fast chargers count for AFIR coverage)
2. Group road segments by `Carretera` and merge geometries into one continuous line
3. Project each fast charger onto the merged line using `shapely.ops.substring`
4. Walk consecutive positions (including route endpoints km 0 and km L)
5. Flag any inter-charger gap > AFIR threshold (60 km TEN-T, 120 km other)
6. Build the gap geometry as a substring of the route line

**Result:** 39 gaps detected across 39 routes (12 TEN-T, 27 non-TEN-T), 1,590 km total uncovered length.

---

### [RESOLVED 2026-04-07] 23 missing constants in `src/constants.py` after merge

**Issue:** After merging `origin/main` with `--allow-unrelated-histories`, we kept our local `constants.py` (researched values) but took Theo's `abm_demand.py`, `geo_utils.py`, and `optimization.py`. Theo's modules imported 23 constants that our `constants.py` didn't define (`EV_PENETRATION_RATE`, `BEV_FRACTION`, `SOC_MEAN`, `MIN_CHARGERS_TENT`, `SUBSTATION_DIST_OPTIMAL_KM`, `MEDITERRANEAN_ROADS`, `ATLANTIC_ROADS`, etc.). All downstream notebooks would have failed to import.

**Fix:** Restored the 23 constants in `constants.py` using values from `references/assumptions.md`. Verified all 5 src modules now import cleanly.

---

### [RESOLVED 2026-04-07] False claim that NB03 is malformed JSON

**Issue:** `memory/blockers.md` (Theo's branch) claimed `notebooks/03_road_network_analysis.ipynb` was malformed JSON and could not be parsed.

**Fix:** Verified the notebook is valid JSON and ran it successfully. Original claim was wrong; removed from blockers.

---

### [RESOLVED] NotebookEdit insertion order

**Issue:** When using `NotebookEdit` with `edit_mode=insert`, inserting multiple cells after the same cell_id causes them to appear in reverse order.

**Fix:** Always insert in sequential order: write cell N+1 → read to find its new ID → insert N+2 after that new ID.

---

### [RESOLVED] constants.py drift from assumptions.md

**Issue:** 8 parameters in `src/constants.py` had incorrect values that diverged from `references/assumptions.md`.

**Fix:** Corrected all 8 values + added 15 new constants. Execute constants fix before any notebook work.
