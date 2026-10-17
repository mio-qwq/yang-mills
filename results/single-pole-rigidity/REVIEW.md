# Independent audit of the single-pole rotation-rigidity lemma

Reviewed file: `/tmp/ym-root-20261017/single-pole-rigidity.md`, version read 2026-10-17 03:11 UTC.

## Verdict

The argument is correct, including its extension to every integer dimension d>=3 and its degree-eight sharpness claim. This is an independently checked elementary theorem in a restricted rational Gaussian class. It is not a Yang–Mills existence or mass-gap theorem, and no literature-novelty conclusion is made.

## Exact hypotheses that should appear in a final statement

- d>=3, m>0.
- P is a real polynomial of total momentum degree <=6, invariant under the hyperoctahedral group W_d of signed coordinate permutations.
- The multiplier P(p)/(p^2+m^2) defines a tempered scalar Gaussian covariance (in particular, a positive distribution of positive type). This assumption supplies a Gaussian model; the algebraic conclusion itself only uses the reflection-positive quadratic forms.
- Reflection positivity means that the distributional quadratic form with kernel C(theta x-y) is real and nonnegative on complex C_c^infinity tests supported in the open reflected half-space. It suffices to impose this for one coordinate mirror and the mirror with normal (e_0+e_1)/sqrt(2), because W_d invariance transfers these conditions to the other mirrors.
- All assertions modulo contacts concern the covariance away from x=0, or the Gaussian moments at pairwise noncoincident arguments. No claim is made that the complete distribution, including its contact part, is rotation invariant.

## Checked proof steps

1. Sign invariance makes P a symmetric polynomial in p_i^2. Degree <=6 gives a basis 1,s1,s1^2,s2,s1^3,s1 s2,s3, where s_k=sum_i p_i^(2k). In d>=3 these span the needed space; substituting s1=-m^2 gives A+B s2+C s3. Thus this reduction is dimension independent for d>=3.

2. With p=q+zn, mirror invariance gives evenness in z. Division by z^2+|q|^2+m^2 yields a polynomial contact contribution and a remainder independent of z. The remainder is P(q+iEn), E=sqrt(|q|^2+m^2), and is real: conjugation replaces iE by -iE, which is the stipulated reflection.

3. Contact terms disappear in the reflected form, since the two times have sum strictly positive. Tangential Fourier localization is legitimate by first allowing tangential Schwartz tests via compact-cutoff approximation, then localizing their Fourier mass. The relevant coefficient is continuous in q. Hence linear reflection positivity forces P(q+iEn)>=0 pointwise. The factor 1/(2E) is positive.

4. All four sign tests are exact. The cubic-in-x leading coefficients are -3/4 and +3/4, with x=r^2; they force C=0. The quartic-in-momentum terms then have quadratic-in-x leading coefficients +2 and -2, forcing B=0. Positivity finally forces A>=0. Each path uses at most three coordinates, so works unchanged for d>=3.

5. Consequently P=c+(p^2+m^2)Q for real polynomial Q and c>=0. Fourier inversion of Q is supported at the origin. Gaussian Wick moments of pairwise separated insertions depend only on c times the massive free covariance and therefore are rotation invariant. If c=0, the reflected one-particle Hilbert space is trivial; the theorem should not imply nontriviality in that case.

6. For sharpness, h_d(p)=sum_i p_i^4-[3/(d+2)](p^2)^2 is a real W_d-invariant degree-four symbol. The field h_d(partial)phi_m is a well-defined Gaussian derivative field. Its differential operator preserves half-space support and commutes with each W_d reflection, so the free-field reflection-positive quadratic form remains positive. Its covariance is h_d(p)^2/(p^2+m^2), and the multiplier is nonnegative on real p. Thus the degree-eight example is valid.

7. On the mass-shell path n=e_0, q=r e_1, h_d=2r^4+2m^2r^2+m^4[1-3/(d+2)], whose square is nonconstant. The draft's averaging argument rigorously proves this excludes rotation invariance modulo contacts: if the kernel were invariant off the origin, every rotational difference of the multiplier would be polynomial; multiplying by p^2+m^2 and averaging in the finite-dimensional space of polynomials preserves its principal ideal. The average is radial and hence constant on the complex mass shell, contrary to the displayed evaluation.

## Interpretive limitations

The degree bound is a polynomial-symbol bound in a finite-pole model. In four dimensions its superficial Gaussian scaling is compatible with engineering dimension <=4, but it is not an identification with the interacting action-density scaling dimension. Generalized free fields with continuous positive spectral measures, and non-Gaussian theories, are outside the theorem. The manuscript's conditional Yang–Mills limit has not been shown to belong to this rational class. Therefore the theorem supplies a restricted obstruction/rigidity test for proposed mechanisms, not a missing proof of rotation restoration for that limit.

The exact algebra checker is `check_single_pole_rigidity.py`. It passes, but checks only the indicated algebra; the distributional and reflection-positivity steps are justified above, not by that script.
