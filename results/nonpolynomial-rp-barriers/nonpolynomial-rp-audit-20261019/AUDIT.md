# Independent audit: finite ellipsoid mixtures and separable Stieltjes covariances

19 October 2026. Local mathematical review; no repository or remote state changed.

## Verdict

Both proposed no-escape results are correct under the explicit scalar, finite-mixture / finite-positive-measure hypotheses below. Two simplifications materially strengthen their proofs:

1. In a positive finite ellipsoid mixture, coincident upper-half-plane poles have residues with the same phase and cannot cancel. Generic-pole arguments, polynomial irreducibility, and resultants are unnecessary. A finite-exponential Hankel lemma proves the conclusion at every nonzero tangential momentum.
2. Every nonzero separable compact-positive-mass Stieltjes product has a single, explicit three-point diagonal-RP counterexample. The same points and coefficients work for atomic, continuous, and singular mass measures. No analytic-continuation or representation theorem is needed for this conclusion.

The optional endpoint / holomorphy argument is also valid with the qualifications and proofs in Section 4. It is secondary to the exact witness.

These are statements about specified scalar Gaussian covariance classes. They do not classify arbitrary nonpolynomial covariances, tensor reflection actions, interacting fields, or Yang–Mills theory. Arbitrary additional contact terms must be kept separate.

## 1. Precise reflection convention and localization

Let n be a unit normal, let R_n=I−2nnᵀ, and write x=tn+z, p=un+k, with z,k perpendicular to n. For a real stationary scalar covariance, use

    Q_n(f)=∫∫ overline{f(x)} C(x−R_n y) f(y) dx dy,

where f is smooth, compactly supported in n·x>0. Full complex covariance RP means Q_n(f) is real and nonnegative for every such f. For a centered real reflection-invariant Gaussian field, this is equivalent to the usual full Gaussian RP. No real-only, non-Hermitian surrogate is used.

If the normal Fourier inverse at tangential momentum k is K_k(t), then on product tests f(t,z)=h(t)g(z),

    Q_n(f)=(2π)^−3 ∫ |ĝ(k)|² Q_k(h) dk,
    Q_k(h)=∫∫ overline{h(t)} K_k(t+s) h(s) dt ds.

A sign reversal in the normal Fourier convention conjugates all rates below and leaves every argument unchanged.

Although g with compactly supported smooth Fourier transform is Schwartz rather than compactly supported, it is an allowed limit: multiply it by smooth spatial cutoffs tending to one. The resulting tests converge in Schwartz space, remain supported in the same compact positive-time interval, and their covariance pairings converge by tempered-distribution continuity.

In both classes considered here, Q_k(h) is continuous in k on the required open frequency set. For ellipsoids with possible zero masses this set is k≠0; for strictly positive compact mass products it is all k. Local uniform normal-integral / exponential bounds justify this continuity. If Q_k(h) were negative or nonreal at one such k, a compactly supported frequency cutoff in a small neighborhood would contradict full RP. Hence full RP implies the fixed-k Hankel condition there, for every h. This is pointwise localization, not an unjustified claim about a single measure-zero Fourier slice.

## 2. Finite positive ellipsoid mixtures

### 2.1 Statement

Let

    Ĉ(p)=Σ_{j=1}^N w_j / (pᵀA_jp+m_j²),

where N is finite, w_j>0, A_j is a real symmetric positive-definite 4×4 matrix, and m_j≥0. The masses may vary. This defines a nonnegative tempered Fourier multiplier; when a mass vanishes, its singularity at p=0 is locally integrable in four dimensions.

Assume covariance RP at the tested mirrors. Reflection invariance may be included explicitly, as in the proposed theorem; the full complex Hankel argument below would supply the needed Hermiticity even without a separate assumption.

Then RP at one normal n forces

    A_j n is parallel to n, for every j.

Consequently RP at the four coordinate mirrors and at diagonal mirrors (e_i+e_j)/√2 along any connected graph on the four coordinates forces

    A_j=a_j I, a_j>0, for every j.

