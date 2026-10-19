# Positive spectral mixtures: ultraviolet rigidity modulo contacts

Independent analytic extension, 19 October 2026. Local research only. No claim about an actual Yang–Mills field without a proof of the spectral-representation hypotheses below.

## Result in brief

Assume a scalar covariance has a positive-mass spectral representation, modulo contacts, with measurable real W₄-invariant polynomial numerators of uniformly bounded degree. Assume its separated reflection form is the integral of the usual per-mass residue forms and that, outside one mass-null set, every per-mass residue is nonnegative at the coordinate and diagonal representative mirrors.

For a nonzero nonnegative smooth positive-half-space profile f and f_d(x)=f(x/d), the upper bound

    B_C(θf_d,f_d)=o(d⁻²)

already forces every polynomial numerator to be constant modulo q+s, for almost every mass s. In particular, a decaying upper bound, including O(log(1/d)⁻²), suffices. The covariance is rotationally invariant away from the origin under the precise contact-renormalized representation stated below. Anisotropic contacts are not eliminated.

This does not force the mass measure to have bounded support. A fully explicit rotational Gaussian example below has

    B_C(θf_d,f_d) ~ K_f / [4 log²(1/d)],     K_f>0.

Thus the extension is not the massless finite-polynomial scaling obstruction in disguise.

## 1. Exact assumptions and scope

Write q(p)=|p|² on R⁴, and let μ be a positive measure on [0,∞). For μ-almost every s, let P_s be a real polynomial invariant under signed permutations W₄. Its coefficients are measurable in s; there is one finite bound on its degree.

We use two explicit representation properties.

1. **Separated reflection formula.** For a W₄ mirror with unit normal n, write p=un+k with k⊥n and put ω_s(k)=sqrt(|k|²+s). For f supported a positive distance inside its positive half-space, the covariance pairing is

       B_C(θ_nf,f) = ∫ Q_{n,s}(f) μ(ds),
       Q_{n,s}(f) = (2π)⁻³ ∫ R_{n,s}(k)/(2ω_s(k))
                       |∫₀∞ exp(−ω_s(k)t) f̂_z(t,k)dt|² dk,
       R_{n,s}(k) = P_s(iω_s(k)n+k).

   The zero-mass factor 1/|k| is the ordinary locally integrable function in three tangential dimensions. All covariance pairings used are finite. Contacts vanish between the strictly separated supports.

2. **Masswise residue positivity.** Outside one μ-null set, R_{n,s}(k)≥0 for every real tangential k, for n=e₀ and n=(e₀+e₁)/sqrt(2). W₄ invariance transfers this to all sixteen mirrors.

The second property follows from full reflection positivity under the separately proved spectral-disintegration theorem in the companion residue report. One sufficient condition there is

    ∫ A(s) exp(−ε sqrt(s)) μ(ds)<∞ for every ε>0,

where A controls the finitely many numerator coefficients, together with tempered-distribution convergence of mass cutoffs modulo polynomial contacts. The present ultraviolet argument may instead take the separated formula and masswise positivity as explicit assumptions. Vague “tempered, locally renormalized” language alone is not substituted for that theorem.

For the final off-origin rotation conclusion, “modulo contacts” means: after mass truncation, the represented covariance, with contact counterterms if needed, converges distributionally to C; all counterterms are supported at the spatial origin. Equivalently, the spectral identity is valid in the quotient by distributions supported at the origin. Cutoffs depend only on s. No nonlocal subtraction is allowed.

No ordinary pointwise positivity of each P_s is needed for rigidity. Ordinary positive type of C would be needed to realize C as a Gaussian covariance; the explicit example in §7 has it.

## 2. A measurable canonical quotient by q+s

Set x_i=p_i² and denote their elementary symmetric polynomials by e₁,e₂,e₃,e₄. The W₄-invariant polynomial ring is R[e₁,e₂,e₃,e₄], with e₁=q and momentum degrees 2,4,6,8.

There is a unique expression P_s=S_s(e₁,e₂,e₃,e₄). Define

    T_s(p)=S_s(−s,e₂(p),e₃(p),e₄(p)).

Then P_s=T_s+(q+s)H_s for an invariant polynomial H_s. Both polynomials have measurable coefficients, since they are obtained by finite algebraic operations on the original coefficients and s. The degree of T_s is bounded by the original common degree bound.

T_s is a unique canonical quotient representative and contains no e₁. If T_s≠0, let D(s) be its highest homogeneous momentum degree and T_{s,D(s)} its top homogeneous part. This part is not divisible by q: its quotient by q would again be invariant, whereas uniqueness in R[e₁,e₂,e₃,e₄] forbids a nonzero polynomial in e₂,e₃,e₄ from being divisible by e₁.

Thus D(s) is measurable, takes values in a finite set of even integers, and measures genuine quotient degree rather than contact-representative degree.

## 3. The top degree is zero or at least eight

The residue ignores H_s:

    R_{n,s}(k)=T_s(i sqrt(|k|²+s)n+k).

