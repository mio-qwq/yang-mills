# Uniform spectral degree is unnecessary: a precise extension and its boundary

19 October 2026. Local analytic research only. This is a conditional scalar spectral-class theorem, not a construction or verification of a Yang–Mills field.

## Main conclusions

1. **Finite degree at almost every mass is enough.** The ultraviolet rigidity theorem does not require a common finite degree bound. Its Fatou argument only needs the countable stratification by genuine quotient degree.
2. **Uniform degree can also be removed upstream.** An increasing finite-degree spectral exhaustion, a genuine tempered-distribution limit modulo local contacts, and locally exponentially integrable signed residues suffice to extract masswise positivity from reflection positivity. In fact, one sufficiently strong exponential damping on each compact frequency annulus suffices; see Section 3.1. Full global reflected-form integrability then follows by monotone convergence, rather than an unproved interchange of unbounded-degree differential operators and spectral integration.
3. **An additional automatic bound is available.** Once the nonnegative spectral reflection formula holds, if the covariance has distribution order `m` near the origin, its genuine quotient degrees satisfy `D(s) <= m+2` almost everywhere. Thus a tempered covariance cannot retain unbounded genuine quotient degree in this class, even before imposing the ultraviolet bound. Original numerator degrees may remain unbounded in contact components.
4. **The original coefficient damping condition is not enough without a degree bound.** An explicit positive-residue family below satisfies all exponential damping conditions on its coefficient norm, but its separated forms diverge. Such divergence cannot be repaired by local contacts.

The remaining substantive restriction is the polynomial-at-each-mass spectral representation with a justified signed-measure Laplace interpretation and local renormalized limit. A common degree bound is not an independent escape route under these weaker hypotheses.

## 1. Precise assumptions without a uniform degree bound

Put `q(p)=|p|^2` on `R^4`. Let `mu` be a positive locally finite Borel measure on `[0,infinity)`. For `mu`-almost every `s`, let

    P_s(p) = sum_alpha a_alpha(s) p^alpha

be a real `W_4`-invariant polynomial of finite degree, allowed to depend without bound on `s`. The countably many coefficient functions are measurable; only finitely many are nonzero at each admissible `s`. Define

    A(s) = sum_alpha |a_alpha(s)| < infinity.

Let `n` be either `e_0` or `(e_0+e_1)/sqrt(2)`. Write `p=un+k`, `k perpendicular to n`, and define

    omega_n(k,s) = sqrt(|k|^2+s),
    R_n(k,s) = P_s(i omega_n(k,s)n+k).

Reflection invariance makes `P_s(un+k)` even in `u`. Consequently `R_n` is a real polynomial in `k`, with measurable coefficients in `s`; the displayed square root does not create a branch ambiguity.

Assume the following.

### E: finite-stage spectral exhaustion

There are increasing measurable sets `E_j` whose union has full `mu` measure, with

    E_j subset [0,M_j],
    deg P_s <= d_j on E_j,
    integral_(E_j) A(s) mu(ds) < infinity,

where `M_j,d_j` are finite and may tend to infinity. No lower bound on the positive masses is imposed. Define the finite-stage tempered multiplier

    F_j(p) = integral_(E_j) P_s(p)/(q(p)+s) mu(ds).

Its existence is elementary: away from `p=0`, its absolute value is bounded by a finite constant times `(1+|p|)^(d_j)/q(p)`, and `1/q` is locally integrable in four dimensions.

There are polynomials `K_j(p)` such that

    F_j - K_j -> C_hat in S'(R^4).                         (E)

Here `C` is a Hermitian, stationary tempered two-point distribution, reflection invariant at the mirrors under consideration. Ordinary positive type is additionally required if `C` is to be a covariance of a Gaussian field. The proof of the two-point assertion itself needs only the stated distribution and reflection forms; we use covariance-pairing notation for it.

