# Finite positive prolate ACG-axis rigidity checkpoint

This additive source-branch checkpoint preserves the accepted analytic theorem, independent audit, exact algebra checkers, and complete pinned source-dependency chain.

## Result and strict scope

For a reflection-invariant finite positive mixture of prolate angular-central-Gaussian (ACG) axis densities, with a nonnegative isotropic background, reflection positivity at a mirror requires every active axis to be normal or tangent to that mirror. This is a necessity condition; normal/tangent geometry alone is not sufficient.

An active oblique axis forces failure for every b,tau>0, however small its positive mixture weight, at every sufficiently large finite tangential frequency in the specified direction. A real smooth compactly supported positive-half-space spacetime witness exists analytically. Its numerical coefficients and frequency threshold are not computed.

Within this finite positive prolate-ACG class, invariance and reflection positivity at every coordinate and diagonal mirror leave only the constant density. The main theorem has compact parameter support strictly inside (0,1); an independently reconciled extension allows probability Borel parameter measures on (0,1), still with finitely many axes. It makes no arbitrary-continuous-axis, arbitrary-angular-density, signed-mixture, oblate-parameter, interacting Yang-Mills, or mass-gap claim.

## Verify and reproduce

- Archive: ym-finite-positive-acg-axis-rigidity-20261019.zip
- Bytes: 218028
- SHA-256: 273ea8168a922477bb33208b7d7ef7b4b256f3ba962421d563a35153b5f92c08
- Requirements: Python 3.12 and preinstalled SymPy 1.14.0. All research inputs are included offline; language/library runtimes are not vendored.

Run `sha256sum -c SHA256SUMS`, extract the ZIP, and read its README.md. From the extracted package directory:

    python -B reproduce.py --integrity-only
    python -B reproduce.py --with-dependency-replay
    python -B -O reproduce.py --with-dependency-replay
    python -B test_package.py
    python -B -O test_package.py

The accepted clean ordinary/optimized full replays pass both new independent 20-identity suites, sign-corruption regressions, all inherited dependency checks, and sixteen package-corruption controls. Repeated builds and clean-extraction rebuilds are byte-identical. The exact final primary proof and independent audit hashes are pinned in VERIFICATION.json and the packaged reconciliation receipt. The unaccepted oblate candidate is excluded.

Symbolic tests verify algebra and package provenance; they do not machine-verify the analytic/topological proof. The work is AI-assisted and makes no external human peer-review or proof-assistant-formalization claim.

## Provenance and archive boundary

VERIFICATION.json is the unchanged pre-archive checkpoint acceptance summary. Its remote_changes=false field describes the earlier local packaging stage. This directory adds exactly four files: the unchanged ZIP, this README, that summary, and SHA256SUMS covering the other three files.

Existing archives, files, branches, main, tags, release assets, and PR state are preserved. This operation creates no PR, merge, tag, or release. A research merge or release requires separate batch approval.
