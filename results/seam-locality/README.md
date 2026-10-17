# Finite-volume seam locality

The [frozen certificate](LOCALITY_CERTIFICATE.md) proves that the original quartic elementary-plaquette mechanism cannot be relocated even one full 0/1 coordinate layer into the strict representative half. The entire quartic reflected covariance matrix vanishes there. This does not establish positivity at higher orders.

For bounded fixed interior observables, a connected-support cumulant criterion gives agreement with a reflection-positive cylinder below the first seam-connected order; coordinate depth L guarantees agreement through degree L. A finite-volume Cauchy bound controls the remaining difference. Connectivity is necessary, not sufficient, and supplies no leading sign.

The [independent AI-assisted review](REVIEW.md) and exact geometry controls support these statements. They are not human peer review or Lean formalization. The later [remote-boundary result](../remote-boundary-obstruction/README.md) supplies a higher-order negative coefficient at every prescribed integer depth.

## Reproduce

From this directory, run `python3 check_quartic.py` and `python3 check_geometry.py`. Both use the standard library. Fresh commands, hashes and full outputs are recorded in [VERIFICATION.md](VERIFICATION.md).

## Frozen-source portability

Proof and review bytes are unchanged. Their historical absolute paths identify local source provenance, not runtime dependencies. [SOURCE_MAP.json](SOURCE_MAP.json) maps every copied file to its origin and SHA-256. The pristine v0.7 dependency cited under `/tmp/ym-torus-remote-audit-20261017/` is the repository's [diagonal-torus proof](../diagonal-torus-obstruction/PROOF.md), SHA-256 `f8167a31b447add79427b35d06460e4be976d7168b257f4e7dd0d9ff9ba07c4e`. Historical source-hash records are preserved verbatim and are not portable shell manifests. No external manuscript is redistributed.

The frozen certificate's suggested longer-tube route was unproved at its writing; the separately reviewed result linked above resolves that specific finite-volume question. No continuum, fixed-physical-source or mass-gap claim follows.
