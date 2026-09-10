# Source and evidence audit v0.6

## Evidence classes

`EXPERIMENTAL_PRIMARY` — peer-reviewed primary experimental result.

`AB_INITIO_PRIMARY` — primary first-principles prediction; not experimental validation.

`METHOD_PRIMARY` — new computational/measurement method or descriptor.

`REPORTED_PREPRINT_CONTESTED` — public claim retained for completeness but not used as an established calibration point.

`SECONDARY_INDEX_PENDING_PRIMARY_METADATA` — discoverability evidence only; never treated as a primary technical source.

## Core calibrated anchors

### Mg2RhH6
Primary: https://doi.org/10.1021/jacs.6c08889

Use: experimentally anchors the Mg/Rh/H chemistry, H5→H6 pathway, ~30 GPa stability/superconductivity onset and field-sensitive zero resistance. It does **not** support ambient recovery without new experiments.

### Hg1223 pressure quench
Primary: https://doi.org/10.1073/pnas.2536178123

Use: proves that a pressure-enhanced superconducting state can be retained to ambient pressure. It also demonstrates why operating pressure, storage temperature and lifetime must be separate fields.

### H3S quantum structural criticality
Primary: https://doi.org/10.1103/b1dd-gzf3

Use: motivates trajectory-based QNE screening near a displacive QCP. It does not establish that proximity to any soft mode raises Tc in every material.

### MgAlFeH6
Primary: https://doi.org/10.1038/s41524-026-02040-x

Use: anchors the carrier-engineered transition-metal-hydride lane and the H-active DOS geometric-mean feature. Predicted ~130 K remains a theoretical result; metastability and disorder/defects remain experimental risks.

### Ambient conventional ceiling
Primary: https://doi.org/10.1038/s41467-025-63702-w

Use: strong portfolio prior after very large-scale EPC + ML screening. The result is summarized as 'equilibrium ambient 300 K conventional superconductivity appears extremely unlikely within the searched landscape', never as a mathematical impossibility theorem.

### BEE-NET
Primary: https://doi.org/10.1038/s41524-026-01964-8

Use: motivates predicting alpha2F rather than scalar Tc. Published domain limitations are preserved; the repo does not deploy it directly on high-pressure hydrides.

### Phonon-assisted nesting
Primary: https://doi.org/10.1038/s41524-026-02160-4

Use: necessary-condition pre-DFPT triage only. The small benchmark and lack of universal Tc mapping remain visible.

## Contested claims

Near-room-temperature La-Sc-H reports remain visible as contested/preprint evidence pending independent reproduction and phase-resolved confirmation. They are excluded from established-benchmark language and from any automated calibration set that assumes the reported state is verified.

## Rule

If a source cannot be traced to a stable primary paper/record, its row is demoted rather than silently repaired from secondary summaries. The website should prefer an explicit 'primary metadata pending' label over a broken or misleading link.
