# Decision intelligence v0.6

## Goal

Maximize **falsifiable information gained per scarce DFPT, SSCHA/PIMD, DAC, beamline, magnetometry, calorimetry, or tunneling slot**. Candidate count is not the objective.

## Portfolio prior

The 2025 Nature Communications ambient-pressure search (>20,000 full EPC calculations and >100 million ML-screened compounds) found a persistent coupling/frequency/stability tradeoff. We therefore assign low portfolio priority to equilibrium ambient-pressure conventional 300 K claims unless a candidate supplies concrete physics that breaks the observed tradeoff and survives high-fidelity stability analysis.

This is a resource-allocation prior, not a theorem.

Primary reference: https://doi.org/10.1038/s41467-025-63702-w

## Explicit Bayesian planning model

For a binary hypothesis H and test outcome T:

- prior `p = P(H)`;
- sensitivity `s = P(+|H)`;
- specificity `c = P(-|not H)`.

Positive-outcome probability:

`P(+) = p*s + (1-p)*(1-c)`.

Posteriors:

`P(H|+) = p*s / P(+)`

`P(H|-) = p*(1-s) / [p*(1-s) + (1-p)*c]`.

Expected information gain is prior binary entropy minus expected posterior entropy. All priors and likelihoods in this repo are assumptions for campaign design unless explicitly calibrated from data.

## Why same-state phase + transport ranks highly

A low-resistance transition is sensitive but can have weak specificity because contact rearrangement, percolation, metallic decomposition products, pressure gradients, or filamentary paths can mimic parts of the signature. Synchronizing structural fingerprinting and transport on the same retained state raises the assumed specificity and therefore the expected information gain.

The useful experimental unit is therefore a `state_id`: pressure, temperature, thermal history, decompression rate, precursor batch, isotope, and elapsed time are logged so XRD/Raman/transport/magnetic observations refer to the same material state.

## Campaign sequence

### Q-MRH6
1. establish Mg2RhH6 and H5/H6 fingerprints at formation pressure;
2. paired cold-fast vs staged decompression on matched samples;
3. same-state Raman/XRD + four-probe transport at every pressure stop;
4. field dependence before promoting any resistance anomaly;
5. H/D matched synthesis and decompression;
6. local magnetometry / Meissner imaging if phase-linked transport survives;
7. tunneling gap spectroscopy only after lower-cost gates justify it.

### MAFH-gradient
1. ordered + SQS structures across x and H-vacancy chemical potentials;
2. charge state, magnetism and hull/phonon gate;
3. calculate Hall-sign/carrier-density predictions;
4. only then synthesize the narrow composition range whose intended carriers are not self-compensated.

### Li3Rh1-yCoyH9
1. reproduce endpoint calculations;
2. CSP/SQS across y and pressure;
3. QNE-aware stability gate;
4. DFPT only on contiguous stable basins;
5. promote only if high-fidelity Tc and <=15 GPa operating stability coexist.

## Updating rules

- A negative result is retained and updates priors; it is not erased from the ledger.
- Tests conditional on earlier success use their own post-gate prior and are never compared naively to unconditional first-wave tests.
- Evidence specificity outranks aesthetic strength of a plot.
- An experiment that cannot identify the phase producing its signal is a screening result, not confirmation.
- Replication value increases when the second lab changes apparatus while preserving the state/protocol definition.
