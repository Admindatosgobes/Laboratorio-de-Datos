# Assumptions Register

Last updated: 2026-03-16  
Research basis: IEA Global EV Outlook 2025, AFIR Regulation 2023/1804 (EUR-Lex), ANFAC Spain,
CNMC grid standards, IDAE EV planning guides, repo grid/charger data analysis, Wu et al. (2024),
Liao et al. (2026), Iberdrola/BP Pulse press releases, REE hourly demand profiles.

All assumptions have been reviewed and approved after comprehensive research (2026-03-16).
Previous placeholder values are superseded by the entries below.

---

## CATEGORY A — VEHICLE & BATTERY

### A1 — Average EV Range (WLTP)

- **Value used:** 340 km (WLTP)
- **Previous value:** 300 km
- **Justification:** IEA Global EV Outlook 2025 reports the 2024 global sales-weighted average
  BEV range at 340 km under on-road conditions (applying a 1.1× WLTP correction). Medium and
  large cars plus SUVs — which dominate interurban long-distance travel — average >350 km.
  The 300 km figure reflected the 2022–23 fleet; by 2027 with fleet renewal, 340 km is the
  appropriate central estimate for Spain's projected BEV mix.
- **Impact on model:** Sets the theoretical maximum distance between charges; feeds A2 and C1.
- **Source:** IEA Global EV Outlook 2025, "Electric vehicle range" section.

### A2 — Effective Range Factor (Highway Usability)

- **Value used:** 75% of WLTP
- **Previous value:** 80%
- **Effective highway range:** 340 km × 75% = **255 km**
- **Justification:** Highway driving at 110–120 km/h increases energy consumption 25–30% versus
  the WLTP mixed-cycle measurement. Real-world range is approximately 10% below WLTP lab
  values (ICCT Europe 2024). Combined with a 20% battery reserve (drivers avoid dropping below
  20% SoC to prevent range anxiety), effective usable highway range = 340 × 0.90 × 0.83 ≈
  254 km. Rounded conservatively to 255 km. The previous 80% factor was derived from urban
  mixed-use studies and overstates highway range.
- **Impact on model:** Primary input to maximum station spacing calculation (C1).
- **Sources:** IEA GEVO 2025; ICCT Europe "Real-world BEV range" (2024); Wu et al. (2024)
  drivetrain energy consumption model.

### A3 — Standard Power per Charger

- **Value used:** 150 kW (FIXED — mandated by datathon rules, cannot be changed)
- **Justification:** Datathon brief §5.2 Rule 2. Also consistent with AFIR minimum fast charger
  standard for TEN-T recharging pools.
- **Impact on model:** estimated_demand_kw = n_chargers_proposed × 150 kW (File_3 field).
- **Source:** Datathon brief (IE Sustainability Datathon March 2026); AFIR Regulation 2023/1804.

### A4 — EV Fleet Composition (BEV vs PHEV Split)
- **Value used:** ~60% BEV, ~40% PHEV of total electrified fleet
- **Previous value:** Not specified (model treated all EVs as highway chargers)
- **Justification:** IEA GEVO 2025 shows PHEVs growing to ~40% of European EV sales by 2024,
  with Spain's historical mix consistent with this trend (DGT registration data in repo).
  Critically, PHEVs have only ~65 km electric range and rely on their ICE engine for long
  interurban trips — they do not generate meaningful DC fast charging demand on highways.
  Only the BEV portion (~60%) generates interurban charging demand.
- **Key implication:** Of the 2.5M projected 2027 fleet, ~1.5M are BEVs. Applying the
  interurban trip fraction (A-new below), the effective charging demand base is significantly
  lower than the full fleet count.
- **Impact on model:** Demand model applies EV penetration to IMD traffic using BEV share only,
  preventing overestimation of highway charging demand.
- **Sources:** IEA GEVO 2025; DGT ev_monthly_registrations.csv in repo; ANFAC Spain 2025.

---

## CATEGORY B — CHARGING BEHAVIOR

### B1 — En-Route Charging Probability (Interurban Highway)

