# Spectral residue positivity and ultraviolet rigidity

Source-only analytic research snapshot, 19 October 2026. These are conditional scalar Gaussian spectral-class results. They do not establish the spectral hypotheses for an interacting Yang–Mills field, a mass gap, or any main-problem conclusion. No novelty, human peer-review, formal-verification, or hosted-CI claim is made.

## Exact assumptions and implications

`spectral-rp-residues-20261019/RESULT.md` proves masswise nonnegative residues from full complex reflection positivity under explicit conditions: a positive locally finite mass measure; measurable real W4-invariant polynomial numerators with a common finite degree bound; absolute coefficient integrability after every positive damping exp(-epsilon sqrt(s)); and actual tempered-distribution convergence of mass cutoffs after polynomial contact counterterms. Reflection invariance and positive type are hypotheses about the total Gaussian covariance.

The proof derives an absolutely convergent separated reflection formula, localizes tangential momentum, and proves an elementary signed-Laplace-measure positivity lemma. A countable dense set and continuity produce one mass-null set valid for all tangential momenta and finitely many mirrors. Merely describing a distribution as tempered or locally renormalized does not replace these hypotheses. Contributions with the same mass are aggregated before the positivity conclusion.

`spectral-uv-rotation-20261019/RESULT.md` assumes the separated residue formula and simultaneous masswise positivity at the coordinate and diagonal representative mirrors. For one nonzero nonnegative smooth compact positive-half-space profile f and f_d(x)=f(x/d), the bound B(theta f_d,f_d)=o(d^-2) forces P_s to be constant modulo q+s almost everywhere. Contact-cutoff convergence then gives O(4) invariance away from the origin. Anisotropic contact terms can remain. The little-o threshold is sharp within the stated class; O(d^-2) alone is insufficient.

The explicit positive radial example has multiplier q^2 integral_e^infinity [(q+s)(log s)^2]^-1 ds and reflected pairing asymptotic K_f/[4 log^2(1/d)]. Its unbounded spectrum is intentional. This verifies the specified fixed-profile asymptotic only, not every bound in an external Yang–Mills test class. The proof handles mass integration with positivity and Fatou's lemma rather than an unverified spectrum-wide dominated-convergence step.

## Dependencies and provenance

The previously audited low-degree quotient and Gaussian reflection-positivity arguments are archived at
[`results/gaussian-numerator-threshold/gaussian-numerator-minimality-audit-20261019/RESULT.md`](https://github.com/mio-qwq/yang-mills/blob/fcd22174fcc43a8d1826206c30929ede01105c97/results/gaussian-numerator-threshold/gaussian-numerator-minimality-audit-20261019/RESULT.md).
Its recorded source SHA-256 is b61ffd1d6f4e471f338b96bb8cf0c9c0d1543a366769fb4277601e67ac6536f1.

Both polished analytic proofs were independently read and approved before this freeze. Their arguments, hypotheses, and limitations are preserved verbatim. Creation-time remarks about local work are historical. The original `SOURCE_MANIFEST.json` remains an immutable provenance record: its preliminary root derivation is intentionally not bundled because the polished proofs supersede it. Local paths are provenance identifiers, not executable dependencies. The spectral residue report is the sibling `spectral-rp-residues-20261019/RESULT.md` in this package.

## Verification

Run `python verify_sources.py` for exact file sizes and SHA-256 checks. `PACKAGE_MANIFEST.json` covers every payload except itself; `SHA256SUMS` includes the manifest and excludes itself. These are source-integrity checks, not numerical or formal verification of functional analysis. No new spectral numerical checker or hosted-CI run is asserted. No papers, binaries, cache files, provisional derivations, or remote publication objects are included.
