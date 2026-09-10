# Physics-informed pre-DFPT screening v0.6

Cheap descriptors are useful only if they reduce expensive labels **without becoming a substitute for the physics they approximate**.

## Feature 1 — H-active DOS geometric mean

`D_geo(EF) = sqrt[D_total(EF) * D_H(EF)]`

The MgAlFeH6 study reports this combined measure as more informative within its family than either total DOS or H-projected DOS alone. The repository uses it as a low-cost triage feature: a candidate with high total DOS but negligible H character, or strong H character inside a nearly insulating state, should not receive the same priority as one carrying both.

Primary reference: https://doi.org/10.1038/s41524-026-02040-x

**Limit:** family-level correlation is not a universal law. The descriptor does not encode matrix elements, phonon frequencies, anharmonicity, Coulomb effects, or stability.

## Feature 2 — phonon-assisted nesting

A 2026 npj Computational Materials paper introduces a phonon-assisted nesting function `P(omega)` and normalized descriptor `P/(m* M)` as a cheap necessary-condition screen for strong electron-phonon coupling. On the paper's small 22-system validation, the reported threshold achieved 100% recall and about 94% precision for its target classification.

Primary reference: https://doi.org/10.1038/s41524-026-02160-4

**Limit:** small benchmark; necessary-condition language matters. We do not map P directly to Tc.

## Feature 3 — learned alpha2F with uncertainty

BEE-NET shows that learning the Eliashberg spectral function itself is a more physically structured target than learning Tc alone. Its published model is not directly transferable to high-pressure, high-frequency hydrides, which motivates a pressure-conditioned extension rather than blind reuse.

Primary reference: https://doi.org/10.1038/s41524-026-01964-8

## Promotion rule

No material is promoted on descriptor values alone. Cheap features can:

- reject obviously low-information regions;
- seed diverse candidate batches;
- prioritize which structures receive DFPT;
- enter an active-learning acquisition function alongside calibrated uncertainty.

The **DFPT / alpha2F calculation remains the dispositional test** for EPC claims.

## Falsifiable benchmark

At an equal budget of N new DFPT labels, compare:

1. random acquisition;
2. uncertainty-only acquisition;
3. descriptor-only acquisition;
4. descriptor + ensemble uncertainty + diversity.

Evaluate recall of the high-lambda/high-Tc tail, calibration error, structural-family coverage, and false-negative rate. The v0.6 hypothesis is useful only if strategy 4 reaches a fixed recall with materially fewer DFPT labels. A target worth testing is >=5x label efficiency on withheld pressure/composition trajectories. Failure is publishable and should remove the descriptor from the acquisition stack.
