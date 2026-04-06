# Data Source Guide

Updated: 2026-03-14

This guide explains what each raw data source is, where it came from, and what it should be used for in the datathon workflow.

## Core Network And Mobility Inputs

### Ministry road network (official Hermes)
- Official URL: `https://mapas.fomento.gob.es/VisorHermes/`
- Service layer: `https://mapas.fomento.gob.es/arcgis2/rest/services/Hermes/0_CARRETERAS/MapServer/19`
- Local file: `data/raw/ministry_roads/hermes_roads.geojson`
- What it is: official Spanish road geometry with attributes such as road name, owner, road type, and TEN-T flags.
- Use it for: building the interurban road graph, filtering to autopistas/autovias/national roads, and anchoring all road-based joins.
- Do not use it for: traffic intensity by itself. Pair it with IMD traffic counts.

### DGT IMD traffic counts (official Hermes transport layer)
- Official URL: `https://mapas.fomento.gob.es/VisorHermes/`
- Service layer: `https://mapas.fomento.gob.es/arcgis2/rest/services/Hermes/2_INSTALACIONES_Y_SERVICIOS/MapServer/1010`
- Local file: `data/raw/additional/dgt_imd_traffic/hermes_traffic_count_stations.geojson`
- What it is: official count-station points with IMD total, light, and heavy traffic values.
- Use it for: estimating baseline road demand and calibrating projected EV traffic per segment.
- Do not use it for: direct station placement. It is a demand signal, not a candidate-location layer.

### Existing EV charging points (official NAP)
- Official URL: `https://nap.dgt.es/dataset/puntos-de-recarga-electrica-para-vehiculos`
- Local file: `data/raw/nap_charging_points/nap_ev_charging_points.xml`
- What it is: official national registry of existing EV charging points.
- Use it for: baseline coverage, current infrastructure mapping, and gap analysis versus the proposed network.
- Do not use it for: future capacity assumptions without cleaning and deduplication.

### DGT vehicle registrations (official DGT microdata)
- Official URL: `https://www.dgt.es/menusecundario/dgt-en-cifras/matraba-listados/matriculaciones-automoviles-mensual.html`
- Local folder: `data/raw/dgt_registrations/`
- What it is: monthly vehicle registration files by period.
- Use it for: EV adoption trend validation, province-level demand signals, and cross-checking forecast realism.
- Do not use it for: direct route-level demand without spatial aggregation.

### EV forecast output from datos.gob.es workflow
- Official brief URL: `https://datos.gob.es/es/conocimiento/ruta-la-electrificacion-descifrando-el-crecimiento-del-vehiculo-electrico-en-espana`
- Local folder: `data/raw/datos_gob_ev_forecast/`
- What it is: the mandatory forecast workflow output used to estimate the EV fleet for the 2027 horizon.
- Use it for: the fleet growth assumption that feeds demand modeling and KPI generation.
- Do not use it for: local route allocation by itself. It needs to be combined with traffic and seasonality.

## Grid Capacity Inputs

### i-DE consumption capacity map
- Official URL: `https://www.i-de.es/conexion-red-electrica/suministro-electrico/mapa-capacidad-consumo`
- Local folder: `data/raw/grid_capacity/ide_iberdrola/`
- What it is: distributor-level node or substation capacity information from Iberdrola's DSO.
- Use it for: available-capacity joins and distributor-specific grid feasibility checks.

### e-distribucion historical access capacity
- Official URL: `https://www.edistribucion.com/es/red-electrica/nodos-capacidad-red/capacidad-generacion.html`
- Local folder: `data/raw/grid_capacity/endesa/`
- What it is: Endesa distribution-network capacity publications.
- Use it for: consolidating node-level capacity outside i-DE territory.

### Viesgo distribution grid map exports
- Official URL: `https://www.viesgodistribucion.com/mapa-interactivo-de-la-red`
- Local folder: `data/raw/grid_capacity/viesgo/`
- What it is: distribution-network capacity publications for the Viesgo area.
- Use it for: completing the DSO coverage needed for nationwide grid viability checks.

### REE transmission generation capacity (official REE)
- Official page: `https://www.ree.es/es/clientes/generador/acceso-conexion/conoce-la-capacidad-de-acceso`
- Direct file: `https://www.ree.es/sites/default/files/12_CLIENTES/Documentos/2026_03_02_GRT_generacion.csv`
- Local files:
  - `data/raw/additional/ree_grid/ree_generation_capacity_nodes_2026_03_02_raw.csv`
  - `data/raw/additional/ree_grid/ree_generation_capacity_nodes_2026_03_02_key_fields.csv`
- What it is: official REE node-level transport-grid access-capacity publication.
- Use it for: transmission-level context, identifying pressured nodes, and checking whether proposed corridors intersect already constrained REE nodes.
- Do not use it for: nearest-substation spatial joins. This publication is tabular and not geocoded.