Every measurable finite-degree family admits an exhaustion with the finite-stage bounds, for example

    E_j = {s<=j, deg P_s<=j, A(s)<=j}.

However, convergence in (E) along such an exhaustion is an actual additional assumption. It is not inferred from a conditionally summed integral or from the word “renormalized.” The theorem permits any exhaustion satisfying the displayed properties. If another cutoff prescription was originally given, its agreement with (E) must be checked.

### R: local exponential total-variation control of residues

For the two representative mirrors, every `a>0`, and every compact set `K` contained in the tangential space with `0` removed, assume

    integral_K integral_[0,infinity)
        exp(-a omega_n(k,s)) |R_n(k,s)|/(2 omega_n(k,s))
        mu(ds) dk < infinity.                             (R)

This is a joint local condition on actual residues, not a spectrum-wide common polynomial degree bound. The exclusion of `k=0` is convenient for signed-measure extraction only; no zero-momentum spectral contribution is discarded in the final reflection formula.

### RP and UV

Assume complex covariance reflection positivity at the two representative mirrors for compactly supported smooth tests strictly inside the corresponding positive half-space. Full complex Gaussian RP implies this assumption, and conversely follows from covariance RP for a reflection-invariant centered Gaussian law.

For the rigidity conclusion, fix any nonzero nonnegative

    f in C_c^infinity({x_0>0}),    f_d(x)=f(x/d),

and assume

    B_C(theta_0 f_d,f_d) = o(d^(-2)) as d downarrow 0.      (UV)

### Theorem

Under E, R and RP:

- outside one `mu`-null set, `R_n(k,s)>=0` for every real `k` and both representative mirrors;
- for every compact smooth positive-half-space test, its reflected form is the finite nonnegative spectral integral of the individual massive residue forms;
- if `C` has distribution order `m` near the origin, the canonical quotient degree satisfies `D(s)<=m+2` almost everywhere.

If UV also holds, then

    P_s(p) = c_s + (q(p)+s) H_s(p),    c_s>=0,

for `mu`-almost every `s`. In particular `C` is `O(4)`-invariant away from the origin. No conclusion removes anisotropic contact terms.

The original uniformly bounded-degree theorem is a special case: take `E_j=[0,j]`; its coefficient damping condition implies R and local coefficient integrability. Thus this is a genuine extension, with a more intrinsic integrability hypothesis.

## 2. Finite-stage division and contact separation

At each mass and mirror, polynomial division in `u^2` gives

    P_s(un+k) = (u^2+|k|^2+s) B_{n,s}(u,k)+R_n(k,s).

On `E_j`, the degree, mass and integrated coefficient size are bounded. Therefore every coefficient of `B_{n,s}` and `R_n` is integrable over `E_j`, and their integrals are genuine finite polynomials.

The inverse Fourier transforms of `integral_(E_j) B_{n,s} mu(ds)` and `K_j` are supported at the spatial origin. Their pairings between a reflected negative-half-space test and a positive-half-space test vanish exactly, before any limit.

For a finite-stage test `g` supported in positive time, define

    L_g(k,omega) = integral_0^infinity exp(-omega t) g_hat_z(t,k) dt.

The elementary one-dimensional transform of `(u^2+omega^2)^(-1)` gives

    B_(F_j-K_j)(theta_n g,g)
      = (2pi)^(-3) integral_R^3 integral_(E_j)
          R_n(k,s)/(2omega_n(k,s)) |L_g(k,omega_n(k,s))|^2
          mu(ds) dk.                                      (1)

For finite stage, this is absolutely integrable by the ordinary fixed-degree estimate. A massless atom is harmless: `1/omega<=1/|k|`, locally integrable in three dimensions. The single displayed undefined point `(k,s)=(0,0)` has zero tangential Lebesgue measure.

Equation (1) also holds for compact positive-time, tangentially Schwartz tests. Such tests are limits in Schwartz space of compact positive-half-space tests, obtained by smooth tangential spatial cutoffs. This observation also extends the RP inequality to these tests.

