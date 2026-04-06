# IE Sustainability Datathon March 2026 — Intelligent Electric Mobility (Iberdrola)

**Team:** Greenlabs

Optimal placement of EV charging stations along Spain's interurban road network for 2027, incorporating electrical grid capacity constraints.

---

## Challenge Overview

Design an optimal EV charging network along Spain's interurban roads (autopistas, autovías, carreteras nacionales) for a 2027 horizon. The solution must cross-reference mobility demand data with electrical grid capacity constraints from three distribution network operators: i-DE (Iberdrola), Endesa (e-distribución), and Viesgo.

**Deliverables:**
- `File_1.csv` — Global Network KPIs (single-row summary scorecard)
- `File_2.csv` — Proposed Charging Locations
- `File_3.csv` — Friction Points (Moderate/Congested only)
- `visualization/bi_map.html` — Self-contained interactive map
- `report/analytical_report.pdf` — 3-5 page executive summary
- `presentation/pitch.pdf` — Max 5 min pitch deck

---

## Repository Structure

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
│   ├── 02_ev_projection_fork.ipynb
│   ├── 03_road_network_analysis.ipynb
│   ├── 04_existing_chargers_baseline.ipynb
│   ├── 05_grid_capacity_consolidation.ipynb
│   ├── 06_demand_modeling.ipynb
│   ├── 07_network_optimization.ipynb
│   ├── 08_grid_viability_friction.ipynb
│   ├── 09_output_generation.ipynb
│   └── 10_visualization_export.ipynb
├── src/
│   ├── __init__.py
│   ├── data_loading.py
│   ├── geo_utils.py
│   ├── grid_analysis.py
│   ├── optimization.py
│   └── constants.py
├── output/
│   ├── File_1.csv
│   ├── File_2.csv
│   └── File_3.csv
├── visualization/
│   └── bi_map.html
├── report/
│   └── analytical_report.pdf
├── presentation/
│   └── pitch.pdf
└── references/
    ├── sources.md
    └── assumptions.md
```

---

## Data Sources

See [references/sources.md](references/sources.md) for full citations.

**Mandatory:**
1. Road Routes — Ministry of Transport and Sustainable Mobility
2. EV Charging Points — National Access Point (NAP)
3. Route to Electrification — datos.gob.es GitHub Fork (**MANDATORY**)
4. i-DE Consumption Capacity Map — Iberdrola Group
5. e-distribución Historical Access Capacity — Endesa
6. Viesgo Interactive Grid Map — Viesgo Distribución
7. DGT Vehicle Registrations — Dirección General de Tráfico

**Additional (Innovation):**
8. DGT IMD Traffic Counts
9. INE Population & Tourism Data
10. REE Grid Data
11. OpenStreetMap Rest Areas (Overpass API)
12. EU TEN-T Core Network Corridors
13. AFIR Regulation Requirements
14. IDAE Studies
15. ANFAC / ACEA EV Statistics

---

## Methodology Overview

1. **EV Projection** (NB 02): Run datos.gob.es fork → 2027 fleet estimate
2. **Road Network** (NB 03): Load Ministry roads → filter interurban → map geometry
3. **Demand Modeling** (NB 06): Traffic × EV share 2027 → charging demand per segment
4. **Optimization** (NB 07): Station placement algorithm (Objective 1)
5. **Grid Viability** (NB 08): Spatial join stations↔substations → grid_status + friction points (Objective 2)
6. **Output** (NB 09): Generate File_1.csv, File_2.csv, File_3.csv in exact format

---

## How to Run

Run notebooks in order from `00` to `10`. Each notebook is self-contained with clear inputs/outputs documented at the top.

```bash
pip install -r requirements.txt
jupyter notebook notebooks/00_environment_setup.ipynb
```

---

## Deliverables

| File | Description |
|------|-------------|
| `output/File_1.csv` | Global Network KPIs — single row summary scorecard |
| `output/File_2.csv` | Proposed Charging Locations with grid status |
| `output/File_3.csv` | Friction Points (Moderate + Congested only) |
| `visualization/bi_map.html` | Self-contained interactive map (no logins required) |
| `report/analytical_report.pdf` | 3-5 page executive summary |
| `presentation/pitch.pdf` | Max 5 min pitch deck |

---

## Key Assumptions

See [references/assumptions.md](references/assumptions.md) for full documentation.

- 150 kW per charger (mandated by datathon rules)
- Max station spacing: 150 km
- Average EV range: 300 km WLTP (240 km effective)
- Grid status thresholds: ≥5 MW = Sufficient, 1-5 MW = Moderate, <1 MW = Congested

---

*This project was developed for the IE Datathon March 2026 in collaboration with Iberdrola.*
