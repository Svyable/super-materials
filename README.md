# super-materials

**Open, falsifiable research toward high-Tc and ultimately room-temperature superconductivity.**

> **Status — v0.7.0, 21 September 2026.** This repository contains literature synthesis, speculative candidate hypotheses, transparent screening models, experiment designs, replication standards, and a public evidence-aware research site. **It does not contain experimental proof of a new superconductor.** Every speculative number is labeled as such.

## Research thesis

The useful object is not just a chemical formula. It is:

**material × preparation path × retained state × decisive measurement × evidence class**.

That framing follows directly from the frontier. High-pressure hydrides show that enormous phonon scales and strong electron-phonon coupling can produce very high Tc, but stability, defects, reaction kinetics, anharmonic/quantum-nuclear effects, and measurement ambiguity are often decisive. Pressure-quenched Hg1223 further demonstrates that a high-Tc state can be trapped at ambient pressure without being thermally stable to room temperature. Those are distinct milestones.

v0.6 adds a second principle: **maximize information gained per expensive calculation or experiment, not the number of candidates generated.**\n\nv0.7 adds a third: **a superconducting state is not technologically useful until its retention envelope is measured.** The repository now treats `Tc` and retained-state survivability as independent objectives and introduces a machine-readable state recipe plus multi-path escape kinetics.

## Current hypotheses

| Lane | Research object | Target | Why it exists | Fastest serious falsifier |
|---|---|---|---|---|
| Q-MRH6 | pressure-quenched Mg2RhH6-delta | progressive decompression toward 0 GPa | experimentally anchored H5→H6 hydride chemistry; asks whether the superconducting H6 state can be kinetically retained | same-state XRD/Raman + four-probe transport during controlled cold decompression; reject if H6 fingerprints vanish before the transport anomaly |
| MIRH-25 | Mg2Ir0.75Rh0.25H6 | 15–30 GPa | mixes experimentally demonstrated Rh chemistry with high-Tc Ir-hydride predictions | ordered/SQS structure search + hull + phonons + EPC; reject if no stable basin exists |
| LMBH-25 | Li1.75Mg0.25BH6-delta | 12–25 GPa | probes whether B-H high-frequency modes survive aliovalent tuning | defect chemical-potential diagram and H-vacancy energetics; reject rigid-band picture if compensation dominates |
| MAFH-gradient | Mg2-xAlxFeH6-delta | 0 GPa | tests carrier engineering around the predicted MgAlFeH6 endpoint | Hall + stoichiometry + ordered/SQS DFT; reject if carriers pin, magnetism wins, or H vacancies erase the intended doping |
| L3-RC-H9 | Li3Rh1-yCoyH9 | <=15 GPa | asks whether Rh-like pairing and Co-like lower-pressure stability can be partially decoupled | convex hull + QNE-aware phonons; require a contiguous stable basin, not a single interpolated point |
| YFRH20 | Y3Fe3RuH20 | recovered 0 GPa | recovery-first lane: engineer electronic H weight inside a recoverable hydride topology | constrained CSP; reject if recovered topology phase-separates or H DOS at EF remains negligible |

## v0.7 — retained-state engineering\n\nThe new engineering quantity is a retention surface `S(T,t,P,history)`: the probability that the verified target state still exists after a specified storage or handling trajectory. This separates ambient-pressure superconductivity from room-temperature survivability. A useful intermediate target may be a high-Tc state that can be manufactured and stored at room temperature even if operation still requires cooling.\n\nThe code in `src/super_materials/retention.py` models multiple competing activated escape channels as a transparent screening baseline. `data/state_recipe_schema_v07.json` defines the minimum metadata needed to make successful and failed retained states reusable. See `research/retained_state_engineering_v07.md`.\n\n## Quantitative screening — with guardrails

The early candidate models intentionally use inexpensive tight-binding / phenomenological inputs plus Allen–Dynes screening. With mu*=0.10, the central toy-model estimates are about 150 K for MIRH-25 and 224 K for LMBH-25. Their broad parameter sweeps extend much wider. **These are hypothesis-calibration values, not DFT results and not predictions of observed Tc.** Any candidate must survive structure, thermodynamics, defects, anharmonic/QNE physics, full electron-phonon calculations, and ultimately experiment before promotion.