Evenness in normal momentum makes this a real polynomial in k. Its top homogeneous term is

    L_{n,s}(k)=T_{s,D(s)}(i|k|n+k).

Its degree is exactly D(s). An identically zero remainder under u²=−|k|² would imply divisibility by q, already excluded. This works for either representative mirror.

Per-mass nonnegativity gives L_{n,s}(k)=lim_{λ→∞} λ⁻ᴰ⁽ˢ⁾R_{n,s}(λk)≥0. The homogeneous low-degree quotient calculation is:

- There is no nonzero degree-two quotient class.
- At degree four, the class is aQ₄, Q₄=Σp_i⁴. The coordinate ray k=e₁ has residue 2a; the diagonal-difference ray k=(e₀−e₁)/sqrt(2) has residue −2a. Thus a=0.
- At degree six, the class is bQ₆, Q₆=Σp_i⁶. The coordinate ray k=e₁+e₂ has residue −6b; the diagonal transverse ray k=e₂ has residue 3b/4. Thus b=0.

Therefore

    T_s=0, or D(s)=0, or D(s)≥8.

The mass term s changes lower tangential degrees but not this leading obstruction.

## 4. The fixed-mass scaling limit

Fix n=e₀ and any nonzero f≥0 in C_c^∞({t>0}); let f_d(x)=f(x/d). Let a>0 be a lower time-coordinate bound on its support. Set

    Φ_v(ξ)=∫₀∞ exp(−sqrt(|ξ|²+v)t) f̂_z(t,ξ)dt.

A direct change of variables gives

    Q_{n,s}(f_d)
      = d⁶ (2π)⁻³ ∫ R_{n,s}(ξ/d)/(2 sqrt(|ξ|²+d²s))
                         |Φ_{d²s}(ξ)|² dξ.                 (1)

For each fixed mass with nonzero top quotient degree D,

    d^(D−6) Q_{n,s}(f_d) → A_D(s),
    A_D(s)=(2π)⁻³ ∫ L_{n,s}(ξ)/(2|ξ|) |Φ_0(ξ)|² dξ.      (2)

Dominated convergence is used only at one fixed mass. For 0<d≤1,

    |dᴰR_{n,s}(ξ/d)| ≤ C_s(1+|ξ|)ᴰ,
    |Φ_{d²s}(ξ)| ≤ ||f||₁ exp(−a|ξ|),
    1/sqrt(|ξ|²+d²s) ≤ 1/|ξ|.

The resulting bound is integrable in R³. Dependence of C_s on s is harmless because no mass integration is made here.

Moreover A_D(s)>0. The nonzero nonnegative homogeneous polynomial L_{n,s} is positive on an open cone. Φ_0 is continuous at zero with Φ_0(0)=∫f>0. A ball where |Φ_0| is positive meets that cone in positive volume. The integral is finite and strictly positive. A_D is measurable, being a fixed finite linear functional of the measurable coefficients of L_{n,s}.

The same profile f works at every mass; no common cone, common coefficient lower bound or mass-dependent test is needed.

## 5. Fatou excludes all positive-measure nonconstant strata

If T_s is nonconstant on a positive-measure set, there exist one D≥8 and finite M such that

    E={s∈[0,M]: D(s)=D}

has positive μ-measure. Nonnegativity of every full per-mass form gives

    d^(D−6) B_C(θ_nf_d,f_d)
        ≥ ∫_E d^(D−6) Q_{n,s}(f_d) μ(ds).

Fatou and (2) imply

    liminf_{d↓0} d^(D−6) B_C(θ_nf_d,f_d)
        ≥ ∫_E A_D(s) μ(ds) >0.                            (3)

The right side may be infinite. Either way, there exist c>0 and d₀>0 such that

    B_C(θ_nf_d,f_d) ≥ c d^(6−D),     0<d<d₀.              (4)

Other masses cannot cancel this lower bound, since the full per-mass reflected forms are nonnegative. Signed lower terms inside one mass are controlled in its fixed-mass limit before Fatou is applied.

If B_C(θ_nf_d,f_d)=o(d⁻²), the left side of (3) tends to zero for every D≥8. Contradiction. Consequently

    P_s ≡ c_s (mod q+s),     c_s≥0,

almost everywhere. Zero quotient is included by c_s=0.

No spectrum-wide dominated convergence was used. Restricting to bounded mass is legitimate because the actual reflection integrand is nonnegative, and no coefficient bounds on that interval are required.

The little-o boundary is sharp within this class: the massless degree-eight example P=Q₄² has a positive leading reflected coefficient and B_C(θf_d,f_d)=A_f d⁻², while remaining anisotropic away from zero. Thus O(d⁻²) alone cannot replace o(d⁻²).

## 6. Rotation and its exact limit

Set ν(ds)=c_s μ(ds). After quotienting out contacts, every truncated covariance is the O(4)-invariant massive Green mixture ∫(q+s)⁻¹ν(ds).

If C_M+K_M→C distributionally, where C_M is that radial mixture and K_M is supported at zero, then for any orthogonal U,

    C−U_*C = lim_M (K_M−U_*K_M).

