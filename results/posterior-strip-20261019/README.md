# Posterior defect decay on fixed-width Wilson strips

Research source checkpoint, 19 October 2026. This directory preserves two separately frozen source bundles and their reproducible checks. It is an additive branch archive, not a release or a solution of the four-dimensional Yang--Mills problem.

## Established result and exact scope

For each fixed finite transverse width and every finite nonnegative coupling beta, normalized Gaussian-conditioned halves of a Wilson strip have exponentially decaying posterior mismatch as their common longitudinal buffer grows. The reflected halves must have exactly the same collar weight, one-block factors, retained links, plaquettes, and interactions throughout that buffer. Arbitrary differences are permitted only beyond it.

For a bounded physical half-test F supported through block r and a shared buffer through block N, write M = ||F||_infinity and p = product_(i=r)^(N-1) tanh(beta C_i), where C_i counts interblock plaquettes. The result is pointwise in the Gaussian collar and consequently applies to the actual posterior rho:

    |P_W F - Q_W F| <= 2 M p,
    D_rho(F) <= 4 M^2 p^2,
    Re Q_mu(F) >= -M^2 p^2,
    dist(Q_mu(F), [0,infinity)) <= 2 M^2 p.

With fixed width and finite beta, each regular contraction coefficient is below one. The proof gives no width-uniform estimate. It does not establish the common-exhaustion condition for balanced growing four-dimensional boxes, simultaneous mixed-direction reflection positivity, a continuum limit, rotation invariance, or a mass gap.

The preceding Gaussian half-gluing result is a general conditional recovery criterion. Its required mismatch-decay hypothesis remains unproved in the general growing four-dimensional setting. The fixed-width theorem verifies that hypothesis only in the stated shared-prefix strip setting. A separate two-state joint-limit example in the new bundle is a limitation of a uniform inference, not a Wilson-model counterexample.

## Frozen artifacts

- `ym-posterior-strip-bound.zip`: the new proof, independent audit, exact finite-state and incidence checks, compact proof dependencies, assertion-preserving runner, and mutation controls. 80,527 bytes; SHA-256 `a1c2e7967360b04dc83d2e0c1f341112146b8d4c1c110e7afd14d50cc5c01890`.
- `gaussian-half-gluing-criterion.zip`: the preceding general conditional criterion, full independent and bond/orientation audits, and complete exact replay certificates. 241,200 bytes; SHA-256 `2e86a733374429ab6aa3cd8df86ef9209a8c28589b3e6a2d5f701c4f1d2c4ad5`.

The new ZIP is self-contained for its checks and already includes compact Gaussian proof/audit dependencies. The older ZIP is retained separately because its full audited artifact and certificates are not otherwise in the parent tree. No expanded duplicate source trees are added. Both ZIPs are byte-for-byte unchanged from their completed local checkpoints; historical statements such as "private", "local", or "no upload" inside them describe their original preparation stage.

`VERIFICATION.json` includes the original YM completion manifest and preceding archive receipt, independent clean-extraction replay and rebuild results, source pins, and the pre-write repository snapshot. `SHA256SUMS` covers the other four files. The verification record predates the branch write; actual remote commit/tree and downloaded-byte verification are recorded separately to avoid self-referential hashes.

## Offline reproduction

Verify this directory with `sha256sum -c SHA256SUMS`. Extract each ZIP into a separate clean directory.

From the root of the extracted posterior-strip ZIP, Python 3 standard library is sufficient:

    python -B verify_bundle.py
    python -O -B verify_bundle.py
    python -B build_zip.py /outside/source/strip-rebuilt.zip

From `gaussian-half-gluing-criterion/` in the extracted older ZIP, use Python 3.12, SymPy 1.14.0, and mpmath 1.3.0:

    python -I -B tools/replay.py
    python -I -B -O tools/replay.py
    python -I -B tools/replay_audit_mutations.py audit/check_audit.py
    python -I -B -O tools/replay_audit_mutations.py audit/check_audit.py
    python -I -B tools/build_archive.py /outside/source/gaussian-rebuilt.zip

Compare fresh outputs to the exact certificates identified in each bundle's README. Both modes were independently replayed after clean extraction and both archives rebuilt byte-identically in both modes. Raw optimized execution can erase assertions; the supplied assertion-preserving runners are essential. The finite checks supplement the analytic proofs and do not integrate the interacting SU(2) model, establish the missing infinite-volume estimates, constitute human peer review, or provide formal proof-assistant verification.

## Additive provenance

Parent commit: `35225c8d43fe3bc8fec3e478c2a92bbb89be37b8`.
Parent tree: `60f31b0ce9687fdf9443dfd52331d2620b9ed99a`.
Target branch: `research-posterior-strip-20261019`.
All five new files are under `results/posterior-strip-20261019/`.

Existing sources, branch tips, tags, releases, and archives are preserved. This archive operation creates no PR, merge, tag, or release.
