# Masswise residue positivity for a locally renormalized spectral superposition

Independent analytic audit, 19 October 2026. Local work only. This is a conditional Gaussian spectral-class theorem, not a Yang–Mills assertion.

## Result in brief

Yes: full complex reflection positivity forces the mass-shell residue to be nonnegative at almost every mass, provided the stated spectral presentation actually gives a signed-measure Laplace representation of the separated reflected covariance, with finite total variation after every positive exponential damping. No positivity of the individual mass contributions is assumed.

The cleanest readily checked sufficient hypotheses below are: uniformly finite polynomial numerator degree; integrable coefficient size after every damping `exp(-epsilon sqrt(s))`; and convergence in tempered distributions after polynomial, hence local, counterterms. Under these hypotheses, for each allowed mirror `n`, reflection positivity implies

    P_s(i sqrt(|k|^2+s) n+k) >= 0

for every tangential `k`, simultaneously outside one `mu`-null set of masses. The same null set can serve any finite collection of mirrors, including the coordinate and diagonal representatives.

The word “tempered” by itself must not be substituted for the signed-measure representation or its growth hypothesis. A more general distributional spectral inversion theorem would require additional work and explicit hypotheses.

## 1. Precise checkable theorem

Work in four Euclidean dimensions, and put `q(p)=|p|^2`. Let `mu` be a positive locally finite Borel measure on `[0,infinity)`. Let

    P_s(p)=sum_{|alpha|<=D} a_alpha(s) p^alpha

be real `W_4`-invariant polynomials of one fixed finite maximum degree `D`, with finite measurable coefficients, for `mu`-almost every `s`. Set

    A(s)=sum_{|alpha|<=D} |a_alpha(s)|.

Assume:

**G. Exponentially damped absolute coefficient integrability.** For every `epsilon>0`,

    integral A(s) exp(-epsilon sqrt(s)) mu(ds) < infinity.       (G)

**L. Local renormalization with an actual distributional limit.** There exist real polynomials `K_T(p)` such that, as `T -> infinity`,

    C_hat_T(p) = integral_[0,T] P_s(p)/(q(p)+s) mu(ds) - K_T(p)

converges in `S'(R^4)` to the Fourier transform `C_hat` of the covariance of a centered real stationary Gaussian tempered field. Assume `C` is invariant under the mirrors in question. (The numerator family is already mirror invariant; this last assumption rules out adding an asymmetric limiting contact term.) Ordinary covariance positivity is a hypothesis about this total covariance only.

Then, for each `W_4` mirror with unit normal `n`, the following are equivalent:

1. The centered Gaussian field has full complex reflection positivity at that mirror, using compactly supported smooth tests strictly inside its open positive half-space.
2. Its covariance reflection form is positive semidefinite there.
3. Outside one `mu`-null set, its real polynomial residue

       R_n(k,s) = P_s(i sqrt(|k|^2+s) n+k),    k perpendicular to n,

   is nonnegative for every real `k`.

The implication needed for the extension is `1 => 3`. Conditions G and L are sufficient rather than claimed necessary. A lower-level version requiring only the separated signed-measure formula is in section 6.

## 2. Polynomial division, real residues, and contacts

Write `p=u n+k`. Invariance under the reflection with normal `n` makes `P_s(u n+k)` even in `u`. Thus division in the variable `u^2` gives

    P_s(u n+k) = (u^2+|k|^2+s) B_{n,s}(u,k) + R_n(k,s).       (1)

Both terms on the right are polynomials in real `u,k`; their coefficients are finite measurable functions of `s`. The substitution `u^2=-(|k|^2+s)` shows that `R_n` is a real polynomial in `k` at every mass, with no square-root ambiguity. Uniform degree implies a constant depending only on `D,n` such that

    |R_n(k,s)| <= c A(s) (1+|k|+sqrt(s))^D.                  (2)

For finite `T`, all coefficients in (1) are integrable on `[0,T]` by G. The inverse Fourier transforms of `B_{n,s}` and `K_T` are supported at the spatial origin. Their covariance pairings between `theta f` and `g` vanish when both tests are supported strictly in the positive half-space. This uses genuine local counterterms, meaning polynomials in the full momentum; a general subtraction supported only on a plane, or an arbitrary nonlocal subtraction, is not interchangeable with them.

This argument does not assert that the contact term is separately positive. Nor does it require the separate mass covariance `P_s/(q+s)` to be positive type.

## 3. Derivation and convergence of the separated formula

