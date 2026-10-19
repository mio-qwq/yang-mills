# Sharp degree-eight threshold in a restricted Gaussian spectral class

Independent analytic audit, 19 October 2026. No originality claim; no remote changes.

## Result

The proposed degree threshold is correct, with the important qualification that it concerns anisotropy **away from the covariance diagonal** within the specified polynomial-numerator class.

Let

- q(p)=p₀²+p₁²+p₂²+p₃²;
- Q₄(p)=Σᵢpᵢ⁴ and Q₆(p)=Σᵢpᵢ⁶;
- W₄ be the signed permutation group on four coordinates;
- P be a real W₄-invariant polynomial with P(p)≥0 on real momentum space;
- C be the tempered covariance with Fourier transform P(p)/q(p).

This locally integrable, polynomially growing multiplier defines a centered real stationary scalar Gaussian random tempered distribution. Use its ordinary scalar pullback action under reflections. Tests below are smooth compactly supported strictly inside an open reflection half-space; equivalently one may use the corresponding Schwartz test space. “Reflection positivity” means the full complex Gaussian reflection form on same-side cylinder observables, not a real-only or pointwise condition.

**Theorem.** If the total momentum degree of P is less than eight, the following are equivalent:

1. The field has full complex reflection positivity at all sixteen W₄ mirrors.
2. It has covariance reflection positivity at the coordinate mirror with normal e₀ and the diagonal mirror with normal (e₀+e₁)/√2.
3. There are a constant c≥0 and a real W₄-invariant polynomial H of degree at most four such that

       P=c+qH.

In item 3, the standing ordinary-positivity assumption P≥0 is still required. For all these covariances,

       C = c G + H(−i∂)δ₀,
       G(x)=1/(4π²|x|²),

as tempered distributions. Thus C(x)=cG(x) for x≠0. Contact terms may be anisotropic, and are not asserted to vanish or to be positive by themselves.

The degree-eight numerator P=Q₄² is ordinarily positive, W₄-invariant, fully reflection positive at all sixteen mirrors and their affine translates, and genuinely anisotropic off the origin. Consequently eight is the least possible total numerator degree for off-origin anisotropy in this class. W₄ invariance excludes odd momentum degrees, so “degree less than eight” and “degree at most six” are equivalent here.

## 1. Existence and conventions

Set

       f̂(p)=∫e^(−ip·x) f(x) dx,
       B_C(f,g)=(2π)⁻⁴∫conj(f̂(p))ĝ(p) P(p)/q(p) dp.

Near p=0 the multiplier is O(|p|⁻²), which is locally integrable in four dimensions; at infinity it has polynomial growth. Consequently B_C is a continuous positive semidefinite Hermitian form on complex Schwartz space. The evenness P(−p)=P(p) makes it a real covariance on real tests. The characteristic functional exp(−B_C(f,f)/2) constructs the centered real Gaussian tempered field, or may be taken as its definition through the usual Gaussian construction.

All assertions about the whole covariance use this fixed spectral distribution. An off-origin derivative kernel, when singular, is not to be integrated through coincidence as though it were locally integrable.

W₄ invariance of P implies invariance of this covariance and Gaussian law under the sixteen reflections. These mirrors consist of four coordinate normals eᵢ and twelve normals (eᵢ±eⱼ)/√2, i<j. Translation invariance transfers reflection positivity at an origin plane to every parallel affine translate.

## 2. Exact residue criterion, including contacts

Fix a reflection with unit normal n under which P is invariant. Write momentum as

       p=u n+k,     k⊥n,     r=|k|.

Reflection invariance says that P(u n+k) is even in u. Thus it is a polynomial in u² whose coefficients are real polynomials in the tangential coordinates k. Polynomial division by u²+r² gives the exact identity

       P(u n+k)=(u²+r²)A_n(u,k)+R_n(k),
       R_n(k)=P(i r n+k).

The last evaluation is a polynomial in k, not an expression with a genuine square-root ambiguity: every power of u is even, and u² is replaced by −|k|². In particular R_n is real and continuous on real k. A_n is a polynomial in all four real momentum coordinates. Since all terms involved are locally integrable near zero,

       P(u n+k)/(u²+r²)=A_n(u,k)+R_n(k)/(u²+r²)

also holds as tempered distributions, without an additional distribution concentrated at zero momentum.

