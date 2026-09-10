# Replication standard v0.6

## Same-state rule

Superconductivity evidence is only combinable when measurements can be tied to the same material state. Each measurement packet should carry a `state_id` defined by sample/batch, precursor route, isotope, pressure, temperature, annealing history, decompression rate, elapsed time, contact geometry and structural fingerprint.

A transport trace measured before a phase transition and an XRD pattern measured after it are not automatically evidence for the same phase.

## Evidence ladder

**Level 0 — anomaly.** Resistance drop, susceptibility feature, diffraction change, or spectroscopic anomaly without a coherent cross-check.

**Level 1 — transport-consistent.** Reproducible four-probe transition with field suppression and current-density checks; contact and geometry artifacts addressed.

**Level 2 — phase-linked.** Structural/spectroscopic fingerprint measured on the same state as transport. Phase fraction and competing phases reported.

**Level 3 — bulk-consistent.** Magnetic shielding/Meissner evidence and/or thermodynamic anomaly consistent with the transition, with calibration and background disclosed.

**Level 4 — mechanism-resolved.** Isotope, gap spectroscopy, alpha2F comparison, critical-field systematics or other measurements connect the phase to a microscopic pairing account.

**Level 5 — independently replicated.** An independent group reproduces phase preparation, transition and decisive controls from an open protocol, ideally on a different apparatus.

**Room-temperature-superconductivity language is reserved for Level 5.**

## Minimal raw-data packet

- instrument-native transport channels, not screenshot traces;
- current, voltage, field, temperature and pressure time series with timestamps;
- pressure calibration before/after thermal cycles;
- raw and processed XRD/Raman plus calibration standard;
- sample images / contact map where feasible;
- ZFC/FC raw magnetometry and background subtraction recipe;
- isotope provenance and measured phase identity for H/D comparison;
- complete synthesis/decompression thermal history;
- scripts and parameters used to produce every public plot.

## Failure taxonomy

A negative or ambiguous run should be tagged, not discarded:

- target phase not formed;
- target phase formed but decomposed before measurement;
- structural identity ambiguous;
- no transport transition;
- transition not field-sensitive;
- transport transition not phase-linked;
- filamentary/surface fraction only;
- magnetic signal inconsistent with bulk shielding;
- thermodynamic anomaly absent at sufficient sensitivity;
- isotope comparison phase-mismatched;
- pressure/temperature history uncontrolled;
- apparatus/contact artifact suspected.

## Replication packet

A replication-ready release contains exact precursor lots/stoichiometry, DAC/gasket/contact geometry, loading atmosphere, pressure-temperature-time recipe, decompression rate, state identifiers, expected structural peaks/modes, success/failure thresholds, raw data schema, and a short list of artifact mechanisms to test deliberately.