At this point no infinite sum of contact distributions has been formed. There is no reason for that contact sum to converge separately, and it is unnecessary.

## 3. Signed spectral positivity from only local frequency control

Take a product test `g(t,z)=h(t)v(z)` with `h` smooth, compactly supported in positive time, and `v_hat=chi` smooth and compactly supported away from `k=0`. If the lower time-support bound is `delta>0`, then

    |L_h(omega)| <= ||h||_1 exp(-delta omega).

Condition R dominates (1) on the compact support of `chi`. The finite-stage distributional limit E and ordinary dominated convergence therefore give

    B_C(theta_n g,g)
      = (2pi)^(-3) integral |chi(k)|^2 Q_h(k) dk,
    Q_h(k) = integral R_n(k,s)/(2omega_n(k,s))
                       |L_h(omega_n(k,s))|^2 mu(ds).        (2)

The function `Q_h` is locally integrable away from zero. RP and arbitrary frequency localization imply `Q_h(k)>=0` for almost every `k`. Continuity in `k` is not assumed or needed here.

### The countability issue

Use the countable family of time tests consisting of rational complex linear combinations of smooth unit-mass bumps tending to delta masses at the times

    1,2,3,... .

Choose all bump supports in `(1/2,infinity)`. Intersect the full-measure sets from (2) for this countable family. Also intersect the full-measure sets on which all the positive rational exponential variation bounds supplied by R hold. Rational damping parameters imply every positive real damping parameter by monotonicity.

At each remaining `k`, define the signed measure

    nu_k = (s -> sqrt(|k|^2+s))_*
        [R_n(k,s) mu(ds)/(2sqrt(|k|^2+s))].                 (3)

It is locally finite and has finite total variation after any positive exponential damping. The latter follows from R by Tonelli, first on a countable cover of tangential annuli. The local-finiteness assertion follows since exponential weights are bounded below on bounded energy intervals.

Passing from bumps to the time delta masses is dominated by a fixed positive exponential damping. Passing from rational to arbitrary complex coefficients is continuity of a finite Gram form. Consequently

    integral |sum_(l=0)^N c_l exp(-(1+l)omega)|^2
        nu_k(domega) >= 0                                  (4)

for all finite complex coefficient vectors.

### Elementary signed-measure lemma

Set `eta_k(domega)=exp(-2omega)nu_k(domega)`, a finite signed measure, and push it forward under `x=exp(-omega)` to the compact interval `[0,exp(-|k|)]`, assigning zero mass to the absent endpoint zero. Equation (4) says that the resulting signed measure integrates `|p(x)|^2` nonnegatively for every polynomial `p`.

For every nonnegative continuous `v`, uniformly approximate `sqrt(v)` by real polynomials. Their squares converge uniformly to `v`, so finite total variation gives a nonnegative integral of `v`. Hence the pushed measure is positive. The map `omega -> exp(-omega)` is injective and has a Borel inverse on its image, and the damping weight is strictly positive. Thus `nu_k` is positive.

The map `s -> sqrt(|k|^2+s)` is also injective. Since `mu` is positive, (3) implies `R_n(k,s)>=0` for `mu`-almost every `s`, for almost every `k`.

Apply Tonelli to the measurable indicator of `{(k,s):R_n(k,s)<0}`. Local finiteness makes `mu` sigma-finite, so for `mu`-almost every `s`, the residue is nonnegative for Lebesgue-almost every `k`. Its polynomial continuity upgrades this to every `k`, including zero. A finite union of null sets handles both representative mirrors. `W_4` invariance transfers the conclusion to every `W_4` mirror.

This proof does not intersect uncountably many exceptional sets and does not assume per-mass positivity before deriving it.

### 3.1 Sharper hypothesis: one late-time damping per annulus suffices

