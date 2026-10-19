# Independent audit: bounded scalar reflection-positive kernels

Date: 19 October 2026.

## Verdict

**PASS for the stated scalar theorem. No substantive analytic gap was found in the reviewed proof.** The argument establishes that a Hermitian scalar function on `R^4 \ {0}`, continuous there and bounded in a punctured neighborhood of zero, is a nonnegative constant off the origin if its reflected point matrices are Hermitian positive semidefinite for the four coordinate normals and the two normals `e_0+e_1`, `e_2+e_3`.

This conclusion is mathematical review, not machine verification or external peer review. It does not establish the separate Yang–Mills rotation theorem, applicability to curvature components or a rotation defect, existence of a Wilson continuum state, or a mass gap.

One convention clarification was requested and has been added by the author: the real-only alternating example `1+h` is **not ordinary positive type**. It refutes the explicitly weakened assumptions of the note, which do not separately require ordinary positive type; it must not be presented as a counterexample to an already assumed genuine continuous positive-type covariance. See Section 8 below.

Reviewed author file: `/workspace/shared/bounded-rp-kernel-test-20261019/RESULT.md`. The final reviewed snapshot, including the rotation-defect warning, the non-positive-type clarification, and the continuous-positive-type averaging corollary, has SHA-256 `9b9e2eaef325d1b527407be1174f91da1fa240251b051b4a356e47cf8746c8a7`. No author files were modified during this audit.

## 1. Reflection invariance and local-to-global boundedness

These steps are correct and do not import ordinary positive type.

For any `z` in the tested open half-space, choose `x,y` there with `x-r_n y=z`. Hermiticity of the two-point reflected matrix gives `C(z)=conj(C(-r_n z))`; the separately stated covariance symmetry gives `C(z)=C(r_n z)`. Covariance symmetry transfers the identity to the other half-space, and continuity handles its nonzero boundary. Applying all coordinate reflections gives evenness, hence real values.

The two equal diagonal entries of the reflected matrix at the points `(t n+z)/2` and `(t n-z)/2`, with `z` tangential, are `C(t n)`. Its positivity therefore yields `C(t n)>=0` and `|C(t n+z)|<=C(t n)`.

For a tested pair `(i,j)`, the applications to the diagonal normal and then to `e_i` indeed give

`0 <= C(t e_i) <= C((t/2)(e_i+e_j)) <= C((t/2)e_i)`.

Iteration bounds the axis by the one fixed local bound, rather than by a bound depending on `t`. The selected two pairs cover every coordinate; any nonzero point can then be bounded using one of its nonzero coordinates. Thus the global boundedness needed later is genuinely proved from the stated local assumption.

## 2. The bounded GNS representation is justified

The direct argument in the note successfully supplies the contraction condition that must not be silently omitted from the published distributional representation theorem.

A precise way to read the construction is to start on the free finite linear span of symbols `v_(t,z)`, equipped with the positive semidefinite kernel form, and define shifts there before passing to its null-space quotient. This avoids any apparent circularity concerning well-definedness. For a fixed formal vector `v=sum c_i v_(t_i,z_i)`, global boundedness gives

`0 <= b_k = ||A_a^k v||^2 <= M (sum |c_i|)^2`

for every nonnegative integer `k`. Symmetry gives

`b_k = <v,A_a^(2k)v>`, hence `b_k^2 <= b_0 b_(2k)`.

The iterated inequality displayed in the note is correct. Letting the iteration depth tend to infinity gives `b_1<=b_0`. When `b_0=0`, the first Cauchy–Schwarz inequality gives `b_1=0` directly. Null vectors are therefore preserved, and the descended shifts are contractions. Each is bounded and symmetric on the completed Hilbert space, hence self-adjoint. The identity `A_a=A_(a/2)^2` makes each positive.

The semigroup is strongly continuous at zero: the squared difference of two shifted kernel vectors is a finite expression in values of `C` at strictly positive normal coordinates, so open-half-space continuity suffices. Uniform contractivity extends this to all Hilbert-space vectors. The self-adjoint contraction semigroup therefore has a nonnegative generator `H`.

Tangential translations are strongly continuous unitaries. They commute with all `A_a`, so they commute with the spectral projections of `H`; their mutually commuting generators and `H` possess the joint spectral measure used in the proof. This is strong commutation of bounded semigroup/unitary operators, not an unsupported claim that unbounded generators merely commute on a core.

The origin-vector construction also works. The vectors `v_t=v_(t,0)` are uniformly bounded; a sequence tending to zero has a weakly convergent subsequence in Hilbert space. For fixed `t>0`, test `v_t=A_(t-t_j)v_(t_j)` against a fixed vector. Strong continuity of the operator on that test vector and uniform boundedness of `v_(t_j)` give `v_t=A_t v_0`. It follows that `v_t` actually converges strongly to `v_0` as `t` decreases to zero. Consequently the representing positive measure is finite and its total mass is exactly `||v_0||^2=lim_(t down to 0) C(t,0)`.