The inverse Fourier transform of A_n is a finite sum of derivatives of δ at the spatial origin. Its covariance pairing between θf and g vanishes whenever f and g are compactly supported strictly inside the positive half-space: the reflected and unreflected supports are disjoint. This is why polynomial contacts contribute nothing to the reflection form on this test space.

Take coordinates x=(t,z), with n the positive t direction and θ(t,z)=(−t,z). Let f,g∈C_c^∞({t>0}). Write f̂_z for the tangential Fourier transform and set

       F_f(k)=∫₀^∞e^(−rt) f̂_z(t,k)dt.

The one-dimensional inverse Fourier transform of (u²+r²)⁻¹, for r>0, is e^(−r|t|)/(2r). Pairing the contact-free part therefore gives

       B_C(θf,g)
         =(2π)⁻³∫_{R³} R_n(k)/(2|k|) conj(F_f(k))F_g(k) dk.       (1)

One may derive (1) first with tangential Fourier cutoffs away from zero, then remove the cutoffs. At k=0 the factor |k|⁻¹ is locally integrable in three dimensions and R_n is bounded locally. At infinity the positive distance of each test support from t=0 provides exponential decay, in addition to tangential Schwartz decay. These estimates justify the limiting formula. The isolated value k=0 does not require a separate normal-momentum pole prescription.

**Residue criterion.** Covariance reflection positivity at this mirror holds if and only if

       R_n(k)≥0 for every real k⊥n.                              (2)

Sufficiency is immediate from the complex Gram form (1). For necessity, suppose R_n(k₀)<0 somewhere. By continuity, there is a nonempty open ball U away from k=0 on which R_n<0; if k₀=0, use a smaller ball near but not containing zero. Choose a nonzero χ∈C_c^∞(U), and let g be its inverse tangential Fourier transform. Then g is Schwartz. Choose h∈C_c^∞((0,∞)), h≥0, h not identically zero. Its Laplace transform

       L_h(r)=∫₀^∞e^(−rt)h(t)dt

is strictly positive for every r≥0. For f(t,z)=h(t)g(z), equation (1) is strictly negative, since F_f(k)=L_h(|k|)χ(k).

This f has compact positive-time support but only Schwartz tangential support. To obtain a compactly supported test in all coordinates, choose η∈C_c^∞(R³) equal to one near zero and put

       f_N(t,z)=h(t)η(z/N)g(z).

Then f_N→f in Schwartz space, each f_N∈C_c^∞({t>0}), and continuity of B_C implies that B_C(θf_N,f_N)<0 for all sufficiently large N. This contradicts RP on compactly supported tests. Thus (2) is necessary even with that narrower test space. In particular an almost-everywhere positivity conclusion upgrades to pointwise positivity because R_n is polynomial.

This argument uses the complex sesquilinear form explicitly. It makes no unsupported inference from pointwise positivity of C or from same-side ordinary positivity.

## 3. Covariance RP and full Gaussian RP

For a reflection-invariant centered Gaussian law, covariance RP is equivalent to full complex Gaussian RP on the same-side L² cylinder algebra.

One direction follows by taking linear cylinder observables. If the starting definition uses only finite linear combinations of Weyl observables, the linear variables are their L² limits as the real exponential parameter tends to zero; Gaussian second moments justify the limit.

For the other direction, take real positive-side tests f₁,…,f_m. The reflected Weyl Gram matrix is

       M_ij=E[conj(e^(iφ(θf_i)))e^(iφ(f_j))]
           =exp(−B_C(f_i,f_i)/2)
            exp(B_C(θf_i,f_j))
            exp(−B_C(f_j,f_j)/2).

The matrix A_ij=B_C(θf_i,f_j) is positive semidefinite by covariance RP. Its entrywise exponential is positive semidefinite, since

       exp_entrywise(A)=Σ_{ℓ≥0} A^(∘ℓ)/ℓ!,

and every Hadamard power is positive semidefinite; the zeroth is the all-ones matrix. Positive diagonal conjugation gives positivity of M for arbitrary complex coefficients.

Finite linear combinations of Weyl observables are dense in finite-dimensional Gaussian L² cylinder spaces. Reflection invariance and Cauchy–Schwarz give continuity of the reflected form in L². Positivity therefore extends to all square-integrable same-side cylinder observables and their L² closure. Polynomial smeared-field observables are included. This establishes the exact complex-Gaussian meaning used in the theorem, including when the reflected covariance has a nontrivial null space.