The theorem remains valid if R is replaced by the strictly weaker condition

    for each compact K subset R^3 without zero, there exists a_K>0 with
    integral_K integral exp(-a_K omega_n(k,s))
        |R_n(k,s)|/(2omega_n(k,s)) mu(ds) dk < infinity.     (R_late)

It is enough to impose this on the countable annular exhaustion

    K_l={k: 1/l <= |k| <= l},    l=2,3,... .

Here is the complete modification. For each `l`, choose `t_l>a_(K_l)/2+1`. Use only the countable time-bump tests approaching delta masses at `t_l,t_l+1,t_l+2,...`, with bump half-width less than `1/2`. Their squared Laplace transforms, and their delta limits, are bounded by a constant times `exp(-a_(K_l) omega)`. Thus (2) and its RP consequence hold on the interior of `K_l` for this countable family. Tonelli gives the same single exponential variation bound for almost every individual `k` there.

The signed measure (3) is locally finite. The bump limits now give

    integral exp(-2t_l omega) |p(exp(-omega))|^2 nu_k(domega)>=0.

Its damped measure `exp(-2t_l omega)nu_k` has finite total variation. The compact-interval polynomial-square proof applies unchanged and makes `nu_k` positive. A countable union over annuli covers all nonzero tangential momenta, after which the original Tonelli/continuity argument gives masswise positivity everywhere.

All subsequent steps remain unchanged. In particular, Section 4 reconstructs every compact positive-half-space test, including tests at arbitrarily early positive times, by monotone convergence and E. Thus those early-time integrals need not be assumed absolutely convergent before positivity is extracted. No inference of early-time convergence is made from late-time damping alone.

In fact R then follows a posteriori. Given a compact annulus `K` and any `a>0`, choose a smooth frequency cutoff equal to one on `K` and a nonzero nonnegative time test supported in `(0,a/2)`. Its Laplace transform is at least `||h||_1 exp(-a omega/2)`. The finite full spectral formula bounds the integral of `exp(-a omega)R/(2omega)` over `K`; residue positivity makes this exactly the absolute-variation bound in R.

## 4. Recovering the global reflected integral by monotone convergence

After Section 3, every integrand on the right of (1) is nonnegative outside a single mass-null set. Fix an arbitrary compact smooth positive-half-space test `g`, with no frequency-support restriction. The sets `E_j` increase to full measure, so monotone convergence gives

    lim_j B_(F_j-K_j)(theta_n g,g)
      = integral Q_(n,s)(g) mu(ds),                         (5)

where

    Q_(n,s)(g) = (2pi)^(-3) integral_R^3
        R_n(k,s)/(2omega_n(k,s)) |L_g(k,omega_n(k,s))|^2 dk
      >= 0.

Distributional convergence E identifies the left side with the finite number `B_C(theta_n g,g)`. Thus the full nonnegative spectral integral is finite and equals that covariance pairing. The same proof applies to compact positive-time, tangentially Schwartz tests, since their correlation tests are Schwartz and E is convergence in `S'`.

This is also why no low-frequency defect is hidden by the annular localization in Section 3. Once masswise positivity is known, (5) recovers the original compact test, all tangential frequencies, and any massless atom directly from finite-stage identities. We do not incorrectly claim that frequency cutoffs vanishing near zero converge to one in the Schwartz topology.

No global absolute-residue estimate, common polynomial degree, or mass-uniform bound on derivatives was used in this step.

## 5. Countable degree strata and the ultraviolet theorem

Let `e_i` be the elementary symmetric polynomials in `p_0^2,...,p_3^2`, so that `e_1=q`. The invariant ring is

    R[p_0,...,p_3]^(W_4) = R[e_1,e_2,e_3,e_4].

For each mass write `P_s=S_s(e_1,e_2,e_3,e_4)` and choose the canonical quotient representative

    T_s = S_s(-s,e_2,e_3,e_4).

