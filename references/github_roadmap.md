# GitHub Projects Roadmap — Iberdrola EV Network 2027

**Project:** Team Greenlabs solution for IE Sustainability Datathon March 2026 (Iberdrola challenge)  
**Objective:** Design optimal interurban EV charging network for Spain targeting 2027 operations  
**Timeline:** Mar 16 – Apr 22, 2026 (37 days)  
**Team:** 6 members + Claude agents  

---

## GitHub Setup Instructions

1. **Create Project:** Repo → Projects → New project → Roadmap template
2. **Add Milestones:** Repo → Issues → Milestones → Create each milestone below
3. **Add Labels:** Repo → Issues → Labels → Create each label below  
4. **Create Issues:** Use titles, milestones, labels, and descriptions from tables below
5. **Configure Views:**
   - **Roadmap view:** Timeline Mar 16–Apr 22, group by Milestone
   - **Board view:** Columns: Backlog → In Progress → In Review → Done
6. **Assign team members** after Mar 18 meeting

### GitHub Dependencies and Effort Tracking

**Dependencies:** GitHub doesn't have native dependency management, but you can:
- Use "Depends on #X" in issue descriptions (GitHub auto-links)
- Reference blocking issues in comments: "Blocked by #6"
- Use task lists in issue descriptions with checkboxes
- GitHub Projects will show these links in the dependency view

**Effort tracking:** GitHub doesn't track time natively. Options:
- Use the "Est. Hours" column as reference only
- Add custom fields in GitHub Projects (Estimated Hours, Actual Hours)
- Use issue templates that ask for effort estimation
- Track time manually or with tools like Toggl/Clockify if needed

**Issue creation:** When creating each issue, copy the title and description from the tables below. Add the "Depends on #X" links after all issues are created (so issue numbers exist).

---

## Milestones

| Milestone | Due Date | Description |
|-----------|----------|-------------|
| `M0 — Project Setup` | **Mar 18** | Team aligned, memory system live, repo structured |
| `M1 — Data Ready` | **Mar 28** | All raw data acquired, pipeline notebooks executed |
| `M2 — Models Built` | **Apr 11** | Demand model + optimization + grid viability complete, draft output files validated |
| `M3 — Submission` | **Apr 22** | All 6 deliverables finalized and submitted |

---

## Labels

| Label | Colour | Meaning |
|-------|--------|---------|
| `stage: setup` | `#6c757d` (Grey) | Infrastructure, memory system, configuration |
| `stage: data` | `#0d6efd` (Blue) | Data acquisition, download scripts, raw processing |
| `stage: modeling` | `#6610f2` (Purple) | Demand model, optimization, grid analysis |
| `stage: output` | `#198754` (Green) | File generation, map, report, pitch |
| `type: notebook` | `#ffc107` (Yellow) | Work happens in a `.ipynb` file |
| `type: script` | `#fd7e14` (Orange) | Work happens in a `.py` file |
| `type: research` | `#20c997` (Teal) | Analysis, documentation, assumptions |
| `priority: high` | `#dc3545` (Red) | Blocks other tasks if delayed |
| `priority: medium` | `#fd7e14` (Orange) | Important but not immediately blocking |
| `priority: low` | `#6c757d` (Light grey) | Nice to have |

---

## Issues — Full List

### MILESTONE M0 — Project Setup (due Mar 18)

| # | Issue Title | Labels | Est. Hours | GitHub Dependencies | Description |
|---|-------------|--------|------------|-------------------|-------------|
| 1 | Set up agent memory system (`CLAUDE.md` + `memory/` directory) | `stage: setup`, `priority: high` | 2h | None | Create CLAUDE.md + memory/ folder structure. Blocks all agent-assisted work. |
| 2 | Create `.claude/rules/` coding standards and data conventions | `stage: setup`, `priority: medium` | 1h | Depends on #1 | Agent workflow standards and coding conventions. |
| 3 | Update `src/constants.py` with approved assumption values | `stage: setup`, `type: script`, `priority: high` | 1h | None | Import all values from references/assumptions.md. Enables NB 06–08 execution. |
| 4 | Create `scripts/` directory and scaffold `download_rutas.py` | `stage: setup`, `type: script`, `priority: high` | 1h | None | Directory structure + initial download script framework. Enables Rutas data acquisition. |
| 5 | Team meeting — roles, task assignments, workflow alignment | `stage: setup`, `priority: high` | 2h | None | **Mar 18 meeting** - assign roles and finalize workflow |

