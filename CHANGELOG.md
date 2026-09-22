# Changelog

## 0.7.0 — 2026-09-21 retained-state engineering

- Promoted retained-state lifetime from a side calculation to a first-class research objective distinct from Tc and ambient operating pressure.
- Added a retention-surface framework S(T,t,P,history) and a technology-facing distinction between superconducting transition temperature and room-temperature survivability.
- Added multi-channel activated escape modeling for competing kinetic failure paths, with survival-probability and retention-temperature utilities.
- Added a machine-readable state-recipe JSON Schema covering precursor, complete preparation path, retained-state identity, same-state measurements, evidence class, and replication status.
- Added explicit room-temperature handling/logistics/storage barrier targets without treating them as predicted material barriers.
- Reframed Q-MRH6 as a failure-boundary mapping experiment whose goal is to learn where structure and superconductivity are lost under decompression.
- Added a recovery-first "retention scaffold + pairing engine" discovery principle and an Open Superconducting State Atlas data contract.

## 0.6.0 — 2026-09-09 decision intelligence + replication architecture

- Added a physics-informed pre-DFPT triage layer: projected-DOS geometric mean plus phonon-assisted nesting P(omega), both explicitly non-predictive screening features.

- Added a transparent Bayesian experiment-selection module with expected information gain, explicit priors, sensitivity/specificity, conditional posteriors, and separate relative-cost reporting.
- Added six assumed experiment models spanning Q-MRH6 phase+transport, resistivity-only screening, isotope/field controls, MAFH defect calculations, Rh/Co-H9 stability triage, and conditional tunneling spectroscopy.
- Added a machine-readable claim/evidence graph so support, constraints, parent anchors, and speculation are not flattened into citations.
- Added a six-level replication standard from anomaly through independent reproduction, plus same-state measurement IDs, raw-data requirements, and a reusable failure taxonomy.
- Added the >20k-EPC / >100M-compound ambient conventional-superconductor ceiling study as a portfolio prior: equilibrium ambient conventional 300 K is treated as extremely unlikely, not mathematically impossible.
- Added a SOTA compute proposal for pressure-conditioned high-frequency alpha2F(P) surrogates with ensemble uncertainty, OOD detection, active learning, and mandatory DFPT confirmation.
- Added Li2AgH6/Li2AuH6 method-spread and hull-distance calibration data to expose the stability/model-uncertainty tradeoff.
- Added interactive Decision Lab, claim graph, replication ladder, and new figures to the GitHub Pages experience.
- Expanded literature ledger to 42 rows and automated tests from 13 to 16.

## 0.4.0 — 2026-09-09 quenchability + state engineering

- Corrected the ambient-pressure superconducting record to the peer-reviewed 151 K pressure-quenched Hg1223 result and separated ambient pressure from room-temperature retention.
- Added a quenchability research program with `Q-MRH6`, a cryogenic decompression hypothesis for experimentally established Mg2RhH6. No ambient Tc is assigned.
- Added a transparent single-barrier Arrhenius retention model and generated lifetime/temperature barrier tables and plots; three days at 77 K requires ~0.28 eV and one year at 300 K ~1.22 eV for nu0=10^13 s^-1.
- Added formation-pressure vs operating-pressure visualization and a generalized mixed-direction Pareto utility so multi-objective tradeoffs remain explicit.
- Added the amorphous-Pd -> PdH3 experiment as evidence that precursor disorder can select metastable hydride reaction pathways.
- Added ambient-recovered fcc lanthanide trihydrides as a room-temperature anharmonic-retention control that is explicitly non-superconducting.
- Demoted Li2MgRuH9 from a primary-style benchmark to `AB_INITIO_SECONDARY_INDEX_PENDING_PRIMARY_METADATA` pending independently resolved publisher metadata.
- Replaced the old Ru/Rh interpolation seed with the better-supported Li3Rh1-yCoyH9 search lane and added MAFH-gradient and Y3Fe3RuH20 hypotheses.
- Added source-audit/evidence taxonomy and expanded automated tests for kinetics and multi-objective dominance.

