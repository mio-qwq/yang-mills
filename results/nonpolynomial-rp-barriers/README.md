# Finite ellipsoid rigidity and separable Laplace-product RP obstruction

Research-source follow-up, 19 October 2026. Two specific nonpolynomial escape routes are excluded, with an independent mathematical audit and exact symbolic witnesses.

## Results and limits

1. A finite positive mixture of massive or massless positive-definite ellipsoidal resolvents that is reflection invariant and reflection positive at a mirror must have that normal as an eigenvector of every participating quadratic form. Coordinate and connecting diagonal mirrors force every form to be scalar. Same-phase upper-pole residues prevent cancellation. Finiteness and strictly positive weights are essential to the stated result.
2. For any finite nonzero positive measure on nonnegative rates, the product of four identical Laplace-mixture factors is bounded, continuous, W4-invariant, and coordinate-reflection-positive. Unless the factor is constant, an exact three-point diagonal test with coefficients (1,-2,1) is strictly negative. This includes arbitrary finite measures, including continuous ones, not merely finite atomic mixtures. Origin-supported contacts cannot repair either obstruction.

These results concern the stated scalar covariance classes. They do not classify nonseparable kernels or continuous mixtures of ellipsoidal matrices; they do not prove general all-mirror rigidity, an interacting-field spectral representation, a Yang–Mills construction, or a mass gap. No novelty, formal-verification, external-human-peer-review, or hosted-CI claim is made. The independent audit's endpoint/holomorphy discussion is a supplementary argument under explicitly checked regularity hypotheses, not an unrestricted RP representation theorem.

## Contents

- `nonpolynomial-rp-escape-20261019/RESULT.md`: complete statements, proofs, a concrete two-time ellipsoid witness, and the universal three-point product witness.
- `nonpolynomial-rp-escape-20261019/VERIFY_EXACT.py` and `.txt`: exact symbolic author checks and their recorded output.
- `nonpolynomial-rp-audit-20261019/AUDIT.md`: independent audit, localization and pole details, and scope qualifications.
- The audit's exact symbolic checkers and text receipts verify the geometric witness and finite interpolation mechanism independently.

## Reproduce

Tested with Python 3.12.14, SymPy 1.14.0, and mpmath 1.3.0. Python 3.10 or later is recommended. `requirements.txt` records the tested dependency versions. With dependencies installed, no network, repository checkout, or external file is needed.

    python -B verify_sources.py
    python -B verify_sources.py --run-checks
    python -B -O verify_sources.py --run-checks

The wrapper validates the complete file set and hashes. Every canonical checker is replayed in normal and optimized Python; explicit exceptions remain active under `-O`. Expected standard output and every frozen byte are compared after each run. `LOCAL_VERIFICATION.json` records the local replay. The symbolic checks validate displayed identities; the universal mathematical claims rest on the written proofs and audit, not on finite computation alone.

`PACKAGE_MANIFEST.json` lists every file except itself and `SHA256SUMS`; `SHA256SUMS` covers every file except itself. An external archive digest authenticates the entire package. Scratch searches and caches are excluded.

## Integration boundary

Prepared locally for the new additive directory `results/nonpolynomial-rp-barriers` in `mio-qwq/yang-mills`, following dedicated-branch commit `47a8e321dcd945ebd7cc185b1fd7bdbd1f140151`. The observed main was `512734760722dc9ad74916abc695409f7fa86e26`. This package performs no remote writes, main changes, PR operations, tags, or releases. A later integration requires its own authorization and fresh baseline checks.
