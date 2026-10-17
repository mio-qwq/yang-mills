# Independent review of corrected L=1 proof and general-depth theorem

Date: 2026-10-17. This continues the independent audit recorded at `/tmp/ym-remote-prism-review-20261017/REVIEW.md`.

## Frozen inputs

1. `/workspace/scratch/477a3dcb7024/remote-prism-L1-20261017/TRANSFER_PROOF_V2.md`
   SHA-256: `282792ef8a56d4cc34b66c4b9d573a776d363f4485cc79e33ca9d4b7c354a227`
2. `/workspace/scratch/477a3dcb7024/remote-prism-general-L-20261017/THEOREM.md`
   SHA-256: `67e19b1dcd4ebe037f9ea0deba0ef43c9c983c759f04ba1b789331475fdfa626`

Both hashes match the supplied frozen values. Neither source was edited.

## Verdict

The corrected V2 resolves the sole false auxiliary assertion identified in the first audit. The general-L theorem, including the explicit rational beta-star and its endpoint, is supported. No substantive gap or new correction was found. The conclusions are finite-volume and small-positive-coupling only.

This review checks the analytic argument and independently runs exact rational/geometric controls; it does not claim to have expanded every finite-lattice integral monomial to arbitrary order.

## V2 comparison

The mathematical change is precisely the restriction of transfer-operator positivity to sufficiently small nonnegative beta. The remaining changes are a heading/status note and review provenance. The earlier trace-norm, spin-network, spectral-subtraction and periodic-trace audit applies unchanged. Odd fundamental winding loops at negative beta therefore no longer contradict the wording.

## Transfer expansion at n=8

The only spatial-size-dependent fact used in the leading transfer coefficient is the graph classification: the nearest-neighbor three-torus is simple, has girth four, and every four-cycle is elementary. This remains true at n=8. A four-step closed walk lifts to the cubic lattice because a nonzero winding displacement has absolute coordinate at least eight, whereas four unit steps have total length four. A simple closed four-step walk on the cubic lattice must use two different axes, each once in either sign, and is an elementary square. There are no length-one or length-two simple cycles, and no length-three cycles. An occupied invariant network of leading degree at most four must therefore be exactly a fundamental square as before. Winding loops start at degree at least eight, strictly above four.

The general theorem's direct trace-norm argument correctly includes the single-link Peter–Weyl multiplicity d_j^2. Its order-m trace norm is sum_j d_j N_(m,j)/(2^m m!)=1/m!, giving entire trace-norm convergence before the analytic nonzero normalization c_0. This is stronger and more explicit than a pointwise eigenvalue estimate. Finite products and the fixed gauge projection preserve it. The spectral and finite-period arguments are unchanged, and do not require n>=11.

Independent finite graph enumeration found all 12 distinct simple four-cycles through the origin at n=8, and matched every one to an elementary square. The same control passed at n=11. The lifting argument, rather than that finite enumeration, establishes the result for all n>=8.

## General geometry, without relying on samples

The k interval is nonempty because n>=6L+5 implies 3L+2<=n-3L-3. Set D=2L+1.

- The cross-pair coordinate difference is n-1-2L=n-D. The short periodic separation is D, because n-D>=4L+4>2L+1=D. Thus there is exactly one shortest direction. The other orientation of the same periodic circle is explicitly higher order.
- For theta p,p the time separation is s_p=n-1-L-k>=2L+2=D+1, and its reverse is k+L+1>=4L+3>=D+1.
- For theta q,q the time separation is s_q=k-L>=2L+2=D+1, and its reverse is n-k+L>=4L+3>=D+1.

Hence the self entries start no earlier than beta^(4D+4), while each cross entry has leading beta^(4D)/(4*256^D). The mixed finite-period remainder has order 4n, also strictly above 4D. No omitted periodic path can alter the leading coefficient.