In particular all W₄ mirrors force every component scalar. Conversely scalar A_j make the mixture rotationally invariant and RP at every Euclidean mirror.

### 2.2 Exact slice formulas

For fixed n, write

    a_j=nᵀA_jn>0,
    b_j(k)=nᵀA_jk,
    d_j(k)=kᵀA_jk+m_j²,
    α_j(k)=b_j(k)/a_j,
    β_j(k)=sqrt(a_j d_j(k)−b_j(k)²)/a_j.

For k≠0, β_j(k)>0 by positive definiteness and the Schur complement, even when m_j=0. With positive masses, this also holds at k=0. Then

    pᵀA_jp+m_j²=a_j[(u+α_j)²+β_j²],

with upper pole

    u_j=−α_j+iβ_j,

and residue

    Res_{u=u_j} w_j/(pᵀA_jp+m_j²)=w_j/(2i a_jβ_j).

Every such upper-pole residue is −i times a strictly positive real number. If several components share an upper pole, their residues add with the same phase and remain nonzero. All normal roots are simple; an upper pole cannot coincide with a lower pole because β_j>0. Thus no cancellation of a nonreal-shifted pole is possible, including nongeneric tangential momenta and globally proportional denominators.

With the inverse convention (2π)^−1∫e^{iut}du, for t>0,

    K_k(t)=Σ_j B_j(k) exp[−z_j(k)t],
    B_j=w_j/(2a_jβ_j)>0,
    z_j=β_j+iα_j.

After equal rates are merged, all remaining coefficients are still strictly positive.

### 2.3 Finite-exponential Hankel lemma

**Lemma.** Let z_1,…,z_r be distinct complex numbers with positive real parts and B_1,…,B_r>0. If

    K(t)=Σ_j B_j e^{−z_j t}

has a positive-semidefinite Hankel kernel K(t+s) for t,s>0, then every z_j is real.

**Proof.** Positivity implies Hermiticity. In particular K(2t) is real for every t>0, so K is real on (0,∞). Distinct complex exponentials are linearly independent on any open interval: differentiation r−1 times gives a Vandermonde matrix in the distinct z_j. Comparing K with its complex conjugate therefore shows that the rate set is invariant under conjugation and that conjugate rates have equal coefficients.

The map

    h ↦ (L_{z_1}(h),…,L_{z_r}(h)),
    L_z(h)=∫_0^∞ e^{−zt}h(t)dt,

from C_c^∞((0,∞);C) to C^r is onto. Otherwise a nonzero linear functional on C^r would annihilate its image, giving a nontrivial linear combination of the exponentials that vanishes as a distribution on (0,∞), contradicting their independence.

Suppose z and its conjugate are distinct. Choose h whose Laplace values are 1 at z, −1 at its conjugate, and zero at all other rates. Since

    Q(h)=Σ_j B_j overline{L_{conjugate(z_j)}(h)} L_{z_j}(h),

the isolated pair contributes −2B_z<0 and every other term vanishes. Contradiction. One can also prescribe the conjugate-compatible values i and −i and take h real. Hence all rates are real. QED.

This is a finite-dimensional separation proof; it does not assume a spectral representation or invoke a converse Bernstein–Widder theorem.

### 2.4 Application and scalar conclusion

Localization and the lemma give α_j(k)=0 for every j and every nonzero k perpendicular to n. Positivity of coefficients ensures no offending rate disappeared when equal rates were merged. Therefore the linear functional k↦nᵀA_jk vanishes on the tangent space, which is equivalent to A_jn being parallel to n.

Coordinate normals make each A_j diagonal. If diagonal A_j has entries a_{j,i}, then the eigenvector condition at (e_i+e_l)/√2 gives a_{j,i}=a_{j,l}. A connected set of diagonal pairs equates all four entries. Scalar components have the standard positive free-field normal exponential at every mirror, so the converse follows directly.