For room-temperature conventional superconductivity, the repository treats the 2025 large-scale ambient-pressure search result as a strong prior: after >20,000 full EPC calculations and screening >100 million compounds, a persistent lambda–omega_log–stability tradeoff remained. That makes an equilibrium ambient-pressure 300 K phonon superconductor an exceptionally high bar, not a logical impossibility. DOI: https://doi.org/10.1038/s41467-025-63702-w

## v0.6 — decision intelligence

A binary experiment is represented by an explicit prior P(H), sensitivity P(+|H), specificity P(-|not H), relative cost, and whether the test is conditional on earlier gates. From those assumptions we compute posterior probabilities and expected information gain in bits. The numbers are **planning assumptions**, not claimed discovery probabilities.

Example Q-MRH6 campaign assumptions:

| Test | Prior | Sens. | Spec. | Expected information | Relative cost |
|---|---:|---:|---:|---:|---:|
| same-state phase + transport | 0.25 | 0.85 | 0.95 | 0.444 bits | 5.0 |
| resistivity only | 0.25 | 0.80 | 0.60 | 0.127 bits | 1.5 |
| isotope + field response | 0.25 | 0.75 | 0.90 | 0.279 bits | 4.0 |
| direct gap spectroscopy | 0.60 conditional | 0.95 | 0.97 | 0.510 bits | 10.0 |

The point is not that these likelihoods are known. The point is that **specificity matters**: a phase-linked transport experiment can be worth far more than another resistance trace because it rules out more artifact classes.

## Physics-informed pre-DFPT triage

Two cheap features enter only as acquisition / rejection aids:

1. `sqrt(D_total(EF) * D_H(EF))`, motivated by the MgAlFeH6 family as a compact measure of simultaneous metallicity and H participation near EF.
2. the 2026 phonon-assisted nesting function P(omega), with normalized descriptor P/(m* M), proposed as a necessary-condition screen for strong EPC.

Neither is accepted as a Tc predictor. The benchmark is falsifiable: at equal DFPT budget, does descriptor+uncertainty acquisition recover the high-lambda/high-Tc set with fewer expensive labels than random or uncertainty-only acquisition? False negatives are published.

## High-fidelity ladder

1. reproduce parent structures/benchmarks;
2. crystal-structure search + convex hull across pressure and composition;
3. defects/disorder and hydrogen chemical potential;
4. harmonic DFPT and mode-resolved alpha2F(omega);
5. anharmonic / quantum-nuclear free-energy and phonon treatment;
6. full-bandwidth / anisotropic Eliashberg where sharp DOS features make constant-DOS approximations unsafe;
7. kinetic pathway / NEB / MLMD for metastable formation and decompression;
8. synthesis + same-state structure, transport, magnetometry, thermodynamics, isotope controls, and—when justified—direct tunneling gap spectroscopy.

## Evidence policy

A result moves through a six-level ladder: anomaly → transport → phase-linked → bulk-consistent → mechanism-resolved → independent replication. A room-temperature-superconductivity claim is reserved for independent reproduction of the phase, transition, decisive controls, and open protocol.

Controversial results remain visible but carry their evidence class. The repository never silently upgrades a preprint, secondary index, or disputed replication into an established benchmark.

## Public site

The GitHub Pages experience is in `docs/` and is intentionally dependency-free. It exposes candidate lanes, interactive evidence maps, decision assumptions, the replication ladder, source provenance, and fast falsifiers rather than presenting a hype-only landing page.

Expected URL: **https://svyable.github.io/super-materials/**

## Key research notes

- `research/retained_state_engineering_v07.md`\n- `data/state_recipe_schema_v07.json`\n- `data/retention_targets_v07.csv`\n- `research/decision_intelligence_v06.md`
- `research/physics_informed_screening_v06.md`
- `research/surrogate_active_learning_v06.md`
- `research/replication_standard_v06.md`
- `data/claim_evidence_graph_v06.json`
- `data/experiment_decisions_v06.csv`
- `data/literature_matrix.csv`

## Reproducibility

The full local research package also contains Python models, XRD simulation, quench kinetics, quantum-criticality toy models, generated figures, and tests. The public repository is structured so new claims can be added only with assumptions, evidence class, and a kill test.

## License

MIT. Scientific claims remain subject to the terms, uncertainty, and provenance of their cited primary sources.