Both source coordinate differences equal the displayed positive s_p,s_q. The sources therefore lie in the strict representative half. Further, k>=3L+2>L and k<=n-3L-3<n-1-L; the other coordinates are exactly L or n-1-L. All endpoints have belt depth at least L, and at least one endpoint realizes that depth exactly. Plaquettes vary only in directions 2 and 3, with bases zero and extent one in those directions, so none of their links wrap for n>=8, even at L=0 where a source is situated on the 0/1 seam boundary. Reflection swaps coordinates 0 and 1 without changing the (2,3) plaquette orientation. Its antilinear action causes no additional sign or conjugation issue because SU(2) plaquette traces and the coefficients of F are real.

Translation invariance makes the one-point means of p and q equal exactly, and does likewise after reflection. Consequently the uncentered reflected form is exactly its connected form. Its leading coefficient is

  -2*(1/4)*(1/256)^D = -2^(-(8D+1)) = -2^(-(16L+9)).

Its degree is 4D=8L+4. The O(beta^(4D+1)) error accounts for cross-pair corrections; the self terms are later.

## Boundary case L=0,n=8

The admissible values are k=2,3,4,5. The two cross entries have D=1 with reverse separation seven. The self separations and their reverses are at least two. Thus the cross coefficient is beta^4/1024 per pair, and the total is -beta^4/512 with self terms O(beta^8). Source plaquettes on x0=7 or x1=0 do not themselves wrap, since all their links point in spectator directions. Their belt depth is exactly zero. This boundary case is consistent with every stated algebra and geometry condition.

At L=1 the general hypotheses reduce exactly to n>=11 and 5<=k<=n-6, so the extension agrees with V2.

## Complex analyticity and the explicit interval

Let S be the real Haar-measurable action sum, with |S|<=M=6n^4, and H=(Theta F)F, with |H|<=4. H is a fixed function of the links independent of the complex coupling z; antilinearity of Theta therefore does not spoil holomorphy of its expectation. On the closed disk |z|<=r=1/(4M),

  |Z(z)-1|<=e^(1/4)-1<=1/3,
  |Z(z)|>=2/3,
  |integral H e^(zS)|<=16/3.

Thus g is holomorphic on a neighborhood of the closed disk and bounded there by 8. Using 12 instead is conservative and valid. The local transfer-derived expansion along positive real beta fixes the Taylor coefficients of this same holomorphic g by uniqueness: coefficients below h vanish, and the degree-h coefficient is -c. Cauchy's estimate yields the stated tail bound; it does not require the transfer perturbation series itself to have radius at least r.

With beta_star=c*r^(h+1)/48,

  beta_star/r=c*r^h/48<1/2,
  24*beta_star/r^(h+1)=c/2.

Therefore the bound applies throughout 0<beta<=beta_star, including equality. Multiplication by beta^h preserves positivity. Since g(beta) is real for real beta,

  g(beta)<=-c beta^h+|g(beta)+c beta^h|<=-(c/2)beta^h<0.

The denominator and powers of r are correct; there is no missing factorial in Cauchy's Taylor-coefficient estimate. The constant is very conservative, but that is not a validity defect.

For L=0,n=8, exact arithmetic gives r=1/98304 and beta_star=1/225614572159760555100365389824. This is a mathematical interval, not a useful numerical coupling claim.

## Independent controls and limits

`check_controls.py` uses exact Python rational arithmetic and finite graph enumeration. `CONTROL_RESULTS.txt` records success for 612 admissible (L,n,k) choices: L=0 through 12 and the first nine admissible n for each L. It checks belt depth, strict half support, both cross distances, both directions of both self distances, exact coefficient identities, nonempty k ranges, and the rational Cauchy inequalities. These samples support implementation accuracy; the symbolic inequalities above cover every integer allowed by the theorem.

No external service was changed. No source was changed. No uniform-in-volume, fixed-coupling, fixed-physical-source, continuum, novelty, or mass-gap conclusion is warranted by this review.