Use coordinates `x=(t,z)`, with `theta(t,z)=(-t,z)`, and tangential Fourier convention `f_hat_z(t,k)=integral exp(-ik.z)f(t,z) dz`. Write

    omega(k,s)=sqrt(|k|^2+s),
    F_f(k,omega)=integral_0^infinity exp(-omega t) f_hat_z(t,k) dt.

For `omega>0`, the inverse one-dimensional Fourier transform of `(u^2+omega^2)^(-1)` is `exp(-omega |t|)/(2omega)`. Finite-T division and then the distributional limit give

    B_C(theta f,g)
      = (2pi)^(-3) integral_R^3 integral_[0,infinity)
          R_n(k,s)/(2omega(k,s))
          conjugate(F_f(k,omega(k,s))) F_g(k,omega(k,s))
        mu(ds) dk.                                           (3)

The double integral is absolutely convergent. Indeed, if both time supports stay above `delta>0`, then for every integer `N`,

    |F_f(k,omega)| + |F_g(k,omega)|
       <= c_N exp(-delta omega) (1+|k|)^(-N).

Together with (2), `1/omega <= 1/|k|` for `k!=0`, and

    omega >= (|k|+sqrt(s))/sqrt(2),

this is dominated by an integrable function after using G and taking `N` large. Powers of `sqrt(s)` are absorbed by a smaller positive exponential damping. The factor `1/|k|` is locally integrable in three tangential dimensions. Thus the possible atom `(k,s)=(0,0)` causes no problem: the slice `k=0` is Lebesgue null, and the surrounding integrability is explicit.

For the limiting argument, each contact pairing is zero before taking the limit, the noncontact integrals converge absolutely by dominated convergence, and L identifies the distributional limit with the covariance pairing. No exchange of a divergent contact integral with a noncontact integral is used.

Equation (3) also holds when time support remains compact and positive but tangential dependence is Schwartz. Multiply by a smooth tangential cutoff `eta(z/N)` and use convergence in Schwartz space. Covariance continuity gives the left-hand limit; the same estimates give the right-hand limit.

## 4. Tangential localization and extraction of positivity at a fixed momentum

Fix `h in C_c^infinity((0,infinity))`, possibly complex, and define for `k!=0`

    Q_h(k) = integral R_n(k,s)/(2omega(k,s))
                    |L_h(omega(k,s))|^2 mu(ds),
    L_h(omega)=integral exp(-omega t)h(t)dt.

Condition G and the polynomial bound give a dominating integrable function locally uniformly for `k` in any compact set not containing zero. Thus `Q_h` is continuous on `R^3 \ {0}`.

For any smooth compactly supported tangential-frequency function `chi` away from zero, take `g` to be its inverse Fourier transform and `f(t,z)=h(t)g(z)`. This is an allowed limit of compactly supported positive-half-space tests, as explained above. Covariance RP gives

    integral |chi(k)|^2 Q_h(k) dk >= 0.

If `Q_h` were negative at one nonzero `k`, continuity would make it negative on a small ball, contradicting this inequality with a nonzero `chi` supported in that ball. Consequently

    Q_h(k)>=0 for every k!=0 and every h.                     (4)

No masswise positivity was used to establish (4), and no positive/negative mass cancellation has yet been ruled out. That is precisely the role of the next lemma.

## 5. Elementary signed-Laplace-measure positivity lemma

**Lemma.** Let `nu` be a real signed locally finite Borel measure on `[r,infinity)`, `r>=0`, satisfying

    integral exp(-a omega) |nu|(domega) < infinity

for every `a>0`. Suppose

    integral |L_h(omega)|^2 nu(domega) >= 0

for all `h in C_c^infinity((0,infinity))`. Then `nu` is a positive measure.

**Proof.** Fix `t0>0` and `b>0`. Approximate the finitely many point masses at times `t_j=t0+jb`, `j=0,...,m`, by smooth nonnegative unit-integral bumps in positive time. Taking arbitrary complex linear combinations and passing to the limit gives

    integral |sum_(j=0)^m c_j exp(-(t0+jb)omega)|^2
              nu(domega) >= 0.                              (5)

The limit is justified by absolute domination: choose all bump supports within `t_j +/- epsilon` for one `epsilon<t0/2`; their Laplace transforms have absolute value at most `exp(-(t0-epsilon)omega)`, up to the fixed coefficient sum. The assumed exponential variation bound dominates the square.

The measure `eta(domega)=exp(-2t0 omega)nu(domega)` is a finite signed measure. Push it forward under the injective map

    x=exp(-b omega)

