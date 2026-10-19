# Bounded scalar kernels and hyperoctahedral reflection positivity

19 October 2026. Independent mathematical audit of the final paragraph of `raw_III.tex`, lines 79981–79988. This note proves a scalar-kernel statement under an explicit standard covariance convention. It does not prove the manuscript's separate Yang–Mills rotation theorem, identify any Wilson continuum states, or establish a mass gap.

## Result

**The bounded-kernel claim is valid for a Hermitian scalar covariance with genuine (complex/Hermitian) one-field reflection positivity.** No assumption of ordinary positive type is needed in addition: it follows in the proof. In fact, local boundedness near the missing origin suffices, and six mirrors already suffice in four dimensions:

- the four coordinate mirrors;
- the mirrors with normals `e_0+e_1` and `e_2+e_3`.

The proof is a finite-spectral-mass obstruction, not a group-density argument. Coordinate reflection positivity gives Cauchy-mixture momentum slices. A diagonal slice has a `t^-2` tail. Coordinate monotonicity spreads that tail across a two-dimensional quadrant, forcing logarithmically infinite mass unless the spectral measure is supported at zero.

There is an important qualification to the manuscript's words “without any hypothesis.” A “two-point kernel” must mean a Hermitian covariance kernel, and reflection positivity must include a Hermitian positive semidefinite form, or its usual equivalent with reflection invariance already imposed. If one asks only for nonnegative diagonal quadratic forms on real tests while omitting reflection invariance, an explicit bounded smooth nonconstant alternating function passes every such real diagonal test. That weaker interpretation is false; it is not standard complex reflection positivity.

## 1. Precise theorem and conventions

Let `C : R^4 \ {0} -> C` be continuous, bounded on some punctured neighborhood of zero, and Hermitian:

    C(-x) = conjugate(C(x)).                                      (H)

For a unit vector `n`, let `r_n = I - 2 n n^T`. Say that `C` is one-field RP at `n` when, for arbitrary points `x_1,...,x_m` with `n·x_i>0`, the matrix

    K_ij = C(x_i - r_n x_j)                                      (RP_n)

is Hermitian positive semidefinite. Equivalently, the corresponding sesquilinear integral form on complex smooth compactly supported half-space tests is nonnegative and real. The equivalence follows by approximating point masses; all reflected differences remain away from zero. A change of convolution/reflection sign convention is harmless under (H) and the resulting reflection symmetries.

**Theorem.** If `(H)` and `(RP_n)` hold for the six normals listed above, then `C(x)=c` for every `x != 0`, where `c>=0`. Consequently the same conclusion holds for all sixteen hyperoctahedral mirrors.

The theorem extends to `R^d`: coordinate RP plus diagonal RP along the edges of any graph covering every coordinate forces constancy. Pairing coordinates proves the four-dimensional version directly. An uncovered coordinate can retain an OU covariance, so the coverage qualification matters.

## 2. RP supplies reflection invariance and a useful bound

Hermiticity of the reflected matrix says, for every `z` with `n·z>0`,

    C(z) = conjugate(C(-r_n z)) = C(r_n z),

where the last equality uses `(H)`. Hermitian symmetry extends this identity to the opposite half-space; continuity covers its boundary away from zero. Thus `C` is invariant under each tested reflection. In particular, the coordinate reflections imply evenness and then real-valuedness.

For `t>0` and `z` tangent to the mirror, use points

    x=(t/2)n+z/2,       y=(t/2)n-z/2.

The reflected two-by-two matrix has equal diagonal entries `C(tn)` and off-diagonal entries `C(tn+z)` and its conjugate. Hence

    C(tn) >= 0,        |C(tn+z)| <= C(tn).                        (1)

This is a consequence of positive semidefiniteness, not an assumption of ordinary positive type.

### Local boundedness already gives global boundedness

For the pair `e_i,e_j` and `n=(e_i+e_j)/sqrt(2)`, apply (1) first with normal `n`, then with normal `e_i`:

    0 <= C(t e_i)
      <= C((t/2)(e_i+e_j))
      <= C((t/2)e_i).                                            (2)