## 4. Invariant quotient through degree six

Independent sign changes in W₄ force every exponent of every momentum monomial to be even. Put x_i=p_i². Then P(p)=S(x₀,x₁,x₂,x₃), where S is a real symmetric polynomial of total x-degree at most three.

Let e_j be the elementary symmetric polynomials in the x_i. The complete list of symmetric-generator monomials of total x-degree at most three is

       1;  e₁;  e₁²,e₂;  e₁³,e₁e₂,e₃.

Here q=e₁. The Newton identities in these degrees are

       Q₄=e₁²−2e₂,
       Q₆=e₁³−3e₁e₂+3e₃.

It follows that there are unique real c,a,b and an invariant H of degree at most four in p such that

       P=c+aQ₄+bQ₆+qH.                                      (3)

For example, modulo e₁ the independent nonzero classes are 1, −2e₂ and 3e₃. No degree-two momentum class remains. The invariance of H also follows directly from divisibility: if P−c−aQ₄−bQ₆=qH, applying w∈W₄ and subtracting gives q(H∘w−H)=0 as a polynomial, so H∘w=H.

At a residue evaluation p=i|k|n+k one has q(p)=0. Consequently the contact summand qH contributes zero and

       R_n(k)=c+aQ₄(i|k|n+k)+bQ₆(i|k|n+k).                   (4)

Equation (3), rather than a homogeneous-only ansatz, is why the argument includes arbitrary mixtures of constant, degree-two, degree-four, and degree-six terms.

## 5. Coordinate and diagonal residues

### 5.1 Coordinate mirror

For n=e₀, write k=(0,k₁,k₂,k₃), put A=k₁², B=k₂², C=k₃², and T=A+B+C. Directly,

       Q₄(i√T,k₁,k₂,k₃)=T²+A²+B²+C²,
       Q₆(i√T,k₁,k₂,k₃)=−T³+A³+B³+C³.

The first is positive for k≠0. The second is nonpositive and is strictly negative when at least two of A,B,C are positive.

### 5.2 Diagonal mirror

For n=(e₀+e₁)/√2 and m=(e₀−e₁)/√2, write

       k=v m+w e₂+z e₃,
       A=v², B=w², C=z², S=B+C, T=A+B+C.

Before taking the residue, the first two original momentum coordinates are (u+v)/√2 and (u−v)/√2. Thus

       Q₄=(u⁴+6u²v²+v⁴)/2+w⁴+z⁴,
       Q₆=(u⁶+15u⁴v²+15u²v⁴+v⁶)/4+w⁶+z⁶.

Substitute u²=−T. The exact simplified results are

       Q₄,res=−2A²−2A(B+C)+(3/2)(B²+C²)+BC,                  (5)

       Q₆,res=3(B+C)[A²+A(B+C)+(B−C)²/4].                   (6)

Both formulas in the root candidate are therefore correct. In particular Q₄,res=−2A² on the diagonal-difference axis B=C=0. Equation (6) is nonnegative everywhere and strictly positive on an open set.

### 5.3 Mixed-degree elimination by explicit rays

Residue positivity holds at every k by §2. Scale each of the following transverse vectors by λ>0.

First, use k=e₁ at the coordinate mirror. Its Q₄ and Q₆ residues are 2 and 0, so

       c+2aλ⁴≥0 for every λ>0.

Second, use k=m at the diagonal mirror. Its residues are −2 and 0, so

       c−2aλ⁴≥0 for every λ>0.

Letting λ tend to infinity proves a≥0 and a≤0 respectively, hence a=0. The Q₆ terms vanish on these two rays, so this step does not assume b=0.

Next, use k=e₁+e₂ at the coordinate mirror. Its Q₆ residue is −6. With a=0,

       c−6bλ⁶≥0 for every λ>0,

which forces b≤0. Use k=e₂ at the diagonal mirror. Its Q₆ residue is 3/4, giving

       c+(3/4)bλ⁶≥0 for every λ>0,

which forces b≥0. Thus b=0. Finally the residue is the constant c, and RP forces c≥0.

This proves necessity in the theorem. It also verifies the candidate's alternative order: its coordinate high-degree test forces b≤0 and its diagonal high-degree test forces b≥0, after which the opposite Q₄ signs force a=0. Any statement of the opposite b inequalities would be a sign reversal; the displayed formulas themselves fix the correct directions.

