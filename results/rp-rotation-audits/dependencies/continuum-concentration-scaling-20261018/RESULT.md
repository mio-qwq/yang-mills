# Joint continuum and infinite-volume audit of the entropy–concentration bridge

18 October 2026. Original quantitative continuation of the two supplied reports. This is a conditional comparison theorem and an abstract non-mixture obstruction to uniform inference. It proves no weak-coupling Wilson estimate, no continuum-limit existence, and no mass gap. No literature search or remote write was performed.

## 1. Findings

Write `a` for the lattice spacing, `L` for the number of sites along one side, and `R=aL` for the physical side length. All limits below can be read along a specified sequence `a→0`, `L=L(a)→∞`; joint infinite physical volume means `R(a)→∞`.

Let the actual selected-sum concentration coefficient be `q(a,L)`, so that

    log μ_{a,L} exp[t(F_{a,L}−μ_{a,L}F_{a,L})]
        ≤ q(a,L)L^d t²/2.

Let `ω_a=osc(A_a)` and let `ρ_a` be the sum of the physical coordinate spans of the link-tail support of `A_a`. For the normalized Wilson action used in the supplied boundary audit, a uniform-in-the-comparison-state estimate is

    |ν_a(A_a)−μ_{a,L}(A_a)|
        ≤ sqrt[12d(d−1) β(a) a q(a,L)/R]
          + ω_a min(1,ρ_a/R).                                    (1)

The minimum in (1) is a safe coarse bound; the exact boundary fraction is given below. Consequently sufficient simultaneous-limit conditions are

    β(a) a q(a,L(a))/R(a) → 0,
    ω_a ρ_a/R(a) → 0.                                             (2)

For the original notation `q=K_{A_a}c(a,L)`, the first condition is `β K_{A_a}c/L→0`, not merely pointwise `c(a,L)=o(L)` at each fixed cutoff and observable.

Important refinements:

- A shrinking selected-source interval `|t|≤δ(a,L)` suffices if additionally `β/(Lδ)→0`. The source scale that has to be exceeded is of order `β/L`, with the observable's normalization already built into `t` and `q`.
- Under an LSI, using only nonwrapping translates removes the additive boundary error entirely. The resulting bound has a mild factor equal to the inverse square root of the retained volume fraction. This refinement needs concentration for that partial sum; it does not follow just from the original full-sum hypothesis.
- A normalized Wilson loop approximating a fixed rectifiable physical contour has bounded norm and wrapping error `O(physical diameter/R)`. There is no support-cardinality or lattice-perimeter multiplier in this boundary term. Its elementary LSI gradient bound does, however, give `q=O(C_{a,L} a^(−2))`. A sufficient LSI-based condition is therefore `β C_{a,L}/(aR)→0`.
- An explicit family of product measures below obeys the two-sided surface-density comparison for every size, has `c(a,L)=1` for every fixed local sum, and has the correct fixed-cutoff thermodynamic limit. Nevertheless, bounded observables of fixed physical support disagree along a joint limit with `β(a)≈log(1/a)`. This is an abstract comparison example, not a Wilson model and not a pair of states for a common finite-range specification.

## 2. Precise setup and the all-cutoff boundary estimate

Fix the spatial dimension `d≥2` and a compact matrix gauge group with normalized Wilson plaquette function `w_p∈[−1,1]`. At cutoff `a`, let the periodic action be

    S_{a,L}=β(a) Σ_p w_p,       β(a)≥0.

Let `μ_{a,L}` be the ordinary side-`L` periodic law and let `ν_a` be any translation-invariant infinite-volume DLR law for that same cutoff and coupling. No relation between `ν_a` and `ν_{a'}` is assumed. Represent torus links by positive-coordinate links whose tails lie in `Q_L={0,…,L−1}^d`; let `ν_{a,L}` be the marginal of `ν_a` on this finite full-lattice link set.

