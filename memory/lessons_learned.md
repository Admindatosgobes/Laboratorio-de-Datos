# Lessons Learned

## NotebookEdit insertion order

When inserting multiple cells with `NotebookEdit edit_mode=insert`, each new cell lands immediately after the anchor cell, not at the end. This reverses the intended order.

**Best practice:** After each insert, re-read the notebook to find the new cell's ID, then insert the next cell after it. For notebooks with 5+ new cells, writing the entire `.ipynb` JSON with the `Write` tool is faster and avoids ordering bugs.

---

## constants.py as single source of truth

All 6 `src/` modules and all notebooks import from `constants.py`. Fixing constants cascades automatically — no need to manually patch downstream code. Always fix constants first before touching anything else.

---

## BEV-only demand scaling matters

Applying charging probability to total IMD traffic (as the original code did) overestimates demand because it includes PHEVs and ICE vehicles. The correct chain is:

1. `daily_bev_flow = IMD × EV_penetration_rate × BEV_fraction`  
   (0.0571 × 0.60 = only 3.4% of total IMD is demand-relevant)
2. `chargers = ceil(daily_bev_flow × 0.12 × 0.37 / 20)`

The old code effectively used 0.07 × total traffic, which is ~2× the correct value.

---

## 86.2% grid saturation — strategic narrative

The high proportion of zero-capacity substations is not a data cleaning problem. It is Spain's genuine grid constraint and should be the central slide in the pitch deck. Every proposed station that gets classified as Congested (i.e., the vast majority) represents a grid investment opportunity for Iberdrola.