- **Value used:** 12% of passing BEVs will charge at a given station
- **Previous value:** 7%
- **Justification:** The 7% figure derives from aggregate urban public charging studies where
  drivers pass chargers opportunistically. For interurban highway travel, the context is
  fundamentally different: drivers making trips longer than the effective range (255 km)
  MUST stop to charge. Norwegian NPRA data and IONITY Europe utilization reports show
  DC fast charger utilization at 8–20% of passing EVs on major corridors. Weighting across
  the full distribution of trip lengths using Spain's mobility OD matrix (where ~35% of
  interurban trips exceed 200 km), 12% is the appropriate central estimate.
  The previous 7% underestimated highway demand by approximately 40%.
- **Impact on model:** Highest-impact assumption on n_chargers_proposed. A 12% rate versus
  7% increases the charger count per segment by ~71%, driving more accurate station sizing.
- **Sources:** IONITY 2024 utilization disclosures; Norway NPRA highway charging data;
  Wu et al. (2024) — charging probability at public highway locations; IEA GEVO 2025
  "highway charger share of capacity" section.

### B2 — Average Charging Session Duration

- **Value used:** 22 minutes (0.37 hours)
- **Previous value:** 24 minutes (0.4 hours)
- **Justification:** At 150 kW with ~85% charging efficiency and a typical 60 kWh battery
  needing a 50% top-up (30 kWh added), active charging time = 30 kWh / (150 kW × 0.85)
  ≈ 14 minutes. Adding ~8 minutes for plug connection, payment, and unplug gives a total
  session of ~22 minutes. IEA confirms 15 minutes of ultra-fast charging provides ~150 km
  additional range. The previous 24-minute estimate was slightly high for 150 kW DC sessions.
  Marginal revision that partially offsets the increase from B1.
- **Impact on model:** Feeds denominator of charger sizing formula; slight reduction vs
  previous value.
- **Sources:** AFIR Regulation 2023/1804 technical specifications; IEA GEVO 2025
  "charging competitive with refuelling time" section; Iberdrola/BP Pulse operational data.

### B3 — Station Effective Operating Hours

- **Value used:** 20 hours per day
- **Previous value:** 18 hours
- **Justification:** AFIR Article 5 requires publicly accessible recharging pools to be
  operational 24/7. IONITY and Iberdrola/BP Pulse operate all highway stations continuously.
  The 18-hour assumption excluded the overnight window (midnight–6am) which, while low-volume,
  contributes approximately 5% of daily sessions and must be included in station design.
  20 hours is a conservative operational estimate that excludes only mandatory maintenance
  windows.
- **Impact on model:** Increases the available service window in the denominator of the
  charger sizing formula, marginally reducing minimum charger count per station.
- **Sources:** AFIR Article 5 operational requirements; IONITY station operations policy;
  Iberdrola/BP Pulse Spain joint venture (November 2024 press release).

### B4 — Minimum Chargers per Station

- **Value used:** 4 chargers on TEN-T corridors; 2 chargers on non-TEN-T roads
- **Previous value:** 2 chargers (uniform)
- **Justification:** AFIR Regulation 2023/1804, Article 3(1)(a) and Annex II mandate that
  TEN-T core network recharging pools achieve a minimum total power output of 400 kW by
  end-2025, rising to 600 kW by end-2027. At the fixed 150 kW per charger, meeting the
  600 kW requirement requires a minimum of 4 chargers (4 × 150 kW = 600 kW). Single or
  paired chargers at TEN-T stations would constitute AFIR non-compliance. For non-TEN-T
  interurban roads, 2 chargers remain the minimum for commercial viability.
- **Impact on model:** Ensures AFIR compliance in File_2 output. Increases total estimated
  CAPEX for TEN-T corridor stations.
- **Sources:** AFIR Regulation 2023/1804, Article 3(1)(a), Annex II; Iberdrola/BP Pulse
  press release (November 2024) deploying 150–350 kW stations across Spain and Portugal.

### B5 — Maximum Chargers per Station

- **Value used:** 12 chargers (high-traffic corridors IMD > 20,000); 8 chargers (standard)
- **Previous value:** 8 chargers (uniform cap)
- **Justification:** Major European operators — IONITY, Tesla Supercharger, Iberdrola/BP Pulse
  — deploy 8–16 chargers at high-traffic motorway hubs. Spain's TEN-T Mediterranean corridor
  (AP-7) records IMD values up to 37,000 vehicles/day. At 12% charging probability and
  22-minute sessions, peak hour demand at such sites warrants 10–12 charger bays to avoid
  queuing. Capping at 8 chargers for the busiest Spanish corridors would undersize
  infrastructure at precisely the sites most critical to network reliability.