Then `P_s=T_s+(q+s)H_s`. These transformations are finite algebraic operations on each degree stratum, hence give measurable coefficient functions over the countable union of strata. If `T_s` is nonzero, write `D(s)` for its highest homogeneous momentum degree and `T_(s,D)` for that part; set `D(s)=-infinity` when `T_s=0`.

The top part is not divisible by `q`: a nonzero polynomial in `e_2,e_3,e_4` cannot be divisible by `e_1` in the invariant polynomial ring. Consequently, for either representative mirror,

    L_(n,s)(k) = T_(s,D(s))(i|k|n+k)

is a nonzero homogeneous polynomial of degree `D(s)`. Otherwise division in normal momentum would make the top part divisible by `q`. It is nonnegative, since it is the leading scaling limit of the nonnegative full residue.

### The degree-eight threshold is masswise

There is no degree-two quotient class. At degree four the quotient class is `a Q_4`, where `Q_r=sum_i p_i^r`. The coordinate ray `k=e_1` gives `2a`, whereas the diagonal-difference ray `k=(e_0-e_1)/sqrt(2)` gives `-2a`; hence `a=0`.

At degree six the class is `b Q_6`. The coordinate ray `k=e_1+e_2` gives `-6b`, whereas the diagonal transverse ray `k=e_2` gives `3b/4`; hence `b=0`.

Thus a nonzero canonical quotient has degree zero or degree at least eight. These are single-mass algebraic facts and do not require a common degree bound.

### Fixed-mass scaling

For the fixed nonzero nonnegative profile in UV, define

    Phi_v(xi) = integral_0^infinity
        exp(-sqrt(|xi|^2+v)t) f_hat_z(t,xi) dt.

A change of variables gives

    Q_(0,s)(f_d) = d^6 (2pi)^(-3) integral
        R_0(xi/d,s)/(2sqrt(|xi|^2+d^2s)) |Phi_(d^2s)(xi)|^2 dxi.

At each fixed mass of quotient degree `D`, ordinary dominated convergence yields

    d^(D-6) Q_(0,s)(f_d) -> A_D(s),
    A_D(s) = (2pi)^(-3) integral
        L_(0,s)(xi)/(2|xi|) |Phi_0(xi)|^2 dxi > 0.         (6)

For completeness, if `a>0` bounds the time support below, an integrable fixed-mass dominator is

    C_s (1+|xi|)^D exp(-2a|xi|)/|xi|.

The nonzero nonnegative polynomial `L` is positive on an open cone. Also `Phi_0` is continuous at zero and `Phi_0(0)=integral f>0`. This proves strict positivity of (6), using the same profile at every mass. The constants may depend on `s`; there is no masswise dominated-convergence claim.

### Countability is sufficient

If nonconstant quotients occur on a positive-measure set, the countable union over finite degrees contains a stratum `{D(s)=D}`, `D>=8`, of positive measure. Intersect with `[0,M]` for some finite `M` if desired. Call the resulting set `E`.

By (5), nonnegativity, and Fatou,

    liminf_(d->0) d^(D-6) B_C(theta_0 f_d,f_d)
      >= integral_E A_D(s) mu(ds) > 0.                     (7)

The right side may be infinite, which strengthens the contradiction. Thus some `c,d_0>0` satisfy

    B_C(theta_0 f_d,f_d) >= c d^(6-D),    0<d<d_0.

UV makes the left side of (7) zero for every `D>=8`. Therefore all nonconstant strata are null. The remaining constant residue is nonnegative by Section 3. This proves `P_s=c_s+(q+s)H_s` almost everywhere.

The little-o threshold remains sharp: the single-mass polynomial `P=Q_4^2` at mass zero has nonnegative residues at all `W_4` mirrors and reflected scaling exactly `A_f d^(-2)`, with a nonconstant quotient. The extension does not turn `O(d^(-2))` into a sufficient bound.

## 6. Temperedness already bounds genuine degrees

