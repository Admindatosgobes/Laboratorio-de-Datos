# Decisions Log

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