The boundary proof from the supplied independent audit works without fixing the value of `β`: its finite-volume inequality is pointwise in `β`. For clarity, per orientation pair the numbers of noncommon plaquettes in the DLR conditional action and the periodic action are respectively

    4L^(d−1)−L^(d−2),       2L^(d−1)−L^(d−2).

All common plaquettes cancel. Since `|w_p|≤1`, the absolute difference of the two unnormalized exponents is at most

    β(a) binom(d,2)[6L^(d−1)−2L^(d−2)].

Normalization can double this bound. Averaging the DLR conditionals preserves both pointwise density inequalities. Thus, with

    b_a=6d(d−1)β(a),       B_{a,L}=b_a L^(d−1),

we have, for every exterior mixture and hence uniformly in `ν_a`,

    exp(−B_{a,L}) ≤ dν_{a,L}/dμ_{a,L} ≤ exp(B_{a,L}),
    H(ν_{a,L}|μ_{a,L}) ≤ B_{a,L}.                         (3)

This statement does not identify a periodic lift with an infinite-volume DLR law. If a different action convention is used, replace `b_a` by its verified boundary coefficient. All results below hold for an abstract entropy bound `H≤b_aL^(d−1)` as well.

Let `A_a` be a real bounded cylinder observable. Its bound, support and derivatives may depend on `a`. Translate its anchor so that its positive-link tails have coordinate minima zero and coordinate maxima `s_{a,j}`. Set

    ω_a=sup A_a−inf A_a,
    θ_{a,L}=Π_j(1−s_{a,j}/L),
    ρ_a=a Σ_j s_{a,j}.

Assume `s_{a,j}<L`; this is a sufficient bounding-box condition for embedding without support identifications. Sparse supports can inject modulo `L` without satisfying this stronger condition. The following are exactly the translates whose entire bounding box lies in `Q_L`:

    T_{a,L}=Π_j {0,…,L−1−s_{a,j}},     |T_{a,L}|=L^d θ_{a,L}.

All other translates are classified as possibly wrapping. This classification is exact for containment of the support's coordinate bounding box; some exceptional algebraic observables might also agree across a seam, which only improves the bound. In particular,

    1−θ_{a,L} ≤ min(1,Σ_j s_{a,j}/L)=min(1,ρ_a/R).        (4)

Use positive-link tails, not just anchor locations. A negatively traversed edge uses the inverse variable of the positive link with the appropriate tail. Vertex/end-point spans are also safe upper bounds. A fixed physical contour approximated with `O(a)` coordinate error has these physical spans bounded by its physical coordinate spans plus `O(a)`.

## 3. Entropy proof, with all varying constants retained

Define the periodic translate sum and average

    F_{a,L}=Σ_{x∈Q_L} A_{a,x},       X_{a,L}=F_{a,L}/L^d.

Assume for both signs, for every allowed real source `t`,

    Λ_{a,L}(t):=log μ_{a,L} exp[t(F_{a,L}−μ_{a,L}F_{a,L})]
        ≤ q_{a,L}L^d t²/2,                              (5)

where `q_{a,L}≥0`. The quantity `q`, not its decomposition into an observable constant and a concentration scale, is what the comparison uses.

The entropy variational inequality gives, for each allowed `t>0`,

    |ν_{a,L}(X_{a,L})−μ_{a,L}(X_{a,L})|
        ≤ b_a/(Lt)+(q_{a,L}/2)t.                         (6)

When (5) holds for all real `t` and `q>0`, optimize at

    t*=sqrt[2b_a/(Lq_{a,L})]

to obtain

    |ν_{a,L}(X_{a,L})−μ_{a,L}(X_{a,L})|
        ≤ sqrt[2b_aq_{a,L}/L].                           (7)

The zero cases follow by a limit or directly: `b=0` gives equality by zero entropy, and a global centered MGF with `q=0` makes the sum constant under every absolutely continuous comparison law.

