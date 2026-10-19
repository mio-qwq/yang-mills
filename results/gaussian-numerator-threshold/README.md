# Restricted Gaussian numerator threshold

Source-only research checkpoint, 19 October 2026. This is a restricted scalar Gaussian spectral result, not a Yang–Mills construction or a resolution of its full source hypotheses. No novelty, human peer-review, or proof-assistant verification claim is made.

## Result and boundary

`gaussian-numerator-minimality-audit-20261019/RESULT.md` proves, in four dimensions for a nonnegative real signed-permutation-invariant polynomial numerator P and spectral covariance P(p)/|p|², that full complex reflection positivity at the sixteen signed-permutation mirrors forces every degree-below-eight noncontact class to be constant. Anisotropic contact terms are allowed. Degree eight is sharp for anisotropy away from the origin, witnessed by P=(sum p_i⁴)².

The same proof classifies homogeneous degree-eight residue-positive classes modulo contacts as alpha*Q4²+gamma*e4 with alpha>=0 and 0<=gamma<=48*alpha. This is not a classification of arbitrary mixed-degree-eight numerators. A final scaling consequence remains within the finite polynomial-numerator class. The analytic reflection-positivity and Gaussian arguments are in the proof; the checker verifies finite polynomial identities only.

All five original source and verification files are copied byte-for-byte. `SOURCE_MANIFEST.json` retains historical source-input paths and hashes. Those candidate/background files are provenance inputs, are not needed to reproduce the self-contained proof and checker, and are deliberately not duplicated here. Original local absolute paths and local-work status statements are historical provenance. This checkpoint does not modify any previously published archive.

## Reproduce

Python standard library only. From this directory, run:

    python gaussian-numerator-minimality-audit-20261019/check_exact.py

The checker writes its adjacent `CHECKS.json`; run on an extracted copy to preserve the frozen tree. It uses assertions and explicitly rejects Python -O and -OO at startup with exit code 2. Those modes are expected rejections, never successful verification. `REPRODUCTION.json` records fresh-copy normal execution and both rejection checks, including byte equality of the generated normal result. `SHA256.json` covers every other bundle file.

There are no binaries, dependency caches, large execution logs, or archive files inside the source tree. The analytic proof, not the finite computation, carries the universal Gaussian and reflection-positivity claims.