Iterate until the argument lies in the fixed punctured neighborhood where `C` is bounded. This bounds the coordinate-axis profile uniformly for every `t>0`. The same argument covers `e_j`; the two selected diagonal pairs cover all four coordinates. For any nonzero `x`, choose `x_i != 0` and use (1) at `e_i`, together with coordinate reflection invariance. This bounds `|C(x)|` by the bounded axis profile. Thus the global bound required below follows from the stated local bound.

## 3. The half-space representation and the missing origin

We use the standard bounded Fourier–Laplace representation on the involutive semigroup

    (0,infinity) x R^(d-1),      (t,z)^sharp=(t,-z).

A bounded continuous function whose kernel `C(t+s,z-w)` is positive semidefinite has the representation

    C(t,z) = integral exp(-lambda t) exp(i p·z) rho(dlambda,dp),
    lambda >= 0,   t>0,                                          (3)

with a positive measure. A precise published reference is Neeb–Ólafsson, *Reflection Positivity and Conformal Symmetry*, Theorem 4.11, Example 4.12(c), and Remark 6.10:
https://arxiv.org/pdf/1206.2039

That reference supplies the representation theorem, not the finite-mirror no-go proof below. For completeness, the following direct GNS argument verifies that the bounded-kernel hypotheses give exactly the finite positive representation being used, including the contraction/“1-bounded” condition.

### Direct verification of the representation input

Start with the formal finite span of symbols `v_(t,z)` and the positive semidefinite pairing given by the kernel `C(t+s,z-w)` on the open half-space. Before taking the null quotient, define normal shifts on that formal span by

    A_a v_(t,z)=v_(t+a,z),       a>0.

These shifts are symmetric for the kernel pairing and commute. If `v` is a finite combination of kernel vectors, put `b_k=||A_a^k v||^2`. Boundedness of `C` gives a uniform bound on `b_k` for all integers `k>=0`, depending on `v` but not `k`. Symmetry and Cauchy–Schwarz give

    b_k^2 <= b_0 b_(2k).

Iterating at `k=1` gives `b_1 <= b_0`: for `b_0>0`, use

    b_1 <= b_0^(1-2^-j) b_(2^j)^(2^-j)

and let `j` increase; if `b_0=0`, the first Cauchy–Schwarz inequality already gives `b_1=0`. Thus null vectors are preserved. Taking the null quotient and its Hilbert completion now gives the GNS space, on which each `A_a` extends to a self-adjoint contraction. Since `A_a=A_(a/2)^2`, it is positive. Continuity of `C` in the open half-space gives strong continuity, including at `a=0`, first on kernel vectors and then on the completion. Hence `A_a=exp(-aH)` for a nonnegative self-adjoint `H`.

Tangential shifts act by a commuting strongly continuous unitary representation `U_z=exp(iP·z)`. The vectors `v_t=v_(t,0)` satisfy

    v_(t+a)=A_a v_t,       ||v_t||^2=C(2t,0)<=sup |C|.

Take a weakly convergent subsequence `v_(t_j) -> v_0` as `t_j downarrow 0`. For fixed `t>0`, eventually `t_j<t`, and

    v_t=A_(t-t_j) v_(t_j) -> A_t v_0 weakly.

Strong continuity of `A` on a fixed test vector, together with boundedness of `v_(t_j)`, justifies this weak limit. Thus `v_t=A_t v_0` for every `t>0`. The joint spectral measure of `(H,P)` in the finite-norm vector `v_0` gives

    C(t,z)=<v_0, exp(-tH) U_z v_0>,

which is (3) with a finite positive measure `rho`. Its total mass is

    rho(total)=||v_0||^2=lim_(t downarrow 0) C(t,0)<=sup |C|.       (4)

The half-space data determine this measure uniquely. Reflection invariance in the normal coordinate extends (3) with `t` replaced by `|t|`. Continuity of `C` at every nonzero boundary point identifies the boundary values with the same finite integral. Dominated convergence then gives a continuous extension through the origin, with value `rho(total)`.

For `lambda>0`, use the elementary Fourier identity

    exp(-lambda |t|)
      = integral_R exp(i k t) lambda/[pi(lambda^2+k^2)] dk.         (5)

For `lambda=0`, the spectral measure is `delta_0`. Combining (3)–(5) yields a finite positive Borel measure `mu` on `R^d` such that

    C(x)=integral exp(i p·x) mu(dp),       mu(total)=C(0).          (6)