There is no exceptional-pole set left to control and no need to interchange uncountably many exceptional sets. The same conclusion also extends to any dimension at least two where the corresponding multiplier defines the covariance distribution and the localization used above is valid.

### 2.5 Scope checks

- Finiteness and strict positive weights matter to this proof. It is not a theorem about arbitrary infinite ellipsoid mixtures or signed mixtures.
- Positive-definite A_j matters; singular quadratic forms can require a different slice analysis.
- Zero masses are allowed here because k≠0 suffices. No statement at the undefined massless k=0 slice is needed.
- Adding a polynomial P(p) changes the covariance by a contact distribution. Such terms vanish in strictly separated reflected pairings. Thus the conclusion concerns the displayed noncontact mixture, not an arbitrary added anisotropic contact term.
- Ordinary nonnegative Fourier covariance alone does not imply reflection positivity. The shifted normal rates are the obstruction.

## 3. Separable compact-mass Stieltjes products

### 3.1 Definition, ordinary covariance, symmetry, and UV scaling

Let μ be a finite, nonzero positive Borel measure supported in [a,b], where 0<a≤b<∞. Define

    g(q)=∫ μ(ds)/(q+s),
    Ĉ(p)=∏_{i=1}^4 g(p_i²).

This is nonnegative and integrable on R⁴. With the same Fourier convention, define

    h(t)=∫ e^{−sqrt(s)t}/(2sqrt(s)) μ(ds),  t≥0.

Fubini and the one-dimensional free resolvent transform give the continuous covariance

    C(x)=∏_{i=1}^4 h(|x_i|).

It is W₄-invariant, bounded by h(0)^4, and nonconstant. Its nonnegative spectral multiplier makes it an ordinary stationary Gaussian covariance. The compact mass hypothesis ensures all displayed integrals and derivatives are elementary dominated integrals.

For a fixed compact smooth profile f and the unnormalized scaling f_d(x)=f(x/d),

    |Q_n(f_d)|≤h(0)^4 d^8 ||f||_1².

The same estimate holds for the ordinary covariance form. Thus the claimed O(d^8) UV bound is correct for this scaling convention. It is not a claim of a uniform |p|^−8 momentum bound: the product multiplier only has that power along generic directions, and behaves differently near coordinate axes. For L²-normalized or distributionally normalized rescalings, the scaling power changes correspondingly.

### 3.2 Coordinate RP

For the first coordinate mirror, the time kernel h(t+s) is a positive Laplace mixture. The tangential factor ∏_{i=2}^4 h(|z_i−w_i|) is an ordinary positive-type kernel. Their product is positive semidefinite by the Schur product theorem, or directly by the positive mass integral and tangential Fourier decomposition. The same proof works for every coordinate mirror.

This is covariance RP and hence full Gaussian RP for these scalar reflection-invariant Gaussian fields.

### 3.3 One universal exact diagonal counterexample

Fix any L>0, put n=(e_1+e_2)/√2, and take

    x_0=( L/2,  L/2,0,0),
    x_1=(3L/2, −L/2,0,0),
    x_2=(5L/2,−3L/2,0,0).

Every point has n·x_i=L/√2>0. The reflection is

    R_n(x_1,x_2,x_3,x_4)=(−x_2,−x_1,x_3,x_4).

Writing h_r=h(rL), the reflected Gram matrix is exactly

    G=h_0² [[h_1², h_0h_2, h_1h_3],
            [h_0h_2, h_1², h_0h_2],
            [h_1h_3, h_0h_2, h_1²]].

For the real coefficient vector c=(1,−2,1),

    cᵀGc=h_0²[6h_1²−8h_0h_2+2h_1h_3].                 (1)

The measure ν(ds)=μ(ds)/(2sqrt(s)) is positive and finite. Cauchy–Schwarz applied to 1 and e^{−sqrt(s)L} gives

    h_1²≤h_0h_2.