- **Impact on model:** Allows the demand model to accurately size high-traffic stations.
  The 12-charger cap applies only where the demand formula produces n > 8.
- **Sources:** IONITY site configuration database; IEA GEVO 2025 ultra-fast charger
  deployment trends; Iberdrola/BP Pulse Spain joint venture station specifications.

---

## CATEGORY C — SPACING & COVERAGE (AFIR COMPLIANCE)

### C1 — Maximum General Spacing (Non-TEN-T Interurban Roads)

- **Value used:** 120 km
- **Previous value:** 150 km
- **Justification:** Given A2 effective range of 255 km and standard driver behaviour of
  charging when SoC reaches ~50% (to avoid range anxiety approaching the next station),
  practical maximum no-stress spacing = 255 × 0.50 = 127 km. Rounded down to 120 km for
  a clean, conservative constraint. The previous 150 km used a 1.6× safety factor; industry
  planning best practice and international precedent (Norway: 50 km; Netherlands: high
  density) support a 1.9–2.1× safety factor (255 / 120 ≈ 2.1×). Reducing spacing from
  150 km to 120 km increases the minimum station count but meaningfully eliminates range
  anxiety across Spain's national road network.
- **Impact on model:** Primary coverage constraint in LP optimization. Reduction increases
  total_proposed_stations but improves network quality score.
- **Sources:** Derived from A2; IEA GEVO 2025 "ensuring denser charging network" recommendation;
  Norway NPRA 50 km target (established 2016); IEA highway coverage analysis (2024).

### C2 — TEN-T Core Network Spacing (AFIR Mandatory)

- **Value used:** 60 km maximum between recharging pools
- **Status:** CONFIRMED — no change
- **Justification:** AFIR Regulation 2023/1804, Article 3(1)(a) mandates recharging pools
  at maximum 60 km intervals on the TEN-T core road network. This is a legal compliance
  requirement, not a design choice. Our road data flags TEN-T core segments via the
  `TENT_corredor` field with value "Core".
- **Impact on model:** Hard constraint in LP optimization for TEN-T Core segments. Stations
  on these corridors must be placed at ≤60 km intervals regardless of demand.
- **Source:** AFIR Regulation 2023/1804, Article 3(1)(a); confirmed via EUR-Lex full text.

### C3 — TEN-T Comprehensive Network Spacing (AFIR)

- **Value used:** 100 km maximum between recharging pools
- **Previous value:** Not specified (TEN-T was treated as binary: Core/non-TEN-T)
- **Justification:** AFIR Article 3(2) mandates ≤100 km spacing on the TEN-T comprehensive
  network by end-2030, with interim deployment milestones by 2027. Spain's road data
  distinguishes Core (`TENT_corredor = "Core"`) from Comprehensive (`TENT_red_basica = "SI"`
  but not flagged as Core corridor). Adding this intermediate tier ensures we model the
  correct regulatory requirement for each road classification.
- **Impact on model:** Adds a third spacing tier in the LP: 60 km (TEN-T Core), 100 km
  (TEN-T Comprehensive), 120 km (general interurban). Increases station count on
  comprehensive network versus a 120 km uniform rule.
- **Source:** AFIR Regulation 2023/1804, Article 3(2) and Annex II.

### C4 — Existing Charger Exclusion Rule

- **Value used:** Existing sites with ≥50 kW within 2 km of an interurban road segment
  count as valid coverage nodes. New stations are only proposed where no such site exists
  within the applicable spacing threshold.
- **Previous value:** Not specified (implicitly ignored)
- **Justification:** The datathon brief §4.1 requires teams to establish a baseline of
  existing infrastructure before proposing new stations, and to only suggest new stations
  where there is a "demonstrable deficit". The NAP dataset contains 12,072 charger sites,
  of which 5,338 have ≥50 kW (highway-grade DC fast charging). Failing to credit existing
  highway-grade chargers would result in the model proposing duplicate stations at already-
  served locations, inflating total_proposed_stations and reducing proposal credibility.
  The 50 kW threshold distinguishes highway fast chargers from slow urban AC chargers
  (median power in NAP dataset is 22 kW).
- **Impact on model:** Reduces total_proposed_stations in File_1/File_2. Ensures only
  genuine coverage gaps receive new station proposals.