Periodic translation invariance gives `μ_{a,L}(X_{a,L})=μ_{a,L}(A_a)`. For `x∈T_{a,L}`, the torus expression equals the genuine infinite-lattice translate on the identified variables, so its `ν_a` expectation is `ν_a(A_a)`. For each of the other translates both values lie in the same interval of length `ω_a`; their expectation difference is at most `ω_a`. Therefore

    |ν_a(A_a)−μ_{a,L}(A_a)|
        ≤ sqrt[2b_a q_{a,L}/L]+ω_a(1−θ_{a,L}).           (8)

This proves (1)–(2). Using oscillation, rather than twice a norm, also shows that adding a cutoff-dependent deterministic constant to the observable has no effect on the required estimate.

The conclusion is equality of the selected expectations up to a vanishing error along the specified joint sequence. It does not assert tightness or existence of any continuum fields. If these observables are the real reflected quadratic tests for which `ν_a(A_a)≥0`, (8) implies `liminf μ_{a,L}(A_a)≥0` whenever its error vanishes. Interpreting that as reflection positivity of a continuum limit additionally requires existence of that limit, correctly matched reflection/test maps, and convergence of the tested expectations.

### 3.1 Shrinking source intervals

Suppose (5) is available only for `|t|≤δ_{a,L}`. Put `h=b_a/L`. The exact upper bound supplied by (6) is

    inf_{0<t≤δ} (h/t+qt/2)
      = sqrt(2hq)                         if δ≥sqrt(2h/q),
      = h/δ+qδ/2                          otherwise,             (9)

for positive `h,q`. In all cases a convenient bound is

    |ν_a(A_a)−μ_{a,L}(A_a)|
      ≤ b_a/(Lδ)+sqrt(2b_aq/L)+ω_a(1−θ).                (10)

Thus sufficient rates are

    b_aq/L→0,       b_a/(Lδ)→0,       ω_a(1−θ)→0.        (11)

The first two conditions are also equivalent to the vanishing of the optimized nonnegative quadratic bound in (9), with the natural zero-case conventions: the infimum is at least `sqrt(2hq)` and at least `h/δ`, and (10) proves the converse. They are not claimed necessary for actual state identification.

If one starts with a tilted-variance estimate, the exact identity is

    Λ(±t)=∫_0^t (t−s) Var_{μ_{a,L,±s}}(F_{a,L}) ds.

A uniform bound `Var≤qL^d` on the selected interval implies (5) there. More generally it suffices to choose `t_a>0` with

    b_a/(Lt_a)→0,
    Λ(t_a)/(t_aL^d)→0 and Λ(−t_a)/(t_aL^d)→0,

together with the wrapping condition. No other source directions are used. A variance estimate at zero still does not give these integrated bounds.

### 3.2 Direct tails when the observable norm grows

The density bound in (3) yields, for every `ε>0`,

    |ν_{a,L}(X)−μ_{a,L}(X)|
      ≤ ε+ω_a exp(B_{a,L}) μ_{a,L}(|X−μ_{a,L}X|>ε).     (12)

For a varying observable it is sufficient that, for every fixed `ε>0`, the second term tends to zero, or that one can choose `ε_a→0` for which it does. One must retain `ω_a` when it grows. In exponential language a sufficient tail margin at thresholds `ε_a→0` is

    −log μ(|X−μX|>ε_a)−B_{a,L}−log(max(1,ω_a))→+∞.

Add the same wrapping error. This is an alternative to the entropy/MGF route. It need not be imposed in addition to (2); in particular (7) itself has no extra norm or logarithmic penalty.

## 4. LSI, derivative budgets, and a stronger nonwrapping variant

Use a product bi-invariant Riemannian metric on the link groups. For the distinct positive links in the support define

    g_{a,e}=||∇_e A_a||∞,
    D_{a,i}=Σ_{e of direction i} g_{a,e},
    K_a=Σ_i D_{a,i}².