Because all masses are strictly positive and μ is nonzero, h is strictly positive and strictly decreasing. Hence

    h_1h_3<h_0h_2.

Therefore (1) satisfies

    cᵀGc≤2h_0²[h_1h_3−h_0h_2]<0.

This proves diagonal-RP failure for every measure in the stated class. The witness is uniform in μ; no atomic/non-atomic case split is necessary.

Because C is continuous, the point witness yields an allowed smooth-test witness. Replace each point mass c_iδ_{x_i} by c_i times the same nonnegative smooth unit-integral bump supported in a sufficiently small ball about x_i. The supports remain strictly in the positive half-space, and the reflected quadratic form tends to the strictly negative value in (1). It is therefore negative for all sufficiently small bump radii.

### 3.4 Single-atom and two-point checks

For μ=qδ_s with q,s>0, let A=q/(2sqrt(s)) and r=e^{−sqrt(s)L}∈(0,1). Then h_j=Ar^j, and the exact value is

    cᵀGc=2 A^4 r²(r²−1)<0.

Equivalently, with a=r², it is 2A^4a(a−1), agreeing with the earlier OU witness.

There is also a two-point witness when μ has at least two support points: use x_0,x_1 and coefficients (1,−1). Its value is

    2h_0²[h_1²−h_0h_2]<0,

because Cauchy–Schwarz is then strict. It vanishes for a single atom, which explains why the uniform three-point witness is preferable.

### 3.5 Exact computational certificate

VERIFY_WITNESS.py constructs the exact reflection matrix and all point differences using SymPy rational expressions, checks all three positive-half-space coordinates, forms the full Gram matrix, and verifies both the general quadratic expression and the single-atom specialization. VERIFY_WITNESS.txt records its successful output.

The computation verifies finite algebra. Positivity, strict monotonicity, smoothing, localization, and analytic conclusions are proved in this note rather than inferred from finite tests.

## 4. Optional analytic-continuation route

The direct witness already settles the product construction. The following validates the proposed complementary analytic explanation and pinpoints its necessary hypotheses.

### 4.1 Endpoint nonremovability for every positive measure

Let a_0=inf supp μ>0. The Stieltjes transform g cannot have a holomorphic extension across z=−a_0 that agrees with its defining germ on z>−a_0.

Here is a self-contained proof that does not assume an endpoint atom or a lower bound on mass density. Shift t=s−a_0 and write

    f(w)=g(w−a_0)=∫ ν(dt)/(w+t),

where ν is finite positive, supported in [0,b−a_0], and every interval [0,r] with r>0 has positive ν-mass. Suppose f extends holomorphically to a neighborhood of w=0. Choose R>0 such that it is holomorphic on a neighborhood of the closed disk |w|≤R, and let M be its maximum modulus on the circle.

For x>0, differentiation under the integral gives

    (−1)^n f^(n)(x)/n!=∫ (x+t)^−n−1 ν(dt).

Let x decrease to zero. Continuity of the extended derivative and monotone convergence give

    ∫ t^−n−1 ν(dt)=|f^(n)(0)|/n!≤M R^−n.

If ν has an atom at zero, the n=0 identity is already impossible. Otherwise choose any 0<r<R. The integral is at least ν([0,r]) r^−n−1. Thus

    ν([0,r])/r · (R/r)^n≤M,

which is impossible as n tends to infinity. This proves nonremovability even for measures whose endpoint mass vanishes faster than every algebraic power.

A Schwarz-reflection plus Stieltjes-inversion proof is also valid, but must explicitly use the real extension on an interval to conclude absence of measure there. The derivative proof avoids that extra theorem.

### 4.2 A nonzero companion factor

At the diagonal mirror, use normal frequency u and tangential frequency v in the first two coordinates, so p_1=(u+v)/√2 and p_2=(u−v)/√2. Fix v>0 and any real remaining tangential frequencies. Up to a strictly positive constant, the normal multiplier is

    F_v(u)=g((u+v)²/2) g((u−v)²/2).

