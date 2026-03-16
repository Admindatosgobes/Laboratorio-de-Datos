# Prompt for Claude Code — Iberdrola Datathon Repository Setup

Paste everything below the line into Claude Code:

---

I'm setting up a repository for the IE Sustainability Datathon March 2026 with Iberdrola. The challenge is to design an optimal EV charging network along Spain's interurban roads (autopistas, autovías, carreteras nacionales) for a 2027 horizon, cross-referencing mobility data with electrical grid capacity constraints.

## 1. CREATE THE FULL DIRECTORY STRUCTURE

```
iberdrola-datathon-2026/
├── README.md
├── .gitignore
├── requirements.txt
├── data/
│   ├── raw/
│   │   ├── ministry_roads/          # Ministry of Transport road network shapefiles/GeoJSON
│   │   ├── nap_charging_points/     # National Access Point existing EV charger dataset
│   │   ├── grid_capacity/
│   │   │   ├── ide_iberdrola/       # i-DE consumption capacity map CSV/XLSX
│   │   │   ├── endesa/              # e-distribución historical access capacity CSV/XLSX
│   │   │   └── viesgo/              # Viesgo distribution capacity CSV/XLSX
│   │   ├── dgt_registrations/       # DGT monthly vehicle registration ZIPs (Jun-Nov 2025)
│   │   ├── datos_gob_ev_forecast/   # Output from the mandatory datos.gob.es GitHub fork
│   │   └── additional/
│   │       ├── dgt_imd_traffic/     # DGT Intensidad Media Diaria (avg daily traffic counts)
│   │       ├── ine_population/      # INE population/tourism by municipality
│   │       ├── ree_grid/            # REE transmission-level data
│   │       ├── osm_rest_areas/      # OpenStreetMap rest areas/service stations extraction
│   │       ├── tent_corridors/      # EU TEN-T core corridor maps for Spain
│   │       └── afir_requirements/   # AFIR regulation reference docs
│   ├── processed/                   # Cleaned and transformed datasets ready for modeling
│   └── interim/                     # Intermediate processing outputs
├── notebooks/
│   ├── 00_environment_setup.ipynb
│   ├── 01_data_ingestion_and_cleaning.ipynb
│   ├── 02_ev_projection_fork.ipynb           # Mandatory: datos.gob.es exercise 3 fork integration
│   ├── 03_road_network_analysis.ipynb        # Load Ministry roads, filter interurban, map geometry
│   ├── 04_existing_chargers_baseline.ipynb   # NAP dataset → filter to interurban → coverage gaps
│   ├── 05_grid_capacity_consolidation.ipynb  # Merge i-DE + Endesa + Viesgo into unified grid dataset
│   ├── 06_demand_modeling.ipynb              # Traffic × EV share 2027 → charging demand per segment
│   ├── 07_network_optimization.ipynb         # Station placement algorithm (Objective 1)
│   ├── 08_grid_viability_friction.ipynb      # Spatial join stations↔substations → grid_status + friction points (Objective 2)
│   ├── 09_output_generation.ipynb            # Generate File_1.csv, File_2.csv, File_3.csv in exact format
│   └── 10_visualization_export.ipynb         # Build self-contained HTML map (Folium/Leaflet)
├── src/
│   ├── __init__.py
│   ├── data_loading.py             # Reusable functions for loading each dataset
│   ├── geo_utils.py                # Spatial operations: nearest substation, point-on-road, haversine
│   ├── grid_analysis.py            # Grid capacity classification logic
│   ├── optimization.py             # Core optimization algorithm for station placement
│   └── constants.py                # All fixed parameters (150 kW per charger, autonomy range, thresholds)
├── output/
│   ├── File_1.csv                  # Global Network KPIs (Summary Scorecard) — single row
│   ├── File_2.csv                  # Proposed Charging Locations
│   └── File_3.csv                  # Friction Points (only Moderate/Congested from File 2)
├── visualization/
│   └── bi_map.html                 # Self-contained interactive map — NO external dependencies/logins
├── report/
│   └── analytical_report.pdf       # 3-5 page executive summary
├── presentation/
│   └── pitch.pdf                   # Max 5 min pitch deck
└── references/
    ├── sources.md                  # Full citation of every data source used
    └── assumptions.md              # All assumptions with justification and references
```

