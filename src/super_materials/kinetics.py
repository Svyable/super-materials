"""Order-of-magnitude metastable retention estimates."""
from __future__ import annotations
import math
K_B_EV = 8.617333262145e-5


def barrier_for_lifetime(temperature_k: float, lifetime_seconds: float, attempt_frequency_hz: float=1e13) -> float:
    """Single-activated-process barrier Ea = kBT ln(nu0*tau), in eV."""
    if temperature_k <= 0 or lifetime_seconds <= 0 or attempt_frequency_hz <= 0:
        raise ValueError("temperature, lifetime and attempt frequency must be positive")
    return K_B_EV * temperature_k * math.log(attempt_frequency_hz * lifetime_seconds)


def lifetime_for_barrier(temperature_k: float, barrier_ev: float, attempt_frequency_hz: float=1e13) -> float:
    if temperature_k <= 0 or barrier_ev < 0 or attempt_frequency_hz <= 0:
        raise ValueError("invalid kinetic parameters")
    return math.exp(barrier_ev/(K_B_EV*temperature_k))/attempt_frequency_hz