There is a useful independent consequence before imposing UV. Let `m` be an order bound for `C` on a compact neighborhood of zero. For the fixed profile, write the reflected pairing as a distribution pairing against its correlation test. Under `f_d(x)=f(x/d)`, that correlation test has the form

    psi_d(x)=d^4 psi(x/d),

where `psi` is one fixed compactly supported smooth function. All the supports for sufficiently small `d` lie in the chosen neighborhood. The definition of distribution order therefore gives

    |B_C(theta_0 f_d,f_d)|
      <= const max_(|alpha|<=m) ||partial^alpha psi_d||_infinity
      <= const d^(4-m).                                    (8)

If a degree stratum `D>m+2` had positive measure, its lower bound from (7) would contradict (8): multiplying (8) by `d^(D-6)` gives an upper bound tending to zero. Hence

    D(s) <= m+2 for mu-almost every s.                      (9)

Every distribution on all of `R^4` has finite order on any fixed compact neighborhood, so temperateness is stronger than needed for this particular consequence. This is an essential degree bound on the quotient, not on arbitrary numerator representatives and not on separately divergent contact polynomials.

The integer `m` is any valid local order bound; it need not be optimal. For every fixed positive `d`, the reflected correlation test `psi_d` vanishes on a neighborhood of zero because its two source supports are strictly separated. The neighborhood shrinks with `d`, but every origin-supported contact still pairs to exactly zero for every `d`. A single fixed compact neighborhood supplies the common distribution estimate (8); no uniform positive separation is needed. An anisotropic contact may increase a chosen order bound `m`, which only weakens (9), and cannot invalidate it.

This consequence is downstream of the signed-measure extraction and nonnegative reflection formula. Finite distribution order alone is not used to bootstrap residue positivity or justify a missing spectral disintegration. The argument would not apply if only a distribution off the origin were supplied, with no extension of finite order through the origin.

## 7. Rotations and contacts without exchanging divergent sums

After UV, finite-stage algebra gives

    F_j(p) = integral_(E_j) c_s/(q(p)+s) mu(ds) + H_j(p),

where `H_j` is a polynomial. Each first term is radial. If `U` is orthogonal, then

    (F_j-K_j) - U_*(F_j-K_j)

is a polynomial in momentum, hence a point-supported distribution in position. By E these differences converge to `C-U_*C` in distributions. Distributions supported at the origin form a closed subspace: they vanish on every test supported off the origin, and this property passes to the limit. Thus `C-U_*C` is supported at zero.

This argument does not require either `H_j` or `K_j` to converge separately, does not define an infinite-order derivative of delta, and does not require an unsubtracted radial Stieltjes integral to converge.

## 8. Explicit boundary examples

### 8.1 Unbounded numerator degrees really are allowed

Let

    mu = sum_(j>=1) 2^(-j) delta_(j^2),
    Q_4(p) = sum_(i=0)^3 p_i^4,
    H_j(p)=4^(-j) Q_4(p)^j,
    P_(j^2)(p)=1+(q(p)+j^2) H_j(p).

The numerator degrees `4j+2` are unbounded. Its monomial coefficient norm is at most `j^2+5`, so even the original exponential coefficient damping condition holds. Take finite stages `1<=j<=N` and subtract

    K_N(p)=sum_(j=1)^N 2^(-j) H_j(p).

Then exactly

    F_N-K_N = sum_(j=1)^N 2^(-j)/(q+j^2)
      -> sum_(j>=1) 2^(-j)/(q+j^2)

as tempered multipliers. The limit is an ordinary nonnegative radial covariance with RP at every mirror. Every residue is one, so R holds immediately. Its reflected scaling is `O(d^6)`, hence satisfies UV.

This example shows that the unbounded-degree extension is nonempty. Its high degrees are contact contributions. The contact series need not be given any separate distributional meaning; finite-stage cancellation is exact.

### 8.2 Coefficient damping alone fails once degree varies

