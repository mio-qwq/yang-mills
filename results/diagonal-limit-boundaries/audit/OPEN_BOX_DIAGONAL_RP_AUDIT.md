# Independent free-boundary reflection-positivity audit

Result: PASS for the mathematical theorem and its stated limiting consequences.

Audited file: `ym-limit-next/OPEN_BOX_DIAGONAL_RP.md`
Final SHA-256: `694bd5050b708155f2fd4489a117dc8c3d6010de0f32265c1a68e7424817c2d0`
Date: 2026-10-17 UTC

1. The integer gap x0-x1 changes by at most one along an edge, so the three link classes exhaust the links and are disjoint. Reflection fixes plane links pointwise and preserves canonical edge orientation. This remains valid for arbitrary retained cubical subcomplexes.
2. The listed plaquette vertex gaps are correct. Exactly the (0,1) plaquettes based at gap zero cross both strict sides; they are individually reflection invariant. Their positive two-edge path A and reflected path B produce standard plaquette holonomy AB^{-1}. The real SU(2) trace is invariant under orientation reversal, so all noncrossing negative terms equal reflected positive terms.
3. Tensor-power decomposition of the fundamental character has nonnegative multiplicities. Nonnegative beta thus gives nonnegative character coefficients. Evaluation of dimension sums at identity gives sum c_j d_j=e^beta; the resulting uniform convergence and matrix-entry absolute bounds justify the finite-cutoff procedure, including beta=0.
4. Haar factorization into X,Y,z is exact. Fixed-plane variables are held common, rather than independently doubled. For each fixed z, the kernel expansion yields the asserted integral of a sum of absolute squares with nonnegative coefficients. F need only be bounded measurable: Fubini and bounded domination suffice. Gauge invariance is unnecessary.
5. The crossing paths contain no plane links; arbitrary sharing of positive links among several crossing paths causes no issue because their features are multiplied before integration. Uniform convergence of a finite product of uniformly bounded kernel cutoffs passes the nonnegative form to the exact Wilson measure, whose normalizer is strictly positive.
6. Every finite reflected moment is nonnegative, so any existing limit remains nonnegative under the stated varying normalizations. On exhausting free boxes, compactness of the countable product of compact link groups gives subsequential local weak limits after identity extension. For fixed bounded continuous local halfspace functions, the reflected product is also bounded continuous and local, so positivity passes to these limits. No extra unproved Gibbs uniqueness or boundary-independence claim is used.

The proof is a verification of a positivity mechanism, with no novelty claim. The periodic/free comparison and continuum construction remain explicitly open. This mathematical audit did not independently re-research the external bibliographic statements; the final documentation-only revision does not alter the audited argument.

No proof file or external service was changed by this auditor.
