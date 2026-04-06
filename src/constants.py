"""
Fixed parameters and constants for the Iberdrola Datathon 2026.
All values are documented and justified in references/assumptions.md
"""

# === MANDATED BY DATATHON RULES (DO NOT CHANGE) ===
POWER_PER_CHARGER_KW = 150          # Fixed at 150 kW per charger for all teams (A3)
EV_FLEET_2027 = 2_498_159           # MANDATORY: SARIMA output for File_1 (E1)

# === EV FLEET SCALING ===
EV_FLEET_DEMAND_BASE = 2_000_000    # Conservative base for demand sizing (E1 note)
BEV_FRACTION = 0.60                 # 60% of EV fleet are BEVs; PHEVs don't need highway fast charging (A4)
TOTAL_VEHICLE_FLEET = 35_000_000    # Spain light vehicle fleet 2027 estimate (E3)
EV_PENETRATION_RATE = EV_FLEET_DEMAND_BASE / TOTAL_VEHICLE_FLEET  # ~0.0571 (E3)

# === EV AUTONOMY ===
AVG_EV_RANGE_KM = 340               # WLTP average range, IEA GEVO 2025 (A1)
USABLE_RANGE_FACTOR = 0.75          # Highway usability: 75% of WLTP (A2)
EFFECTIVE_RANGE_KM = int(AVG_EV_RANGE_KM * USABLE_RANGE_FACTOR)  # 255 km (A2)

# === STATION SPACING CONSTRAINTS (AFIR three-tier structure) ===
MAX_STATION_SPACING_TENT_CORE_KM = 60   # AFIR Art. 3(1)(a) — legally binding (C2)
MAX_STATION_SPACING_TENT_COMP_KM = 100  # AFIR Art. 3(2) — comprehensive network (C3)
MAX_STATION_SPACING_KM = 120            # General interurban, non-TEN-T (C1)
AFIR_SPACING_KM = MAX_STATION_SPACING_TENT_CORE_KM  # backward-compat alias

# === GRID STATUS THRESHOLDS (MW available at nearest substation) ===
GRID_SUFFICIENT_MIN_MW = 5.0    # >= 5 MW → Sufficient (D1)
GRID_MODERATE_MIN_MW = 1.0      # >= 1 MW and < 5 MW → Moderate (D2)
# < 1 MW → Congested (D3)

GRID_STATUS_LABELS = {
    'sufficient': 'Sufficient',
    'moderate': 'Moderate',
    'congested': 'Congested',
}

# === SUBSTATION MATCHING (tiered by connection distance, D4) ===
SUBSTATION_DIST_OPTIMAL_KM = 5      # Direct LV/MV connection, economically optimal
SUBSTATION_DIST_FEASIBLE_KM = 15    # MV line extension, cost-feasible (~€100–300K CAPEX)
SUBSTATION_DIST_HIGH_COST_KM = 25   # High-cost extension; requires feasibility study
MAX_SUBSTATION_SEARCH_RADIUS_KM = SUBSTATION_DIST_HIGH_COST_KM  # 25 km max
DEFAULT_STATUS_IF_NO_SUBSTATION = 'Congested'  # If no substation within radius (D5)

# === DEMAND MODELING — ABM behavioral parameters ===
CHARGING_PROBABILITY = 0.12         # 12% of BEVs charge at a given station (B1, Norwegian/IONITY data)
AVG_CHARGE_DURATION_HOURS = 0.37    # 22-minute average DC fast charge session (B2)
EFFECTIVE_OPERATING_HOURS = 20      # Hours/day station effectively available (B3, AFIR Art. 5)

# ABM agent SOC distribution parameters
SOC_MEAN = 0.65                     # Mean departure state of charge (behavioral model)
SOC_STD = 0.15                      # SOC heterogeneity across driver population
RANGE_ANXIETY_THRESHOLD = 0.20      # Drivers charge when <20% remaining range

# === CHARGER COUNT CONSTRAINTS (AFIR compliance, B4/B5) ===
MIN_CHARGERS_TENT = 4               # AFIR Annex II: 4 × 150 kW = 600 kW min on TEN-T by 2027 (B4)
MIN_CHARGERS_STANDARD = 2           # Non-TEN-T minimum for commercial viability (B4)
MAX_CHARGERS_HIGH_TRAFFIC = 12      # High-traffic corridors IMD > 20,000 (B5)
MAX_CHARGERS_STANDARD = 8           # Standard cap (B5)
HIGH_TRAFFIC_IMD_THRESHOLD = 20_000 # IMD threshold separating standard vs high-traffic

# === EXISTING CHARGER EXCLUSION RULE (C4) ===
MIN_EXISTING_CHARGER_POWER_KW = 50  # Only ≥50 kW counts as valid interurban coverage
EXISTING_CHARGER_ROAD_BUFFER_KM = 2 # Distance from road to count as coverage

# === SEASONAL MULTIPLIERS (for peak summer on coastal corridors) ===
SEASONAL_MULTIPLIERS = {
    'default': 1.0,
    'mediterranean_summer': 2.0,  # AP-7, A-7 Jul-Aug
    'atlantic_summer': 1.5,       # A-8, AP-9 Jul-Aug
}

# === ROAD CLASSIFICATIONS FOR SEASONAL ADJUSTMENT ===
MEDITERRANEAN_ROADS = ['AP-7', 'A-7', 'AP-4', 'A-3', 'A-31']  # Coastal Mediterranean corridors
ATLANTIC_ROADS = ['A-8', 'AP-9', 'A-6', 'AP-66']               # Atlantic/northern corridors

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