Keep `mu=sum_(j>=1)2^(-j)delta_(j^2)`, but take

    P_(j^2)(p) = 16^(-j) Q_4(p)^(2j).

Its degree is `8j`, its coefficient norm is exactly one, and therefore

    integral A(s) exp(-epsilon sqrt(s)) mu(ds)<infinity

for every `epsilon>0`. Every individual numerator is nonnegative on real momentum. At every `W_4` mirror its residue is an even power of a real polynomial, hence nonnegative.

At the coordinate mirror,

    R_0(k,j^2) = 16^(-j) [(|k|^2+j^2)^2+sum_i k_i^4]^(2j)
      >= 16^(-j) j^(8j).

On any fixed nonempty compact tangential annulus, `omega~j`, so the weighted residue terms in R grow at least as a constant times

    j^(8j) exp(-a j)/(32^j j).

They do not even tend to zero. Condition R fails maximally.

More concretely, choose a nonnegative product test `f(t,z)=h(t)g(z)` with `h` supported in a fixed interval `(a,T)` and `g_hat` bounded below by a positive constant on a small annulus. Then `L_h(omega)>=||h||_1 exp(-T omega)`, and the nonnegative finite-stage reflected pairings diverge. Local contact counterterms vanish on this pairing, so no choice of such counterterms can make the finite stages converge to a distribution on all of `R^4`.

This is a counterexample to retaining the old coefficient-damping estimate as a substitute for the old common-degree bound. It is not a counterexample to the rigidity theorem: it has no required covariance limit and no UV bound.

### 8.3 Even excellent separated damping does not produce a distributional extension

In the preceding family replace `2^(-j)` by `exp(-j^3)`. Now R holds, and every strictly separated reflected form is finite: for fixed separation, the relevant residue integrals grow at most `exp(O(j log j))`, from the polynomial coefficients and the gamma integrals of `|k|^(8j) exp(-a|k|)`, while the weight is `exp(-j^3)`.

Nevertheless no contact-renormalized limit can exist as a distribution through the origin. The canonical quotient of `Q_4^(2j)` has genuine degree `8j` and positive spectral weight for every `j`. If such a limit existed, Section 6 would bound these degrees essentially, a contradiction. Equivalently, the separated reflected form grows faster than every fixed inverse power along the small-scale profile family: for any chosen power, select one sufficiently large fixed `j` and use its positive lower bound.

This illustrates that local residue integrability and positivity do not imply a tempered, or even finite-order local, extension at coincidence. E is a separate hypothesis. It also cannot evade UV.

## 9. Exact remaining scope

- No anisotropic counterexample satisfying E, R, RP and UV can be obtained merely by allowing a finite but unbounded polynomial degree at different masses.
- Coincident-mass auxiliary contributions must be aggregated first; only their aggregate residue is identified by the Laplace argument.
- Infinite power series or nonpolynomial numerators at one fixed mass are not covered by countable degree stratification. Nor are merely conditional signed spectral sums without R or an alternative rigorously proved uniqueness/inversion theorem.
- A representation valid only off the origin does not automatically supply E or a finite-order extension through the origin.
- The theorem does not establish this spectral class for actual interacting Yang–Mills limits, tensor fields, or general stationary random fields. That remains a separate applicability problem.
- All manipulations were local. No remote repository, PR, release, or published object was changed.

## Companion inputs

This proof extends and explicitly replaces the uniform-degree uses in:

- `/workspace/shared/spectral-rp-residues-20261019/RESULT.md`
- `/workspace/shared/spectral-uv-rotation-20261019/RESULT.md`

The key new steps are the locally controlled signed-residue extraction followed by global monotone reconstruction, the countable-stratum formulation, and the automatic finite-order quotient-degree bound. The proof is self-contained apart from standard Fourier/distribution facts, Tonelli/Fatou/dominated convergence, polynomial uniform approximation on a compact interval, and the invariant polynomial ring identity explained above. It should receive independent mathematical review before any external publication.