**Subtotal M0:** 5 issues, ~7 hours

---

### MILESTONE M1 — Data Ready (due Mar 28)

| # | Issue Title | Labels | Est. Hours | GitHub Dependencies | Description |
|---|-------------|--------|------------|-------------------|-------------|
| 6 | Build and run `download_rutas.py` — download 3 reference dates | `stage: data`, `type: script`, `priority: high` | 3h | Depends on #4 | Download informacion_tramo, od_rutas, calidad for dates: 20240824, 20241016, 20240331 (~300 MB total) |
| 7 | Download Rutas geometry (shapefile + `rt_tramo_val.csv`) | `stage: data`, `type: script`, `priority: high` | 1h | Part of #6 | Download shared geometry files: Geometria_tramos.shp + rt_tramo_val.csv |
| 8 | Expand pyspainmobility OD download (Apr, Jul, Oct 2022) | `stage: data`, `type: script`, `priority: medium` | 2h | None | Download additional seasonal periods for enrichment beyond existing Jan 2022 week |
| 9 | Research and acquire additional datasets (elevation, weather, cross-border) | `stage: data`, `type: research`, `priority: medium` | 4h | None | Find and download: SRTM elevation, AEMET weather, DGT cross-border traffic |
| 10 | Execute NB 02 — finalize EV fleet projection (SARIMA output) | `stage: data`, `type: notebook`, `priority: high` | 1h | Depends on #3 | Run remaining cells, export ev_projection_2027.csv for File_1 KPI |
| 11 | Execute NB 03 — road network filtering and IMD matching | `stage: data`, `type: notebook`, `priority: high` | 2h | None | Execute existing code, export processed road + IMD data for demand model |
| 12 | Execute NB 04 — existing charger baseline (filter to ≥50 kW, interurban) | `stage: data`, `type: notebook`, `priority: high` | 2h | None | Filter NAP to highway-grade chargers within 2km of AP-/A-/N- roads. Creates pre-opened coverage nodes. |
| 13 | Execute NB 05 — grid capacity consolidation (i-DE + Endesa + Viesgo) | `stage: data`, `type: notebook`, `priority: high` | 2h | None | Execute existing code, export unified grid_capacity for spatial joins |
| 14 | Log all acquired datasets in `memory/data_inventory.md` | `stage: data`, `type: research`, `priority: medium` | 1h | Depends on #1 | Document all raw data: source, date, schema, status. Close at M1. |

**Subtotal M1:** 9 issues, ~18 hours

---

### MILESTONE M2 — Models Built (due Apr 11)

