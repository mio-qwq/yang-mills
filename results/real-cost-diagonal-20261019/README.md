# Four-axis diagonal-reflection-positivity obstruction checkpoint

This additive source archive contains the accepted analytic obstruction, exact algebra checks, and independent audit. It is a source-branch checkpoint, not a release.

## Result and strict scope

For the specified four-axis angular-central-Gaussian mixture, every positive mixture weight 0 < epsilon <= 1 fails diagonal reflection positivity for all b,tau > 0. The parameter density is supported in [ell,L] with 0 < ell < L < 1. Every sufficiently large finite tangential frequency along (e1-e2)/sqrt(2) gives a negative Hankel form for the mirror normal (e1+e2)/sqrt(2); W4 symmetry gives the other diagonal mirrors.

A genuine real smooth compactly supported positive-half-space countertest exists analytically, but its coefficients, support, and numerical frequency threshold are not computed. The previous coordinate-RP repair remains valid; this theorem excludes that same family as a simultaneous coordinate-and-diagonal repair. It proves no general W4 rigidity, rotational reconstruction, interacting Yang-Mills construction, or mass gap. The supplementary finite-b pole lemma is not needed for the main theorem.

## Verify and reproduce

- Archive: ym-diagonal-rp-obstruction-20261019.zip
- Bytes: 186043
- SHA-256: 6265bc42d9dc442cefe8b187e5759453c518be90d87383d7143ffbebe360128f
- Requirements: Python 3.10+ and SymPy 1.14.0. Source proof dependencies are included offline; Python and SymPy runtimes are not bundled.

First run `sha256sum -c SHA256SUMS`, then extract the ZIP and read its README.md. From the extracted package directory:

    python reproduce.py --with-dependency-replay
    python -O reproduce.py --with-dependency-replay
    python test_package.py
    python -O test_package.py

The acceptance record reports clean ordinary/optimized full replay, 22 primary and 22 independent exact identities, residue-corruption rejections, the nested coordinate/W4/axial dependency chain, and all 11 package-corruption controls in both modes. A deterministic rebuild is byte-identical. The historical audit pins an earlier 17353-byte proof; an additive independent final-version review verifies its exact prefix in the final 18291-byte proof and the 938 appended bytes. Both original records remain unchanged.

These checks support algebra and provenance; they do not formally verify the analytic proof or compute an explicit compact countertest. The work is AI-assisted and makes no external peer-review or proof-assistant-verification claim.

## Provenance and archival boundary

VERIFICATION.json is an unchanged copy of the pre-archive local acceptance record. Its local-only scope describes packaging, before this separate additive source commit. This directory adds only this README, that receipt, the unchanged ZIP, and SHA256SUMS. The manifest covers the other three files.

Existing source paths, branches, main, tags, release assets, and historical receipts are preserved. This archival operation does not create a PR, merge, tag, or release. A research merge or release requires separate batch approval.