For a torus link `(y,i)`, the derivative of the full translate sum contains at most one translated derivative for each support link of direction `i`. The triangle inequality gives a norm bound `D_{a,i}`. Summing squared link gradients proves

    ||∇F_{a,L}||∞²≤K_aL^d.                              (13)

Suppose

    Ent_{μ_{a,L}}(f²)≤2 C_{a,L} μ_{a,L}(|∇f|²).         (14)

Apply this to `f=exp(tF/2)`. After dividing by the MGF, it gives

    tΛ'(t)−Λ(t)≤C_{a,L}K_aL^d t²/2.

Integrating the derivative of `Λ(t)/t` from zero, and applying the same calculation to `−F`, proves (5) with

    q_{a,L}=C_{a,L}K_a.                                 (15)

Only an inequality valid for the relevant exponential functions is needed. A gauge-invariant restricted LSI suffices when those sums are gauge invariant. No such weak-coupling constant is supplied here.

### 4.1 Remove the additive boundary term when partial-sum concentration is available

Let

    G_{a,L}=Σ_{x∈T_{a,L}} A_{a,x},       N=|T_{a,L}|=θL^d.

Both expectations now identify the local observable exactly:

    ν_{a,L}(G)=Nν_a(A_a),       μ_{a,L}(G)=Nμ_{a,L}(A_a).

There is no seam error. If `G` has a centered MGF bound `q_int N t²/2`, entropy gives

    |ν_a(A_a)−μ_{a,L}(A_a)|
        ≤ sqrt[2b_a q_int/(Lθ)].                         (16)

Under the LSI (14), one can take `q_int=C_{a,L}K_a`, with no extra boundary factor hidden in that coefficient. Here is the counting proof, which is useful for very large observable norms. For each direction `i` and link `y`, put

    w_{y,i}=Σ_{e of direction i} g_{a,e} 1_{y−tail(e)∈T}.

The derivative norm is at most `w_{y,i}`. Since `0≤w_{y,i}≤D_{a,i}`,

    Σ_y w_{y,i}²≤D_{a,i} Σ_y w_{y,i}
                 =N D_{a,i}².

Summing in `i` proves `||∇G||∞²≤NK_a`, and Herbst proves (16).

Consequently, if `θ` stays bounded away from zero, the sole nontrivial LSI rate for this version is

    β(a) C_{a,L}K_a/L→0.                                (17)

One does not also need `ω_aρ_a/R→0`. The support must fit with a positive retained fraction, but its physical span need not be a vanishing fraction of `R`. If `ρ_a/R→0`, then `θ→1` and the coefficient asymptotically matches (8). The original concentration assumption for the full sum alone is not a license to use (16): concentration for `G` is an additional fact, supplied here by the LSI.

## 5. Explicit rates in physical units

For an arbitrary verified selected-sum bound, the basic dimensionless concentration parameter is

    β(a) a q(a,L)/R.

The physical volume is `R^d`. Replacing the sum by its Riemann-sum version `a^dF` and dividing by `R^d` produces exactly the same average `F/L^d`; it does not eliminate any cutoff factors in (1).

Here are useful sufficient power-law formulations. They are examples of rates to prove, not asserted Wilson estimates.

### 5.1 A physical-size parametrization

Suppose, with constants independent of the joint sequence,

    β(a) ≤ C a^(−b) [log(1/a)]^u,
    C_{a,L} ≤ C a^(−γ) R^η [log(1/a)]^v,
    sqrt(K_a) ≤ C a^(−κ),
    ω_a ≤ C a^(−m),       ρ_a ≤ C a^(−r),

and choose `R(a)=a^(−p)`, `p>0`, up to integer rounding of `L=R/a`. The squared concentration term is bounded by a constant times

    a^[1−b−γ−2κ+p(1−η)] [log(1/a)]^(u+v),

and the additive wrapping term by a constant times `a^[p−m−r]`. For `η<1`, the strict conditions

    p>m+r,
    p>(b+γ+2κ−1)/(1−η),       p>0                       (18)

