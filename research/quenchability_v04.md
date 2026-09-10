# Quenchability and retained-state engineering

## Why this is a separate objective

The pressure-quench Hg1223 experiment (PNAS 2026; https://doi.org/10.1073/pnas.2536178123) demonstrates 151 K superconductivity at ambient pressure in a state prepared under pressure and released at low temperature. The state is metastable and thermally limited. Therefore three milestones must never be conflated:

1. superconductivity at high pressure;
2. superconductivity after pressure release;
3. survival of that state at room temperature for a useful lifetime.

## Q-MRH6 hypothesis

`Q-MRH6 = pressure-quenched Mg2RhH6-delta`.

The parent Mg2RhH6 phase is experimentally synthesized and superconducting from 30 GPa (JACS 2026; https://doi.org/10.1021/jacs.6c08889). The hypothesis is only that some H6-rich fraction might be kinetically retained below its equilibrium formation window under a controlled decompression path.

No ambient-pressure Tc is assigned.

## First-wave experiment

Use matched DAC samples and randomize protocol where practical:

- form Mg2RhH5 precursor;
- hydrogenate to the H6 phase above 30 GPa;
- establish diffraction/Raman and four-probe baseline;
- compare cold-fast decompression against staged decompression with controlled dwell times;
- at each pressure stop record pressure, temperature, elapsed time, phase fingerprint and transport under the same `state_id`;
- repeat an H/D pair with matched phase identity;
- after any retained transition, measure field dependence before decompression continues.

## Retention-barrier screening

For a single activated escape process with attempt frequency `nu0`, survival time scale is approximately

`tau = exp(Ea/kBT) / nu0`.

Thus a target barrier is

`Ea = kBT ln(nu0 tau)`.

For `nu0 = 10^13 s^-1`, order-of-magnitude examples are roughly 0.28 eV for several days at 77 K and ~1.2 eV for year-scale retention at 300 K. These are design thresholds—not predicted Mg2RhH6 barriers.

## Computation

Before expensive recovery attempts, calculate plausible exit paths:

- H6 → H5 hydrogen loss;
- octahedral → square-pyramidal local rearrangement;
- H diffusion to interfaces/electrodes;
- metal-sublattice reconstruction / disproportionation.

Use NEB or enhanced sampling after endpoint structures and chemical potentials are credible. Pressure-dependent barriers matter more than a single 0 GPa value.

## Stop rules

Stop the ambient-recovery lane if repeated, phase-verified protocols show the H6 signature always disappears above a pressure floor that cannot be materially shifted by temperature, rate, precursor state or isotope. Do not reinterpret an unlinked resistance drop as retained H6 superconductivity.
