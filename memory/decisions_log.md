# Decisions Log

**Purpose:** Record all key technical and strategic decisions with rationale and date.

---

## 2026-04-05

### Decision: Run Deterministic + ABM Demand Models in Parallel
**Context:** Choice between single deterministic demand model (original plan) vs adding an agent-based model as a second track.
**Decision:** Build both — deterministic as critical-path guaranteed submission, ABM as differentiator + digital-twin validation. Reconcile in NB 06d, feed blended output to NB 07, re-run ABM against proposed network in NB 07b.
**Rationale:**
- Deterministic model guarantees a complete submission even if ABM fails late.
- ABM captures queueing, driver heterogeneity, temporal peaks — things deterministic can't. Matches mentor's "pitch the idea / digital twin" guidance.
- Triangulation ("both methods converge within X%") is strong T1/T3 scoring material.
- ABM produces the visual centrepiece (driver-flow animation) for the 5-min pitch.
**Impact:** Splits Phase 2 into parallel Track A (deterministic, Person A) and Track B (ABM, Person B). New notebooks: NB 06a, 06b, 06c, 06d, 07b. Original NB 06 stub replaced.

### Decision: Phase 0 Foundation Refresh (constants + memory)
**Context:** `src/constants.py` had drifted from approved values in `references/assumptions.md`; memory files (`project_state.md`, `task_board.md`, `blockers.md`) described March setup phase but reality was further along.
**Decision:** Full refresh of constants.py to match assumptions.md (all 25+ values, with assumption IDs cited inline). Full rewrite of the three memory files to reflect actual repo state. Remove `notebooks/test.ipynb` for submission hygiene.
**Rationale:**
- CLAUDE.md protocol depends on memory files being accurate — stale files produce wrong agent advice.
- Every downstream notebook imports from `constants.py`. Fixing drift once propagates everywhere.
- Backwards-compat aliases kept (`MAX_STATION_SPACING_KM`, `AFIR_SPACING_KM`) so existing notebook imports don't break.
**Impact:** Unblocks Phase 1 (src stubs) and Phase 2 (modelling).

---

## 2026-03-17

### Decision: Hybrid LP + Scoring Optimization Approach
**Context:** Choice between greedy interval covering, full facility location LP, or multi-criteria scoring  
**Decision:** Hybrid approach — Set Cover LP for placement, demand-weighted sizing with MCDA scoring  
**Rationale:** 
- LP gives mathematical rigor for minimizing station count (directly addresses datathon objective)
- MCDA scoring provides explainable sizing and strategic narrative
- Hybrid balances optimization quality with implementation timeline
**Impact:** Determines NB 07 architecture

### Decision: Rutas por Carretera as Primary Demand Data
**Context:** Choice between pyspainmobility OD matrix vs Ministry Rutas por Carretera  
**Decision:** Use Rutas por Carretera `informacion_tramo` as primary input, pyspainmobility as optional enrichment  
**Rationale:**
- Rutas already provides segment-level flows (what we need)
- No complex OD→road routing required
- Official ministry data, more defensible
- 3 reference dates available (summer/autumn/spring)
**Impact:** Simplifies NB 06 demand model significantly

### Decision: Three-Tier Spacing Constraints
**Context:** AFIR regulation analysis revealed Core vs Comprehensive TEN-T distinction  
**Decision:** 60 km (TEN-T Core), 100 km (TEN-T Comprehensive), 120 km (general roads)  
**Rationale:** 
- AFIR compliance requires tiered approach
- 120 km general = 255 km effective range ÷ 2.1 safety factor
- More conservative than original 150 km
**Impact:** Increases minimum station count but improves coverage quality

### Decision: BEV-Only Demand Modeling
**Context:** Fleet composition analysis (assumption A4)  
**Decision:** Apply highway charging demand only to BEV portion (~60% of fleet)  
**Rationale:** PHEVs use ICE on long trips, don't need DC fast charging  
**Impact:** Reduces effective demand base by ~40% vs naive total-fleet approach

### Decision: Agent Memory System Architecture
**Context:** Multi-agent coordination needs  
**Decision:** Shared `memory/` directory with structured markdown files, CLAUDE.md auto-loaded  
**Rationale:**
- Single source of truth across all agents
- Git-tracked for audit trail
- Human-readable format
- Works with both Claude and non-Claude agents
**Impact:** Enables coordinated agent work across team

---

## 2026-03-16

### Decision: Revised Assumptions Based on Research
**Context:** Initial assumptions needed validation against official sources  
**Decision:** Updated 8 assumptions, added 5 new ones (see `references/assumptions.md`)  
**Key changes:**
- Charging probability: 7% → 12% (interurban-specific)
- Max spacing: 150 km → 120 km (tighter safety factor)  
- Min chargers TEN-T: 2 → 4 (AFIR compliance)
- Grid reality: 87% of substations are Congested (authentic constraint)
**Rationale:** IEA Global EV Outlook 2025, AFIR regulation text, actual grid data analysis  
**Impact:** More realistic demand model, tighter optimization, grid-focused narrative

---

## Key Pending Decisions

*To be resolved at team meeting Mar 18:*

### Team Role Assignments
**Context:** 6 team members need clear work allocation  
**Options:** Functional (data/model/viz) vs end-to-end ownership  
**Decision date:** Mar 18 team meeting

### Development Environment 
**Context:** Local Jupyter vs Google Colab for submission  
**Status:** Need team preference and compatibility check  
**Decision date:** Mar 18 team meeting

### Report Language
**Context:** Analytical report could be Spanish, English, or bilingual  
**Status:** Need team/jury preference clarification  
**Decision date:** Mar 18 team meeting