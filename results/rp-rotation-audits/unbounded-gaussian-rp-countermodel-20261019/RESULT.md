# A linear Gaussian boundary countermodel for finite-mirror rotation claims

19 October 2026. Independent audit and exact certificate. No remote changes.

## Result and scope

There is a genuine centred real Gaussian random tempered distribution on R⁴
which is translation invariant, invariant under the hyperoctahedral group W₄,
and fully reflection positive at all sixteen W₄ mirror directions and all their
affine translates, but whose scalar covariance is not O(4)-invariant even away
from coincidence. Its off-origin covariance is smooth, homogeneous of degree
−10, and has position-uniform separated-support bounds and power-law clustering.

The example is simply

    ψ = Q(∂)φ,             Q(p) = p₀⁴ + p₁⁴ + p₂⁴ + p₃⁴,

where φ is the massless real Gaussian free field with

    G(x) = 1/(4π² |x|²).

This is a linear operation on a random distribution. No pointwise Wick square,
renormalized product, stress tensor, lattice construction, or limiting family
is required.

**What this establishes:** the combination of translation/W₄ invariance,
genuine full complex reflection positivity at the finite mirrors, separated
position-uniform bounds, and power-law clustering does not force scalar
two-point rotation invariance without an additional restrictive hypothesis.
In particular, boundedness cannot simply be removed from the bounded-kernel
result audited separately.

**What this does not establish:** this is not a counterexample to the YM4
remark's full hypotheses (a)–(d), including its logarithmic ultraviolet input
and Wilson-limit prerequisites. It does not verify the more ambitious
composite-field/stress-tensor countermodel in the source's outstanding
Proposition 10.8. It proves neither that proposition's stress-flux statement
nor its claimed rotation-invariant short-distance germ. It is not a
Yang–Mills construction or a mass-gap result. No novelty claim is made.

The domain of the random field itself is Schwartz tests, or compactly supported
smooth tests. Off-diagonal covariance integrals extend to separated L¹ tests;
that extension must not be confused with existence of ψ(f) for every C¹ or
continuous test.

## 1. Construction and ordinary positivity

Use the Fourier convention

    f̂(p) = ∫ exp(−ip·x) f(x) dx,
    f(x) = (2π)⁻⁴ ∫ exp(ip·x) f̂(p) dp.

The locally integrable function |p|⁻² is the Fourier transform of G. In four
dimensions it is integrable near p=0 and has polynomial growth at infinity.
The massless free field is therefore a centred real Gaussian random tempered
distribution with covariance

    Bφ(f,g) = (2π)⁻⁴ ∫ conjugate(f̂(p)) ĝ(p) / |p|² dp.

The differential operator Q(∂) is a continuous real linear map on Schwartz
space and on tempered distributions. Since each term has even order four,

    ψ(f) := φ(Q(∂)f)

is exactly the distributional derivative, with no integration-by-parts sign.
Thus ψ exists on the same probability space. Alternatively, its positive
continuous Gaussian characteristic functional directly constructs its law.
Its covariance is

    Bψ(f,g) = (2π)⁻⁴ ∫ conjugate(f̂(p)) ĝ(p) Q(p)² / |p|² dp.   (1)

The multiplier is nonnegative and even on real momentum space. Near zero it
is O(|p|⁶), and globally it has polynomial growth. Equation (1) is therefore
a positive, continuous covariance on Schwartz space. In particular, this is
ordinary positive type as a distribution, not merely a formal off-diagonal
kernel or a real-only reflected quadratic form.

Write C = Q(∂)²G for this fixed covariance distribution. Its distributional
extension through zero is fixed by construction. The off-origin function
derived below is not locally integrable at zero, so an unqualified integral
against that function over coincident supports is not its definition. Contact
terms cannot be discarded when discussing the full ordinary covariance.

## 2. Translation and W₄ invariance

The signed permutation group W₄ acts on scalar tests by ordinary pullback.
For every w∈W₄,

    Q(wp) = Q(p),             |wp|² = |p|².

Therefore Q(∂) commutes with the W₄ pullbacks, and with translations. Since φ
is invariant under translations and all orthogonal transformations, ψ is
invariant under translations and W₄. The same conclusion follows directly
from (1), and centred Gaussian laws are determined by their covariances.

The sixteen reflection directions are the four coordinate normals eᵢ and
the twelve normals (eᵢ±eⱼ)/√2, i<j. Their reflections are signed permutations:
coordinate sign changes, coordinate swaps, and swaps with both signs reversed.
Thus Q(∂) commutes with each of these reflections. It also commutes with each
affine translate of those reflections, because it commutes with translations.

It is essential that ψ is being regarded as a scalar random distribution with
this standard pullback action. Under a general orthogonal transformation,
the fixed differential polynomial Q is not invariant.

