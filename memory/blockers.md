# Blockers

## Active Blockers

- `notebooks/03_road_network_analysis.ipynb` is malformed JSON and cannot be opened reliably in notebook tooling.
- Several `src/` modules and notebooks still reference pre-refactor constant names that no longer exist in `src/constants.py` (for example `EV_FLEET_2027`, `BEV_FRACTION`, `MIN_CHARGERS_STANDARD`, `MIN_EXISTING_CHARGER_POWER_KW`, `SUBSTATION_DIST_OPTIMAL_KM`).
- The repo contains placeholder submission outputs (`output/File_1.csv`–`File_3.csv`) but no populated NB06–NB10 outputs yet.
- `visualization/bi_map.html` is referenced by docs, but has not been generated.
- `notebooks/test.ipynb` is still present as an exploratory notebook and may not belong in the final submission set.

---

## Resolved Blockers

### [RESOLVED] NotebookEdit insertion order

**Issue:** When using `NotebookEdit` with `edit_mode=insert`, inserting multiple cells after the same cell_id causes them to appear in reverse order (each new cell is inserted immediately after the anchor, pushing previous inserts down).

**Fix:** Always insert in sequential order: write cell N+1 → read to find its new ID → insert N+2 after that new ID. Or: write entire notebook as raw JSON using the `Write` tool for complex multi-cell implementations.

---

### [RESOLVED] constants.py drift from assumptions.md

**Issue:** 8 parameters in `src/constants.py` had incorrect values that diverged from `references/assumptions.md`. All downstream notebooks inherited wrong calculations.

**Fix:** Corrected all 8 values + added 15 new constants. Execute constants fix before any notebook work.