Let

    u_0=v+i sqrt(2a_0).

The second argument equals −a_0. The first argument equals

    2v²−a_0+2iv sqrt(2a_0),

which lies strictly in the upper half-plane. For every z with Im z≠0,

    Im g(z)=−Im z ∫ |z+s|^−2 μ(ds),

so g(z) is analytic and nonzero there. Thus the first factor is analytic and nonzero near u_0. The map u↦(u−v)²/2 has derivative i sqrt(2a_0)≠0 at u_0, so a holomorphic extension of the product near u_0 would give an extension of g across −a_0, contradicting Section 4.1.

The relevant germ is connected to the real axis: along u=v+iy with 0≤y<sqrt(2a_0), the second argument is −y²/2>−a_0, and the first argument stays in the upper half-plane when y>0. This supplies the path for the identity-theorem comparison with any purported RP extension.

### 4.3 What is needed for RP to imply the requisite holomorphy

It is insufficient to cite “RP implies Stieltjes” for a generic tempered distribution without checking slice regularity and localization. Here those checks are available:

- F_v is real, even, continuous, and integrable on the real u-axis, with O(|u|^−4) tails.
- Its inverse Fourier transform K_v is bounded, continuous, even, and tends to zero at infinity.
- Full RP plus the pointwise localization in Section 1 gives positive semidefiniteness of K_v(t+s).

A bounded continuous Hankel-positive kernel has a finite positive Laplace representation

    K_v(t)=∫_[0,∞) e^−λt ρ_v(dλ),  t≥0.

For completeness, a direct bounded-kernel GNS construction verifies the support and finiteness instead of presupposing them. Start with formal vectors e_t, t>0, and inner products K_v(t+s). Positive normal shifts T_a e_t=e_{t+a} are symmetric. For a finite linear combination ξ, the sequence b_j=||T_a^jξ||² is uniformly bounded by boundedness of K_v and obeys b_j²≤b_0 b_{2j}. Iteration gives b_1≤b_0, including the null-vector case. Hence shifts descend to self-adjoint contractions; T_a=T_{a/2}² makes them positive. Kernel continuity gives a strongly continuous semigroup T_a=e^−aH with H≥0.

The vectors e_t have uniformly bounded norms. A weak limit e_0 along t decreasing to zero satisfies e_t=T_te_0, by strong continuity of the shifts against fixed test vectors. The spectral measure of H in e_0 is a finite positive measure ρ_v and gives the representation. Its total mass is K_v(0), using continuity at zero. Since K_v tends to zero at infinity, ρ_v has no atom at zero.

Fourier transformation of the even extension yields, first as finite measures / distributions and then for real u≠0 by continuity,

    F_v(u)=∫_(0,∞) 2λ/(λ²+u²) ρ_v(dλ).

No additional contact term occurs: the original inverse transform is a continuous function on the whole line and the finite spectral construction agrees there. For complex u with Re u≠0, the integrand is holomorphic and locally uniformly bounded in λ; indeed

    2λ/(λ²+u²)=1/(λ−iu)+1/(λ+iu),

so its modulus is at most 2/|Re u|. The finite measure therefore gives a holomorphic extension to each open half-plane Re u>0 and Re u<0.

Because Re u_0=v>0, Section 4.2 contradicts this holomorphy. This independently proves the same diagonal-RP failure as the exact witness.

## 5. Final audit assessment

- Finite positive ellipsoid mixture: accepted, including varying nonnegative masses, with the k≠0 localization explicitly stated. Stronger pointwise same-phase residues replace generic resultants.
- Separable product ordinary covariance, W₄ invariance, boundedness, coordinate RP, and unnormalized-profile O(d^8): accepted.
- Product diagonal-RP failure: accepted with a universal exact three-point witness; this is the recommended primary proof.
- Endpoint singularity and nonzero companion factor: accepted; derivative estimates cover all positive compact measures.
- RP-to-Stieltjes holomorphy: accepted only with the integrable-slice, bounded-continuous inverse transform, and localization hypotheses verified above. It should not be exported as an unconditional assertion about arbitrary tempered covariances.
- General anisotropic nonpolynomial escape routes remain open outside these classes. No general-field or Yang–Mills conclusion follows from this audit.

