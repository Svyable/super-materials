# GitHub Pages site

The public research experience is a dependency-free static site in `docs/`. It is rebuilt from repository data by `python scripts/build_site.py` and deployed by `.github/workflows/pages.yml` **after the test suite and reproducibility script pass**.

Expected project URL once the public repository exists and Pages is enabled:

**https://svyable.github.io/super-materials/**

GitHub currently requires the repository publishing source to be configured once under **Settings → Pages → Build and deployment → Source → GitHub Actions**. The checked-in workflow then deploys `docs/` on every push to `main` and can also be run manually.

The site intentionally avoids a framework/CDN. This keeps the public artifact auditable, fast, and runnable from a single Pages payload. `scripts/build_site.py` copies curated data, research notes, and generated figures into that payload so the site does not depend on fetching files outside its own project path.

## v0.6 public experience

The static site now exposes the research program as an evidence system rather than a long README:

- interactive evidence-aware pressure–Tc frontier;
- hypothesis cards with fastest falsifiers;
- Decision Lab with explicit Bayesian assumptions and expected information gain;
- claim/evidence graph separating anchors, constraints, mechanism support and speculation;
- six-level replication ladder;
- quench/retention engineering;
- searchable literature ledger;
- reproducible model and fingerprint gallery;
- downloadable decision, replication, experiment and source-audit artifacts.

No external JavaScript framework or CDN is required. A Pages deploy is gated on reproduction + tests + site build. The project deliberately keeps a static generated data layer (`docs/assets/data/site-data.js`) so public claims can be traced to versioned repository inputs.


## v0.6 release integrity

The site exposes the physics-informed screening registry and is built hermetically: generated figures/data/downloads are deleted and rebuilt on every deployment. `scripts/validate_site.py` rejects broken local links, stale version metadata, missing dynamic gallery assets, malformed claim/evidence references, and JavaScript syntax errors when Node is available.