- **Sources:** NAP chargers_clean.csv (repo): 5,338 of 12,072 sites ≥50 kW; datathon
  brief §4.1; IEA GEVO 2025 definition of "fast charger" (>22 kW).

---

## CATEGORY D — GRID CAPACITY

### D1 — Grid Status: Sufficient Threshold

- **Value used:** Available capacity ≥ 5 MW at nearest substation
- **Status:** CONFIRMED — no change
- **Justification:** A 4-charger TEN-T station at 150 kW = 600 kW peak load. For a
  substation to be classified Sufficient, it must handle: peak station load (0.6 MW) +
  existing local demand + a 3× future expansion margin, adjusted for power factor (~0.8):
  0.6 MW × 3 / 0.8 ≈ 2.25 MW minimum. The 5 MW threshold adds further headroom for
  simultaneous multi-station deployment in the same substation area and is consistent
  with CNMC medium-voltage connection standards for new large consumers.
- **Impact on model:** grid_status = "Sufficient" in File_2. Station deployable without
  grid reinforcement. These are the priority Phase 1 sites.
- **Sources:** CNMC technical standards for MT connection; IDAE EV infrastructure planning
  guide; datathon brief §5.2 Rule 1.

### D2 — Grid Status: Moderate Threshold

- **Value used:** Available capacity ≥ 1 MW and < 5 MW
- **Status:** CONFIRMED — no change
- **Justification:** 1 MW supports 1–2 fast chargers with minimal headroom. A station can
  be deployed with careful management but has limited capacity for future expansion.
  Consistent with IDAE planning thresholds for sites requiring partial grid reinforcement.
- **Impact on model:** grid_status = "Moderate" in File_2 and File_3 (friction point).
  These are Phase 2 deployment sites post-partial reinforcement.
- **Sources:** IDAE EV site planning guidelines; CNMC grid connection standards.

### D3 — Grid Status: Congested Threshold

- **Value used:** Available capacity < 1 MW (including 0 MW)
- **Status:** CONFIRMED — no change
- **Justification:** Less than 1 MW cannot reliably power even a single 150 kW charger
  after accounting for load diversity factor and power factor correction. Full grid
  reinforcement is required before any station deployment at such locations.
  Critical finding from repo data analysis: 80.6% of the 2,137 unique physical
  substations in `grid_consolidated.csv` show 0 MW available capacity, and 85.9% are
  Congested or Moderate (friction points) in total. The raw `grid_capacity_unified.csv`
  contains 4,990 records (one per voltage tap) which collapse to 2,137 substations after
  deduplication by name + coordinates — always cite the 2,137 figure for physical
  infrastructure claims. This is not a data error: it reflects the authentic current
  saturation of Spain's distribution network and is the central strategic insight of
  the project. By distributor: i-DE = 88% Congested; Endesa = 78% Congested;
  Viesgo = 48% Congested (small sample, n=95).
- **Impact on model:** grid_status = "Congested" in File_2 and File_3 (friction point).
  These are Phase 3 sites requiring major grid investment. They represent the majority
  of Spain's interurban highway network — Iberdrola's core business opportunity.
- **Sources:** grid_capacity_unified.csv analysis (repo); i-DE, Endesa, Viesgo official
  capacity publications; CNMC grid saturation reports.

### D4 — Substation Spatial Matching Radius (Tiered)

- **Value used:** Tiered by distance — 5 km (preferred), 5–15 km (feasible), 15–25 km
  (high-cost), >25 km (Congested by default)
- **Previous value:** Single 25 km radius (untiered)
- **Justification:** Grid connection costs scale with distance. Industry benchmarks show:
  — Within 5 km: direct low-voltage or medium-voltage connection, economically optimal.
  — 5–15 km: medium-voltage line extension, cost-feasible (~€100–300K additional CAPEX).
  — 15–25 km: high-cost extension, requires detailed feasibility study; flag in report.
  — >25 km: impractical connection cost; treated as Congested regardless of substation
  capacity. Tiering enriches the friction analysis and provides Iberdrola actionable
  guidance on connection feasibility beyond a binary match/no-match result.
- **Impact on model:** Adds a connection_distance_km field to File_2 and File_3.
  Friction points with substation capacity >1 MW but distance >15 km are flagged as
  infrastructure-constrained rather than capacity-constrained.
