# Sharp low-degree single-pole rotation rigidity

Status: written proof and exact algebra checks passed a separate AI-assisted mathematical review. No human peer review, proof-assistant formalization or historical-priority claim. This theorem concerns a restricted Gaussian class, not Yang–Mills existence or the mass gap.

Let d>=3 be an integer, m>0, and P be a real polynomial invariant under all signed coordinate permutations, of total degree at most6. Suppose C(p)=P(p)/(p·p+m²) is a positive tempered scalar Gaussian covariance, reflection positive for the coordinate and diagonal mirrors of W4. Then

P(p)=c+(p·p+m²)Q(p), c>=0.

Consequently C differs from c/(p·p+m²) only by a contact distribution. Its separated-point correlations are rotation invariant. Degree8 is sharp within this single-pole polynomial class.

## Proof

Write s_k=Σp_i^(2k). The fundamental theorem of symmetric polynomials, applied to p_i², implies P mod(s_1+m²)=A+B s_2+C s_3. Fix a unit mirror normal n and tangent momentum q. Write p=q+z n. Polynomial division in z expresses the normal Fourier covariance as a polynomial (contact) plus its two simple poles z=±iE, E²=|q|²+m². Since P is invariant under reflection across n, the remainder is even in z, hence constant in z. The positive-time covariance is therefore

k_q(t)=P(q+iEn)e^(-Et)/(2E), t>0.

Reflection positivity applied to tests localized near tangent momentum q forces P(q+iEn)>=0. Indeed the reflected quadratic form at that momentum is this scalar coefficient times |∫_0^∞ f(t)e^(-Et)dt|². Tangential localization justifies pointwise necessity by continuity.

Put x=r², M=m². To eliminate C, first use n=e0, q=r(e1+e2)/sqrt2; then s_3=-(x+M)^3+x^3/4, leading coefficient -3/4. Next use n=(e0+e1)/sqrt2, q=r e2; then s_3=x^3-(x+M)^3/4, leading coefficient +3/4. Lower-degree terms cannot cancel the leading x³ coefficient. Positivity for all r forces C=0.

To eliminate B, use n=e0,q=r e1, yielding s_2=(x+M)^2+x² with leading coefficient2. Next use n=(e0+e1)/sqrt2,q=r(e0-e1)/sqrt2, yielding s_2=(x²-6x(x+M)+(x+M)²)/2 with leading coefficient-2. Hence B=0. The residue inequality then gives A>=0. This proves the asserted polynomial divisibility.

## Degree-eight example

Let h(p)=Σp_i^4−3(Σp_i²)^2/(d+2) and P=h². P is nonnegative on real momentum, so C is a positive tempered covariance. The real differential operator h(∂) commutes with all W4 mirror reflections. Applying it to the isotropic massive Gaussian free field preserves reflection positivity for each such mirror, giving covariance h(p)²/(p²+m²). Equivalently h(q+iEn) is real for a mirror normal n: reflection sends the complex vector to its conjugate while preserving h. Thus its squared residue is nonnegative.

This covariance is not O4-invariant modulo contact terms. If it were, its residue on the complex mass shell would be constant (radial polynomials restrict there to constants). On p=q+i sqrt(|q|²+m²)e0 with q=r e1, h=2r4+2m²r²+m4(1−3/(d+2)) is nonconstant, and its square is nonconstant. The algebraic justification of this implication is supplied below.

## Scope

Finite-degree single-pole Gaussian covariance only. General spectral measures, non-Gaussian laws, RG limits and nonabelian observables are not covered. Related primary literature is Arici et al., Reflection positivity in higher derivative scalar theories, https://arxiv.org/abs/1712.04308 . Its rational-propagator framework is relevant background; no claim that the present specialization is historically new is made. Engineering-dimension terminology should be defined rather than equated with the true scaling dimension of interacting YM observables.

### Completed algebraic justification of sharpness

If the inverse Fourier kernel were rotationally invariant away from zero, C(Rp)−C(p) would be a polynomial for every real rotation R, because its inverse Fourier distribution is supported at the origin. Therefore P(Rp)−P(p) is divisible by p²+m². Averaging the polynomial P over the compact orthogonal group gives an invariant polynomial P0, and P0−P remains divisible by p²+m² (a finite-dimensional invariant ideal component). Every orthogonally invariant polynomial is a polynomial in p², so P would be constant modulo p²+m². The nonconstant complex-mass-shell evaluation above disproves this. The same proof and sign tests work for every d>=3 (unused coordinates are zero); h may be replaced by s2−3s1²/(d+2), whose square remains a degree-eight example.

The separate review confirms this step. Literature novelty is not established.

## Positivity and test-function conventions

Reflection positivity here means the covariance form with kernel C(theta*x-y) is real and nonnegative for every complex smooth compactly supported test in the open positive half-space. It suffices to assume one coordinate mirror and one diagonal mirror, since W_d covariance transfers them. A tempered positive covariance defines a centered Gaussian random distribution. Contact terms need not themselves be rotation invariant, but do not affect separated-support covariance or reflected tests. If c=0 the reflected one-particle space is trivial; nontriviality is not part of the conclusion.