suffice, regardless of fixed logarithmic powers. At a zero power exponent the logarithmic factors must be checked separately. If `η=1`, making `R` larger does not improve this particular concentration upper bound. If `η>1`, larger `R` worsens it; a separate rate or argument is needed unless the remaining powers already permit a chosen joint scale.

With the nonwrapping LSI version, replace `p>m+r` by support fitting with `θ` bounded below; `p>r` is one convenient stronger sufficient condition. The norm is still accounted for through the derivative budget whenever the observable is multiplied by a growing factor.

### 5.2 A lattice-size concentration scale

Suppose instead that the original factorization obeys

    β(a) ≤ C a^(−b) [log(1/a)]^u,
    K_{A_a} ≤ C a^(−k),
    c(a,L) ≤ C a^(−γ)L^α [log(1/a)]^v,       0≤α<1.

For `R=a^(−p)`, the sufficient concentration inequality is

    (p+1)(1−α)>b+k+γ.                                   (19)

The original full-sum boundary term additionally requires `p>m+r` under the preceding oscillation/span assumptions. The statement `c(a,L)=o(L)` at each fixed `a` is compatible with every `α<1`, but gives neither a bound on `γ` nor on `K_{A_a}` nor a rate of approach. It therefore does not imply (19) on a prescribed diagonal.

## 6. Fixed physical Wilson loops

Let `γ_a` be a lattice loop approximating a fixed contour of finite physical length `ℓ`, with `n_a≤Cℓ/a` traversals, including repeated and inverse traversals. Suppose its physical coordinate spans are bounded. Define the normalized real Wilson observable

    W_a=(1/N_c) Re Tr Hol(γ_a),       |W_a|≤1.

Fix a unitary defining representation and a Lie-algebra metric with `|Tr(XU)/N_c|≤κ_G||X||` for every unitary `U`. Differentiating one occurrence of a link or its inverse inserts one Lie-algebra matrix, conjugated by unitary factors. Its normalized real trace has absolute derivative at most `κ_G` for a unit tangent direction. If a distinct positive link occurs `m_e` times, including inverse occurrences, then

    ||∇_e W_a||∞≤κ_G m_e.

Writing `n_{a,i}` for the total number of traversals in direction `i`,

    K_{W_a}≤κ_G² Σ_i n_{a,i}²≤κ_G² n_a².                (20)

A metric change changes `κ_G` and the corresponding LSI constant consistently. Cauchy–Schwarz gives `κ_G=1` with the normalized Hilbert–Schmidt norm `||X||²=Tr(X*X)/N_c`, and `κ_G=N_c^(−1/2)` with the unnormalized Hilbert–Schmidt norm. The result does not assume a simple loop, no backtracking, or distinct traversed edges.

Combining (8), (15), and (20) gives

    |ν_a(W_a)−μ_{a,L}(W_a)|
      ≤ C_d,G ℓ sqrt[β(a) C_{a,L}/(aR)]
        + 2 ρ_a/R.                                      (21)

Hence, for bounded `ℓ,ρ_a`, a sufficient condition is

    R→∞,       β(a) C_{a,L}/(aR)→0.                     (22)

The boundary term contains the coordinate span, not `n_a`, `n_a^d`, or the number of supporting links. For a fixed physical loop it is `O(1/R)`, rather than a cutoff-uniform `O(1/L)`. In particular, the constants suppressed by `O_A(1/L)` in a fixed-observable theorem cannot be frozen when the lattice realization of the same physical loop grows.

Examples under hypothetical concentration inputs:

- If `β(a)=O(log(1/a))` and `C_{a,L}=O(1)`, the elementary bound (22) follows from `R≫log(1/a)/a`. Any power `R=a^(−p)` with `p>1` suffices; `p=1` requires extra logarithmic growth.
- If the same logarithmic coupling bound holds and `C_{a,L}=O(a^(−γ))`, any `p>1+γ` suffices.
- If `C_{a,L}=O(L^α)` for `0≤α<1`, logarithmic `β` and a fixed physical contour are handled by `(p+1)(1−α)>2`, equivalently `p>(1+α)/(1−α)`.