## 3. Genuine full complex reflection positivity

### 3.1 Free-field covariance positivity

For a chosen reflection plane, use coordinates (t,z) with the positive side
t>0 and reflection θ(t,z)=(−t,z). Let f,g be smooth compactly supported tests
strictly in t>0. Define

    F_f(k) = ∫₀^∞ exp(−|k|t) f̂_z(t,k) dt,       k∈R³.

Integrating the free propagator in the normal momentum gives

    Bφ(θf,g)
      = (2π)⁻³ ∫ [conjugate(F_f(k)) F_g(k)] / (2|k|) dk.         (2)

Here θf=f∘θ. The k=0 singularity is locally integrable in three tangential
dimensions. Formula (2) is a complex/Hermitian positive semidefinite Gram
form. Rotational invariance of G gives it for every plane orientation, and
translation invariance gives it for every affine offset.

### 3.2 From covariance RP to Gaussian-law RP

For completeness, covariance positivity gives the full Gaussian statement,
not just the one-field statement. For real same-side tests f₁,…,fₘ, the
characteristic-functional reflection matrix is

    Mᵢⱼ = E exp(iφ(fⱼ−θfᵢ))
         = exp(−Bφ(fᵢ,fᵢ)/2) exp(−Bφ(fⱼ,fⱼ)/2)
           exp(Bφ(θfᵢ,fⱼ)).                                   (3)

The matrix Aᵢⱼ=Bφ(θfᵢ,fⱼ) is positive semidefinite by (2). Its entrywise
exponential is positive semidefinite: expand it as the convergent sum of
Hadamard powers A^{∘n}/n!, using the Schur product theorem, with n=0 the
all-ones matrix. Multiplication by the two positive diagonal factors in (3)
preserves positivity. Consequently

    E conjugate(F(θφ)) F(φ) ≥ 0

for every complex linear combination F of same-side Weyl observables
exp(iφ(f)). Their span is dense in each finite-dimensional Gaussian
L²-cylinder space. Reflection preserves the measure, so the displayed
sesquilinear form is continuous in L² by Cauchy–Schwarz. This gives RP for all
square-integrable same-side cylinder functions, including polynomials in
smeared fields. No real-only interpretation is being used.

This Gaussian covariance-to-law equivalence is standard; see Jaffe–Ritter,
*Quantum Field Theory on Curved Backgrounds, I*, §1.6 and Theorem 1.2:
https://arxiv.org/abs/hep-th/0609003 . Equations (2)–(3) supply the massless
flat-space argument needed here directly.

### 3.3 RP survives the local intertwining operator

Fix any of the sixteen W₄ mirror directions, with any affine offset. A
constant-coefficient differential operator does not enlarge support:

    supp Q(∂)f ⊆ supp f.

It also commutes with this reflection, as proved in §2. Thus a positive-side
functional of ψ pulls back to a positive-side functional of φ, and reflection
of that pullback equals pullback of the reflected functional. Applying free
Gaussian RP proves

    E conjugate(F(θψ)) F(ψ) ≥ 0                                (4)

for the full complex same-side cylinder algebra and its L² closure. In
particular,

    Bψ(θf,g) = Bφ(θ Q(∂)f, Q(∂)g)

is positive semidefinite. This proves exactly the full-RP assertion for all
sixteen affine mirror families.

At the coordinate mirror t=0 there is an especially explicit check. Repeated
integration by parts has no boundary terms, since the tests stay a positive
distance from the plane, and gives

    F_{Q(∂)f}(k) = [|k|⁴ + k₁⁴+k₂⁴+k₃⁴] F_f(k).

Consequently the ψ reflected form is (2) with nonnegative weight

    [|k|⁴ + k₁⁴+k₂⁴+k₃⁴]² / (2|k|).                          (5)

The weight is strictly positive for k≠0. This also supplies the strict
positivity used in the ultraviolet witness below.

## 4. Explicit off-origin kernel and exact certificates

For x≠0, differentiate the ordinary function G to obtain

    C(x) = N₈(x) / (4π² |x|¹⁸),                               (6)

where N₈ is the following homogeneous harmonic polynomial of degree eight.
Define each symmetric monomial sum to include each distinct monomial once:

    m₈    = Σᵢ xᵢ⁸,
    m₆₂   = Σᵢ≠ⱼ xᵢ⁶ xⱼ²,
    m₄₄   = Σᵢ<ⱼ xᵢ⁴ xⱼ⁴,
    m₄₂₂  = Σᵢ Σ_{j<k; j,k≠i} xᵢ⁴ xⱼ² xₖ²,
    m₂₂₂₂ = x₀²x₁²x₂²x₃².

Then

    N₈ = 18432 [51 m₈ − 476 m₆₂ + 1186 m₄₄
                 + 12 m₄₂₂ − 216 m₂₂₂₂].                     (7)

