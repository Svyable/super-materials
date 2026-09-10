# Quantum-criticality-aware hydride search

## Motivation

Cherubini, Raghav and Casula (PRL 137, 046102, 2026; https://doi.org/10.1103/b1dd-gzf3) locate the H3S Im-3m ↔ R3m displacive quantum critical point near 134 GPa using path-integral molecular dynamics with an ML potential. The experimental Tc maximum lies in the neighboring centrosymmetric regime with large nuclear quantum fluctuations.

This does **not** imply that quantum criticality universally raises Tc. It supplies a falsifiable search strategy: sample a trajectory across a structural softening regime and ask whether superconducting pairing improves before the lattice loses the relevant state.

## Search coordinate

For each candidate family, vary at least two of:

- hydrostatic pressure;
- substitution/composition;
- H/D isotope;
- hydrogen vacancy concentration;
- carrier concentration.

At each state record:

1. harmonic phonon spectrum and soft eigenvector;
2. quantum/anharmonic free-energy curvature along the soft coordinate;
3. mode-resolved contribution to lambda and alpha2F(omega);
4. omega_log and total lambda;
5. energy-dependent DOS around EF;
6. hydrogen vacancy formation energy / diffusion propensity;
7. phase competition and decomposition pathway.

## Guardrail

A vanishing phonon frequency is not automatically optimal. If a soft sector raises lambda while collapsing the logarithmic frequency, Tc can peak at an interior point. The high-fidelity calculation must therefore test the full trajectory instead of selecting the softest harmonic structure.

## Target families

### Mg2RhH6 / Mg2Ir-RhH6
Pressure trajectory spanning the observed H5→H6 transformation and any lower-pressure decompression branch. Look for a soft coordinate that remains structurally identifiable while EPC strengthens.

### Li3Rh1-yCoyH9
Composition + pressure search. Promote only continuous QNE-stable basins; isolated alloy-interpolation maxima are rejected.

### Mg2-xAlxFeH6-delta
Carrier/defect trajectory at ambient pressure. Distinguish electronic proximity to a DOS feature from a genuine structural critical regime; monitor Fe magnetism and H-vacancy compensation.

## Falsification

The QCP search lane is rejected for a family when:

- softening does not enhance mode-resolved pairing;
- Tc monotonically falls as the critical coordinate is approached;
- the relevant state decomposes or loses hydrogen first;
- isotope/composition shifts are inconsistent with the proposed structural mode;
- QNE removes rather than stabilizes the proposed basin.

Quantum criticality is a search coordinate, not an evidence label for superconductivity.
