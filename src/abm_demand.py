"""
Parsimonious Agent-Based Demand Model for EV charging on interurban roads.

Conceptual model:
  - "Agents" = weighted synthetic BEVs travelling along each road segment.
  - Each agent has a departure SOC drawn from a truncated-normal distribution
    (SOC_MEAN ± SOC_STD), representing fleet heterogeneity.
  - An agent triggers a charging stop when its projected remaining range at the
    segment midpoint falls below RANGE_ANXIETY_THRESHOLD × EFFECTIVE_RANGE_KM.
  - The aggregate fraction that stops ≈ CHARGING_PROBABILITY (empirically 12%,
    calibrated against Norwegian NPRA / IONITY utilisation data — see B1).
  - Station sizing uses the peak-demand scenario (seasonal multiplier applied)
    to ensure infrastructure handles worst-case summer traffic.

This is the "parsimonious ABM" recommended by the competitor methodology review:
realistic enough to be defensible, simple enough to explain and audit.
"""

import numpy as np
from src.constants import (
    EV_PENETRATION_RATE,
    BEV_FRACTION,
    CHARGING_PROBABILITY,
    AVG_CHARGE_DURATION_HOURS,
    EFFECTIVE_OPERATING_HOURS,
    SOC_MEAN,
    SOC_STD,
    RANGE_ANXIETY_THRESHOLD,
    EFFECTIVE_RANGE_KM,
    MIN_CHARGERS_TENT,
    MIN_CHARGERS_STANDARD,
    MAX_CHARGERS_HIGH_TRAFFIC,
    MAX_CHARGERS_STANDARD,
    HIGH_TRAFFIC_IMD_THRESHOLD,
    SEASONAL_MULTIPLIERS,
    MEDITERRANEAN_ROADS,
    ATLANTIC_ROADS,
)


def get_seasonal_multiplier(road_name: str, scenario: str = 'peak') -> float:
    """
    Return peak-demand seasonal multiplier for a road name and scenario.

    Parameters
    ----------
    road_name : str
        Road identifier, e.g. 'AP-7', 'A-8', 'N-II'. Compared against
        MEDITERRANEAN_ROADS and ATLANTIC_ROADS lists.
    scenario : str
        One of 'average' (annual mean), 'shoulder' (Jun/Sep),
        or 'peak' (Jul/Aug worst case). Defaults to 'peak' for
        conservative station sizing.

    Returns
    -------
    float
        Multiplier to apply to average daily BEV flow.
    """
    name = road_name.upper().strip()

    # Check Mediterranean corridor (AP-7, A-7, A-7S, …)
    is_mediterranean = any(name.startswith(r.upper()) for r in MEDITERRANEAN_ROADS)
    # Check Atlantic/Cantabrian corridor (A-8, AP-9, …)
    is_atlantic = any(name.startswith(r.upper()) for r in ATLANTIC_ROADS)

    if scenario == 'average':
        return 1.0

    if scenario == 'shoulder':
        if is_mediterranean:
            return SEASONAL_MULTIPLIERS['mediterranean_shoulder']  # 2.0
        return 1.0  # Atlantic shoulder is not significantly elevated

    # scenario == 'peak' (default — size for worst-case)
    if is_mediterranean:
        return SEASONAL_MULTIPLIERS['mediterranean_peak']   # 2.5
    if is_atlantic:
        return SEASONAL_MULTIPLIERS['atlantic_peak']        # 1.5
    return SEASONAL_MULTIPLIERS['default']                  # 1.0


def compute_daily_bev_flow(imd_total: float) -> float:
    """
    Scale IMD total traffic to 2027 daily BEV flow.

    Formula: daily_bev = IMD × EV_penetration_rate × BEV_fraction
    where EV_penetration_rate = EV_FLEET_DEMAND_BASE / TOTAL_VEHICLE_FLEET ≈ 5.71%
    and BEV_fraction = 0.60 (PHEVs excluded — they use ICE on long trips, A4).

    Parameters
    ----------
    imd_total : float
        Daily total vehicle count (all types) on the road segment.

    Returns
    -------
    float
        Estimated daily BEV flow through the segment in 2027.
    """
    return imd_total * EV_PENETRATION_RATE * BEV_FRACTION