### REE transmission demand requests (official REE)
- Official page: `https://www.ree.es/es/clientes/consumidor/acceso-conexion/conoce-el-estado-de-las-solicitudes`
- Direct file: `https://www.ree.es/sites/default/files/12_CLIENTES/Documentos/publicacion-solicitudes-acceso-demanda-febrero-2026.xlsx`
- Local files:
  - `data/raw/additional/ree_grid/ree_demand_requests_2026_02_raw.xlsx`
  - `data/raw/additional/ree_grid/ree_demand_requests_2026_02.csv`
- What it is: official list of demand-access requests received in transport-grid nodes >= 220 kV.
- Use it for: identifying where large new loads are already competing for transport-grid access and adding context to friction-point narratives.
- Do not use it for: precise station siting. It is a market-pressure indicator, not a geospatial asset map.

## Population And Seasonality Inputs

### INE municipal population
- Official page: `https://www.ine.es/dynt3/inebase/es/index.htm?padre=525`
- Direct file: `https://www.ine.es/pob_xls/pobmun.zip`
- Local files:
  - `data/raw/additional/ine_population/ine_pobmun.zip`
  - `data/raw/additional/ine_population/ine_pobmun_2025.xlsx`
  - `data/raw/additional/ine_population/ine_population_municipal_2025.csv`
- What it is: official municipal population counts from the 2025 padron revision.
- Use it for: municipality demand weighting, urban/rural context, and local population exposure near routes or candidate sites.

### INE hotel occupancy by province
- Official table page: `https://www.ine.es/jaxi/Tabla.htm?tpx=75843`
- Direct file: `https://www.ine.es/jaxi/files/tpx/es/csv_bd/75843.csv`
- Local files:
  - `data/raw/additional/ine_population/ine_hotel_occupancy_provinces_2024_raw.csv`
  - `data/raw/additional/ine_population/ine_hotel_occupancy_provinces_2024_monthly.csv`
- What it is: official provincial hotel occupancy by month.
- Use it for: deriving seasonality multipliers for tourism-heavy provinces and defending the `seasonal_multiplier` field in notebook 06.
- Do not use it for: municipality-level tourism directly. It is provincial, not municipal.

### INE hotel travelers and overnight stays by province
- Official table page: `https://www.ine.es/jaxiT3/Tabla.htm?t=2074&L=0`
- Direct file: `https://www.ine.es/jaxiT3/files/t/es/csv_bd/2074.csv`
- Local files:
  - `data/raw/additional/ine_population/ine_hotel_travelers_overnights_provinces_raw.csv`
  - `data/raw/additional/ine_population/ine_hotel_travelers_overnights_provinces_2025_monthly.csv`
- What it is: official time series of hotel travelers and overnight stays by province.
- Use it for: province-level tourism pressure, validating seasonal travel peaks, and identifying provinces where summer charging demand should be scaled upward.

## Candidate Location And Compliance Inputs

### Official service areas used as candidate locations
- Official URL: `https://mapas.fomento.gob.es/VisorHermes/`
- Service layer: `https://mapas.fomento.gob.es/arcgis2/rest/services/Hermes/2_INSTALACIONES_Y_SERVICIOS/MapServer/1356`
- Local file: `data/raw/additional/osm_rest_areas/hermes_service_areas.geojson`
- What it is: official motorway service-area points from Hermes.
- Use it for: candidate station locations on major corridors.
- Note: the folder name mentions OSM, but the stored file intentionally uses the more trustworthy official source.

### TEN-T corridor network
- Official URL: `https://mapas.fomento.gob.es/VisorHermes/`
- Service layer: `https://mapas.fomento.gob.es/arcgis/rest/services/Hermes/NEW_RED_TRANSEUROPEA_DE_TRANSPORTE__TEN_T_2024/MapServer/5`
- Local file: `data/raw/additional/tent_corridors/hermes_tent_roads_2024.geojson`
- What it is: official TEN-T road corridor segments in Spain.
- Use it for: AFIR checks, corridor prioritization, and communicating compliance with strategic European routes.

### AFIR regulation
- Official URL: `https://eur-lex.europa.eu/eli/reg/2023/1804/oj/eng`
- Local folder target: `data/raw/additional/afir_requirements/`
- What it is: the legal reference behind minimum charging coverage on the TEN-T core network.
- Use it for: policy justification in the report and for explaining the 60 km spacing logic.
- Do not use it for: numeric demand modeling.

### Safe parking areas (official Hermes)
- Official URL: `https://mapas.fomento.gob.es/VisorHermes/`
- Service layer: `https://mapas.fomento.gob.es/arcgis2/rest/services/Hermes/2_INSTALACIONES_Y_SERVICIOS/MapServer/1354`
- Local file: `data/raw/additional/hermes_parking_areas/hermes_safe_parking_areas.geojson`
- What it is: official certified safe and secure parking areas (AESP) on Spanish highways. Includes parking capacity, security level (Gold/Silver/Bronze), and available services.
- Use it for: secondary candidate locations for EV chargers on long-haul routes, especially for overnight charging scenarios. These sites already have infrastructure, security, and highway access.
- Records: 12 certified parking areas.

## Fuel Station Infrastructure