The independent standard-library checker builds this polynomial by repeated
differentiation, rather than taking (7) as input. Its recurrence is

    D^α |x|⁻² = N_α(x) / (|x|²)^{|α|+1},
    N_{α+eⱼ} = |x|² ∂ⱼN_α − 2(|α|+1)xⱼN_α,      N₀=1.

It sums the sixteen ordered terms ∂ᵢ⁴∂ⱼ⁴, verifies (7), ΔN₈=0, invariance
under all 384 signed permutations, and invariance of Q under all sixteen
mirror reflections. Those are exact integer/rational calculations.

### 4.1 Real-space anisotropy at explicit equal-radius points

Let

    u = (1,0,0,0),        v = (3/5,4/5,0,0).

Both have norm one, and the SO(2) block with columns (3/5,4/5) and
(−4/5,3/5) sends u to v. The exact values are

    4π² C(u) = N₈(u) = 940032,
    4π² C(v) = N₈(v) = 19060586496/78125,

and hence

    4π² [C(u)−C(v)] = 54379413504/78125 ≠ 0.                   (8)

Thus the covariance is not O(4)-invariant away from zero. Smoothness makes
this a separated-test failure as well: take sufficiently small nonnegative
smooth approximate identities around 0 and u, and rotate both by the displayed
rotation. Their covariance difference tends to the nonzero value in (8), so
it is nonzero for sufficiently small fixed supports. This is not a defect
confined to contact terms.

### 4.2 Independent complex-null/contact-term certificate

Let R now rotate coordinates 1 and 2 by the same rational SO(2) block, fixing
coordinates 0 and 3, and evaluate the polynomial on complex vectors

    p = (i,1,0,0),       Rp = (i,3/5,4/5,0).

These obey the algebraic null equation Σⱼpⱼ²=Σⱼ(Rp)ⱼ²=0. Direct evaluation
gives

    Q(p)=2,       Q(Rp)=962/625,
    Q(p)²−Q(Rp)² = 637056/390625 ≠ 0.                          (9)

Therefore Q(p)²−Q(Rp)² is not divisible by the complex polynomial Σⱼpⱼ².
If the difference of the covariance and its rotated version were supported
only at the origin, its Fourier transform would be a polynomial P. On real
p≠0 this would give the polynomial identity

    Q(p)²−Q(Rp)² = (Σⱼpⱼ²) P(p).

An identity on that real open set is an identity of polynomials, hence also
holds for complex p; (9) contradicts it. This independently verifies that
the anisotropy cannot be removed by contact terms.

The rotation in this certificate need not be the rotation in (8); each is an
independent explicit witness.

## 5. Separated bounds, singularity, and clustering

Equation (6) is smooth away from zero and homogeneous of degree −10. An
explicit, deliberately nonoptimal bound follows from (7): the sum of the
absolute values of all its monomial coefficients is 246841344, and each
degree-eight monomial is at most |x|⁸ in absolute value. Therefore

    |C(x)| ≤ A |x|⁻¹⁰,       A=246841344/(4π²).                (10)

For compactly supported smooth f,g whose supports have distance d>0,

    |Bψ(f,g)|
      = |∬ conjugate(f(x)) C(x−y) g(y) dx dy|
      ≤ A d⁻¹⁰ ||f||₁ ||g||₁.                                (11)

The right side is independent of support position and nonincreasing in d.
If each support lies in a ball of radius R, then

    |Bψ(f,g)| ≤ A d⁻¹⁰ (π²R⁴/2)² ||f||∞ ||g||∞.

This also implies a bound with any test norm dominating the sup norm,
including the manuscript's sharp norm. The connected cumulants of this
Gaussian field are zero for n≥3, so their separated bounds are trivial.
These statements concern the resulting off-diagonal functionals; they do
not identify this model with the manuscript's approximating Wilson family.

For two fixed compact test clusters separated by a translation a, every
cross covariance is O(|a|⁻¹⁰). Wick's formula then proves the corresponding
factorization of smeared polynomial moments with that error: every term in
the difference contains at least one cross contraction. For bounded Weyl
cylinder functions, the same conclusion follows immediately from their
joint Gaussian characteristic function. In particular, there is ordinary
power-law clustering of these local smeared observables. No stress-tensor
decay or far-sphere flux conclusion follows from this calculation.

By (8), along the coordinate axis

    C(te₀) = [940032/(4π²)] |t|⁻¹⁰.

Thus the covariance is not locally bounded at zero. Also, the spectral
multiplier in (1) grows like |p|⁶ along a coordinate ray; it is not a bounded
L² covariance operator. These are substantive ultraviolet failures, not a
failure of ordinary positivity or of the complex RP convention.