In particular, the extension is of ordinary positive type. No separate Bochner-positivity hypothesis was assumed. Uniqueness of the Fourier transform of finite measures makes the measure obtained from every reflection direction the same `mu`.

## 4. A two-dimensional finite-measure lemma

**Lemma.** A finite positive Borel measure `mu` on `R^2` whose characteristic function is RP at `e_1`, `e_2`, and `(e_1+e_2)/sqrt(2)` is a nonnegative multiple of `delta_(0,0)`, provided the characteristic function is invariant under those reflections.

Write momenta as `(p,q)`. The half-space representation for `e_1` gives

    mu(dp,dq)
      = delta_0(dp) nu_0(dq)
        + integral_(lambda>0) k_lambda(p) dp nu(dlambda,dq),
    k_lambda(p)=lambda/[pi(lambda^2+p^2)].                         (7)

The analogous formula holds after interchanging `p,q`. The diagonal reflection gives the same decomposition in

    t=(p+q)/sqrt(2),       s=(p-q)/sqrt(2).                        (8)

These are decompositions of the identical finite measure, by Fourier uniqueness.

### 4.1 Singular parts cannot hide the contradiction

From the `e_2` decomposition, the `q`-marginal of `mu`, restricted to `q != 0`, is absolutely continuous. The positive-`lambda` measure in (7), integrated over `p`, is dominated by that marginal because each Cauchy density has integral one. Hence that measure's `q`-marginal is absolutely continuous away from zero. Formula (7) now implies that `mu` is jointly absolutely continuous away from the two coordinate axes. This uses the special product structure in (7); absolute continuity of two marginals alone would not suffice.

The positive-`lambda` part of the diagonal decomposition assigns zero mass to either coordinate axis: on each fixed `s` line, an axis meets the line in at most one `t`, and the conditional `t` measure has a density. The zero-`lambda` part lies on `t=0`, whose intersections with the coordinate axes consist only of the origin. Therefore the coordinate axes have no mass away from the origin.

It follows that

    mu = a delta_(0,0) + f(p,q) dp dq,       a>=0, f>=0, f in L^1. (9)

The zero-`lambda` part in any of the three decompositions is now supported at the origin. The positive-`lambda` parameter measure has an absolutely continuous tangential marginal: a singular tangential marginal would produce positive mass on a Lebesgue-null family of parallel lines, contrary to (9).

### 4.2 Coordinate RP gives coordinate monotonicity

Disintegrating (7) in `q` gives, for almost every `q != 0`,

    f(p,q)=integral_(lambda>0) k_lambda(p) nu_q(dlambda)            (10)

for almost every `p`. Each `k_lambda(p)` is even and decreases for `p>0`. The other coordinate decomposition gives the same statement in `q`.

Thus on the positive quadrant `f` has a coordinatewise nonincreasing representative. One standard justification, avoiding choices on exceptional slices, is to mollify `f` on compact subquadrants: both distributional partial derivatives are nonpositive, so nonnegative mollification gives smooth coordinatewise decreasing functions. At Lebesgue points these converge back to `f`. Consequently, for any two Lebesgue points `u,v` with both coordinates of `u` strictly smaller than those of `v`,

    f(u) >= f(v).                                                (11)

This almost-everywhere version is enough below.

### 4.3 Diagonal RP forces a nonintegrable tail

Suppose `f` is not zero. In diagonal coordinates, disintegration gives

    f((t+s)/sqrt(2),(t-s)/sqrt(2))
       = integral_(lambda>0) k_lambda(t) eta_s(dlambda)            (12)

for almost every `(t,s)`. The positive-`lambda` parameter measure is finite and nonzero. By taking a bounded transverse window and a bounded positive energy interval, then a positive level set, there exist numbers

    0<alpha<=beta<infinity, R<infinity, m>0,

and a measurable set `E subset [-R,R]` of positive finite Lebesgue measure such that

    eta_s([alpha,beta]) >= m      for almost every s in E.

Consequently

    f((t+s)/sqrt(2),(t-s)/sqrt(2))
       >= alpha m/[pi(beta^2+t^2)]                               (13)

for almost every `(t,s)` in `R x E`. Almost every such point also maps to a Lebesgue point of `f`. Thus no evaluation on a fixed null diagonal or an unjustified exceptional slice is being used.

