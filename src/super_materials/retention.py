"""Retention-surface utilities for metastable states.

These functions intentionally model independent first-order escape channels.
They are screening tools, not a mechanistic claim about any material.
"""
from __future__ import annotations

import math
from collections.abc import Sequence

from .kinetics import K_B_EV


def _attempt_frequencies(count: int, attempt_frequency_hz: float | Sequence[float]) -> list[float]:
    if isinstance(attempt_frequency_hz, (int, float)):
        values = [float(attempt_frequency_hz)] * count
    else:
        values = [float(v) for v in attempt_frequency_hz]
        if len(values) != count:
            raise ValueError("one attempt frequency is required per barrier")
    if any(v <= 0 for v in values):
        raise ValueError("attempt frequencies must be positive")
    return values


def escape_rate(
    temperature_k: float,
    barriers_ev: Sequence[float],
    attempt_frequency_hz: float | Sequence[float] = 1e13,
) -> float:
    """Total escape rate in s^-1 for independent activated channels."""
    barriers = [float(e) for e in barriers_ev]
    if temperature_k <= 0:
        raise ValueError("temperature must be positive")
    if not barriers or any(e < 0 for e in barriers):
        raise ValueError("barriers must be non-empty and nonnegative")
    attempts = _attempt_frequencies(len(barriers), attempt_frequency_hz)
    return sum(
        nu * math.exp(-barrier / (K_B_EV * temperature_k))
        for barrier, nu in zip(barriers, attempts)
    )


def survival_probability(
    temperature_k: float,
    duration_seconds: float,
    barriers_ev: Sequence[float],
    attempt_frequency_hz: float | Sequence[float] = 1e13,
) -> float:
    """Probability of no escape event over duration in the screening model."""
    if duration_seconds < 0:
        raise ValueError("duration must be nonnegative")
    rate = escape_rate(temperature_k, barriers_ev, attempt_frequency_hz)
    return math.exp(-rate * duration_seconds)


def retention_temperature(
    duration_seconds: float,
    barriers_ev: Sequence[float],
    target_survival: float = 0.5,
    attempt_frequency_hz: float | Sequence[float] = 1e13,
    min_temperature_k: float = 1.0,
    max_temperature_k: float = 2000.0,
    tolerance_k: float = 1e-6,
) -> float:
    """Highest temperature giving at least target survival for a fixed duration.

    Uses bisection because survival decreases monotonically with temperature in
    this deliberately simple independent-channel model.
    """
    if duration_seconds <= 0:
        raise ValueError("duration must be positive")
    if not 0 < target_survival < 1:
        raise ValueError("target_survival must lie strictly between 0 and 1")
    if min_temperature_k <= 0 or max_temperature_k <= min_temperature_k:
        raise ValueError("invalid temperature bounds")

    low_s = survival_probability(
        min_temperature_k, duration_seconds, barriers_ev, attempt_frequency_hz
    )
    high_s = survival_probability(
        max_temperature_k, duration_seconds, barriers_ev, attempt_frequency_hz
    )
    if low_s < target_survival:
        raise ValueError("target survival is not reached at the lower bound")
    if high_s >= target_survival:
        raise ValueError("target survival still holds at the upper bound")

    low = min_temperature_k
    high = max_temperature_k
    while high - low > tolerance_k:
        mid = (low + high) / 2
        s = survival_probability(
            mid, duration_seconds, barriers_ev, attempt_frequency_hz
        )
        if s >= target_survival:
            low = mid
        else:
            high = mid
    return low