Support at zero is closed under distributional limits. Hence C is O(4)-invariant away from the origin. Anisotropic contacts may remain; no complete distributional rotational invariance is asserted.

The ultraviolet hypothesis need only hold on the one selected reflected profile family. Applying this to a source-specific class T(d,c) still requires checking that this profile belongs to that class at the claimed parameter.

## 7. A nonvacuous critical inverse-log example

Define an exact radial momentum multiplier

    F(q)=q² ∫_e^∞ ds / [(q+s)(log s)²],     q≥0.            (5)

It converges, and

    0≤F(q)≤q²∫_e^∞ ds/[s(log s)²]=q².

Thus F defines a positive-type tempered covariance and a centered real stationary Gaussian tempered field, O(4)-invariant as a complete distribution.

This is already an ordinary convergent spectral representation with uniformly degree-four numerator:

    μ(ds)=1_{s≥e} ds/(log s)²,     P_s(p)=q(p)².

Its residue is q²|_{q=−s}=s²≥0 at every orthogonal mirror. It has covariance RP and, by the Gaussian equivalence, full complex Gaussian RP.

The effective constant-residue measure is

    ν(ds)=1_{s≥e} s²/(log s)² ds.

Its unrenormalized Stieltjes integral diverges. The exact identity

    s²/(log s)² [1/(q+s)−1/s+q/s²]
        = q²/[(q+s)(log s)²]                              (6)

gives its twice-subtracted interpretation. Do not separate the individual divergent subtraction integrals. With a finite cutoff M, (6) is an ordinary identity, and both subtractions are polynomial contacts. Cutoff multipliers converge to (5) in tempered distributions, dominated by q²; their separated reflection forms are monotone positive integrals.

### 7.1 An explicit fixed-height profile

A concrete choice is

    ψ(r)=exp(−1/(1−r²)) for |r|<1, and ψ(r)=0 otherwise,
    f(t,z)=ψ(2t−3) ψ(z₁)ψ(z₂)ψ(z₃).

It is smooth, nonzero, nonnegative, and compactly supported with 1≤t≤2. Its scaled support has height comparable to d and fixed amplitude. The reflected pair is disjoint. Membership in additional source-specific test classes is separate.

The calculation below holds for any nonzero nonnegative f∈C_c^∞({t>0}).

### 7.2 Exact scaled pairing

Using Φ_v from §4, put

    J_f(v)=(2π)⁻³ ∫ |Φ_v(ξ)|²/[2 sqrt(|ξ|²+v)] dξ.

J_f is continuous and strictly positive at finite v≥0, and bounded near zero. Since

    sqrt(|ξ|²+v) ≥ (|ξ|+sqrt(v))/2,
    |Φ_v(ξ)|≤||f||₁ exp(−a sqrt(|ξ|²+v)),

we have J_f(v)≤C_f exp(−a sqrt(v)). Therefore

    K_f=∫₀∞ u²J_f(u)du

is finite and strictly positive.

The exact reflected pairing for (5) is

    B_C(θf_d,f_d)
      = d⁶∫_e^∞ s² J_f(d²s)/(log s)² ds
      = ∫_{ed²}^∞ u² J_f(u)/[log(u/d²)]² du.              (7)

### 7.3 Endpoint-safe asymptotic

Let T=log(1/d)→∞. Then

    4T² B_C(θf_d,f_d)
      = ∫_{exp(1−2T)}^∞ u²J_f(u) 4T²/(2T+log u)² du.

Split at u=exp(−T).

On exp(1−2T)≤u<exp(−T), the denominator is at least one and J_f is bounded. This contribution is at most C_f T²exp(−3T)→0.

On u≥exp(−T), the ratio 4T²/(2T+log u)² is at most four and tends to one for fixed u>0. Dominated convergence, with the moving cutoff included as an indicator, applies using 4u²J_f(u).

Consequently

    4 log²(1/d) B_C(θf_d,f_d) → K_f>0,
    B_C(θf_d,f_d) ~ K_f/[4 log²(1/d)].                     (8)

This proves the stated profile-family asymptotic only. It does not establish every upper or lower bound in a Yang–Mills source's entire test class.

## 8. Boundaries and companion results

The ultraviolet argument handles varying quotient degrees, measurable unbounded coefficients, varying angular cones, signed lower-degree terms, contacts, and an unbounded positive mass spectrum.

It does not establish the required representation for interacting Yang–Mills fields, remove contacts, or infer masswise positivity without a spectral-disintegration theorem.

The low-degree quotient and residue calculations come from the independently audited “Sharp degree-eight threshold in a restricted Gaussian spectral class,” especially its §§2, 4–5 and 10.

The companion “Masswise residue positivity for a locally renormalized spectral superposition” supplies the upstream disintegration step under explicit exponential total-variation integrability and contact-cutoff convergence assumptions. The example (5), with P_s=q² and μ(ds)=ds/(log s)² on s≥e, satisfies those assumptions.

No repository was modified, PR merged, or release published.