Let `(p,q)` be a Lebesgue point in the positive quadrant and set `r=max(p,q)`. The product set

    {sqrt(2)r+R+1 < t < sqrt(2)r+R+2} x E

has positive planar measure. Select a point `(t,s)` there where (13) holds and its image is a Lebesgue point. Both image coordinates strictly exceed `(p,q)`. Equation (11) and the upper bound on `t` imply, with a fixed `c>0`,

    f(p,q) >= c/(1+r^2)                                         (14)

for almost every positive `(p,q)`. But

    integral_1^infinity integral_0^p [c/(1+p^2)] dq dp
      = integral_1^infinity c p/(1+p^2) dp
      = infinity.                                               (15)

This contradicts `f in L^1`. Therefore `f=0`, proving the lemma.

## 5. Returning to four dimensions

Restrict the continuously extended covariance to the `(x_0,x_1)` coordinate plane. It is the Fourier transform of the finite `(p_0,p_1)` marginal of `mu`. RP is inherited by placing all tested points in that plane, or by transverse smooth approximation. The two-dimensional lemma therefore makes this marginal a point mass at `(0,0)`. Positivity implies `mu` is supported on `{p_0=p_1=0}`.

The pair `(x_2,x_3)` gives support on `{p_2=p_3=0}`. Intersecting these full-measure conditions gives `mu=c delta_0`; equation (6) gives `C=c`. This finishes the theorem.

This argument does not assert that six reflections generate a dense subgroup of `O(4)`. They do not. The conclusion comes from boundedness plus analytic/spectral positivity constraints.

## 6. Exact limitations and convention tests

### 6.1 Real quadratic nonnegativity alone is weaker, and false as a replacement

Define

    h(x)=exp(-|x|^2) product_(i=0)^3 x_i
                       product_(0<=i<j<=3)(x_i^2-x_j^2).          (16)

This is bounded, smooth, nonconstant, real, and even in four dimensions. Under every signed permutation `w`, it obeys

    h(w x)=det(w) h(x).

For any hyperoctahedral reflection `r`, `det(-r)=-1` in dimension four. Therefore

    h(y-r x)=h(-r(x-r y))=-h(x-r y).                              (17)

The reflected bilinear kernel is antisymmetric. Its quadratic form vanishes for every real test. Thus `C=1+h` has reflected real quadratic value `(integral f)^2 >= 0` at all sixteen mirrors, despite being nonconstant and bounded. It fails Hermitian RP: a nonzero antisymmetric contribution is visible on complex tests and prevents the form from being real. It also fails reflection invariance and ordinary positive type: its continuous extension has `C(0)=1`, whereas `h` takes a positive value and then `C(x)>1`, contradicting the positive-type bound `|C(x)|<=C(0)`. Thus it is not the covariance of a probability field. This is only a counterexample to the weakened definition, not to the theorem above.

The original convolution bilinear form is itself symmetric because `h(-x)=h(x)`; the failure is symmetry of the *reflected* form. Thus merely saying “real even two-point bilinear kernel” does not repair a real-only definition without its reflection-invariance/Hermitian-form requirement.

If even Hermitian covariance symmetry is omitted and only one chosen half-space per oriented normal is tested, there is a second elementary loophole: arbitrary perturbations supported in a common untested Weyl chamber may be invisible. Standard covariance/RP conventions exclude this. The precise definition should be stated instead of inferring it from the words “without any hypothesis.”

### Real-only tests are sufficient if a continuous positive-type covariance is assumed

There is a separate repair for the real-only formulation. Suppose `C` is a continuous ordinary positive-type function on **all** of `R^4` and has nonnegative real quadratic reflected forms at all sixteen mirrors. Average it over `W_4`:

    C_bar(x)=(1/384) sum_(w in W_4) C(w x).

Hermitian covariance symmetry extends the real RP inequality to the opposite half-space when a conjugation reverses the chosen normal. Thus every summand satisfies the conjugate mirror inequality and `C_bar` has real-only RP at all sixteen mirrors. The average is real and reflection invariant, so its reflected matrices are real symmetric; real quadratic positivity now implies complex Hermitian RP. The main theorem makes `C_bar` constant.