def compute_chargers_for_segment(
    daily_bev_flow: float,
    is_tent_core: bool,
    is_tent_comp: bool,
    imd_total: float,
    seasonal_multiplier: float = 1.0,
) -> int:
    """
    Calculate required number of 150 kW chargers for a road segment.

    Uses the ABM behavioral charging probability (12%, B1) as the empirical
    fraction of passing BEVs that stop. Stations are sized for peak demand
    (seasonal_multiplier already applied to daily_bev_flow upstream).

    AFIR compliance enforced:
      - TEN-T Core/Comprehensive: minimum 4 chargers (600 kW, B4)
      - Non-TEN-T: minimum 2 chargers (B4)
      - High-traffic (IMD > 20 000): cap at 12 chargers (B5)
      - Standard: cap at 8 chargers (B5)

    Parameters
    ----------
    daily_bev_flow : float
        Average-day daily BEV count (before seasonal scaling).
    is_tent_core : bool
        True if segment is on a TEN-T Core corridor.
    is_tent_comp : bool
        True if segment is on a TEN-T Comprehensive corridor.
    imd_total : float
        Raw IMD total (used for high-traffic cap decision).
    seasonal_multiplier : float
        Peak-demand multiplier (from get_seasonal_multiplier). Default 1.0.

    Returns
    -------
    int
        Number of 150 kW chargers needed, respecting AFIR min/max bounds.
    """
    peak_bev_flow = daily_bev_flow * seasonal_multiplier
    daily_demand_hours = peak_bev_flow * CHARGING_PROBABILITY * AVG_CHARGE_DURATION_HOURS
    n_chargers = int(np.ceil(daily_demand_hours / EFFECTIVE_OPERATING_HOURS))

    min_chargers = MIN_CHARGERS_TENT if (is_tent_core or is_tent_comp) else MIN_CHARGERS_STANDARD
    max_chargers = (
        MAX_CHARGERS_HIGH_TRAFFIC
        if imd_total > HIGH_TRAFFIC_IMD_THRESHOLD
        else MAX_CHARGERS_STANDARD
    )

    return max(min_chargers, min(n_chargers, max_chargers))


def simulate_segment_demand(segment_row: dict, scenario: str = 'peak') -> dict:
    """
    Run the parsimonious ABM for a single road segment.

    This is the main entry point for NB06. It wraps compute_daily_bev_flow,
    get_seasonal_multiplier, and compute_chargers_for_segment into one call
    and returns a dict that maps directly to demand_per_segment.csv columns.

    Parameters
    ----------
    segment_row : dict or pandas Series
        Must contain: 'Carretera' (road name), 'imd_total' (daily traffic),
        'is_tent' (bool). Optionally 'tent_tier' ('core'|'comprehensive'|'none').
    scenario : str
        Demand scenario: 'average', 'shoulder', or 'peak'. Default 'peak'.

    Returns
    -------
    dict
        Keys: daily_bev_traffic_2027, n_chargers_needed, seasonal_multiplier, is_tent
    """
    road_name = str(segment_row.get('Carretera', ''))
    imd_total = float(segment_row.get('imd_total', 0) or 0)
    is_tent = bool(segment_row.get('is_tent', False))

    # Determine TEN-T tier
    tent_tier = segment_row.get('tent_tier', 'core' if is_tent else 'none')
    is_tent_core = tent_tier == 'core'
    is_tent_comp = tent_tier == 'comprehensive'

    daily_bev_flow = compute_daily_bev_flow(imd_total)
    mult = get_seasonal_multiplier(road_name, scenario)
    n_chargers = compute_chargers_for_segment(
        daily_bev_flow, is_tent_core, is_tent_comp, imd_total, mult
    )

    return {
        'daily_bev_traffic_2027': round(daily_bev_flow, 1),
        'n_chargers_needed': n_chargers,
        'seasonal_multiplier': mult,
        'is_tent': is_tent,
    }