## 2. CREATE THE .gitignore

Include patterns for:
- `data/raw/**/*.zip` and large binary files
- `data/raw/**/*.shp`, `*.dbf`, `*.shx`, `*.prj` (shapefiles are large — track with Git LFS or ignore)
- `__pycache__/`, `.ipynb_checkpoints/`, `*.pyc`
- `.env`, `*.log`
- OS files: `.DS_Store`, `Thumbs.db`
- But DO NOT ignore `output/*.csv` — those are deliverables
- Do NOT ignore `visualization/*.html` — that's a deliverable too

## 3. CREATE requirements.txt

Include these libraries (these are what we'll use in Google Colab and locally):
```
pandas>=2.0
geopandas>=0.14
shapely>=2.0
folium>=0.15
numpy>=1.24
matplotlib>=3.7
seaborn>=0.13
scikit-learn>=1.3
scipy>=1.11
requests>=2.31
openpyxl>=3.1
xlrd>=2.0
pyproj>=3.6
rtree>=1.1
branca>=0.7
```

## 4. CREATE README.md

Write a professional README with:
- Project title: "IE Sustainability Datathon March 2026 — Intelligent Electric Mobility (Iberdrola)"
- Brief description: Optimal placement of EV charging stations along Spain's interurban road network for 2027, incorporating electrical grid capacity constraints.
- Team name: [TEAM_NAME] (placeholder)
- Sections: Challenge Overview, Repository Structure (reproduce the tree above), Data Sources (list all mandatory + additional with URLs), Methodology Overview (briefly: EV projection → road network → demand modeling → optimization → grid viability → output), How to Run (point to notebooks 00-10 in order), Deliverables (File 1, 2, 3 + map + report + pitch), Key Assumptions (link to references/assumptions.md)
- At the bottom: "This project was developed for the IE Datathon March 2026 in collaboration with Iberdrola."

## 5. CREATE references/sources.md

Pre-populate with all known data sources in this format:

```markdown
# Data Sources

## Mandatory Sources
1. **Road Routes** — Ministry of Transport and Sustainable Mobility
   - URL: https://www.mitma.gob.es/ (exact dataset link TBD)
   - Content: Interurban road network geometry (autopistas, autovías, carreteras nacionales)
   - Used in: Notebooks 03, 06, 07

2. **Electric Vehicle Charging Points** — National Access Point for Traffic and Mobility
   - URL: https://nap.mitma.es/
   - Content: Existing EV charging station locations across Spain
   - Used in: Notebooks 04, 07

3. **Route to Electrification (datos.gob.es)** — GitHub Fork (MANDATORY)
   - URL: https://datos.gob.es/ (link to specific repo TBD)
   - Content: EV growth projection model → 2027 fleet estimate
   - Used in: Notebooks 02, 06, 09

4. **i-DE Consumption Capacity Map** — Iberdrola Group
   - URL: https://www.i-de.es/conexion-red/mapa-capacidad-consumo
   - Content: Substation-level available capacity (MW) + coordinates
   - Used in: Notebooks 05, 08

5. **e-distribución Historical Access Capacity** — Endesa
   - URL: https://www.edistribucion.com/ (capacity documents section)
   - Content: Node-level access capacity data (CSV/XLSX)
   - Used in: Notebooks 05, 08

6. **Viesgo Interactive Grid Map** — Viesgo Distribución
   - URL: https://www.viesgodistribucion.com/
   - Content: Substation-level capacity for northern Spain
   - Used in: Notebooks 05, 08

7. **DGT Vehicle Registrations** — Dirección General de Tráfico
   - URL: https://www.dgt.es/microdatos/
   - Content: Monthly registration data by province (Jun-Nov 2025)
   - Used in: Notebooks 01, 06

## Additional Sources (Innovation)
8. **DGT IMD Traffic Counts** — Intensidad Media Diaria
   - Content: Average daily traffic volume per road segment
   - Used in: Notebooks 03, 06

9. **INE Population & Tourism Data** — Instituto Nacional de Estadística
   - URL: https://www.ine.es/
   - Content: Municipal population, tourism flow by province
   - Used in: Notebook 06

10. **REE Grid Data** — Red Eléctrica de España
    - URL: https://www.ree.es/ / https://www.esios.ree.es/
    - Content: Transmission-level demand/capacity by region
    - Used in: Notebook 05

11. **OpenStreetMap Rest Areas** — via Overpass API
    - Content: Service stations and rest areas on Spanish motorways
    - Used in: Notebook 07

12. **EU TEN-T Core Network Corridors** — European Commission
    - Content: Trans-European Transport Network maps for Spain
    - Used in: Notebooks 03, 07 (AFIR compliance check)

13. **AFIR Regulation Requirements** — EU Alternative Fuels Infrastructure Regulation
    - Content: Mandatory charging pool spacing (every 60 km on TEN-T core by end 2025)
    - Used in: Notebooks 07, Report

14. **IDAE Studies** — Instituto para la Diversificación y Ahorro de la Energía
    - URL: https://www.idae.es/
    - Content: EV charging patterns and infrastructure planning studies
    - Used in: Report, assumptions

15. **ANFAC / ACEA EV Statistics** — Manufacturer associations
    - Content: Average EV range by model, fleet composition data
    - Used in: Assumptions (autonomy range justification)
```

## 6. CREATE references/assumptions.md

```markdown
# Assumptions Register

All assumptions used in this model are documented below with justification.

## A1 — Average EV Autonomy Range
- **Value used:** 300 km (WLTP)
- **Effective range (80% usable):** 240 km
- **Justification:** Based on weighted average of top-selling EVs in Spain (2024-2025 fleet mix). Sources: ANFAC registration data, ACEA EV report.
- **Impact on model:** Determines maximum station spacing (~120-150 km between chargers to ensure no driver falls below 20% battery).

## A2 — Maximum Station Spacing
- **Value used:** 150 km
- **Justification:** Derived from A1. Conservative buffer: 240 km effective range ÷ ~1.6 safety factor = 150 km. Also aligned with AFIR requirement of charging pools every 60 km on TEN-T core network (our spacing is more conservative for non-TEN-T roads).
- **Impact on model:** Core parameter for the optimization algorithm's coverage constraint.

## A3 — Standard Power per Charger
- **Value used:** 150 kW (FIXED — mandated by datathon rules)
- **Impact on model:** estimated_demand_kw = n_chargers_proposed × 150 kW

## A4 — Grid Status Classification Thresholds
- **Sufficient:** Available capacity ≥ 5 MW at nearest substation
- **Moderate:** Available capacity between 1 MW and 5 MW
- **Congested:** Available capacity < 1 MW
- **Justification:** A typical interurban charging station with 4 fast chargers requires 0.6 MW (4 × 150 kW). "Sufficient" means the substation can comfortably host the station plus future expansion. "Moderate" means it can host a station but with limited headroom. "Congested" means grid reinforcement is needed before deployment.
- **Spatial matching method:** Each proposed station is matched to the nearest substation within a [X] km radius using haversine distance. If no substation exists within radius, classified as Congested by default.
- **Sources:** [TBD — cite industry standards, CNMC reports, or IDAE planning guides]

## A5 — Number of Chargers per Station
- **Method:** Based on projected daily EV traffic at that road segment × average charging probability × average charging duration.
- **Formula:** n_chargers = ceil((daily_ev_traffic × charging_probability × avg_charge_hours) / operating_hours_per_day)
- **Default range:** 2-8 chargers per station depending on corridor traffic volume.
- **Assumptions within:**
  - Charging probability per passing EV: ~5-10% on any given trip
  - Average charging session: 20-30 minutes for DC fast charging
  - Operating hours: 18 hours/day effective utilization window
- **Sources:** [TBD — IDAE, ChargePoint utilization studies]

## A6 — EV Fleet Projection 2027
- **Value used:** [OUTPUT FROM DATOS.GOB.ES FORK]
- **Source:** Mandatory GitHub fork of datos.gob.es Exercise 3
- **Used for:** total_ev_projected_2027 in File 1, and as input to demand model

## A7 — Seasonal Traffic Adjustment
- **Method:** Apply seasonal multiplier to IMD traffic data for summer months (Jul-Aug) on Mediterranean and coastal corridors.
- **Multiplier:** 1.5x - 2.5x depending on corridor (AP-7, A-7 highest)
- **Justification:** DGT historical traffic data shows peak summer volumes on coastal routes.
- **Impact on model:** Station sizing on tourist corridors accounts for peak demand, not just annual average.

## A8 — Interurban Road Filter
- **Rule:** Only autopistas (AP-), autovías (A-), and carreteras nacionales (N-) are included.
- **Exclusion:** Urban road sections excluded regardless of municipality size, per datathon rules.
- **Method:** Filter using Ministry of Transport road classification field.
```

## 7. CREATE src/constants.py

```python
"""
Fixed parameters and constants for the Iberdrola Datathon 2026.
All values are documented and justified in references/assumptions.md
"""

# === MANDATED BY DATATHON RULES (DO NOT CHANGE) ===
POWER_PER_CHARGER_KW = 150  # Fixed at 150 kW per charger for all teams

# === EV AUTONOMY AND SPACING ===
AVG_EV_RANGE_KM = 300       # WLTP average range
USABLE_RANGE_FACTOR = 0.80  # Drivers won't go below 20% battery
EFFECTIVE_RANGE_KM = AVG_EV_RANGE_KM * USABLE_RANGE_FACTOR  # 240 km
MAX_STATION_SPACING_KM = 150  # Conservative max gap between stations
AFIR_SPACING_KM = 60        # EU AFIR requirement on TEN-T core corridors

# === GRID STATUS THRESHOLDS (MW available at nearest substation) ===
GRID_SUFFICIENT_MIN_MW = 5.0    # >= 5 MW → Sufficient
GRID_MODERATE_MIN_MW = 1.0      # >= 1 MW and < 5 MW → Moderate
# < 1 MW → Congested

GRID_STATUS_LABELS = {
    'sufficient': 'Sufficient',
    'moderate': 'Moderate',
    'congested': 'Congested',
}

# === SUBSTATION MATCHING ===
MAX_SUBSTATION_SEARCH_RADIUS_KM = 25  # Max distance to match a station to a substation
DEFAULT_STATUS_IF_NO_SUBSTATION = 'Congested'  # If no substation found within radius

# === DEMAND MODELING ===
CHARGING_PROBABILITY = 0.07     # 7% of passing EVs will charge at a given station
AVG_CHARGE_DURATION_HOURS = 0.4 # ~24 minutes average DC fast charge session
EFFECTIVE_OPERATING_HOURS = 18  # Hours per day the station is effectively available

# === SEASONAL MULTIPLIERS (for peak summer on coastal corridors) ===
SEASONAL_MULTIPLIERS = {
    'default': 1.0,
    'mediterranean_summer': 2.0,  # AP-7, A-7 Jul-Aug
    'atlantic_summer': 1.5,       # A-8, AP-9 Jul-Aug
}

# === OUTPUT FILE NAMES ===
OUTPUT_FILE_1 = 'File_1.csv'  # Global Network KPIs
OUTPUT_FILE_2 = 'File_2.csv'  # Proposed Charging Locations
OUTPUT_FILE_3 = 'File_3.csv'  # Friction Points

# === OUTPUT SCHEMAS ===
FILE_1_COLUMNS = [
    'total_proposed_stations',
    'total_existing_stations_baseline',
    'total_friction_points',
    'total_ev_projected_2027',
]

FILE_2_COLUMNS = [
    'location_id',
    'latitude',
    'longitude',
    'route_segment',
    'n_chargers_proposed',
    'grid_status',
]

FILE_3_COLUMNS = [
    'bottleneck_id',
    'latitude',
    'longitude',
    'route_segment',
    'distributor_network',
    'estimated_demand_kw',
    'grid_status',
]

# === ACCEPTED VALUES ===
VALID_GRID_STATUSES_FILE2 = ['Sufficient', 'Moderate', 'Congested']
VALID_GRID_STATUSES_FILE3 = ['Moderate', 'Congested']  # Sufficient NOT allowed in File 3
VALID_DISTRIBUTORS = ['i-DE', 'Endesa', 'Viesgo']
```

## 8. CREATE PLACEHOLDER NOTEBOOKS

For each notebook in the `notebooks/` folder, create a minimal .ipynb file (or .py file that can be uploaded to Colab) with:
- A markdown title cell with the notebook name and purpose
- A markdown cell listing "Data inputs" and "Data outputs" for that notebook
- An empty code cell with `# TODO: implement`

Use this pattern for each:

**00_environment_setup.ipynb**: "Install dependencies, mount Google Drive, verify all raw data files are accessible."

**01_data_ingestion_and_cleaning.ipynb**: "Load all raw datasets. Clean, standardize coordinate systems to WGS84 (EPSG:4326). Save cleaned versions to data/processed/."

**02_ev_projection_fork.ipynb**: "Run the datos.gob.es Exercise 3 EV growth model. Extract the 2027 projected EV fleet number for Spain. This is MANDATORY — the output feeds directly into File 1 and the demand model."

**03_road_network_analysis.ipynb**: "Load Ministry of Transport road network. Filter to autopistas (AP-), autovías (A-), carreteras nacionales (N-). Remove urban sections. Build the interurban road graph/geometry."

**04_existing_chargers_baseline.ipynb**: "Load NAP charging point dataset. Filter to stations on interurban roads only. Calculate total_existing_stations_baseline for File 1. Identify current coverage gaps."

**05_grid_capacity_consolidation.ipynb**: "Load i-DE, Endesa, and Viesgo capacity datasets. Standardize into unified format: substation_id, latitude, longitude, available_capacity_mw, distributor_network. Save consolidated grid dataset."

**06_demand_modeling.ipynb**: "Combine: road network segments + DGT traffic counts (IMD) + EV fleet projection 2027 + seasonal multipliers. Calculate projected daily EV traffic per road segment. Determine required number of chargers per station candidate."

**07_network_optimization.ipynb**: "Run the station placement optimization. Inputs: road network with demand, existing charger locations, spacing constraints. Output: list of proposed new station locations with n_chargers_proposed. Algorithm should minimize total stations while ensuring full coverage (no gap > MAX_STATION_SPACING_KM)."

**08_grid_viability_friction.ipynb**: "For each proposed station from notebook 07, find nearest electrical substation from the consolidated grid dataset. Assign grid_status based on available capacity thresholds. Generate friction points list (Moderate + Congested only)."

**09_output_generation.ipynb**: "Assemble and validate File_1.csv, File_2.csv, File_3.csv in the exact required format. Print structure and first/last rows of each file for verification. Run validation checks: correct column names, no Sufficient in File 3, estimated_demand_kw = n_chargers × 150."

**10_visualization_export.ipynb**: "Build self-contained HTML map using Folium. Plot all File 2 stations color-coded: Green=Sufficient, Yellow=Moderate, Red=Congested. Popups show: location_id, route_segment, n_chargers_proposed, grid_status. Add layers: existing chargers, road network, friction points. Export to visualization/bi_map.html — must work offline with no logins."

## 9. ORGANIZE EXISTING FILES

Look in the current directory and any subdirectories for files I may have already downloaded. If you find any of the following types, move them to the appropriate `data/raw/` subfolder:
- Road network files (.shp, .geojson, .gpkg, .kml) → `data/raw/ministry_roads/`
- Charging point CSVs/JSONs → `data/raw/nap_charging_points/`
- i-DE capacity files (.csv, .xlsx, .pdf) → `data/raw/grid_capacity/ide_iberdrola/`
- Endesa/e-distribución capacity files → `data/raw/grid_capacity/endesa/`
- Viesgo capacity files → `data/raw/grid_capacity/viesgo/`
- DGT registration ZIPs → `data/raw/dgt_registrations/`
- The datathon PDF brief → root of repository as `datathon_brief.pdf`
- Any other datasets → `data/raw/additional/` with a note

## 10. FINAL VERIFICATION

After creating everything, run `find . -type f | head -50` and `tree -L 3` to show me the full structure. Confirm:
- All directories exist
- All placeholder files are created
- .gitignore is properly configured
- README.md is complete
- constants.py has all the right values
- sources.md and assumptions.md are populated

Then tell me what data files you found and where you placed them, and what files are still missing that I need to download manually.