## 6. Final-manuscript confirmation and stronger stated scope

The final author manuscript reviewed is:

    nonpolynomial-rp-escape-20261019/RESULT.md
    SHA-256: 90adedb134457befe8816d82058278c7d95767ae1b34046a41d6c2e4d780afb5

It validly broadens Section 3 of this audit to **every finite nonzero positive measure σ on [0,∞)** with h(t)=∫e^−λ|t|σ(dλ). No compact support, positive spectral gap, rationality, or finite moments are required. The product is constant exactly when σ is supported at zero. Otherwise h is strictly decreasing, the same Cauchy–Schwarz estimate applies, and the same three-point witness is strictly negative. A positive atom at zero mixed with any positive-mass component does not repair diagonal RP. Dominated convergence supplies boundedness and continuity even for unbounded spectral support.

The author's finite interpolation proof is also correct. It chooses r so the finitely many nodes e^−rλ_j are distinct and the selected conjugate pair is nonreal, then prescribes the conjugate-compatible values i e^{t_0λ} and −i e^{t_0 conjugate(λ)}. The real interpolating polynomial gives Laplace values i and −i after multiplication by e^−t_0λ. Their squares each equal −1, so the isolated pair contributes exactly −2B. The exceptional r values form a countable set; there is no missing existence condition. VERIFY_INTERPOLATION.py supplies an additional exact rational-node check with three modes and a real polynomial, producing precisely −2.

### Explicit four-ellipsoid example independently recalculated

For

    F(p)=Σ_{j=0}^3 1/(|p|²+p_j²+1),

take n=(e_0+e_1)/√2 and k=(e_0−e_1)/√2. The first two terms have

    a=3/2, b=±1/2, c=5/2,
    β=±1/3, ω=√14/3, B=1/√14.

The last two terms have β=0, ω=√2, B=1/(2√2). Therefore

    K(T)=(2/√14)e^{−√14 T/3}cos(T/3)+(1/√2)e^{−√2 T}.

With r=3π/2, t=e^{−π√14/2}, s=e^{−3π√2/2}, times r,3r and coefficients (−s²,1), the nonoscillatory contribution vanishes. The remaining form is exactly

    −(2/√14)t²(s²+t²)²<0.

All coefficients, normal poles, and the sign were checked independently. The author's VERIFY_EXACT.py was read and rerun successfully. It verifies these algebraic identities and the product witness; the accompanying analytic smoothing and localization arguments are valid.

### Primary-reference verification

The primary arXiv HTML was checked directly. Arici, Becker, Ripken, Saueressig, and van Suijlekom, *Reflection Positivity in higher derivative scalar theories*, arXiv:1712.04308, Theorem 3.7, is indeed the criterion for a real rational function of the Laplacian without nonnegative-real spectral poles: reflection positivity is characterized by simple negative-real poles with nonnegative residues. Sections 3.2 and 3.3 treat pole separation and RP violations. This is contextual support; it is not applied as a theorem about the anisotropic multiplier or arbitrary nonrational covariances.

Primary sources: https://arxiv.org/html/1712.04308 and https://arxiv.org/abs/1712.04308.

The final manuscript explicitly clarifies that added W₄-invariant contact terms need not become O(4)-invariant. Its rotational conclusion concerns the noncontact resolvent part / covariance away from the origin. No unresolved mathematical defect was found in the final statements or proofs.

### Checker hardening

Both independent checkers use explicit `require` / `RuntimeError` checks rather than removable Python assertions. Normal and `python -O` runs both passed and produced identical output. This hardening changes execution robustness, not the mathematical claims.