These are deliberately conservative LSI/gradient sufficient rates. They are not lower bounds on the box size actually needed by Wilson measures. A directly proved selected-loop sum estimate may have a much smaller `q` than (20)–(15).

For a growing multiplicative normalization `A_a=Z(a)W_a+c(a)`, oscillation and derivative budgets multiply by `|Z|`, while the additive deterministic subtraction does nothing. The full-sum version requires

    β C_{a,L}|Z|²/(aR)→0,       |Z|ρ_a/R→0.             (23)

The nonwrapping LSI version eliminates the second requirement provided `θ` stays bounded below. No particular Wilson-loop renormalization, existence, or nontrivial continuum limit is assumed.

Finite reflected test polynomials are handled in the same way, by their actual derivative budgets and bounding-box spans. For example, if `f_a=Σ_{k=1}^m c_k W_{k,a}` with fixed `m,c_k`, let `S=Σ|c_k|`. Then `||f_a||∞≤S`, and a genuine real reflection test `A_a=Re[overline(f_a(θU)) f_a(U)]` has `||A_a||∞≤S²` and derivative sum bounded by the product rule by `S` times the derivative sums of `f_a` and its reflection. Reflection preserves the derivative norm and only changes the support location. If the total fixed-coefficient physical loop length is bounded, this gives `K_a=O(a^(−2))` again. Translate the entire composite test `τ_x[(θf_a)f_a]`; reflecting `τ_x f_a` about a fixed, unshifted plane can instead make the two halves separate with `x`, changing the support premise. Such a test is generally not `|f_a|²` pointwise; its nonnegative expectation is the reflection-positivity assertion. Cutoff-dependent coefficients, degree, or number of loops must instead be retained explicitly in `ω_a,K_a`.

## 7. Product-family counterexamples to a cutoff-uniform inference

These are scalar-spin product laws, with no rare-phase mixture. They are not Wilson measures, and the reference finite-volume family is not generated by one volume-independent common Gibbs interaction. Their purpose is precise: the abstract surface-comparison and pointwise concentration hypotheses alone contain no missing joint-limit uniformity. The examples even satisfy the abstract surface bound for every side length and have the correct fixed-cutoff thermodynamic limit.

### 7.1 A reusable product family

At each cutoff choose `0<δ_a≤1/4` and an integer crossover side `L_a*`. On `{−1,+1}^{(Z/LZ)^d}`, let

    q_a=1/2+δ_a,
    p_{a,L}=q_a−δ_a min(1,L_a*/L),
    μ_{a,L}=Bernoulli(p_{a,L})^{⊗L^d},
    ν_a=Bernoulli(q_a)^{⊗Z^d},

where the Bernoulli parameter is the probability of spin `+1`. These are fully supported and translation invariant. For probabilities in `[1/2,3/4]`, the derivatives of `log p` and `log(1−p)` have absolute value at most `4`. Thus the log-density ratio per coordinate has absolute value at most

    4δ_a min(1,L_a*/L).

Summing over sites gives, for every `L`,

    |log(dν_{a,L}/dμ_{a,L})|
       ≤ 4δ_a min(1,L_a*/L)L^d
       ≤ 4δ_a L_a* L^(d−1).                              (24)

The same coefficient bounds relative entropy. At fixed `a`, `p_{a,L}→q_a`, so every fixed local expectation converges to that of `ν_a` as `L→∞`.

All these product reference measures have a uniform elementary concentration input. If changing one spin of a local observable `A` can change its value by at most `u_e` at support coordinate `e`, then changing one torus spin changes `F_A=Σ_x A_x` by at most `D_A=Σ_e u_e`. The independent-coordinate martingale bound gives

    log μ_{a,L} exp[t(F_A−μ_{a,L}F_A)]
       ≤ L^d D_A² t²/8.                                 (25)

