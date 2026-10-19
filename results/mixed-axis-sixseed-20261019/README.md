# Finite positive mixed prolate/oblate ACG-axis rigidity

Source-only scalar Gaussian covariance research archive, 19 October 2026.

## Accepted result and limits

For a reflection-invariant finite positive mixture of ACG angular densities, with
nonnegative isotropic background, mirror reflection positivity forces every
anisotropically active axis to be normal or tangent. The accepted extension covers
both prolate and oblate parameters and their positive mixtures. One oblique active
axis forces failure for every b,tau>0, with real compact smooth positive-time
spacetime witnesses at every sufficiently large finite tangential frequency.
No explicit witness or frequency threshold is computed.

The primary statement uses compact-inner parameter support. The reconciled extension
permits arbitrary positive probability Borel parameter measures on (-1,1), retaining
a finite axis set. Atoms at zero are isotropic; degenerate atoms at +/-1 are excluded.
Normal/tangent necessity is not sufficiency, and oblate normal-axis RP is not proved.
Signed mixtures are outside scope.

Finite axis support is essential: uniformly averaging any fixed nonzero ACG parameter
over continuous axes yields the constant isotropic density, which is RP at every
mirror despite oblique axes in that representation. This refutes unrestricted
representation-level axis necessity. Arbitrary nonconstant continuous-axis mixtures
and the broader angular-density classification remain unresolved. There is no
interacting Yang-Mills or mass-gap claim.

## Reproduce

Check the three payload files with `sha256sum -c SHA256SUMS`, then extract the ZIP.
From the extracted directory, with Python 3.12 and SymPy 1.14.0 already installed:

    python -B reproduce.py --integrity-only
    python -B reproduce.py --with-dependency-replay
    python -O -B reproduce.py --with-dependency-replay
    python -B test_package.py
    python -O -B test_package.py
    python -B build_archive.py /tmp/ym-mixed-axis-rebuilt.zip

No network is needed. The source archive contains its exact predecessor ZIP once,
including nested dependencies, and resolves all research-source pins offline.
Primary and independent checkers verify 55+36 exact identities. Their corruption
controls and inherited dependency tests run in ordinary and optimized modes, as do
24 package-integrity controls. Repeated builds and clean-extraction rebuilds match
byte-for-byte in the same Python/zlib toolchain.

Read RESULT.md, AUDIT.md and the final reconciliation files inside the archive.
All original source bytes are preserved. Historical candidate material is provenance
only, and the predecessor retains its historical prolate-only scope; the accepted
mixed-sign result is supplied by this subsequent package.

## Verification and archival status

VERIFICATION.json includes the frozen clean-extraction replay receipt, with hashes
of the original test receipts. Its `checkpoint_verification.remote_changes: false`
describes the checkpoint before this additive source archival operation.
This directory adds exactly the original ZIP, this README, SHA256SUMS and
VERIFICATION.json to the specified preceding research commit. It creates no PR,
merge, tag or release and overwrites no existing archive.
The exact tests check algebra and packaging. They are not proof-assistant
verification of the analytic, convergence, measure, topology or compact-witness
arguments, external peer review, a cryptographic signature or a hostile-code sandbox.
