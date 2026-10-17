# Independent assistant review: SU(N), N >= 3, dimension-six extension

Date: 2026-10-17 UTC. Reviewed candidate `/tmp/ym-root-20261017/su-n-extension.md` and its explicit symmetric-cubic representatives. This is an AI-assisted mathematical and computational review, not human peer review or formal proof-assistant verification. The frozen SU(2) packet was not modified.

## Verdict

No blocking flaw found in the proposed extension under the same precise local polynomial, constant-coefficient, gauge-invariant curvature-jet conventions as the SU(2) theorem. The antisymmetric W4 quotient dimensions are 6 off shell and 5 modulo the full Yang–Mills differential ideal, for every N >= 3. Four added independent classes are the displayed symmetric-color cubic representatives. This establishes a bounded local operator-algebra result only. Historical priority remains unassessed.

## Independent computational checks

The independently written `check_symmetric_cubic.py` constructs all 384 signed-permutation actions on the six-dimensional two-form representation, and computes the symmetric-cube character through (chi(g)^3 + 3 chi(g) chi(g^2) + 2 chi(g^3))/6. Its inner product with the two-form character is exactly 4.

Separately, it constructs a 56-column linear system for cubic polynomials satisfying all four coordinate-reflection equations and the two component stabilizer swaps. The matrix rank is 52, leaving dimension 4. The four proposed representatives satisfy the system and have rank 4. Reversing the relative minus sign in the fourth representative fails the system, providing a negative test. This checker does not import the root's orbit-enumeration code.

Also reran characters2.py, independent_characters.py, check_certificate.py and validate_equivariance.py from the frozen SU(2) packet; all passed. The output is saved separately in reproduced_su2_checks.txt. Minor determinants remain (586,990,585) off shell and (579,149,336) on shell modulo 1009, ordered as current/divergence/curl.

## Color tensors

Here is a precise route to the invariant-tensor assertion. Complexify to sl_N and embed it in End(C^N), with equivariant projection X -> X - tr(X)I/N. An invariant multilinear form on sl_N extends by this projection to End(C^N). The degree-two and degree-three invariant contraction theorem (equivalently Schur–Weyl centralizers on two and three tensor factors) says these forms are spanned by permutation contractions, hence products of traces indexed by permutation cycles. On traceless arguments, every permutation having a singleton cycle vanishes. At degree two only tr(XY) remains. At degree three only tr(XYZ) and tr(XZY) remain. Their sum and difference give the symmetric d and alternating f tensors, with no mixed-symmetry invariant. For N >= 3 both are nonzero and independent; the alternating one is the nonzero Lie bracket paired with the trace form. For the symmetric one take H=diag(i,i,-2i,0,...,0): tr(H^3)=6i. Multiplication by -i makes this symmetric form real on anti-Hermitian arguments. No new rank-three invariant appears at N=3 from epsilon tensors: contractions of a paired upper/lower epsilon are already permutation contractions.

## Full nonlinear equations and divergences

At weights 4 and 5, only quadratic color invariants occur, so potentials and currents retain the dimensions 7 and 16 off shell (7 and 12 on shell). At weight 6 the symmetric cubic channel adds exactly four density components. Normal-gauge jet coordinates and the affine principal EOM constraints used in the SU(2) proof apply to any su_N: their top spatial maps do not depend on the color algebra. Nonlinear commutator corrections use f, whose antisymmetric W4 density multiplicity is zero. They cannot introduce a d-color correction or relation. Thus density multiplicities are 15 and 10.

The seven curl images remain independent: the same fixed-color evaluations apply, and the trace pairing on a nonzero real anti-Hermitian H is nonzero. Their divergences vanish identically. Consequently divergence ranks are at most 16-7=9 and 12-7=5. The existing nonzero minors give matching lower bounds using fixed-color fields. For the on-shell tests, null-plane-wave sums in one fixed color direction solve the full nonlinear equations exactly, rather than only their linearization. Hence every member of the full EOM differential ideal vanishes on those tests. This proves the ranks 9 and 5 without a covariant Poincare lemma or an assumption that a linearized quotient equals the nonlinear one.

There is also a direct check that all four added cubic classes survive the full quotient. Let f_{mu nu} be an arbitrary constant real antisymmetric matrix and set A_mu(x)=-(1/2) f_{mu nu} x_nu H. Then F_{mu nu}=f_{mu nu}H, D F=0, and the exact Yang–Mills equations hold. Every gauge-invariant dimension-five current is quadratic of type F D F and vanishes identically on these fields, as does its divergence. Every EOM-ideal expression vanishes. The four proposed cubic components reduce to four independent cubic polynomials in the six freely chosen f components, multiplied by the nonzero d(H,H,H). Thus no nonzero combination of them can be an EOM term plus a divergence.

Finally, the quotient dimensions follow from 15-9=6 and 10-5=5. The absence of cubic f in the target ensures the quadratic sector and the new symmetric cubic sector do not acquire a hidden nonlinear mixing relation at this weight.

## Presentation recommendations

State the color invariant argument rather than merely asserting that f and d exhaust all tensors. Add the constant Cartan-curvature solution test above: it makes the survival of the four new classes transparent. Keep the exact local-algebra conventions, the limitation to gauge-invariant divergence currents, and the distinction between AI-assisted checking and human peer review. No claim of novelty, global existence, continuum rotational invariance, or mass gap is supported by this review.
