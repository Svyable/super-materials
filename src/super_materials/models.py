"""Minimal transparent superconductivity screening equations."""
from __future__ import annotations
import math


def allen_dynes_tc(lambda_ep: float, omega_log_k: float, mu_star: float=0.10) -> float:
    """McMillan/Allen-Dynes-style screening Tc in kelvin.

    This simplified expression omits strong-coupling correction factors f1/f2 and should
    not be treated as a substitute for converged Eliashberg/SCDFT calculations.
    """
    if lambda_ep <= 0 or omega_log_k <= 0 or mu_star < 0:
        raise ValueError("invalid parameters")
    den = lambda_ep - mu_star*(1+0.62*lambda_ep)
    if den <= 0:
        return 0.0
    return (omega_log_k/1.2)*math.exp(-1.04*(1+lambda_ep)/den)
