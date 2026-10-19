# Variable-degree scalar spectral rigidity: extension and boundary

19 October 2026. A compact source-only follow-up preserving the final theorem, exact finite algebra checker, and independent analytic review byte for byte.

## Result and precise scope

A common finite degree bound is unnecessary for the stated scalar spectral-class theorem. The numerators must still be finite polynomials at almost every mass, with measurable coefficients and a positive locally finite reference measure. The theorem requires a finite-stage tempered-distribution limit modulo local contacts, reflection positivity, and a locally controlled signed-residue Laplace representation.

One sufficiently strong exponential damping bound on each compact tangential annulus suffices initially. The proof extracts masswise nonnegative residues, then recovers all separated reflected forms and every positive damping parameter by monotone convergence. If the covariance has local distribution order m, genuine quotient degrees obey D(s) <= m+2 almost everywhere, without imposing the ultraviolet bound. Together with the stated ultraviolet scaling assumption, the earlier rotation conclusion modulo contacts follows.

The examples separate unbounded contact-representative degree from genuine quotient degree, show why coefficient damping alone fails, and show that excellent separated damping does not itself give a distributional extension through coincidence.

This does not construct a Yang-Mills field, establish the spectral representation for interacting or tensor fields, or cover infinite-degree numerators at a fixed mass or unjustified conditional spectral sums. No claim of a mass-gap solution, publication novelty, external human peer review, or formal proof verification is made.

## Contents

- spectral-degree-boundary-20261019/RESULT.md: complete theorem, hypotheses, proofs and boundary examples
- spectral-degree-boundary-20261019/check_exact.py and CHECKS.json: exact finite algebra checks supporting the examples
- spectral-degree-independent-audit-20261019/RESULT.md: independent analytic review, including late damping, exceptional sets, distribution order, and all boundary examples; it identifies the exact reviewed source hash

The checker verifies selected finite polynomial identities. It does not certify analytic limit arguments. Those arguments require the proof and mathematical review in the two manuscripts.

## Reproduction

Use Python 3.9 or later and SymPy. The checked environment used Python 3.12.14 and SymPy 1.14.0. Dependencies are not bundled or installed automatically.

    python verify_sources.py
    python verify_sources.py --run-checks

The second command runs the algebra checker under ordinary and optimized Python and rechecks all exact package bytes, including its generated CHECKS.json. Checks use explicit failure logic active under -O. LOCAL_VERIFICATION.json records local results; it is not hosted CI.

## Provenance

This is an additive follow-up to the spectral-residue-uv-rigidity source archive at commit a3526bbae6058087772602f61ad7af7d28345130 of mio-qwq/yang-mills. The earlier companion proofs remain in that archive. Absolute workspace paths in the immutable manuscripts identify original sources; matching component directory names are preserved here. Package creation itself changes no repository, PR, merge, tag, or release.