For sufficiency, P=c+qH gives R_n=c at every one of the sixteen mirrors. If the full ordinary-positivity hypothesis P≥0 holds and c≥0, §§2–3 give full Gaussian RP. Conjugacy under W₄ then confirms that the two representative mirrors suffice for all sixteen, although the residue argument already applies individually.

## 6. What ordinary positivity permits for contact terms

There is no independent condition H≥0 when c>0. The exact ordinary-positivity condition is

       c+q(p)H(p)≥0 for every real p.

For example,

       P=1−q+q²=(q−1/2)²+3/4

is positive everywhere, and its covariance is G−δ₀−Δδ₀. Here H=−1+q is negative near p=0, but the entire covariance remains positive type and reflection positive. Thus the contact part is not required to be a positive covariance by itself.

Conversely,

       P=q Q₄

has degree six and covariance Fourier multiplier Q₄. It is a positive pure-contact Gaussian covariance, with zero reflected covariance between separated half-spaces. It is W₄-invariant but not O(4)-invariant as a distribution. Its off-origin covariance is identically zero. Adding a positive c gives cG plus this anisotropic contact. These examples show why the theorem must not assert full-distribution rotational invariance.

A completely explicit ordinary-positivity test is available in degree at most six. Write

       H=h₀+h₁q+h₂q²+h₃Q₄.

For p≠0 put s=q(p)>0 and τ=Q₄(p)/q(p)². Then τ∈[1/4,1], with both endpoints attained, and

       P(p)=c+h₀s+h₁s²+s³(h₂+h₃τ).

Therefore P≥0 on R⁴ is equivalent to

       c+h₀s+h₁s²+m s³≥0 for every s≥0,
       m=h₂+min(h₃/4,h₃).

This is only a convenient restatement of ordinary positivity; the RP argument itself imposes no further constraint on H. When c=0, ordinary positivity does imply H≥0 by division by q for p≠0 and continuity at zero.

## 7. The sharp degree-eight example

Take P=Q₄². It is nonnegative on real momentum space, even, W₄-invariant, and of degree eight. For any W₄ mirror, Q₄ is even in the normal momentum, so its residue is real. Hence

       R_n(k)=[Q₄(i|k|n+k)]²≥0.

The residue criterion and Gaussian equivalence prove full complex RP at all sixteen mirrors. Translation invariance gives all their affine translates. Equivalently, if φ is a massless GFF, ψ=Q₄(∂)φ is a real Gaussian distribution; the local differential operator preserves half-space supports and commutes with these reflections, transporting full RP from φ.

Its covariance is Q₄(∂)²G, smooth away from zero and homogeneous there of degree −10. Here is a short exact certificate that its anisotropy is not confined to contact terms.

Consider the complex vector

       p=(i,1,0,0),

and a real orthogonal rotation R fixing e₀ and e₃ and sending e₁ to (e₁+e₂)/√2. Then

       q(p)=q(Rp)=0,
       Q₄(p)=2,
       Q₄(Rp)=3/2,
       P(p)−P(Rp)=4−9/4=7/4≠0.                              (7)

If C minus its rotated covariance were supported at the spatial origin, its Fourier transform would be a polynomial K. On real p≠0 this would imply

       P(p)−P(Rp)=q(p)K(p).

Both sides are polynomials, so equality on that open real set is a polynomial identity and holds on complex vectors as well. Equation (7) contradicts it. Thus the off-origin covariance is not rotationally invariant. Because this covariance is smooth away from zero, this is also a failure detectable by separated smooth test pairs, not just an abstract distributional distinction.

The separately completed countermodel package gives further real-space formulas, exact rational witnesses, separated-support bounds, and clustering. None of those additional estimates is needed for the degree threshold proved here.

## 8. Counterexample attempts and boundary of the theorem