By Bochner's theorem, the original `C` has a finite positive spectral measure. The spectral measure of `C_bar` is its average under `W_4`. Since positive measures cannot cancel mass away from zero, this average can be supported at zero only when the original measure is supported there. Hence the original `C` is constant too.

Continuity at zero is explicit in this corollary. Positive type plus continuity only away from zero does not itself guarantee that continuity: the point function `1_(x=0)` illustrates the distinction. This corollary further emphasizes that the alternating example is not a counterexample to a genuine continuous finite-variance covariance claim.

### 6.2 Ordinary coordinate OU examples do not contradict the theorem

The bounded W_4-invariant covariance

    C_OU(x)=exp(-sum_i |x_i|)

is positive type and RP at all coordinate mirrors. It fails diagonal RP explicitly. In the first two coordinates let

    x_0=(1/4,1/4), x_1=(3/4,-1/4), x_2=(5/4,-3/4),

with the other coordinates zero. All lie in `x_0+x_1>0`. For reflection in that diagonal, writing `a=exp(-1)`, the reflected matrix is

    [[a,a,a^2], [a,a,a], [a^2,a,a]].

The coefficient vector `(1,-2,1)` gives `2a(a-1)<0`. This is an exact finite witness; no numerically guessed violation is needed.

### 6.3 Origin values, distributions, and contact terms

The theorem concerns a bounded function away from zero and proves its continuous regular extension. Assigning a different value at the single point zero changes neither the regular distribution nor the half-space forms.

If instead one starts with an arbitrary distribution whose restriction away from zero is that function, it may differ from the regular extension by a distribution supported at the origin, i.e. a finite linear combination of derivatives of `delta_0`. All strictly positive-half reflected test differences stay away from zero; hence such contact terms are invisible to these RP tests. The theorem establishes constancy of the off-origin function, not the absence, positivity, or rotational symmetry of arbitrary contact terms. A separate hypothesis is needed to classify them.

### 6.4 Tensor fields require their actual reflection action

For a tensor-valued covariance, the reflection acts on field indices. Odd normal-index components carry signs, and an arbitrary component is not a scalar RP kernel of the form used here. One cannot apply (7) componentwise without checking this action. A valid scalar contraction or scalar observable must be identified first.

The separate supplied `YM_Rotation_Invariance_simplified.pdf` has a probability law of closed distributional two-forms, full characteristic-functional RP, and a global Gaussian `L^2` domination assumption. Its Theorem A is not the bounded scalar theorem proved here. Nor does this note verify the separate implication from Theorem 0 clauses (a)–(d) concerning the manuscript's separated curvature two-point tests. A bounded rotation defect `C(Rx)-C(x)` cannot automatically be substituted for `C`: reflection-positive kernels form a convex cone, which is not closed under subtraction, and the rotated kernel may not satisfy the same mirror inequalities before rotation invariance is known.

### 6.5 Unbounded kernels and lower dimensions

The boundedness hypothesis has content. Standard free scalar covariances in dimension at least two have ultraviolet divergence at the origin and can be RP in every direction. In one dimension `exp(-m|t|)` is bounded, nonconstant, and RP; the two-dimensional logarithmic divergence step is unavailable. The two-dimensional lemma is the critical obstruction used here.

## 7. Source status and verification

- The pinned main source states the bounded-kernel assertion at `raw_III.tex` lines 79981–79988 and points to an unnamed theorem. The companion source audit reports no exact proof location in pinned raw I/II/III.
- The representation input used here is independently sourced: Neeb–Ólafsson, arXiv:1206.2039v2, Theorem 4.11, Example 4.12(c), Remark 6.10. Definition 1.8 also explicitly separates ordinary positive type, reflection invariance, and reflected semigroup positivity in the conventional definition.
- The finite-mirror measure argument in Sections 4–5 is supplied in full above; no novelty claim is made.
- `check_exact.py` checks all sixteen rational reflection matrices, the alternating transformation identity on exact rational samples, the OU reflected-distance pattern, and the exact symbolic quadratic polynomial `2a(a-1)`.
- These finite checks verify the explicit certificates, not the measure-theoretic proof. That proof should receive independent mathematical review before external publication.
- No remote mutation, PR merge, or release publication was performed.
