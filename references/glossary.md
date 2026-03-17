# Acronym Glossary

Last updated: 2026-03-16  
Scope: All acronyms used across project documentation, assumptions register, source guides,
notebooks, and research references.

---

| Acronym | Full Name | What It Is / Role in the Project |
|---------|-----------|----------------------------------|
| **AC** | Alternating Current | Type of electrical current used in slow chargers (3–22 kW). Relevant for distinguishing slow AC from fast DC charging infrastructure in the NAP dataset. |
| **ACEA** | European Automobile Manufacturers Association *(Assoc. des Constructeurs Européens d'Automobiles)* | EU-level industry body publishing EV registration and market share data. Cross-validation source for Spain's EV fleet projections. |
| **AESP** | Áreas de Estacionamiento Seguro y Protegido | Spain's certified safe and secure parking areas on highways (Gold/Silver/Bronze classification). 12 certified sites in the repo — secondary candidate locations for overnight EV charging. |
| **AFIR** | Alternative Fuels Infrastructure Regulation *(EU Regulation 2023/1804)* | The binding EU regulation mandating minimum EV charging coverage on TEN-T roads. Sets the 60 km spacing rule on TEN-T Core and 100 km on TEN-T Comprehensive. The primary compliance framework for this project. |
| **ANFAC** | Asociación Nacional de Fabricantes de Automóviles y Camiones | Spain's national vehicle manufacturers association. Publishes monthly EV registration statistics and annual electrification barometers. Used to cross-validate SARIMA fleet projections. |
| **AP** | Autopista de Peaje | Toll motorway in Spain (e.g. AP-7, AP-9). One of the three interurban road types in scope for this project. |
| **API** | Application Programming Interface | Programmatic data access endpoint. Used to retrieve REE electricity data (`apidatos.ree.es`) and MITECO fuel station data. |
| **BEV** | Battery Electric Vehicle | A fully electric vehicle with no combustion engine. The only EV category that generates significant interurban highway charging demand (PHEVs use ICE on long trips). ~60% of Spain's projected 2027 EV fleet. |
| **CAPEX** | Capital Expenditure | Upfront investment cost. Used in assumption F1 (€80–130K per installed 150 kW charger) to quantify the total network investment required in the analytical report. |
| **CCAA** | Comunidades Autónomas | Spain's 19 autonomous communities (regions). Used as spatial aggregation unit for tourism, population, and grid territory mapping. |
| **CNMC** | Comisión Nacional de los Mercados y la Competencia | Spain's national markets and competition regulator. Sets technical standards for grid connection, tariffs, and DSO capacity publication obligations. Source for grid threshold justifications (D1–D4). |
| **DC** | Direct Current | Type of electrical current used in fast chargers (≥50 kW). All proposed stations in this project use DC fast charging at 150 kW (mandated by datathon rules). |
| **DGT** | Dirección General de Tráfico | Spain's General Directorate of Traffic. Publishes IMD traffic counts, total vehicle fleet statistics, and seasonal traffic data. Core data source for demand modeling. |
| **DSO** | Distribution System Operator | Operator of the local electricity distribution grid. The three DSOs covering Spain's highway network are: i-DE (Iberdrola), e-distribución (Endesa), and Viesgo. Grid viability analysis is conducted per DSO territory. |
| **EU** | European Union | The regulatory authority behind AFIR, CO2 vehicle standards (Regulation 2019/631), and TEN-T network policy. |
| **EUR-Lex** | European Union Law Database | Official EU legal database where the full text of AFIR (Regulation 2023/1804) was retrieved and verified. |
| **EV** | Electric Vehicle | Umbrella term for all electrified vehicles (BEV + PHEV). Used broadly in the project but split into BEV/PHEV for demand modeling purposes. |
| **GEVO** | Global EV Outlook | IEA's annual flagship report on electric vehicle markets, technology, and policy. The 2025 edition is a primary research source for assumptions A1, A2, B1, B2, E1, and E2. |
| **GW** | Gigawatt | Unit of power. Spain has ~136 GW installed electricity generation capacity (REE 2024), relevant for the smart charging and grid context narrative. |
| **i-DE** | Iberdrola Distribución Eléctrica | Iberdrola's own distribution system operator. Covers ~3,016 substations in the repo. Has the highest congestion rate of the three DSOs (92% Congested) but is Iberdrola's home territory — the core business case for grid reinforcement investment. |
| **ICCT** | International Council on Clean Transportation | Independent research NGO publishing real-world BEV range studies and EV policy analysis. Source for the WLTP-to-real-world correction factor used in assumption A2. |
| **ICE** | Internal Combustion Engine | Conventional petrol/diesel engine. PHEVs use ICE on long interurban trips, which is why they do not generate highway DC fast charging demand. |
| **IDAE** | Instituto para la Diversificación y Ahorro de la Energía | Spain's national energy agency under the Ministry for Ecological Transition. Publishes EV infrastructure planning guidelines, the MOVES subsidy programme, and energy efficiency standards. Source for grid threshold justifications (D1–D3) and EV deployment planning. |
| **IE** | Instituto de Empresa | The business school organising this datathon (IE Sustainability Datathon, March 2026). |
| **IEA** | International Energy Agency | Paris-based intergovernmental energy body. The IEA Global EV Outlook 2025 is the primary external reference for EV range (A1), charging probability (B1), fleet projections (E1), and strategic recommendations. |
| **IGN** | Instituto Geográfico Nacional | Spain's national geographic institute. Source of the province and autonomous community boundary files used for spatial joins throughout the project. |
| **IMD** | Intensidad Media Diaria | Average Daily Traffic Intensity — the official DGT metric for daily vehicle counts at traffic stations. The primary demand signal for corridor-level station sizing. Expressed in vehicles/day. Median on Spain's interurban network: ~8,155 vehicles/day; maximum: ~190,000 (AP-7). |
| **INE** | Instituto Nacional de Estadística | Spain's national statistics institute. Source for municipal population data, hotel occupancy by province, and hotel traveler/overnight stay data — used to build seasonal demand multipliers. |
| **IONITY** | IONITY GmbH | Pan-European high-power charging network (co-owned by BMW, Ford, Hyundai, Mercedes, VW). Key benchmark for interurban station configurations (8–16 chargers), utilization rates (8–20%), and 24/7 operational standards. Referenced in assumptions B1, B3, B5, F3. |
| **KPI** | Key Performance Indicator | Summary metrics required in File_1.csv (e.g. total_proposed_stations, total_ev_projected_2027, total_estimated_demand_kw). |
| **LP** | Linear Programming | Mathematical optimization technique used in NB 07 to solve the Set Cover problem: minimise total station count subject to spacing coverage constraints. Implemented with PuLP or OR-Tools. |
| **MITECO** | Ministerio para la Transición Ecológica y el Reto Demográfico | Spain's Ministry for Ecological Transition. Operates the official fuel station registry API (12,216 gas stations), a key source for candidate co-location sites. |
| **MOVES** | Plan de Incentivos para el Vehículo Eficiente | Spain's national EV purchase subsidy programme (MOVES I, II, III). Key policy driver of EV adoption acceleration, referenced in the fleet projection context (E1). |
| **MOVILIA** | Encuesta de Movilidad de las Personas Residentes en España | Spain's National Household Mobility Survey by the Ministry of Transport. Source for the 35% interurban trip fraction assumption (E6). |
| **MT** | Media Tensión | Medium Voltage electricity distribution (typically 1–36 kV in Spain). The voltage level at which most highway charging stations would connect to the distribution grid. Referenced in CNMC connection standards for D1–D4. |
| **MW** | Megawatt | Unit of power capacity. Used throughout the grid analysis: Sufficient ≥5 MW, Moderate 1–5 MW, Congested <1 MW. |
| **NAP** | National Access Point | Spain's official national registry of EV charging points, published by DGT. Contains 12,072 sites; 5,338 qualify as highway-grade (≥50 kW). Core baseline dataset for existing coverage analysis (assumption C4). |
| **NPRA** | Norwegian Public Roads Administration *(Statens vegvesen)* | Norway's highway authority. Operates one of the world's most mature EV highway charging networks. Referenced for real-world charger utilization rates (B1) and highway spacing precedent (C1). |
| **OD** | Origin-Destination | A matrix representing trip flows between geographic units (municipalities, provinces). The pyspainmobility OD matrix is the primary demand data source for routing actual inter-city trips through the road network in NB 06. |
| **OSM** | OpenStreetMap | Open-source geographic data platform. Referenced in the repo folder name `osm_rest_areas`, though the stored data uses the official Hermes source. Used as a fallback for any missing geospatial features. |
| **PHEV** | Plug-in Hybrid Electric Vehicle | A vehicle with both an electric motor and a combustion engine. ~65 km electric range in Europe (IEA). Uses ICE on interurban trips — excluded from highway DC fast charging demand (assumptions A4, E2). ~40% of Spain's projected 2027 EV fleet. |
| **PNIEC** | Plan Nacional Integrado de Energía y Clima | Spain's National Integrated Energy and Climate Plan. Sets national targets for EV adoption, renewable energy, and emissions reduction to 2030. Policy context for the strategic section of the analytical report. |
| **PV** | Photovoltaic | Solar panel technology generating electricity directly from sunlight. Spain has large installed solar PV capacity — the basis for the smart charging window recommendation (assumption F2, 10:00–16:00). |
| **REE** | Red Eléctrica de España | Spain's transmission system operator (TSO). Operates the high-voltage (≥220 kV) national grid. Source for installed capacity data (136 GW), hourly demand profiles, and transmission-level connection access requests. Distinct from the DSOs (i-DE, Endesa, Viesgo) who operate the distribution grid. |
| **SARIMA** | Seasonal AutoRegressive Integrated Moving Average | Time series forecasting model used in NB 02 to project Spain's cumulative EV fleet to December 2027 (~2.5M vehicles). Output is mandatory input for File_1.csv per datathon rules (assumption E1). |
| **SoC** | State of Charge | Battery charge level expressed as a percentage (0–100%). Drivers typically charge when SoC drops to ~20–30%, creating the practical spacing constraint: effective range × 50% SoC buffer = maximum comfortable inter-station distance. |
| **TEN-T** | Trans-European Transport Network | The EU's strategic cross-border transport infrastructure network. Divided into Core (highest priority, 60 km AFIR spacing rule) and Comprehensive (100 km AFIR spacing rule). 77 corridor segments flagged in the repo road data. |
| **TSO** | Transmission System Operator | Operator of the high-voltage national electricity grid. In Spain: REE. Distinct from DSOs who operate the local distribution network below 220 kV. |
| **V2G** | Vehicle-to-Grid | Technology enabling EVs to discharge electricity back into the grid. Mentioned in assumption F2 as a strategic recommendation for smart-charging capable stations in Iberdrola's network. |
| **WLTP** | Worldwide Harmonised Light Vehicle Test Procedure | The standardised lab test used to measure EV range on a controlled drive cycle. Real-world highway range is ~10% below WLTP due to higher speeds and accessory loads. Core of assumptions A1 (340 km WLTP) and A2 (75% effective factor). |
| **ZEV** | Zero-Emission Vehicle | A vehicle with zero tailpipe emissions (BEVs and FCEVs qualify; PHEVs do not). The EU mandates 100% ZEV new car sales by 2035 under Regulation 2019/631, the long-run policy driver of EV adoption growth underlying all fleet projections. |