## 0.3.0 — 2026-09-09 frontier mechanisms + portfolio expansion

- Added a late-Q3-2026 frontier update incorporating Li2MgRuH9, CaH6-delta vacancy physics, Y3Fe4H20 recovery, Li3CuH4 anharmonicity, and RbPH3 quantum stabilization.
- Added ten falsifiable design rules: pairing division-of-labor, complementary sublattices, dynamic H stoichiometry, independent recoverability, QNE triage, carrier engineering, energy-dependent EPC, evidence-aware multi-objective selection, suppression of molecular H2 units, and non-equivalence of chemical vs hydrostatic pressure.
- Added `MAFH-25 = Mg1.5Al0.5FeH6` as an ambient-pressure carrier-engineering screening lane derived from Mg2FeH6/MgAlFeH6, with no assigned Tc.
- Added `LMRRH-25 = Li2MgRu0.75Rh0.25H9` as a 8–20 GPa composition-search seed connecting low-pressure Li2MgRuH9 framework coupling with Rh-H electronic motifs; no endpoint interpolation is treated as a Tc prediction.
- Added hydrogen vacancy/decompression/recovery accounting and explicit H/D phase-matching requirements.
- Added a transparent pressure–Tc Pareto utility and Q3 frontier dataset while keeping stability and evidence quality as separate axes.
- Added a virtual-parent MAFH-25 CIF and simulated screening XRD fingerprint.
- Added CaAuH6 as a predicted ambient-pressure metal-embedded-H-unit benchmark and added H2-unit suppression as a structural search descriptor.
- Added NEO-DFT and deep-free-energy QNE-aware structure search as benchmarkable 2026 acceleration methods.
- Added an explicit controversy ledger: reported 298 K LaSc2H24 is classified as `REPORTED_PREPRINT_CONTESTED` because independent reproduction attempts have been publicly reported unsuccessful.
- Added a cross-class nickelate control showing hydrostatic pressure and substitution/strain-induced lattice compression cannot be treated as the same scalar tuning axis.
- Expanded automated tests from 5 to 7.

## 0.2.0 — 2026-09-09 SOTA research expansion

- Added a September 2026 evidence-class SOTA review and curated literature matrix.
- Added a fidelity ladder from local structure search through DFT/DFPT, QNE/SSCHA, full-bandwidth anisotropic Migdal–Eliashberg, disorder/defects, and reaction-path kinetics.
- Reframed MIRH-25 to test both Mg2RhH5-like and Mg2IrH7-like precursor pathways rather than assuming endpoint interpolation.
- Reframed LMBH-25 as the defect-coupled Li(2−x)Mg(x)BH(6−δ) family because aliovalent Mg substitution may be hydrogen-vacancy compensated.
- Added explicit opportunity-cost benchmarks (Li3RhH9, Li3IrH9, MgAlFeH6, ABIrH6 derivatives) and SOTA advancement/stop criteria.
- Added a 300 K Allen–Dynes requirement solver and generated threshold curve.
- Added an evidence-class pressure–Tc landscape figure.
- Added pathway-first experimental decision tree, repeated-anneal protocol, phase-matched isotope controls, and NV-center local magnetometry option.
- Added ML-search context from 2026 36-million-structure high-pressure and >2-million-structure ambient-pressure hydride studies.
- Expanded automated tests from 3 to 5 and made the calculation runner importable directly from the source tree.

## 0.5.0 — 2026-09-09

- Added a quantum-criticality-aware search program anchored to the July 2026 H3S displacive-QCP result.
- Added `criticality.py`, a transparent two-mode soft-phonon trade-off model and tests; no material-specific Tc claim is made from it.
- Added pressure/composition/isotope QCP screening matrices for Mg2RhH6, Li3Rh/CoH9, Mg/Al/FeH6, and H3S calibration.
- Added a five-gate material × preparation path × retained state × decisive-measurement decision system.
- Added H3S QCP, deep-free-energy LaScH8, and La3In electride evidence to the literature matrix.
- Added an interactive static research site under `docs/` plus a GitHub Pages deployment workflow.
