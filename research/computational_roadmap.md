# High-fidelity computational roadmap

The cheap models in this repository generate questions. Promotion requires a fidelity ladder that attacks the largest uncertainty first.

## Stage 0 — reproduce parents

Reproduce lattice parameters, phase ordering, electronic states and published phonon/EPC benchmarks for experimental or well-established parent phases. A workflow that cannot reproduce the parent does not get to predict a derivative.

## Stage 1 — crystal structure search

For each pressure/composition window:

- multiple formula units;
- relevant ordered substitution patterns;
- unconstrained and motif-seeded searches;
- H-deficient and H-rich stoichiometries;
- decomposition products on the same level of theory.

Build pressure-dependent convex hulls rather than checking a candidate in isolation.

## Stage 2 — disorder and defects

For substitutional lanes compare ordered cells and SQS-like disorder models. For hydrogen-rich systems calculate vacancy/interstitial formation energies as a function of hydrogen chemical potential. Aliovalent substitution is not rigid-band doping until compensation is ruled out.

## Stage 3 — harmonic lattice dynamics

Converge q/k meshes and smearing. Record mode-resolved lambda and alpha2F(omega), not only scalar lambda/omega_log. Imaginary modes trigger a structural search or anharmonic analysis, not automatic stabilization by wishful interpretation.

## Stage 4 — quantum nuclei and anharmonic free energy

Hydrogen systems require explicit checks where zero-point motion or anharmonicity can reorder phases or stabilize/soften modes. Use SSCHA, path-integral methods, validated quantum-nuclear surrogates, or a benchmarked lower-cost alternative. Treat method spread as uncertainty.

## Stage 5 — superconductivity beyond a constant DOS

Where DOS varies sharply near EF, compare standard Allen-Dynes/isotropic treatments with full-bandwidth and, where justified, anisotropic Migdal-Eliashberg calculations. Report mu* assumptions and sensitivity.

## Stage 6 — kinetic synthesizability

A thermodynamically metastable state can still matter if a realistic path reaches it. Use precursor-lattice compatibility, NEB, metadynamics or ML molecular dynamics to test formation and decompression routes. Record barriers and time/temperature scales rather than calling a positive hull distance 'synthesizable'.

## Stage 7 — active learning

Use cheap descriptors and alpha2F surrogates only to select the next exact calculation. Hold out chemical families and pressure trajectories, calibrate uncertainty, and benchmark against random acquisition at equal DFPT budget.

## Stage 8 — experiment contract

Every promoted candidate must ship with:

- exact structure candidates and strongest XRD peaks;
- Raman/IR discriminants;
- target pressure/temperature path;
- competing phases and their fingerprints;
- predicted field/isotope behavior;
- phase-linked transport protocol;
- magnetic/thermodynamic follow-up;
- kill criteria and raw-data schema.

The shortest path to a useful result is often the shortest path to a decisive negative result.