to the compact interval `[0,exp(-br)]`, assigning zero mass to the absent endpoint `x=0`. Equation (5) says that the pushed measure integrates `|p(x)|^2` nonnegatively for every complex polynomial `p`.

For every nonnegative continuous function `v` on that compact interval, uniformly approximate `sqrt(v)` by real polynomials. Their squares converge uniformly to `v`; finite total variation allows passage of integrals. Hence the pushed signed measure integrates every nonnegative continuous function nonnegatively and is positive. The map is injective with a Borel inverse on its image, so `eta` is positive. Multiplication by the strictly positive weight `exp(2t0 omega)` then proves that `nu` is positive. QED.

This proof is also an elementary uniqueness/separation argument for the Laplace spectral measure. It avoids presupposing a positive spectral representation and avoids invoking a Bernstein–Widder theorem without checking its hypotheses.

### Apply the lemma to the spectral representation

For each fixed `k!=0`, define

    nu_k = (s -> sqrt(|k|^2+s))_*
              [ R_n(k,s) mu(ds)/(2sqrt(|k|^2+s)) ].            (6)

It is a signed locally finite measure; G and (2) give all positive exponential variation bounds. Equation (4) is exactly the lemma's positivity hypothesis. Therefore `nu_k>=0`.

The map `s -> sqrt(|k|^2+s)` is strictly increasing and has the Borel inverse `s=omega^2-|k|^2` on its image. Positivity of its pushforward is consequently positivity of the measure inside brackets in (6). Since `mu` is positive and the denominator is strictly positive,

    R_n(k,s)>=0 for mu-almost every s, for each fixed k!=0.   (7)

To make the exceptional set independent of `k`, choose a countable dense subset of `R^3 \ {0}` and take the union of its exceptional `mu`-null sets. Outside that union, `R_n(k,s)>=0` on a dense set, and polynomial continuity gives nonnegativity at every real `k`, including zero. Finally take the union over the finitely many mirrors desired. This proves the promised common-null-set conclusion.

### Converse and full Gaussian positivity

Masswise residue positivity makes (3) a positive complex Gram form, so it gives covariance RP. For a reflection-invariant centered Gaussian law, covariance RP is equivalent to full complex Gaussian RP: reflected Weyl Gram matrices are positive diagonal conjugates of the entrywise exponential of the reflected covariance Gram matrix; its positivity follows from the Hadamard-product theorem and its power series. Linear cylinder observables, or their Weyl difference-quotient limits, give the reverse implication. The Gaussian equivalence is exactly the one already established in the single-mass audit.

## 6. Weaker abstract hypotheses and the disintegration issue

The coefficient condition G is convenient, not intrinsic. The same conclusion follows directly from the following lower-level assumptions for each mirror:

- Formula (3) represents the separated reflection form and is absolutely integrable on product tests `h(t)g(z)` with `g_hat` compactly supported away from `k=0`.
- The signed kernels `nu_k` in (6) are measurable in `k`, are locally finite, and obey `integral exp(-a omega) |nu_k|(domega)<infinity` for every `a>0` for Lebesgue-almost every `k`.
- The functions `Q_h` are locally integrable in `k`, so that frequency localization is legitimate.
- For `mu`-almost every `s`, `k -> R_n(k,s)` is continuous; the polynomial family supplies this automatically.

Here `Q_h` need not be continuous. For each time test, tangential localization only proves `Q_h>=0` for almost every `k`. To avoid the invalid intersection of uncountably many full-measure sets, restrict first to a countable family of rational complex linear combinations of smooth delta approximations at the times `1+j`, `j=0,1,...`. The approximating bumps may be chosen from one explicit countable sequence with support in `(1/2,infinity)`. Intersect these countably many full-measure sets, and include the full-measure set where the exponential variation bounds hold for positive rational `a`. Monotonicity then gives all positive real `a`.

At each remaining `k`, pass to the delta limits, then to arbitrary complex coefficients in the finite Gram matrices. The proof in section 5 only needs `t0=b=1`, so this countable family suffices. It gives `R_n(k,s)>=0` for `mu`-almost every `s`, for almost every `k`.

Since `mu` is locally finite and hence sigma-finite, Tonelli applied to the indicator of the measurable set `{(k,s): R_n(k,s)<0}` converts this into: for `mu`-almost every `s`, the residue is nonnegative for Lebesgue-almost every `k`. Its continuity then upgrades this to every `k`. This is the rigorous disintegration/Fubini step. No uncountable-null-set exchange is needed.

