"""Transparent Bayesian planning helpers.

Inputs are explicit planning assumptions, not empirical discovery probabilities.
"""
from __future__ import annotations
import math


def binary_entropy_bits(p: float) -> float:
    if not 0.0 <= p <= 1.0:
        raise ValueError("p must be in [0,1]")
    if p in (0.0, 1.0):
        return 0.0
    return -(p * math.log2(p) + (1-p) * math.log2(1-p))


def posterior_probability(prior: float, sensitivity: float, specificity: float, positive: bool) -> float:
    for name, value in {"prior": prior, "sensitivity": sensitivity, "specificity": specificity}.items():
        if not 0 <= value <= 1:
            raise ValueError(f"{name} must be in [0,1]")
    if positive:
        den = prior*sensitivity + (1-prior)*(1-specificity)
        return prior*sensitivity/den if den else prior
    den = prior*(1-sensitivity) + (1-prior)*specificity
    return prior*(1-sensitivity)/den if den else prior


def expected_information_gain_bits(prior: float, sensitivity: float, specificity: float) -> float:
    p_pos = prior*sensitivity + (1-prior)*(1-specificity)
    p_neg = 1-p_pos
    post_pos = posterior_probability(prior, sensitivity, specificity, True)
    post_neg = posterior_probability(prior, sensitivity, specificity, False)
    return binary_entropy_bits(prior) - (p_pos*binary_entropy_bits(post_pos) + p_neg*binary_entropy_bits(post_neg))


def summarize_test(prior: float, sensitivity: float, specificity: float) -> dict[str,float]:
    return {
        "prior": prior,
        "posterior_positive": posterior_probability(prior,sensitivity,specificity,True),
        "posterior_negative": posterior_probability(prior,sensitivity,specificity,False),
        "expected_information_bits": expected_information_gain_bits(prior,sensitivity,specificity),
    }
