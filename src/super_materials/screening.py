"""Cheap screening descriptors.

These functions are acquisition features only; they are not superconducting-Tc predictors.
"""
from __future__ import annotations
import math


def projected_dos_geomean(total_dos_ef: float, hydrogen_dos_ef: float) -> float:
    """Return sqrt[D_total(EF) * D_H(EF)] for non-negative DOS values."""
    if total_dos_ef < 0 or hydrogen_dos_ef < 0:
        raise ValueError("DOS values must be non-negative")
    return math.sqrt(total_dos_ef * hydrogen_dos_ef)
