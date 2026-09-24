# State Atlas v0.8

## Why an atlas

v0.7 defined retained-state engineering. v0.8 makes it cumulative.

A field cannot learn retention physics efficiently if only the winning composition and highest transition temperature survive publication. The reusable object is the **state trajectory**: precursor, pressure/temperature path, recovered phase, time-dependent degradation, measurement linkage, and explicit limitations.

The initial atlas is intentionally small and high-confidence. It contains calibration cases that teach different things rather than a long scrape of loosely comparable papers.

## Initial calibration set

### Hg1223 — superconductivity retained, thermal envelope limited

Deng et al. report ambient-pressure superconductivity up to 151 K after pressure quenching HgBa2Ca2Cu3O8+δ from 18.9 GPa at 4.2 K. A related pressure-quenched state with Tc=149 K remained in the DAC at 77 K for at least three days and was stable through cycling up to about 170 K with slight Tc loss. Cycling another retained state to room temperature reduced its ambient-pressure Tc from 147 K to 143 K.

Primary source: https://doi.org/10.1073/pnas.2536178123

Atlas lesson: **ambient pressure is not the same as room-temperature retention**. Degradation is graded, not necessarily a single sharp failure temperature.

### Y3Fe4H20 — structural retention without superconductivity

Caussé et al. synthesized Y3Fe4H20 starting at 60 GPa and followed the Cmcm phase to ambient pressure at room temperature. XRD established metastability for roughly 30 hours in one run. Other recovered samples examined after about one to three months showed a 7–8% volume reduction attributed to hydrogen desorption. The material is metallic but reported non-superconducting.

Primary source: https://doi.org/10.1038/s41467-026-74232-4

Atlas lesson: **a retention scaffold can be a success even when pairing is a failure**. Long-lived structure and superconductivity are independent observables.

### Pd hydrides — precursor state changes the pathway

Liu et al. formed metastable PdH3 at about 32.2 GPa and ~2000 K from amorphous Pd nanoparticles. After unloading, the recovered product was PdH1.3 rather than PdH3. A crystalline-fcc Pd control followed a different path: Pd3H5 at high pressure and PdH0.706 after recovery.

Primary source: https://doi.org/10.1021/acsnano.5c06652

Atlas lesson: **precursor microstructure belongs in the material definition**. Composition alone does not specify the accessible metastable basin.

### Mg2RhH6 — formation anchor, recovery unresolved

Wu et al. experimentally synthesize Mg2RhH6 through a two-step Mg2RhH5 → Mg2RhH6 hydrogen-insertion route. Superconductivity emerges around 30 GPa with Tc≈24 K and rises to about 29 K when synthesized at 53 GPa, with zero resistance and field suppression of Tc.

Primary source: https://doi.org/10.1021/jacs.6c08889

Atlas lesson: this is the anchor for Q-MRH6, **not an ambient-recovery claim**. v0.8 keeps unresolved retention explicitly unresolved.

## Data policy

`data/state_atlas_v08.json` obeys four rules:

1. missing quantities are `null`, never guessed;
2. every record has a DOI-resolved provenance and explicit limitations;
3. superconductivity and structural retention are separate fields;
4. transformation on recovery is retained as data rather than treated as a failed record.

The lightweight validator in `src/super_materials/atlas.py` enforces the minimum contract without adding a new dependency.

## Q-MRH6 campaign generation

The same module generates a 12-run factorial first wave:

- three decompression profiles: cold-fast, cold-staged, warmer staged control;
- H and D;
- crystalline and deliberately disordered precursor states.

Every run uses the same pressure ladder:

`30 → 20 → 15 → 10 → 5 → 2 → 1 → 0 GPa`

and the same mandatory state linkage:

`phase fingerprint + four-probe transport + elapsed time + pressure + temperature`.

The matrix intentionally does **not** invent universal decompression rates or dwell times. Those depend on the actual apparatus and should be registered by the experimental team. The machine-generated design fixes the comparison axes without pretending to know instrument constraints.

## What counts as progress

A Q-MRH6 run is informative even if superconductivity disappears.

The campaign promotes a preparation path when it reproducibly pushes the verified H6 phase to a lower pressure while retaining a same-state superconducting signature.

It kills or redirects a path when:

- the H6 structural fingerprint disappears before the transport anomaly;
- the transport signal survives in a structurally different state;
- isotope/precursor changes do not shift the retention boundary after replication;
- hydrogen loss or mechanical instability explains the observed floor.

The goal is to learn the **failure surface**, not manufacture a favorable plot.

## Next atlas expansion

The next records should be selected for information diversity:

- a room-temperature structurally retained hydride with quantified hydrogen-loss kinetics;
- a pressure-quenched superconducting state with bulk magnetic follow-up;
- a decompression failure with synchronized structure + transport;
- a metastable state stabilized by anharmonicity rather than a simple static barrier;
- independent replications or failures of existing retained-state claims.

That dataset can then support survival-analysis and active-learning methods without training on a winner-only literature.
