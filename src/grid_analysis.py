"""
Grid capacity classification logic.
"""

from src.constants import GRID_SUFFICIENT_MIN_MW, GRID_MODERATE_MIN_MW, DEFAULT_STATUS_IF_NO_SUBSTATION


def classify_grid_status(available_capacity_mw):
    """
    Classify grid status based on available capacity at nearest substation.

    Returns: 'Sufficient', 'Moderate', or 'Congested'
    """
    if available_capacity_mw is None:
        return DEFAULT_STATUS_IF_NO_SUBSTATION
    if available_capacity_mw >= GRID_SUFFICIENT_MIN_MW:
        return 'Sufficient'
    elif available_capacity_mw >= GRID_MODERATE_MIN_MW:
        return 'Moderate'
    else:
        return 'Congested'


def is_friction_point(grid_status):
    """Return True if this station is a friction point (Moderate or Congested)."""
    return grid_status in ['Moderate', 'Congested']