If “finite after subtractions” only means conditionally summing a divergent signed integral, these assumptions are not automatic. One must either prove the signed-measure growth and formula, or replace the measure lemma by an appropriate distributional Laplace inversion theorem with its own verified hypotheses. This audit makes no claim that such a replacement is impossible; it is an additional proof obligation.

## 7. An especially simple finite-subtraction sufficient condition

A stronger, common checkable condition is that for some finite `N>=0`,

    integral A(s) (1+s)^(-N) mu(ds) < infinity.               (8)

It implies G. It also supplies an explicit locally renormalized tempered distribution without having to assume its existence separately. Choose an integer `M>=1` with `M+1>=N`, keep the integral over `[0,1)` unchanged, and on `[1,infinity)` replace the integrand by

    P_s(p) [ 1/(q+s) - sum_(j=0)^(M-1) (-q)^j/s^(j+1) ]
      = P_s(p) (-q)^M/[s^M(q+s)].                            (9)

The subtracted expression is polynomial in full momentum at each mass. On real momentum the absolute value of (9) is bounded by

    A(s) (1+|p|)^D q(p)^M s^(-M-1),

which is integrable in mass by (8), and has polynomial momentum growth. The low-mass piece is bounded by a constant times `(1+|p|)^D/q(p)` away from zero; this is locally integrable in four dimensions. The resulting multiplier is tempered, and cutoffs converge in `S'`. One may add any finite polynomial contact term.

The resulting total distribution is not automatically a covariance: its positive-type property must still be checked or assumed. Once it is a reflection-invariant Gaussian covariance, the theorem applies. The subtraction construction establishes the representation and temperateness, not ordinary positivity.

## 8. Sharp scope qualifications and small examples

1. **Distinct masses cannot conceal a negative residue.** At fixed tangential momentum, distinct `s` give distinct `omega`. The Laplace tests separate their spectral weights; positivity of the integrated form is enough to force the aggregate residue at each mass nonnegative.

2. **Coincident masses can cancel before this theorem is applied.** If a different representation indexes contributions by an auxiliary label `lambda`, and several labels have the same mass `s(lambda)`, only their conditional aggregate at that mass is identifiable. RP need not make each auxiliary contribution positive. For example, two copies at the same mass with residues `2` and `-1` sum to a positive residue `1`. In the theorem, `P_s` is already the single aggregate numerator assigned to mass `s`.

3. **The reference measure's positivity matters.** If the base measure were signed, the conclusion would be positivity of `R_n(k,s) mu(ds)`, rather than positivity of the numerical density `R_n` relative to that signed measure. Using a positive base measure (or its total variation with a signed density) removes this ambiguity.

4. **Ordinary covariance positivity does not suffice.** The rotationally invariant function

       1/(q+1) - 1/(q+2) = 1/[(q+1)(q+2)]

   is nonnegative for real momentum and defines a stationary Gaussian covariance. It has a negative residue at mass squared `2`, and it fails RP. At a fixed `k`, choose a positive-time test whose Laplace transform vanishes at `sqrt(|k|^2+1)` but not at `sqrt(|k|^2+2)`; section 4 localization makes the negative reflected form into an actual allowed test. A concrete such time test is `h(t)=phi(t)-exp(a omega_1)phi(t-a)`, where `phi` is a nonzero nonnegative compactly supported positive-time bump and `a>0`. Its Laplace transform is `L_phi(omega)[1-exp(a(omega_1-omega))]`.

5. **Arbitrary local counterterms are invisible to these separated RP tests.** They cannot repair a negative residue. They may repair or impair ordinary covariance positivity and may preserve anisotropy exactly at coincidence.

6. **No atom at zero was silently discarded.** A massless atom is included for every `k!=0`; the measure-theoretic and continuity argument then constrains its polynomial residue at `k=0` as well. Only the undefined displayed factor at the single product point `(0,0)` is omitted from a Lebesgue tangential integral.

7. **No general-field conclusion follows.** Polynomial scalar numerators, the stated local renormalization and signed-measure controls are genuine restrictions. The result does not establish rotational invariance or ultraviolet properties for arbitrary stationary Gaussian measures, matrix-valued fields, interacting theories, or Yang–Mills theory.

## 9. Sources and audit status

The argument is analytic and self-contained. It builds on the polynomial division, contact support, compact-test approximation, and Gaussian equivalence proved in the local single-mass audit:

    /workspace/shared/gaussian-numerator-minimality-audit-20261019/RESULT.md

No external theorem beyond standard measure integration, Fourier transformation, polynomial uniform approximation on a compact interval, and the Gaussian/Hadamard argument is essential. No repository, PR, release, or remote object was changed.
