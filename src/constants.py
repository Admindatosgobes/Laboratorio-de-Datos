"""
Fixed parameters and constants for the Iberdrola Datathon 2026.

All values are documented and justified in `references/assumptions.md`.
The assumption ID (e.g. A1, B1, C2) is cited against each constant so that
changes to this file can be traced back to a researched, approved entry.

Last synced with assumptions.md: 2026-04-05 (Phase 0 foundation refresh).
"""

# ======================================================================
# MANDATED BY DATATHON RULES — DO NOT CHANGE
# ======================================================================

POWER_PER_CHARGER_KW = 150              # A3 — fixed at 150 kW per charger (brief §5.2 Rule 2)
EV_FLEET_MANDATORY_FILE1 = 2_498_159    # E1 — SARIMA fork output; must appear in File_1.csv


# ======================================================================
# CATEGORY A — VEHICLE & BATTERY
# ======================================================================

AVG_EV_RANGE_KM = 340                   # A1 — WLTP, IEA GEVO 2025 sales-weighted avg
USABLE_RANGE_FACTOR = 0.75              # A2 — highway usability (was 0.80)
EFFECTIVE_RANGE_KM = 255                # A2 — 340 × 0.75, rounded conservative (was 240)
BEV_FRACTION_OF_FLEET = 0.60            # A4 — ~60% BEV / 40% PHEV of EV fleet


# ======================================================================
# CATEGORY B — CHARGING BEHAVIOUR
# ======================================================================

CHARGING_PROBABILITY = 0.12             # B1 — interurban highway (was 0.07)
AVG_CHARGE_DURATION_HOURS = 0.37        # B2 — ~22 min at 150 kW (was 0.40)
EFFECTIVE_OPERATING_HOURS = 20          # B3 — AFIR 24/7 minus maintenance (was 18)

MIN_CHARGERS_TENT = 4                   # B4 — AFIR 600 kW requirement = 4 × 150 kW
MIN_CHARGERS_NON_TENT = 2               # B4 — commercial viability minimum

MAX_CHARGERS_STANDARD = 8               # B5 — standard cap
MAX_CHARGERS_HIGH_TRAFFIC = 12          # B5 — cap for high-traffic sites
HIGH_TRAFFIC_IMD_THRESHOLD = 20_000     # B5 — IMD value triggering 12-charger cap


# ======================================================================
# CATEGORY C — SPACING & COVERAGE (AFIR COMPLIANCE)
# ======================================================================

MAX_SPACING_GENERAL_KM = 120            # C1 — non-TEN-T interurban (was 150)
MAX_SPACING_TENT_CORE_KM = 60           # C2 — AFIR Art 3(1)(a), legally binding
MAX_SPACING_TENT_COMPREHENSIVE_KM = 100 # C3 — AFIR Art 3(2)

# Backwards-compatible aliases (kept so notebooks that import the old
# names do not break while they are being migrated):
MAX_STATION_SPACING_KM = MAX_SPACING_GENERAL_KM
AFIR_SPACING_KM = MAX_SPACING_TENT_CORE_KM

# C4 — existing charger baseline exclusion
EXISTING_CHARGER_MIN_POWER_KW = 50      # ≥50 kW counts as highway-grade coverage
EXISTING_CHARGER_SNAP_RADIUS_KM = 2     # distance from road to count as "on corridor"


# ======================================================================
# CATEGORY D — GRID CAPACITY
# ======================================================================

# Status thresholds (MW available at nearest substation)
GRID_SUFFICIENT_MIN_MW = 5.0            # D1 — ≥5 MW → Sufficient
GRID_MODERATE_MIN_MW = 1.0              # D2 — 1–5 MW → Moderate
# D3 — <1 MW → Congested

GRID_STATUS_LABELS = {
    'sufficient': 'Sufficient',
    'moderate': 'Moderate',
    'congested': 'Congested',
}

# D4 — tiered substation spatial matching (haversine km)
SUBSTATION_RADIUS_PREFERRED_KM = 5      # direct MV connection, optimal CAPEX
SUBSTATION_RADIUS_FEASIBLE_KM = 15      # MV line extension, ~€100–300K extra
SUBSTATION_RADIUS_HIGH_COST_KM = 25     # high-cost extension, flag for study
MAX_SUBSTATION_SEARCH_RADIUS_KM = SUBSTATION_RADIUS_HIGH_COST_KM  # >25 km → Congested

# D5
DEFAULT_STATUS_IF_NO_SUBSTATION = 'Congested'


# ======================================================================
# CATEGORY E — DEMAND SCALING
# ======================================================================

EV_FLEET_BASE_CASE_2027 = 2_000_000     # E1 — conservative base for demand model
TOTAL_SPANISH_LIGHT_FLEET_2027 = 35_000_000  # E3 — DGT + ~1% growth
EV_PENETRATION_RATE_2027 = EV_FLEET_BASE_CASE_2027 / TOTAL_SPANISH_LIGHT_FLEET_2027  # ≈5.7%

INTERURBAN_TRIP_FRACTION = 0.35         # E6 — MOVILIA, report context only

# Seasonal multipliers applied to IMD traffic counts
SEASONAL_MULTIPLIERS = {
    'default': 1.0,
    # E4 — Mediterranean corridors (AP-7, A-7)
    'mediterranean_shoulder': 2.0,      # Jun, Sep
    'mediterranean_peak': 2.5,          # Jul–Aug
    # E5 — Atlantic / Cantabrian corridors (A-8, AP-9)
    'atlantic_summer': 1.5,             # Jul–Aug
}


# ======================================================================
# CATEGORY F — ECONOMIC (REPORT USE)
# ======================================================================

CAPEX_PER_CHARGER_EUR_LOW = 80_000      # F1 — installed, all-in, low estimate
CAPEX_PER_CHARGER_EUR_HIGH = 130_000    # F1 — installed, all-in, high estimate
CAPEX_PER_CHARGER_EUR_MID = 105_000     # midpoint for single-number report figures


# ======================================================================
# OUTPUT SCHEMAS — exact column order required by brief §5.2
# ======================================================================

OUTPUT_FILE_1 = 'File_1.csv'
OUTPUT_FILE_2 = 'File_2.csv'
OUTPUT_FILE_3 = 'File_3.csv'

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

VALID_GRID_STATUSES_FILE2 = ['Sufficient', 'Moderate', 'Congested']
VALID_GRID_STATUSES_FILE3 = ['Moderate', 'Congested']  # Sufficient NOT allowed in File 3
VALID_DISTRIBUTORS = ['i-DE', 'Endesa', 'Viesgo']
