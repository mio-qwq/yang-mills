# Charge-conjugation refinement: independent review

2026-10-17 UTC. AI-assisted mathematical review and exact symbolic checks; not human peer review or formal verification. No novelty claim.

## Result

The refinement is correct. For SU(N), N >= 3, the dimension-six antisymmetric W4 quotient splits into C-even dimensions **2 off shell / 1 on shell**, and C-odd dimensions **4 off shell / 4 on shell**. For SU(2), the C-even dimensions are also 2/1 and the C-odd sector is zero. These conclusions use the same local polynomial and gauge-invariant-current conventions as the reviewed classification.

## Transformation proof

On anti-Hermitian matrices define C(X)=-X^T. This is a real-linear involutive Lie algebra automorphism: [C(X),C(Y)]=-[X,Y]^T=C([X,Y]). Since C commutes with ordinary differentiation, F(C(A))=C(F(A)) and D_{C(A)}C(T)=C(D_A T). Every covariant curvature jet therefore transforms by the same color involution, with its spatial indices unchanged.

The quadratic trace pairing is even:

tr(C(X) C(Y)) = tr(YX) = tr(XY).

A cyclic cubic trace transforms by reversal and a minus sign:

tr(C(X) C(Y) C(Z)) = -tr(ZYX) = -tr(XZY).

Thus f(X,Y,Z)=tr(X[Y,Z]) is even, while d(X,Y,Z)=-i tr(X{Y,Z}) is odd. The factor -i defines a real trilinear form on anti-Hermitian matrices and does not change the sign. Charge conjugation here is a linear field transformation on real observables, not an antiunitary operation conjugating their numerical coefficients. For SU(2), the symmetric cubic invariant vanishes (equivalently C is inner), so no new odd channel occurs.

## Descending to the quotient

The only color invariant at weight-five current order is the quadratic pairing of F and D F; hence every such gauge-invariant current is C-even. Weight-four curl potentials are also quadratic and C-even. Ordinary divergence and curl commute with C. The full Yang–Mills equation J_mu=D_nu F_nu_mu transforms covariantly by C, so its differential ideal is C-stable. Consequently both off-shell and on-shell quotients split into even and odd eigenspaces.

All added symmetric cubic representatives are C-odd. Their dimension is four both before and after imposing the equations, as established by the exact constant-Cartan-curvature tests in the extension review. There are no C-odd currents whose divergences could remove them. The original quadratic channel and possible alternating cubic channel are C-even; the latter has zero antisymmetric W4 multiplicity. The current divergence ranks 9/5 therefore subtract entirely from the even density multiplicities 11/6, giving 2/1. The odd density multiplicity remains 4/4.

## Wilson action and relevance to rotation restoration

For lattice links U, charge conjugation is U -> U* (entrywise complex conjugation), consistent with exp(A) -> exp(-A^T). Any ordered plaquette product transforms to its entrywise conjugate. Hence Re tr(U_p) is unchanged, and the usual Wilson plaquette action sum_p [1 - (1/N) Re tr(U_p)] is C-even. Product Haar measure is invariant under this group automorphism as well.

Spacetime rotations and their infinitesimal variations commute with this color transformation. Thus rotation variations of a C-even action belong to the even sector. In a regulator, renormalization prescription and observable/source sector preserving C, counterterms for that sector can and should be chosen C-even; the four new C-odd representatives are excluded by this symmetry. They do not themselves supply additional obstructions in the physical C-even rotation-restoration problem.

The qualification matters: arbitrary allowed insertions, C-breaking sources or a C-breaking prescription need not have this property. Nor does exclusion of these four classes solve rotation restoration: the surviving even quotient and the analytic/continuum arguments still require treatment. This statement concerns the action and symmetry-preserving local counterterm problem, not a claim about every selected infinite-volume state.

## Independent exact checks

`check_charge.py` uses explicit noncommuting traceless anti-Hermitian 3x3 matrices and exact symbolic arithmetic. It checks the involution, bracket automorphism, pairing parity, f parity, d parity, nonzero f/d witnesses, and Wilson real-trace invariance on a nonreal SU(3) trace. It passes; the witnesses have f=24 and d=26. The displayed general identities supply the all-N proof; matrix tests are supplementary consistency checks.
