# Retained-State Engineering v0.7

## Thesis

A useful superconducting technology is not specified by critical temperature alone.

For every candidate, track two independent temperatures:

- `Tc`: below this temperature the verified state superconducts;
- `Tretain(t, S*)`: highest storage/handling temperature at which that same state survives for duration `t` with at least target survival probability `S*`.

The near-term engineering objective is therefore not only "raise Tc." It is to create states with useful `Tc`, ambient-pressure operation, and a retention envelope compatible with fabrication, shipping, storage, cycling, and repeatable measurement.

The research object becomes:

**material × precursor × preparation path × retained state × retention surface × decisive measurement × evidence class**.

## Why this is now a first-class program

Pressure-quenched HgBa2Ca2Cu3O8+δ reached 151 K superconductivity at ambient pressure, while the retained state was reported to degrade after warming above roughly 200 K. That separates ambient pressure from room-temperature survivability.

Primary source: https://doi.org/10.1073/pnas.2536178123

Experimentally synthesized Mg2RhH6 becomes superconducting near 30 GPa after an H-deficient precursor is converted into an H6 octahedral phase. The route itself is evidence that precursor state and hydrogen insertion history are design variables.

Primary source: https://doi.org/10.1021/jacs.6c08889

Ambient recovery of Y3Fe4H20 demonstrates that a structurally unconventional hydrogen-rich phase can be trapped after decompression without thereby establishing superconductivity. Recovery physics and pairing physics must remain separate axes.

Primary source: https://doi.org/10.1038/s41467-026-74232-4

Recent CaH6-δ calculations link decompression-driven H vacancies to shear instability, faster H diffusion, and suppressed superconductivity. Hydrogen retention, mechanics, and Tc can fail together but should still be measured separately.

Primary source: https://doi.org/10.1103/ng2f-ldwh

The 2026 PNAS programmatic framework explicitly separates Prediction and Engineering challenges. v0.7 makes retained-state lifetime a measurable bridge between them.

Primary source: https://doi.org/10.1073/pnas.2520324123

## Retention surface

A retained state should be represented by measurements over:

`S = S(T, t, P, history, isotope, precursor, microstructure)`

where `S` is the probability that the target structural/electronic state still exists after the specified treatment.

Do not infer `S` from transport alone. The state definition should require structural or spectroscopic fingerprints tied to the same `state_id`.

Minimum retention experiment:

1. establish the target phase at formation conditions;
2. measure phase fingerprint + transport baseline;
3. move to a specified pressure/temperature state;
4. hold for a registered duration;
5. re-measure phase fingerprint, transport, and when justified magnetic response;
6. continue until the retained phase fails or the planned envelope is demonstrated;
7. publish failures and ambiguous states with the same metadata as successes.

## Competing escape pathways

The old single-barrier Arrhenius model remains useful as a lower-cost threshold calculation, but real retained phases may have several competing exits:

- H loss to interfaces or electrodes;
- H6 → H5 local reconstruction;
- shear-driven lattice transformation;
- disproportionation or phase separation;
- oxygen/hydrogen ordering changes;
- grain-boundary nucleation;
- defect-cluster migration.

For independent first-order escape channels,

`k_escape(T) = Σ_i ν_i exp(-E_i / kBT)`

and a simple survival model is

`S(T,t) = exp[-k_escape(T) t]`.

This is still a screening model, not a claim that real transformations are single-step or independent. Deviations from it are scientifically useful because they signal collective kinetics, heterogeneous barriers, or changing mechanisms.

## v0.7 scorecard

Never collapse these into one miracle score:

| Axis | Symbol | Preferred direction |
|---|---|---|
| formation pressure | `Pform` | lower |
| operating pressure | `Pop` | lower |
| superconducting transition | `Tc` | higher |
| retained-state survival at 300 K | `S300(t)` | higher |
| room-temperature lifetime | `tau300` | higher |
| superconducting volume fraction proxy | `fSC` | higher |
| critical current density | `Jc(T,H)` | higher |
| thermal-cycle endurance | `Ncycle` | higher |
| evidence level | categorical | stronger |
| abundance/toxicity/manufacturability | separate descriptors | better |

A state that survives room-temperature handling but has modest Tc can be an important engineering success. A state with spectacular Tc that cannot survive decompression or handling remains a physics result rather than a technology.

## First campaign: Q-MRH6 retention map

The immediate objective is not "prove ambient-pressure Mg2RhH6." It is to learn the topology of failure.

Recommended pressure ladder:

`30 → 20 → 15 → 10 → 5 → 2 → 1 → 0 GPa`

At each pressure stop, compare at least:

- cold-fast decompression;
- cold-staged decompression;
- warmer-staged decompression;
- matched H/D where feasible;
- crystalline vs intentionally disordered precursor if synthesis allows.

Log all observations under one state recipe. The most valuable result may be a reproducible boundary where H6 structure, transport, or both fail.

Promotion criterion: a protocol shifts the verified H6 retention floor downward reproducibly while preserving the same-state superconducting signature.

Stop criterion: no credible preparation-path variable shifts the phase-retention floor after adequate replication.

## Recovery-first discovery lane

Search for **retention scaffold + pairing engine** rather than maximizing calculated Tc in isolation.

A candidate should earn expensive EPC/SSCHA work when it combines evidence for:

1. a mechanically/chemically persistent scaffold;
2. electronically active H or another high-frequency pairing sublattice;
3. a plausible kinetic path into the desired basin;
4. suppressible low-barrier escape routes;
5. a decisive experiment that can identify the retained phase.

This makes recoverable non-superconducting hydrides useful negative controls and design parents instead of dead ends.

## Open Superconducting State Atlas

The public data object should be a state recipe, not a headline claim.

For every measured state publish:

- composition and uncertainty;
- precursor identity and microstructure;
- full pressure/temperature/time trajectory;
- isotope and hydrogen source;
- anneal/laser dose;
- decompression rate and dwell schedule;
- structural/spectroscopic fingerprint;
- transport trace metadata;
- magnetic/thermodynamic measurements where available;
- elapsed time since preparation;
- retained/failure/ambiguous label;
- raw-data pointers;
- evidence class;
- independent replication status.

The schema in `data/state_recipe_schema_v07.json` is the minimum machine-readable contract.

## Near-term success definition

A world-changing intermediate result does not have to be a 300 K superconductor.

A state with:

- ambient-pressure operation,
- Tc high enough for cheap closed-cycle or liquid-nitrogen-adjacent cooling,
- room-temperature storage/handling lifetime,
- reproducible bulk superconductivity,
- useful Jc,
- manufacturable chemistry,

would remove a major practical barrier even before room-temperature superconductivity itself is reached.

v0.7 therefore optimizes for **useful retained quantum matter**, not a single record number.