| # | Issue Title | Labels | Est. Hours | GitHub Dependencies | Description |
|---|-------------|--------|------------|-------------------|-------------|
| 15 | NB 06 — Load and process Rutas `informacion_tramo` for 3 reference dates | `stage: modeling`, `type: notebook`, `priority: high` | 4h | Depends on #6, #7 | Parse and clean segment flow data from all 3 dates. Extract `largo` trips for EV demand. |
| 16 | NB 06 — Join road names, filter to AP-/A-/N-, attach geometry | `stage: modeling`, `type: notebook`, `priority: high` | 2h | Depends on #15, #11 | Join rt_tramo_val.csv for road names. Filter to interurban roads only. Attach geometries. |
| 17 | NB 06 — Scale to 2027 EV demand (penetration rate × BEV fraction) | `stage: modeling`, `type: notebook`, `priority: high` | 2h | Depends on #16, #10 | Apply: largo_trips × 5.7% EV penetration × 60% BEV fraction = daily_ev_trips |
| 18 | NB 06 — Apply seasonal correction, compute `n_chargers_needed` per segment | `stage: modeling`, `type: notebook`, `priority: high` | 2h | Depends on #17 | Weight by season, apply charger sizing formula: daily_ev × 12% prob × 0.37h / 20h |
| 19 | NB 06 — Output `demand_per_segment.parquet`, validate against IMD cross-check | `stage: modeling`, `type: notebook`, `priority: high` | 2h | Depends on #18 | Export final demand model. Cross-validate total against DGT IMD station counts. |
| 20 | Implement `src/geo_utils.py` — BallTree nearest substation function | `stage: modeling`, `type: script`, `priority: high` | 3h | None | Build find_nearest_substation() using scipy BallTree + haversine. Used by NB 07 + 08. |
| 21 | Implement `src/optimization.py` — candidate generation and coverage matrix | `stage: modeling`, `type: script`, `priority: high` | 4h | None | Build generate_candidates(), build_coverage_matrix(), solve_set_cover(). Core LP functions. |
| 22 | NB 07 — Build candidate location set (service areas + gas stations + existing charger exclusion) | `stage: modeling`, `type: notebook`, `priority: high` | 3h | Depends on #12, #19 | Generate candidate points. Mark existing ≥50kW chargers as pre-opened. Filter to within 2km of roads. |
| 23 | NB 07 — Formulate and solve Set Cover LP (PuLP) with 3-tier spacing constraints | `stage: modeling`, `type: notebook`, `priority: high` | 5h | Depends on #21, #22 | **CRITICAL PATH** Solve minimize stations s.t. 60km/100km/120km spacing constraints |
| 24 | NB 07 — Size each station (sum nearby demand → charger formula → clamp) | `stage: modeling`, `type: notebook`, `priority: high` | 2h | Depends on #23 | For each opened station: collect nearby segment demand, apply sizing formula, clamp 2-12 range |
| 25 | NB 07 — Gap-fill uncovered demand points, validate AFIR compliance | `stage: modeling`, `type: notebook`, `priority: high` | 2h | Depends on #24 | Add synthetic candidates for remaining gaps. Validate 60km TEN-T Core coverage. |
| 26 | NB 08 — Spatial join proposed stations to nearest substation (BallTree) | `stage: modeling`, `type: notebook`, `priority: high` | 3h | Depends on #13, #20, #25 | For each proposed station: nearest substation within 25km, assign DSO, capacity, distance |
| 27 | NB 08 — Classify `grid_status`, apply distance tiers, flag friction points | `stage: modeling`, `type: notebook`, `priority: high` | 2h | Depends on #26 | Sufficient/Moderate/Congested classification. Distance tiers. Generate File_3 friction points. |
| 28 | Sensitivity analysis — vary EV projection (1.5M / 2.0M / 2.5M scenarios) | `stage: modeling`, `type: notebook`, `priority: medium` | 3h | Depends on #19 | Re-run demand model with different fleet assumptions. Quantify uncertainty range for report. |
| 29 | Cross-validate optimization output against existing charger network | `stage: modeling`, `type: notebook`, `priority: medium` | 2h | Depends on #25, #12 | Compare proposed vs existing coverage. Identify genuine gaps vs over-provision. QA step. |

**Subtotal M2:** 15 issues, ~39 hours

---

### MILESTONE M3 — Submission (due Apr 22)

| # | Issue Title | Labels | Est. Hours | GitHub Dependencies | Description |
|---|-------------|--------|------------|-------------------|-------------|
| 30 | NB 09 — Assemble File_1.csv (global KPIs), validate schema | `stage: output`, `type: notebook`, `priority: high` | 2h | Depends on #25, #27 | Count total stations, demand, EV projection. Single row with all required KPI fields. |
| 31 | NB 09 — Finalize File_2.csv and File_3.csv, validate all required fields | `stage: output`, `type: notebook`, `priority: high` | 2h | Depends on #30 | Export proposed_stations and friction_points. Validate schema compliance vs datathon spec. |
| 32 | NB 10 — Build Folium map (stations, corridors, grid status, existing chargers) | `stage: output`, `type: notebook`, `priority: high` | 5h | Depends on #31 | Interactive map: color-coded stations, TEN-T corridors, existing charger points, popups |
| 33 | NB 10 — Add extra layers (traffic heatmap, AFIR compliance, TEN-T overlay) | `stage: output`, `type: notebook`, `priority: medium` | 3h | Depends on #32 | Enhanced layers: IMD heatmap, 60km coverage circles, coverage gap indicators, legend |
| 34 | Write analytical report — methodology and data sections | `stage: output`, `type: research`, `priority: high` | 6h | Depends on #14 | 3-5 page report: intro, data sources, assumptions, methodology. Can start at M1. |
| 35 | Write analytical report — results and strategic recommendation sections | `stage: output`, `type: research`, `priority: high` | 5h | Depends on #29 | Results, grid friction analysis, phased deployment strategy, business case for Iberdrola |
| 36 | Build pitch deck (5 min max, problem → approach → findings → recommendation) | `stage: output`, `type: research`, `priority: high` | 4h | Depends on #35 | Max 5-minute presentation: problem → our approach → key findings → recommendation to jury |
| 37 | Full notebook QA pass — all cells executed, all outputs visible | `stage: output`, `priority: high` | 3h | Depends on #32, #31, #28 | **QUALITY GATE** All notebooks run end-to-end cleanly, outputs committed and visible |
| 38 | Final output validation — schema compliance, field names, file formats | `stage: output`, `priority: high` | 1h | Depends on #31 | Automated schema validation against datathon requirements. Final field name check. |
| 39 | Submission packaging | `stage: output`, `priority: high` | 1h | Depends on #37, #38 | **Apr 22 AM** Package all 6 deliverables for submission |

