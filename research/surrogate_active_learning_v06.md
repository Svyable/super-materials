# Pressure-conditioned alpha2F active learning v0.6

## Opportunity

The expensive quantity we actually need for conventional superconductors is not merely Tc; it is the electron-phonon spectral information that supports Tc and reveals which modes matter. BEE-NET (npj Computational Materials, 2026) demonstrates a learned `alpha^2F(omega)` route and reports strong accuracy against its DFT/Allen-Dynes label distribution, but the authors explicitly flag ambient-pressure / frequency-range limitations for high-Tc hydrides.

Reference: https://doi.org/10.1038/s41524-026-01964-8

## Proposed extension

Learn `alpha^2F(omega, P)` for hydrogen-rich materials with:

- structures relaxed at multiple pressures;
- frequency support at least to ~500 meV;
- composition/structure embeddings plus pressure, volume and cheap physics descriptors;
- ensemble predictions for epistemic uncertainty;
- explicit out-of-distribution scores by chemistry/topology/pressure;
- direct DFPT labels for every promoted point;
- pressure trajectories kept together during train/test splitting to prevent leakage.

## Acquisition function

A candidate-pressure state receives priority when it combines:

- model uncertainty;
- structural-family novelty/diversity;
- physically plausible H-active DOS;
- phonon-assisted nesting signal where available;
- proximity to a stability/criticality boundary without crossing into imaginary-mode instability;
- portfolio value (moderate operating pressure, recoverability experiment, or mechanism-discriminating control).

No single descriptor may dominate acquisition.

## Data object

Store the full spectral target and metadata:

`material_id, structure_id, P, V, alpha2F grid, phonon DOS, lambda, omega_log, N(EF), H-projected DOS, q/k meshes, pseudopotential, XC functional, smearing, stability flags, anharmonic/QNE correction state, uncertainty`.

This makes later method upgrades possible without relabeling everything as scalar Tc.

## Benchmark

1. Seed with diverse parents plus pressure trajectories.
2. Hold out entire chemical/topological families.
3. Compare random, uncertainty-only, descriptor-only and combined acquisition.
4. At each round, compute exact DFPT for selected points and retrain.
5. Score spectral distance, lambda/omega_log error, Tc(P) topology, calibration, and high-value-tail recall.

**Promotion target:** >=5x reduction in new DFPT labels needed to reconstruct a withheld Tc(P) dome to the chosen fidelity, while retaining calibrated uncertainty and low false-negative rate.

If the target is not met, the surrogate remains a visualization/interpolation tool and does not control compute allocation.