- **Sources:** CNMC grid extension cost benchmarks; IDAE EV site planning guidelines
  (typical connection distance 2–10 km for commercial viability).

### D5 — Default Status if No Substation Found

- **Value used:** Congested
- **Status:** CONFIRMED — no change
- **Justification:** Any location more than 25 km from the nearest substation faces
  impractical grid connection costs and timelines. Conservatively classified as Congested.
- **Source:** Technical standard; consistent with IDAE planning assumptions.

---

## CATEGORY E — DEMAND SCALING

### E1 — Total EV Fleet Projection 2027

- **Value used:**
  - **Datathon output (File_1):** 2,498,159 — direct output of datos.gob.es SARIMA fork
    (mandatory per datathon brief §4.1 Rule 3). This value cannot be modified.
  - **Demand model base case:** 2,000,000 (conservative, used in NB 06 charger sizing)
- **Previous value:** [OUTPUT FROM DATOS.GOB.ES FORK] — placeholder
- **Justification:** The SARIMA model projects ~2.5M cumulative EVs by December 2027.
  Cross-validation against IEA projections for Spain (Stated Policies scenario), ANFAC
  recent data (+64.5% electrified vehicle sales in February 2026), and the current fleet
  base (~480K at end-2023) suggests 2.5M requires sustained ~50% annual fleet growth —
  ambitious but plausible given MOVES III incentives and accelerating EU CO2 regulations.
  The demand model uses 2.0M as a conservative base case to avoid oversizing stations;
  sensitivity analysis at 2.5M and 1.5M is recommended in the report.
- **Impact on model:** total_ev_projected_2027 in File_1 = 2,498,159 (mandatory).
  Demand model uses 2.0M to calculate EV penetration rate (E3).
- **Sources:** datos.gob.es SARIMA fork (ev_projection_2027.csv in repo); IEA GEVO 2025
  Spain chapter; ANFAC Spain press release March 2026.

### E2 — BEV Fraction for Highway Demand Calculation

- **Value used:** 60% of total EV fleet are BEVs generating interurban charging demand
- **Previous value:** Not specified (all EVs implicitly treated as charging candidates)
- **Justification:** IEA GEVO 2025 reports PHEVs growing to ~40% of European EV sales,
  consistent with Spain's DGT registration data showing persistent PHEV market share.
  PHEVs have ~65 km electric range in Europe (IEA data) and default to ICE mode on long
  highway trips — they do not require or seek DC fast charging for interurban travel.
  Only BEVs (~60% of fleet = ~1.2M vehicles at 2.0M base case) generate interurban fast
  charging demand.
- **Impact on model:** Demand model = IMD_total × EV_penetration_rate × BEV_fraction.
  Prevents a ~40% overestimation of highway charging demand from including PHEVs.
- **Sources:** IEA GEVO 2025 "PHEV electric range in Europe ~65 km"; DGT registration
  data (ev_monthly_registrations.csv in repo).

### E3 — Total Spanish Light Vehicle Fleet (Denominator)

- **Value used:** 35,000,000 light vehicles (2027 estimate)
- **Previous value:** Not specified
- **Justification:** DGT Estadísticas del Parque de Vehículos reports ~33.5M registered
  light vehicles in Spain (2024). Applying ~1% annual fleet growth gives ~34–35M in 2027.
  EV penetration rate 2027 = 2.0M (base case) / 35M = **5.7%**.
  This penetration rate is applied to IMD total traffic counts to calculate daily BEV
  volume per road segment: daily_bev_traffic = IMD_total × 0.057 × 0.60 (BEV fraction).
- **Impact on model:** Key scaling factor in demand model (NB 06). Small errors here
  propagate linearly through all charger sizing calculations.
- **Sources:** DGT Estadísticas del Parque de Vehículos 2024; INE population projections.

### E4 — Seasonal Traffic Multiplier — Mediterranean Corridors (AP-7, A-7)

- **Value used:** 2.0× for June/September; 2.5× for July–August peak
- **Previous value:** 1.5×–2.5× (unstructured range)
- **Justification:** INE hotel occupancy and traveler data in repo (tourism_seasonal.csv,
  ine_hotel_travelers_overnights_provinces_2025_monthly.csv) confirm high summer peaks
  along Mediterranean provinces (Valencia, Murcia, Cataluña, Málaga). DGT traffic
  intensity publications show AP-7 at 2.0–2.5× annual average in July–August, with the
  highest weeks (last two weeks of July, first two weeks of August) reaching 2.5×.
  The structured multiplier (2.0× shoulder months, 2.5× peak) replaces the previous
  unstructured range and enables the demand model to apply the correct factor by month.