For completeness, a centered random variable lying in an interval of length `r` has log-MGF at most `r²t²/8`: under any tilt its variance is at most `r²/4`, and integrate the centered log-MGF twice. Exposing independent coordinates produces martingale increments with conditional interval lengths at most the corresponding coordinate changes; applying this bound conditionally and iterating proves (25).

Consequently the original factorization can be taken as

    K_A=D_A²/4,       c(a,L)=1.

This is uniform in the single-spin bias and in `L`, for every fixed bounded local observable `A`. In particular `c(a,L)/L→0` even uniformly in `a`. What fails below is uniform control of all the other factors and the required joint scale.

### 7.2 Bounded norm, fixed physical support, logarithmic surface coefficient

Fix `d≥2`, choose `0<κ<1/4`, and let integers `n→∞` parametrize the cutoff. Set

    a_n=1/n,       s_n=n^d,
    δ_n=κ/sqrt(s_n),
    L_n*=ceil(sqrt(s_n) log n),       β_n=log n.

Then

    R_n=a_n L_n* ~ n^(d/2−1) log n →∞,
    4δ_n L_n*=O(β_n).

Thus (24) is a two-sided `exp[O(β_n L^(d−1))]` density comparison for every `L`. At the chosen diagonal `L=L_n*`, the reference product measure is unbiased.

Let `D_n={0,…,n−1}^d` and define the real bounded observable

    A_n=sin[(1/sqrt(s_n)) Σ_{x∈D_n} σ_x].

Its norm is at most one, and its physical support lies in a fixed unit cube. The wrapping estimate tends to zero because `n/L_n*→0`, including in `d=2`, where the ratio is `O(1/log n)`. Symmetry under the unbiased reference law gives

    μ_{a_n,L_n*}(A_n)=0.

Under `ν_n`, independence gives the exact complex expectation

    ν_n exp[i s_n^(−1/2) Σ_{x∈D_n}σ_x]
      = [cos(s_n^(−1/2))+2iδ_n sin(s_n^(−1/2))]^(s_n).

Writing `s=s_n`, expansion of the factor inside brackets is

    1+(−1/2+2iκ)/s+O(s^(−2)).

Its `s`th power therefore tends to `exp(−1/2+2iκ)`, and

    ν_n(A_n)−μ_{a_n,L_n*}(A_n)
        → exp(−1/2) sin(2κ)>0.                          (26)

For this selected observable a single spin change changes `A_n` by at most `2/sqrt(s_n)`. There are `s_n` support coordinates. Thus (25) holds with

    K_{A_n}=s_n,       c(a_n,L)=1.

The selected coefficient is genuinely of order `s_n`, not merely an overestimate from bounded differences. At the unbiased diagonal put `s=s_n`, `u=1/sqrt(s)`. For a site `y` in a translated block, independence gives `μ(A_{n,x}σ_y)=sin(u)cos(u)^(s−1)`, and it is zero outside that block. Each site belongs to exactly `s` translated blocks, so `μ(Fσ_y)=s sin(u)cos(u)^(s−1)`. The independent centered unit-variance spins form an orthonormal family in `L²(μ)`. Orthogonal projection therefore gives

    Var_μ(F)/L^d ≥ s² sin²(u)cos(u)^(2s−2) ~ e^(−1)s.

Any quadratic centered MGF coefficient valid in a neighborhood of zero must be at least `Var(F)/L^d`, by differentiation at zero. Together with (25), its best value is `Θ(s_n)`.

Every fixed-cutoff local statement remains true, the physical volume diverges, the observable is bounded, its physical support is fixed, and `β_n` grows only logarithmically, yet the diagonal identification fails. The corrected concentration rate diagnoses the failure:

    β_n K_{A_n}c/L_n* ~ sqrt(s_n) →∞.