An inner-product convention may reverse the sign of the tangential momentum variable. This has no mathematical effect; one can choose the unitary translation convention consistently or replace `p` by `-p` in the measure.

**Editorial refinement addressed:** the final version now explicitly defines shifts on the formal span, before quotienting by null vectors. This adds no hypothesis and does not alter the argument.

## 3. Origin extension and one common finite momentum measure

For a fixed tested normal, the finite Fourier–Laplace representation is valid throughout the positive half-space. Reflection invariance gives the corresponding formula with `|t|` on the negative half-space. At `t=0,z!=0`, continuity of the given function and dominated convergence identify the original boundary values with the same integral. Dominated convergence also makes this integral continuous at `(0,0)`. Thus the extension is proved rather than presumed.

For each positive Laplace parameter, the Cauchy density in the normal momentum has integral one and Fourier transform `exp(-lambda |t|)`. For parameter zero, its replacement is the unit point mass at normal momentum zero. Integrating these probability measures against the finite parameter measure gives a finite positive Borel measure on all momenta, with the asserted total mass.

The formula holds for every point of the continuous extension. Fourier uniqueness for finite measures therefore makes the measures produced from the different normals identical. Neither an extra Bochner-positivity assumption nor an unproved interchange involving infinite mass is needed.

## 4. Singular-axis removal in the two-dimensional lemma

The disintegration argument is valid. Two absolutely continuous marginals alone would not suffice, but the proof uses more than that.

The `q`-marginal away from zero is absolutely continuous by the `e_2` Cauchy-mixture representation. In the `e_1` representation, the marginal of the positive-parameter measure in the tangential `q` variable is dominated by this marginal of the original finite measure. That tangential parameter marginal is therefore absolutely continuous away from zero. On almost every such `q` slice, the conditional normal `p` measure has a density. Fubini's theorem then gives joint absolute continuity off the two coordinate axes.

In diagonal coordinates, each positive-parameter conditional measure has a density in `t`. At fixed tangential coordinate `s`, either coordinate axis is met at a single value of `t`; that conditional measure gives the intersection zero mass. The zero-parameter diagonal component is confined to `t=0`, which intersects the coordinate axes only at the origin. Thus all nonzero axis mass disappears.

This proves the decomposition `mu=a delta_0+f(p,q) dp dq`, with nonnegative integrable `f`. Any zero-parameter component in any of the three representations is confined to the origin: its supporting line has zero two-dimensional Lebesgue measure. The positive-parameter components cannot charge the origin, because their normal conditional measures have densities. They are consequently dominated by the absolutely continuous part, and their tangential marginals are absolutely continuous. This last observation justifies the subsequent disintegrations against Lebesgue measure, including in diagonal coordinates.

## 5. Monotonicity and the positive-measure tail window

These two delicate parts are correct in the current version.

For almost every fixed tangential coordinate, the density in the positive normal coordinate is a positive mixture of decreasing Cauchy densities. This implies that each of the two distributional partial derivatives of `f` is nonpositive on the open positive quadrant. Convolution with a nonnegative compactly supported mollifier is smooth and coordinatewise decreasing on compact interior regions. At Lebesgue points the mollified functions converge to `f`; passing to the limit proves the order inequality for every pair of Lebesgue points whose two coordinates are strictly ordered. No arbitrary choice of exceptional slices is required.

If `f` has positive mass, the positive-parameter diagonal measure also has positive mass. A countable cover by bounded transverse windows and compact parameter intervals contained in `(0,infinity)` provides one window carrying positive mass. Absolute continuity in `s`, followed by a positive level set of the parameter-mass density, gives a set `E` of positive Lebesgue measure and constants `alpha,beta,m` exactly as used in the note.

For each Lebesgue point `(p,q)` in the positive quadrant, put `r=max(p,q)`. The rectangle

`(sqrt(2)r+R+1, sqrt(2)r+R+2) x E`

has positive planar measure. The lower-bound exception set and the non-Lebesgue-point set have planar measure zero, also after the orthogonal coordinate change. Hence an admissible point exists in that rectangle. Its two original coordinates both exceed `r`, so coordinate monotonicity compares it with `(p,q)`.

For an explicit uniform constant, the upper endpoint satisfies

`beta^2+t^2 <= beta^2+4r^2+2(R+2)^2 <= D(1+r^2)`,

where `D=max(4,beta^2+2(R+2)^2)`. Thus one may take `c=alpha*m/(pi*D)>0` in the lower bound `f(p,q)>=c/(1+max(p,q)^2)` at almost every positive point.

Integrating over `p>=1` and `0<q<p` gives `c integral_1^infinity p/(1+p^2) dp=infinity`. This is a genuine logarithmic divergence contradicting finite spectral mass. It does not evaluate `f` on a single null diagonal or assume uniform lower bounds on individual exceptional slices.

## 6. Restriction back to four dimensions