**Subtotal M3:** 10 issues, ~32 hours

---

## Effort Summary by Milestone

| Milestone | Issues | Total Estimated Effort | Calendar Window | Team Capacity |
|-----------|--------|----------------------|-----------------|---------------|
| M0 — Setup | 5 issues | ~7 hours | Mar 16–18 (2 days) | Setup phase |
| M1 — Data Ready | 9 issues | ~18 hours | Mar 18–28 (10 days) | Parallel data acquisition |
| M2 — Models Built | 15 issues | ~39 hours | Mar 29–Apr 11 (14 days) | Core development |
| M3 — Submission | 10 issues | ~32 hours | Apr 12–22 (10 days) | Outputs + polish |
| **TOTAL** | **39 issues** | **~96 hours** | **37 days** | **6 team members** |

**Capacity analysis:** 96 hours ÷ 6 people = ~16 hours per person total, or roughly 2–3 focused working days each across the entire project. Very achievable with good parallel execution.

---

## Critical Path (Dependencies)

The tasks that cannot slip without delaying the whole project:

```
SETUP PHASE
#3 (constants.py) ────► #10 (NB 02 EV projection) ────► #17 (demand scaling)

DATA ACQUISITION
#6 (download_rutas.py) ────► #15 (load Rutas data) ────► MODELING CHAIN

CORE MODELING CHAIN  
#15 → #16 → #17 → #18 → #19 (NB 06 demand model)
                      └─► #22 → #23 → #24 → #25 (NB 07 optimization)
                                            └─► #26 → #27 (NB 08 grid)
                                                     └─► #30 → #31 (outputs)

PARALLEL FEEDS TO CRITICAL PATH
#12 (charger baseline) ────► #22 (candidate generation)
#13 (grid capacity)    ────► #26 (grid spatial join)
#20 (geo_utils.py)     ────► #26 (nearest substation)
#21 (optimization.py)  ────► #23 (Set Cover LP)

FINAL PHASE
#31 ────► #32 ────► #33 (map)
     └─► #37 ────► #38 ────► #39 (submission)

REPORT (PARALLEL)
#14 ────► #34 ────► #35 ────► #36 (pitch)
```

**Highest-risk issues:**
- **#6** (download script) — blocks everything downstream
- **#15** (Rutas data processing) — complex new data format
- **#23** (Set Cover LP) — mathematical complexity, potential debugging needed
- **#34-35** (analytical report) — requires calendar time, cannot be rushed

---

## GitHub Projects Configuration

### Roadmap View Setup
- **Timeline:** Mar 16 – Apr 22, 2026
- **Grouping:** By Milestone  
- **Status tracking:** % complete per milestone
- **Swimlanes:** One per team member (assign after Mar 18 meeting)

### Board View Setup  
- **Columns:** `Backlog` → `In Progress` → `In Review` → `Done`
- **Filters:** By milestone, by assignee, by label
- **Automation:** Move to "In Review" when PR opened, move to "Done" when merged

### Issue Templates (Optional)
Create issue templates for:
- **Notebook work:** Template with checklist (execute cells, validate outputs, commit with outputs visible)
- **Script work:** Template with checklist (unit tests, documentation, integration test)
- **Research work:** Template with deliverable specification

---

## Project Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Technical quality** | All notebooks execute cleanly end-to-end | CI check or manual validation |
| **Output compliance** | Files match datathon schema exactly | Automated schema validation |
| **Code documentation** | All functions have docstrings | Pre-commit hook check |
| **Agent coordination** | Memory files updated after each major task | Manual audit |
| **On-time delivery** | All milestones hit within 1 day | GitHub Projects timeline |

---

**Last updated:** 2026-03-17  
**Status:** Ready for team assignment after Mar 18 meeting  
**Next action:** Create GitHub Project and import this structure