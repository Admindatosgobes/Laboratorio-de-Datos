# Blockers

## Active Blockers

_(none — pipeline is fully implemented)_

---

## Resolved Blockers

### [RESOLVED] NotebookEdit insertion order

**Issue:** When using `NotebookEdit` with `edit_mode=insert`, inserting multiple cells after the same cell_id causes them to appear in reverse order (each new cell is inserted immediately after the anchor, pushing previous inserts down).

**Fix:** Always insert in sequential order: write cell N+1 → read to find its new ID → insert N+2 after that new ID. Or: write entire notebook as raw JSON using the `Write` tool for complex multi-cell implementations.

---

### [RESOLVED] constants.py drift from assumptions.md

**Issue:** 8 parameters in `src/constants.py` had incorrect values that diverged from `references/assumptions.md`. All downstream notebooks inherited wrong calculations.

**Fix:** Corrected all 8 values + added 15 new constants. Execute constants fix before any notebook work.
