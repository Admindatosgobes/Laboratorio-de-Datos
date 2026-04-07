# Decisions Log

## 2026-04-07 — NB04 Coverage Gap Detection Rewrite

**Decision:** Replaced NB04's centroid-distance gap detection with a linear-referencing-per-route approach.

**Rationale:** Original logic measured `dist(segment_centroid, nearest_charger)` and flagged segments where this exceeded `max_spacing_km`. This always returned 0 gaps because (a) road segments are short (~15 km avg), so every centroid is close to *some* charger, and (b) it asks the wrong question — AFIR violations are about long *inter-charger* stretches along a route, not point-to-point distances. New algorithm: per-route, project each fast charger (≥50 kW) onto the merged route geometry using `shapely.ops.substring`, sort by along-route position, walk consecutive positions including route endpoints, flag any gap > tier threshold.

**Impact:** 39 AFIR gaps detected across 39 routes (12 TEN-T, 27 non-TEN-T), 1,590 km total uncovered. Worst case: N-435 with a 149 km gap. Provides realistic input for NB07 station placement.

---

## 2026-04-07 — Merge with origin/main using `--allow-unrelated-histories`

**Decision:** Merged Theo's `origin/main` (which was a fresh-root snapshot after an accidental empty-tree push) into our local `main`. Kept our `constants.py`, took Theo's version of all other conflicting files (`data_loading.py`, `geo_utils.py`, `optimization.py`, notebooks 03-10, memory files, .gitignore).

**Rationale:** Theo's branch had useful new implementations (`abm_demand.py`, geo_utils functions, optimization functions, split-track notebook scaffolds, processed datasets) but had stripped our researched constants down to a simplified version. Our `constants.py` was backed by `references/assumptions.md` and matched what his modules actually need to import.

**Impact:** Unified repo with both contributions. After merge, restored 23 missing constants in `constants.py` so all `src/` modules import cleanly. Backup branch `backup-local-main` preserved.

---

## 2026-04-06 — Adopted Split-Track Notebook Scaffolds Selectively

**Decision:** Keep the existing integrated `06`–`10` notebooks on `main`, but add the teammate's split-track scaffolds (`06a`–`06d`, `07b`) as auxiliary planning notebooks instead of replacing current files.

**Rationale:** The teammate's `phase1-notebook-scaffolds` branch adds a useful work-division pattern for deterministic vs ABM development, but it assumes an earlier repo state where `src/geo_utils.py`, `src/optimization.py`, and most notebook logic were still stubs. Replacing current notebooks or memory files would regress a more advanced local state.

**Impact:** Team can use the extra notebook split for parallel work without losing the more advanced implementations already present on `main`.

## 2026-04-06 — ABM Methodology Adaptation

**Decision:** Use parsimonious ABM (statistical behavioral model) rather than full individual-vehicle simulation.

**Rationale:** Competitor teams (borrador_proyecto_abm.pdf, borrador_proyecto_secuencial.pdf) used ABM thinking, but we have real IMD traffic data. Full individual-vehicle simulation adds noise without improving accuracy when we already have empirical traffic counts. The key behavioral insight (range anxiety, SOC distribution) is captured by the 12% charging probability parameter (B1) derived from empirical data.

**Formula:** `daily_bev_flow = IMD × 0.0571 × 0.60` where 0.0571 = EV penetration rate and 0.60 = BEV fraction (PHEVs use ICE on highways).

---

## 2026-04-06 — Sequential Greedy over LP Set Cover

**Decision:** Replace the LP Set Cover approach (original plan) with sequential greedy placement.

**Rationale:** Sequential greedy naturally produces a "deployment sequence" narrative useful for the pitch. It also respects residual demand updates after each station placement. Scoring: `V_i = n_chargers_needed × gap_length_km`.

---

## 2026-04-06 — AFIR Three-Tier Spacing

**Decision:** Use legally binding AFIR tiered spacing: TEN-T Core 60 km, TEN-T Comprehensive 100 km, General interurban 120 km.

**Rationale:** Single flat threshold was not AFIR-compliant. The brief requires AFIR compliance.

---

## 2026-04-06 — Constants Correction

**Decision:** Corrected 8 values in `src/constants.py` that diverged from `references/assumptions.md`.

| Parameter | Old | New | Source |
|---|---|---|---|
| CHARGING_PROBABILITY | 0.07 | 0.12 | B1 |
| AVG_CHARGE_DURATION_HOURS | 0.4 | 0.37 | B2 |
| EFFECTIVE_OPERATING_HOURS | 18 | 20 | B3 |
| AVG_EV_RANGE_KM | 300 | 340 | A1 |
| USABLE_RANGE_FACTOR | 0.80 | 0.75 | A2 |
| EFFECTIVE_RANGE_KM | 240 | 255 | = 340×0.75 |
| MAX_STATION_SPACING_KM | 150 | 120 | C1 |

---

## 2026-04-06 — Grid Saturation is Real

**Decision:** Treat 86.2% substation saturation (0 MW available) as authentic data, not errors.

**Rationale:** Consistent across all 3 DSOs (i-DE 92%, Endesa 81%, Viesgo 64%). This is Spain's actual grid constraint. All stations at 0 MW capacity substations are classified as Congested → friction points. This is the central strategic finding.