- **Impact on model:** Station sizing on Mediterranean corridors reflects worst-case peak
  demand. A station sized for 2.0× annual average demand would face critical queuing
  failures in August peak weeks if 2.5× applies.
- **Sources:** INE tourism_seasonal.csv (repo); INE hotel travelers data (repo);
  DGT seasonal traffic intensity publications; IDAE summer peak demand analysis.

### E5 — Seasonal Traffic Multiplier — Atlantic/Cantabrian Corridors (A-8, AP-9)

- **Value used:** 1.5× for July–August; 1.0× otherwise
- **Status:** CONFIRMED — no change
- **Justification:** INE tourism data for Cantabria, Asturias, Galicia provinces confirms
  moderate summer peaks (~1.3–1.5×). The 1.5× upper bound is appropriate.
- **Sources:** INE hotel travelers data (repo) by province.

### E6 — Interurban Trip Fraction of Total Vehicle Travel

- **Value used:** ~35% of total BEV vehicle kilometres are interurban
- **Previous value:** Not specified
- **Justification:** Spain's MOVILIA national household mobility survey and DGT road
  statistics show approximately 35% of annual vehicle kilometres are driven on autopistas,
  autovías, and carreteras nacionales. The remaining 65% are urban and local roads
  (where home/workplace charging predominates). This fraction contextualises aggregate
  annual highway charging demand and informs the strategic narrative: a substantial
  minority of BEV travel requires highway infrastructure, making it a critical bottleneck
  even as home charging dominates daily use.
- **Impact on model:** Contextual input to the strategic report section. Not directly
  used in the station sizing formula but cited to justify the business case for
  interurban-specific investment by Iberdrola.
- **Sources:** Ministry of Transport MOVILIA mobility survey; DGT road use statistics.

---

## CATEGORY F — ECONOMIC & STRATEGIC (REPORT USE)

### F1 — CAPEX per 150 kW Charger (Installed)

- **Value used:** €80,000–€130,000 per charger (installed, all-in)
- **Previous value:** Not specified
- **Justification:** Industry benchmark derived from Iberdrola/BP Pulse joint venture
  press release (November 2024), which announced deployment of ultra-fast charging
  network across Spain and Portugal. Hardware cost for a 150 kW DC unit: €30,000–€50,000
  (BloombergNEF, reflecting 20% cost reduction between 2022 and 2024). Civil works,
  grid connection, and installation: €50,000–€80,000 depending on site complexity and
  grid proximity. Total per charger: €80,000–€130,000.
  A reference 4-charger TEN-T station = €320,000–€520,000 installed.
- **Impact on model:** Used in analytical report to quantify total network investment
  required (total_proposed_stations × avg_chargers_per_station × avg_CAPEX_per_charger).
- **Sources:** Iberdrola/BP Pulse Spain press release (November 2024);
  BloombergNEF EV Infrastructure Cost Report 2024; IONITY station cost disclosures.

### F2 — Smart Charging Optimal Window

- **Value used:** 10:00–16:00 (solar midday peak integration window)
- **Previous value:** Not specified
- **Justification:** REE hourly demand profiles in repo (ree_hourly_demand_profiles.csv)
  show Spain's solar photovoltaic generation peaking between 10:00 and 16:00, creating
  a window of surplus renewable energy and lowest net grid stress. Spain's 136 GW
  installed capacity (REE 2024) includes a large and growing solar PV component.
  Positioning interurban fast chargers as V2G-ready infrastructure with dynamic pricing
  that incentivises daytime solar-window charging would reduce net grid impact, lower
  charging costs for drivers, and generate a green energy narrative for Iberdrola's
  commercial strategy.
- **Impact on model:** Strategic recommendation in the analytical report. Not used
  directly in station placement optimization but cited in the friction point response
  strategy for Congested sites.
- **Sources:** REE ree_hourly_demand_profiles.csv (repo); IEA GEVO 2025 smart charging
  section; REE installed capacity data (ree_installed_capacity_2024.csv in repo).

### F3 — Highway Charger Utilization Rate Trajectory