1. **A lower-degree anisotropic filter.** A W₄-invariant differential filter of degree at most two is a polynomial in q. Its nonconstant part annihilates the massless kernel away from zero. Squaring its symbol cannot give a lower-degree off-origin anisotropic example.
2. **A non-square numerator.** No factorization assumption was used. Every real W₄-invariant degree≤6 numerator is handled by (3), whether or not it is a square or sum of squares.
3. **Mixed degrees masking bad signs.** The four rays in §5.3 eliminate this possibility. In particular the first two kill a without any b contribution; the others kill b. A finite constant cannot offset an unbounded negative λ⁴ or λ⁶ term.
4. **Adding large positive contact terms.** A qH term may repair ordinary positivity of P, but its residue is exactly zero. It cannot repair a negative reflected residue.
5. **A negative residue only on a thin set.** A polynomial residue negative at a point is negative on an open neighborhood. Compact test localization detects it by §2. There is no measure-zero escape.
6. **Using only compactly supported tests.** Schwartz-to-compact tangential cutoffs preserve the negative reflected form, so the localization argument does not secretly enlarge the allowed algebra.
7. **Anisotropic contact terms.** They are genuine allowed examples already in degree six; the theorem deliberately leaves them. A claim of complete distributional rotational invariance would be false.
8. **Other denominators or general fields.** Rational spectral measures with additional poles, non-polynomial numerators, matrix-valued or nonscalar fields, interacting fields, and general stationary Gaussian measures are outside the claim. No threshold is asserted for them.
9. **Boundary-supported tests.** The proof uses smooth tests supported in the open half-space, the standard local-field formulation. It makes no claim about an enlarged algebra containing singular tests supported exactly on the reflection plane, for which contacts may matter.
10. **Yang–Mills and ultraviolet hypotheses.** This degree-eight example is strongly singular and does not satisfy the full Yang–Mills source hypotheses. The degree threshold neither proves that source's outstanding proposition nor refutes its full ultraviolet-controlled implication.

## 9. Exact cone of homogeneous degree-eight classes

There is a stronger classification at the first admissible degree. This section concerns a **homogeneous degree-eight numerator modulo contact terms**. It is not a classification of arbitrary mixed-degree numerators of total degree eight.

The symmetric-generator monomials of total degree four in x_i=p_i² are

       e₁⁴, e₁²e₂, e₂², e₁e₃, e₄.

Modulo e₁=q, the two independent classes can therefore be represented uniquely as

       P₈ ≡ αQ₄²+γe₄ (mod q),
       e₄(p)=p₀²p₁²p₂²p₃².

**Cone classification.** The homogeneous class has nonnegative residues at all sixteen mirrors if and only if

       α≥0,       0≤γ≤48α.                                  (8)

Every class in this cone has an ordinarily positive representative: P₈=αQ₄²+γe₄ is nonnegative on real momentum space. Thus these residue-positive classes are all realizable by Gaussian fields satisfying the stated RP conditions.

For the coordinate mirror, with a,b,c the three nonnegative transverse squared coordinates and S=a+b+c,

       Q₄,res=S²+a²+b²+c²,
       e₄,res=−Sabc.                                        (9)

For the diagonal mirror in §5.2,

       e₄,res=(2A+B+C)²BC/4≥0.                              (10)

Equation (10) follows directly from p₀²p₁²=(u²−v²)²/4 and u²=−(A+B+C).

Necessity of (8) has three exact witnesses:

- At the diagonal-difference axis A=1, B=C=0, the residue is 4α, so α≥0.
- At the diagonal point A=√3−1, B=C=1, formula (5) gives Q₄,res=0 and (10) gives e₄,res=3. The residue is 3γ, so γ≥0.
- At the coordinate point a=b=c=1, Q₄,res²=144 and e₄,res=−3. The residue is 144α−3γ, so γ≤48α.

For sufficiency, both terms in the diagonal residue are nonnegative when α,γ≥0. At the coordinate mirror,

       (S²+a²+b²+c²)²≥48Sabc.                               (11)

For example, a²+b²+c²≥S²/3 and abc≤S³/27 give the inequality. An exact polynomial certificate is stronger and requires no optimization:

       (S²+a²+b²+c²)²−48Sabc
         =2 Σ_pairs(a−b)⁴
          +16 Σ_pairs c(a+b)(a−b)².                         (12)

The sum is over the three unordered pairs from {a,b,c}, and c in each summand denotes the remaining variable. Every displayed term is nonnegative. Using 0≤γ≤48α, (9) is therefore nonnegative. The two reflection conjugacy classes in W₄ exhaust all sixteen mirrors, proving sufficiency. The cone has extremal rays represented by Q₄² and Q₄²+48e₄.