### MITECO gas station locations (official Ministry of Ecological Transition)
- Official API: `https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres/`
- Official data catalogue: `https://datos.gob.es/en/catalogo/e05068001-precio-de-carburantes-en-las-gasolineras-espanolas`
- Local files:
  - `data/raw/additional/miteco_gas_stations/miteco_gas_stations_raw.json` (full API response)
  - `data/raw/additional/miteco_gas_stations/miteco_gas_stations.csv` (cleaned, key fields)
  - `data/raw/additional/miteco_gas_stations/miteco_gas_stations.geojson` (geocoded points)
- What it is: official registry of all 12,216 fuel stations in Spain with precise coordinates, brand, province, municipality, address, and operating hours.
- Use it for: identifying candidate EV charger locations on interurban roads. Gas stations are ideal co-location sites because they already have land, highway access, services, and customer flow. Filter by `road_side` and proximity to interurban roads to find the best candidates.
- Do not use it for: assuming all gas stations are viable EV sites. Cross-reference with grid capacity to check electrical feasibility.
- Records: 12,214 geocoded stations across all 52 provinces.

## Administrative Boundaries

### Spain province boundaries
- Source: derived from IGN (Instituto Geográfico Nacional) via CartoDB open data
- Local file: `data/raw/additional/ign_boundaries/spain_provinces.geojson`
- What it is: polygon boundaries for all 52 Spanish provinces with province codes (`cod_prov`) and autonomous community codes (`cod_ccaa`).
- Use it for: spatial joins between point data (stations, traffic counts, gas stations) and province-level statistics (tourism, population aggregates). Essential for connecting INE province-level data to geographic locations.
- Records: 52 province polygons.

### Spain autonomous community boundaries
- Source: derived from IGN (Instituto Geográfico Nacional) via CartoDB open data
- Local file: `data/raw/additional/ign_boundaries/spain_ccaa.geojson`
- What it is: polygon boundaries for all 19 Spanish autonomous communities/cities with CCAA codes (`cod_ccaa`).
- Use it for: regional-level aggregation, visualization by autonomous community, and policy-relevant geographic grouping.
- Records: 19 CCAA polygons.

## Electricity System Context

### REE national electricity demand (official REE public API)
- Official API: `https://apidatos.ree.es`
- API documentation: `https://www.ree.es/en/apidatos`
- Local files:
  - `data/raw/additional/ree_demand/ree_national_demand_2024.json` (raw API response)
  - `data/raw/additional/ree_demand/ree_national_demand_2024_monthly.csv` (monthly MWh)
- What it is: official monthly electricity demand for peninsular Spain in 2024.
- Use it for: understanding seasonal electricity demand patterns and identifying months where grid is already under pressure. Helps contextualize whether summer tourism peaks align with grid stress.
- Records: 12 monthly values.

### REE installed generation capacity by technology (official REE public API)
- Official API: `https://apidatos.ree.es/en/datos/generacion/potencia-instalada`
- Local files:
  - `data/raw/additional/ree_demand/ree_installed_capacity_2024.json` (raw API response)
  - `data/raw/additional/ree_demand/ree_installed_capacity_2024.csv` (by technology)
- What it is: official breakdown of Spain's 136 GW installed generation capacity by technology (solar PV, wind, combined cycle, hydro, nuclear, etc.).
- Use it for: grid context in the report and presentation. Shows Spain's energy mix and renewable capacity, which supports the narrative that EV charging can be powered by clean energy.
- Records: 17 technology categories.

### REE hourly demand profiles (official REE public API)
- Official API: `https://apidatos.ree.es/en/datos/demanda/demanda-tiempo-real`
- Local files:
  - `data/raw/additional/ree_demand/ree_hourly_demand_profile_summer.json` (July 15, 2024)
  - `data/raw/additional/ree_demand/ree_hourly_demand_profile_winter.json` (January 15, 2024)
  - `data/raw/additional/ree_demand/ree_hourly_demand_profiles.csv` (combined hourly CSV)
- What it is: hourly real, forecasted, and scheduled electricity demand for representative summer and winter days.
- Use it for: understanding daily demand curves and identifying off-peak windows for smart charging strategies. Shows how EV charging at night or midday (solar peak) could complement grid operations.
- Records: 1,728 hourly values (2 days x 3 series x 288 5-min intervals).

## Practical Workflow Recommendation

If you want the leanest high-value pipeline:
- Use `hermes_roads.geojson` + `hermes_traffic_count_stations.geojson` + EV forecast for route demand.
- Use `ine_population_municipal_2025.csv` and `ine_hotel_occupancy_provinces_2024_monthly.csv` to justify local demand scaling and seasonality.
- Use `spain_provinces.geojson` to spatially join point data with province-level statistics.
- Use NAP chargers and Hermes service areas for baseline vs candidate comparison.
- Use `miteco_gas_stations.geojson` as candidate sites — filter to stations near interurban roads for co-location opportunities.
- Use DSO capacity files for nearest-grid feasibility.
- Use REE demand and capacity files for grid-context evidence in the report and friction-point narratives.
- Use `ree_hourly_demand_profiles.csv` to identify optimal charging windows in the report.