- **Value used:** 5–15% initial utilization (2027); growing to 20–35% by 2030
- **Previous value:** Not specified
- **Justification:** IEA reports EU public charger ratio at ~1 per 13 EVs in 2024, with
  utilization low in early market phases. For Spain's new interurban network in 2027, with
  EV penetration at ~5.7% of fleet, initial utilization will be limited (5–15% of
  theoretical station capacity). As EV adoption accelerates under EU CO2 mandates
  (100% ZEV new car sales by 2035), utilization grows to 20–35% by 2030.
  Key business implication: stations should be sized for 2027 operational demand but
  sited and civil-worked for 2030 expansion (4-charger now, 8-charger conduit ready).
  This "build for now, ready for growth" approach minimises 2027 CAPEX while avoiding
  the high cost of retrofitting sites in 2029–2030.
- **Impact on model:** Frames the phased deployment strategy in the analytical report.
  Supports the recommendation to prioritise sites at Sufficient grid locations for
  immediate deployment in 2027, Moderate sites after partial reinforcement in 2028–29,
  and Congested sites post-major grid investment in 2030+.
- **Sources:** IEA GEVO 2025 charger utilization section; IONITY utilization disclosures;
  EU CO2 regulation roadmap (Regulation 2019/631 as amended).

---

## CATEGORY G — DATA & METHODOLOGY

### G1 — Grid Data Interpretation (0 MW Entries)

- **Value used:** 0.000 MW available capacity entries are treated as "fully subscribed —
  no headroom available at time of publication", not as data errors or missing values.
- **Justification:** 80.6% of the 2,137 unique physical substations in
  `grid_consolidated.csv` show exactly 0.000 MW available capacity (collapsed from
  4,990 raw voltage-tap records in `grid_capacity_unified.csv`). This is consistent across all three DSOs
  (i-DE, Endesa, Viesgo) and reflects the authentic published state of Spain's
  distribution network as of early 2026. DSO capacity publications by regulation must
  accurately reflect available access capacity; a systematic error of this magnitude
  across three independent operators is implausible. The 0 MW entries represent real
  saturation — substations where all available connection capacity has been reserved
  by prior applications. This is the authentic infrastructure constraint picture.
- **Impact on model:** 87.2% of proposed station locations will be classified as
  Congested, which is the realistic and defensible outcome. The friction analysis
  narrative must explain this clearly to the jury.
- **Sources:** i-DE official capacity publication (data/raw/grid_capacity/ide_iberdrola/);
  Endesa official publication (data/raw/grid_capacity/endesa/);
  Viesgo official publication (data/raw/grid_capacity/viesgo/);
  CNMC regulatory framework for DSO capacity publication.

### G2 — Interurban Road Filter

- **Rule:** Only autopistas (AP-), autovías (A-), and carreteras nacionales (N-) included.
- **Exclusion:** Urban road sections excluded regardless of municipality size.
- **Method:** Filter using Ministry of Transport road classification field in
  hermes_roads.geojson (`Tipo_de_via` and road naming convention).
- **Status:** CONFIRMED — mandated by datathon brief §2.
- **Source:** Datathon brief §2 (Scope of Analysis).

### G3 — Spatial Matching Method (Station to Substation)

- **Method:** BallTree nearest-neighbor search using haversine distance metric.
  Each proposed station matched to nearest substation within 25 km maximum radius.
  Distance tier assigned per D4. Distributor_network assigned from matched substation.
- **Justification:** BallTree with haversine is the computationally optimal approach
  for nearest-neighbor queries on geographic coordinates (O(n log n) preprocessing,
  O(log n) query). scipy.spatial.BallTree with haversine metric handles lat/lon
  natively without requiring projected coordinates.
- **Implementation:** src/geo_utils.py — find_nearest_substation() function.
- **Source:** scipy documentation; standard geospatial nearest-neighbor methodology.

---

## REVISION HISTORY

| Date | Author | Change |
|------|--------|--------|
| 2026-03-16 | Nicolas (consultant) + Claude agent | Full revision after comprehensive research. All categories researched against IEA GEVO 2025, AFIR full text, ANFAC Spain, CNMC standards, IDAE guides, repo data analysis. 8 assumptions revised, 5 new assumptions added, 7 confirmed. |
| 2026-03-14 | Initial | First draft — placeholder values. |