Every nonzero class in this homogeneous cone is anisotropic away from the origin; the following argument applies even without cone positivity. For a homogeneous degree-eight polynomial P₈, averaging its spectral multiplier P₈(p)/q(p) over the compact group O(4) gives κ|p|⁶=κq(p)³ for some real κ. This holds as an equality of tempered distributions, since the multiplier is locally integrable, polynomially bounded, and the compact-group average may be interchanged with pairing against a Schwartz function. The averaged covariance is consequently pure contact.

If the original covariance were rotationally invariant away from zero, its restriction there would equal the restriction of its rotational average and hence vanish. It would be supported at zero. The Fourier transform of a distribution supported at one point is a polynomial K; equality with P₈/q on real p≠0 would give the polynomial identity P₈=qK. This contradicts a nonzero quotient class. Thus every nonzero class in (8) is genuinely off-origin anisotropic, not merely anisotropic in its spectral representative.

For a general mixed-degree-eight P, (8) is a necessary condition on its top nonzero degree-eight quotient class, obtained by large-momentum scaling of the residues. It is not by itself sufficient for all lower-degree terms, which may still make the total residue negative at finite momentum. The preceding low-degree theorem and homogeneous cone result do not conflate these two problems.

## 10. A restricted scaling consequence

The following observation concerns only the finite polynomial-numerator class. It does not make a claim about the full Yang–Mills hypotheses or about other spectral denominators.

Let P have any finite degree and satisfy the original ordinary positivity, W₄ invariance, and all-sixteen RP conditions. Remove all q-multiples, grading the remaining quotient class by homogeneous momentum degree. If the class is nonzero, let D be its largest nonzero homogeneous degree.

At any W₄ mirror the residue of that homogeneous component is a nonzero homogeneous polynomial of degree D. To see that it is nonzero, recall polynomial division in §2: an identically zero remainder at even one such mirror is equivalent to divisibility of that component by q. Nonnegativity of the total residue and the limit λ→∞ show that the leading residue is nonnegative everywhere. The degree≤6 necessity argument, which used residue positivity and did not require ordinary positivity of the representative, now implies

       D=0 or D≥8.

Choose any nonzero nonnegative f∈C_c^∞({t>0}); a smooth radial bump centered sufficiently far inside the half-space is one option. Define f_d(x)=f(x/d), and take its reflection as the negative-side test. The Fourier–Laplace transform F_f tends to the strictly positive total integral of f as k→0. A nonzero nonnegative homogeneous leading residue is positive on some open cone. That cone meets arbitrarily small neighborhoods of zero. Consequently its coefficient in the reflected pairing (1) is strictly positive.

Homogeneity, or the direct change of variables k→k/d in (1), gives the finite expansion

       B_C(θf_d,f_d)=Σ_j A_j d^(6−j),      A_D>0,             (13)

where j ranges over the nonzero homogeneous quotient degrees; contacts contribute zero. Hence

       B_C(θf_d,f_d) ~ A_D d^(6−D) as d↓0.

If D=0, this is a positive constant times d⁶. If D≥8, it diverges at least as fast as d⁻². If the entire quotient vanishes, the reflected pairing is identically zero. None of these possibilities is comparable, above and below by positive constants, to (1+log(1/d))⁻² along this fixed-height profile family.

This carefully distinguishes upper and lower requirements: a noncontact D≥8 component violates a decaying inverse-logarithmic upper bound on this reflected profile; a massless D=0 component can satisfy such an upper bound but fails a positive inverse-logarithmic lower bound. Applying the observation to a particular source's quantitative test class additionally requires checking that the chosen profile belongs to that class. The previously completed countermodel does that for its explicit bump at the stated parameter; this audit does not silently extend that test-class verification to an unspecified parameter.

## 11. Audit status and reproducibility

The proof above is analytic and self-contained. The accompanying standard-library checker independently expands the two diagonal residues, verifies the low-degree Newton identities, checks all four forcing rays, verifies the degree-eight cone witnesses and its nonnegative polynomial certificate, and checks the exact complex-null anisotropy witness using rational squared coordinates. It does not certify functional analysis or Gaussian RP; those arguments are supplied in §§1–3.

Run:

       python check_exact.py

The checker writes CHECKS.json. Input file hashes and exact local source paths are recorded in SOURCE_MANIFEST.json. No source repository was modified, no PR merged, and no release published.
