# Scalar Gaussian coordinate-mirror reflection-positivity repair

Source-only recovery archive, 19 October 2026. This additive directory contains one original deterministic ZIP and three metadata files.

## Accepted scope and status

For the stated scalar Gaussian family and all b,tau>0, constant dilution with epsilon=1/1200 repairs reflection positivity at every coordinate mirror, with strict common-cut spectral margin 37/600. The positive density is nonconstant. Diagonal-mirror reflection positivity remains unproved; this is not an interacting Yang-Mills construction or mass-gap result.

All 71 current exact symbolic checks pass in both modes, including independent algebra and deliberate-corruption controls. The 164 prior mixture checks and the nested original axial-family replay also pass. Both current and dependency payload integrity checks reject tampering. These finite symbolic checks support the retained analytic proofs.

Independent audits are AI-assisted. No human peer review, proof-assistant verification, historical-originality claim, P-versus-NP solution or interacting Yang-Mills mass-gap proof is asserted.

## Recovery

1. Run `sha256sum -c SHA256SUMS` in this directory.
2. Extract `ym-coordinate-rp-repair-20261019.zip` into a fresh directory and enter `ym-coordinate-rp-repair-20261019`.
3. Read the included README, proof and audit documents. Run `python reproduce.py --with-dependency-replay` or `python -O reproduce.py --with-dependency-replay` for the current result and full pinned dependency chain. Omitting that flag runs the current result with dependency integrity checks only.

For a quick integrity-only check, run `python reproduce.py --integrity-only` or `python -O reproduce.py --integrity-only`.

Requires Python 3.10+ and SymPy 1.14.0. The reproduction entry point places generated files and temporary executables in disposable directories. No dependency installation or numerical-solver run was performed by this archive operation.

Archive: 107,485 bytes. SHA-256: `22c52749cb61123aedadc1313d316b8c5eebb36232c1bf71c7e8130036c61b0d`.

## Verification and preservation

The frozen local checkpoint completed clean-extracted normal/optimized replays, negative controls and deterministic byte-identical archive rebuilds. This archive operation freshly verified every checkpoint-manifest file, ZIP SHA-256 and size, CRC, forbidden-path/cache/executable exclusion, and both normal/optimized integrity-only wrappers. VERIFICATION.json records these checks and supporting receipt hashes; it does not preclaim post-commit remote verification.

Original ZIP bytes and retained research sources are unchanged. Embedded local-only provenance statements refer to package construction before this source-branch commit. The exact pinned prior proof dependencies remain inside the ZIP for offline recovery. No expanded duplicate source tree, executable binary, large regenerable ledger or cache is added.

This operation adds a new source branch only. It creates no PR, merge, tag, release or release attachment. Any later research PR merge or external research release requires separate consolidated approval.