## 6. An explicit ultraviolet scaling obstruction

Fixed-height scaled tests exhibit the covariance exponent exactly. For any
disjoint fixed profiles f,g, put f_d(x)=f(x/d), g_d(x)=g(x/d). Homogeneity and
the eight-dimensional volume element give

    Bψ(f_d,g_d) = d⁻² Bψ(f,g).                                (12)

Here is a smooth, nonnegative pair which additionally lies in the precise
class T(d;1/2) recorded in the analytic-rotation audit, and has positive
covariance.

Set a=19/20, ε=1/100, and

    b₀(x) = (1−|x|²/a²)₊²,
    b = b₀ * ρ_ε,

where ρ_ε is a nonnegative radial smooth mollifier of integral one, supported
in the radius-ε ball and positive in its interior. Then b is smooth,
nonnegative, radial, and supported in the radius-24/25 ball. If M=||b||∞,
elementary convolution and radial integration give

    (9024/9025)² ≤ M ≤ 1,
    ∫b = π²a⁴/12 > 1/2 ≥ M/2,
    Lip(b) ≤ 8/(3√3 a) < 2M.                                  (13)

The middle strict inequality already follows from π²>9. The last strict
inequality follows by squaring rational inequalities using the lower bound
on M; the checker verifies it exactly.

Now take

    f_{+,d}(x)=b(x/d−2e₀),     f_{−,d}(x)=b(x/d+2e₀).

Each support lies in a radius-d ball. Their support distance is exactly
(52/25)d, their masses are at least (1/2)M d⁴, and their Lipschitz constants
are at most 2M/d. Thus they satisfy all defining conditions of T(d;1/2).
They are reflections of one another across x₀=0.

Let A₀=Bψ(f_{+,1},f_{−,1}). Formula (5) proves A₀>0: the Fourier–Laplace
transform of f_{+,1} tends to its strictly positive integral as k→0, while
the weight in (5) is strictly positive for k≠0. Consequently (12) gives

    Bψ(f_{+,d},f_{−,d}) = A₀ d⁻² → +∞.                        (14)

This is incompatible with the logarithmically decaying fixed-height upper
bound from Theorem 0(iv) on that test class, whose right side is
O((1+log(1/d))⁻²) for fixed admissible coupling and scale parameters. The
comparison is a scaling diagnosis, not an assertion that ψ has a Wilson
approximating family or meets the remark's other prerequisites. In particular,
the example cannot be used to refute the full (a)–(d) implication. The explicit
test-class check is at θ=1/2 (and hence also at every smaller positive θ);
no identification of the remark's unspecified θ₀ is being asserted.

## 7. Relation to the supplied source and to the bounded theorem

The source is pinned at commit 785a68fdeef78a1da854c4807fe1f17b597d05e7.

- The scalar two-point remark at raw III, lines 79931–79988, includes a
  specific logarithmic ultraviolet upper bound and Wilson-limit assumptions.
  Its separate bounded-kernel sentence concerns a bounded off-origin function.
  The present example has neither of those ultraviolet properties.
  https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/theorem_0_complete_account_raw_III.tex#L79931-L79988
- The later proposition at raw III, lines 109238–109346, is expressly marked
  “Proof outstanding”. It proposes a shifted Wick-quadratic derivative
  observable, additional stress-tensor statements, and a rotation-invariant
  short-distance germ. Its displayed off-diagonal two-point expansion already
  contains Q(∂)²G, multiplied by 4·24²·λ². This note isolates a linear Gaussian
  field with that covariance and proves its narrower properties. It does not
  supply the missing composite construction or those additional claims.
  https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/theorem_0_complete_account_raw_III.tex#L109238-L109346

The previously supplied bounded-kernel audit proves constancy for a Hermitian
scalar covariance, continuous away from zero and locally bounded near zero,
with genuine complex RP at six suitable mirrors. The present example has
those positivity conventions but fails the local bound. It therefore
complements rather than contradicts that result. The anisotropy in (8) also
shows why replacing ultraviolet control by separated-support bounds and
large-distance decay is insufficient in the broad class of random
distributions considered here.

## 8. Reproduction and verification limits

Run, using Python 3 and only its standard library:

    python check_exact.py

It produces CHECKS.json and verifies all finite polynomial, mirror, rational
rotation, contact-term-witness, coefficient-bound, and bump-bound calculations.
It is an exact arithmetic checker, not a formal proof assistant and not a
computer verification of the infinite-dimensional Gaussian or analytic RP
arguments. Those arguments are proved in §§1–3 and §§5–6 above.

SOURCE_MANIFEST.json records the input hashes, relevant line ranges, and
immutable source links. The package does not duplicate the raw external
sources. No source repository was edited, no upstream code was run, no PR
was merged, and no release was published.