This is a fixed-physical-volume-support scalar observable, not a Wilson contour observable. It does not prove that the elementary Wilson-loop bound is optimal, or that Wilson structure cannot improve it.

### 7.3 The coupling and normalization factors cannot simply be discarded either

The same family separates two further issues.

1. Growing surface coefficient with fixed observable: take `a_n=1/n`, `L_n*=n²`, and fixed `δ∈(0,1/4]`. Let the abstract coupling scale be `β_n=L_n*`. Equation (24) has coefficient `O(β_n)`, and the bounded one-spin observable `A=σ_0` has `K_A=1`, `c=1`. At `L_n*`, its expectation gap is `2δ`, while `R_n=n→∞`. The missing factor is `β_n/L_n*`, which does not vanish. At each fixed cutoff the local thermodynamic limit still agrees.

2. Growing normalization with fixed microscopic support: take `a_n=1/n`, `L_n*=n²`, `β_n=log n`, and `δ_n=β_n/L_n*` for sufficiently large `n`. The density coefficient in (24) is `4β_n`. For `A_n=σ_0/(2δ_n)`, the diagonal expectation gap is exactly one. Here `K_{A_n}=1/(4δ_n²)`, `c=1`, and there is no wrapping error at all. The amplitude blowup, hence concentration coefficient, cannot be suppressed.

These examples are exact counterexamples only to the proposed abstract uniform inference. They are not counterexamples to the supplied fixed-cutoff Wilson theorem, to uniqueness for any common Wilson specification, or to a continuum Yang–Mills theorem.

## 8. What pointwise fixed-cutoff results still allow

If, for every fixed positive `a`, every selected `A_a` has a finite constant `K_{A_a}` and an actual Wilson estimate `c(a,L)/L→0` as `L→∞`, then the fixed-cutoff theorem remains valid. It also gives a nonquantitative diagonal choice: along any countable cutoff sequence `a_n→0`, choose `L_n` sufficiently large that the comparison error is below `1/n` and `a_nL_n≥n`. For finitely many tests at stage `n`, take the largest of their finitely many required sizes. A countable family can be covered by including its first `n` members at stage `n`.

This uses an arbitrarily large cutoff-dependent box size; it provides no explicit physical-volume rate, no result along a separately prescribed diagonal, and no uniformity permitting an interchange of limits. Conversely, if the infinite-volume limit is taken first at each fixed cutoff and the two infinite-volume states have already been identified there, no new uniform finite-size estimate is needed merely to preserve that equality through a later continuum limit of their expectations. Existence and the other continuum properties remain separate questions.

## 9. Verification and stopping point

The proofs above are finite-volume inequalities followed by explicit limits. They use the supplied sublinear-concentration report, variance audit, and boundary-count/gradient audit; there was no new literature search. The main source refinement is the joint condition `β K_A c/L→0`, with the varying support/normalization terms retained. The nonwrapping-LSI argument improves the boundary handling when its stronger functional input is available.

An independent mathematical reviewer checked the entropy/source optimization, partial-sum LSI argument, power exponents, and product construction, finding no substantive gap. Its support-embedding wording correction was incorporated, as was the first-chaos lower bound showing that the counterexample’s concentration coefficient genuinely grows like its support size. This is an internal mathematical audit, not human peer review. The companion `geometry-audit.md` records an independent audit of loop geometry and reflected products. The original standard-library `check_scaling.py` passes 27 floating-point sanity assertions, including the full and nonwrapping MGF bounds on all 512 and 65,536 configurations of two finite product systems, entropy/density checks, and the explicit diagonal expectation limit. `scaling_checks.json` records the output. These are supplementary finite checks, not exact certificates; the conclusions rest on the proofs above. No unknown repository code was executed. No remote state was changed.

The missing mathematical input is still an actual weak-coupling concentration, integrated-source, or tail estimate for the required selected observables, with cutoff and size quantifiers strong enough for a specified joint sequence. Without that input, the rates in this report are sufficient targets only. No ongoing external process requires monitoring.