Restricting the continuous covariance to one coordinate pair is legitimate. Its momentum measure is precisely the finite positive marginal on that pair. The point-matrix RP conditions restrict by taking all points in the plane; such points retain strictly positive normal coordinates and never create an evaluation at the missing origin in a reflected difference.

The two-dimensional lemma makes the first pair marginal a point mass at zero. Positivity, not cancellation, then forces the original measure to be supported where those two coordinates vanish. The second pair gives the complementary support condition. Their intersection is the origin, proving constancy.

The stated graph-cover extension uses the same reasoning edge by edge and is valid when every coordinate belongs to an edge. No connectedness is needed. If one coordinate is uncovered, an OU covariance depending only on that coordinate provides the stated nonconstant example.

## 7. Published representation source: verified scope

I independently opened the versioned primary source [Neeb–Olafsson, *Reflection Positivity and Conformal Symmetry*, arXiv:1206.2039v2](https://arxiv.org/pdf/1206.2039v2) and checked:

- Theorem 4.11 requires a positive definite, 1-bounded distribution on the involutive open cone and provides a positive measure representation.
- Example 4.12(c) specializes it to the half-space Fourier–Laplace formula with a nonnegative normal parameter.
- Remark 6.10 expressly discusses bounded positive definite half-space functions and their Fourier–Laplace representations.
- Definition 1.8 treats ordinary positive type, reflection invariance, and positivity on the reflected semigroup as separate conditions.

The source does not itself prove the finite-six-mirror no-go theorem. The audited direct GNS construction supplies the boundedness-to-contraction and finite-mass details needed here; citing Theorem 4.11 alone without those checks would be incomplete. The current proof does include them.

## 8. Convention counterexample and OU certificate

The alternating polynomial is

`P(x)=product_i x_i * product_(i<j)(x_i^2-x_j^2)`.

It has degree 16 and 24 nonzero expanded monomials. Permuting coordinates multiplies it by the permutation sign; changing coordinate signs multiplies it by their product. Thus `P(w x)=det(w)P(x)` for every signed permutation, as an identity of polynomials. The Gaussian factor preserves this transformation law. In dimension four, `det(-r)=-1` for each tested reflection. The reflected contribution is therefore antisymmetric and cancels from real diagonal quadratic forms. Complex Hermitian positivity detects the antisymmetric part and fails.

Crucially, `C=1+h` is not ordinary positive type: `C(0)=1`, whereas

`P(1,2,3,4)=3628800` and `C(1,2,3,4)=1+3628800*exp(-30)>1`.

This violates the elementary positive-type bound `|C(x)|<=C(0)`. The author added this limitation explicitly in the final reviewed version. Therefore this counterexample supports the need to specify the weak real-only convention; it does not negate a theorem that already assumes a continuous genuine covariance on all of space.

For a continuous ordinary positive-type covariance on all of `R^4`, real-only RP at all sixteen mirrors can in fact be upgraded indirectly: average over the signed-permutation group, use Hermitian symmetry to cover both orientations of each half-space, and use group invariance to make the averaged reflected real form symmetric. It is then complex RP, so the main theorem makes the average constant. The average of the original positive Bochner measure under this finite group cannot lose any positive mass off zero, forcing the original measure to be concentrated at zero as well. This separate corollary is now included in the final reviewed version with continuity at zero explicit. It is valid and is not needed for the main proof.

The OU example is genuine ordinary positive type and coordinate RP. Its diagonal reflected distances are exactly

`[[1,1,2],[1,1,1],[2,1,1]]`.

For `a=exp(-1)` and coefficients `(1,-2,1)`, the resulting quadratic expression is exactly `2a^2-2a<0`. This defeats diagonal RP, not coordinate RP, and consequently does not contradict the theorem.

## 9. What this audit does not establish

- Contact distributions at the origin are invisible to strictly separated half-space tests. The theorem classifies the off-origin regular function, not those contact terms.
- Tensor or curvature components use their field-index reflection action; scalar RP cannot be assumed component by component.
- A bounded difference `C(Rx)-C(x)` is not automatically RP. The positive cone is not closed under subtraction, and the rotated kernel need not satisfy the available mirror inequalities.
- No claim about the original Yang–Mills proof, its full hypotheses, or its exact supporting source location is established by this audit.
- No claim of mathematical novelty is made.

## 10. Reproducible checks and change control

The author's standard-library exact checker was copied into this audit directory and rerun there; all its checks passed without modifying the source directory.

`independent_certificates.py` was written separately for this audit. It expands `P` symbolically and verifies all 384 signed-permutation transformation identities, including all sixteen reflection identities, rather than only evaluating sample points. It also independently checks the positive-type obstruction value and the exact OU certificate. Results are in `independent_checks.json`.

Commands:

`python check_author_certificates.py`

`python independent_certificates.py`

The finite scripts do not verify the measure-theoretic proof. That proof was checked analytically as detailed above. No remote change, merge, release, or external communication was performed.
