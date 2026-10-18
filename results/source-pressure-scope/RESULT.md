# Do the pinned YM4 source estimates imply H2?

18 October 2026. A source-scope and logical-implication audit. This does not audit the complete multiscale construction or establish a continuum limit or mass gap.

## Result

**No implication from the inspected source estimates to H2 is established.** Even if every stated multiscale input is granted, two independent additions are needed:

1. A thermodynamic estimate for **homogeneous sources**: the global source theorem supplies an extensive upper bound on a corrected partition function, not a volume-independent zero-free neighborhood or a bound on its logarithm. Its guaranteed logarithm radius decreases with the volume.
2. Coverage of the **reflected-product and general local source directions** in H2: the theorem inserts a scalar weight into the coefficient of the Wilson plaquette action. It does not state stability for the exponential of a homogeneous sum of arbitrary bounded local observables, including products of two separated insertions.

There is a stronger-looking result in the companion account, and it does not close the gap: its volume-independent zero-free neighborhood is for a fixed finite number of bounded-radius, separated action-density insertions. The constants depend on their number and radius, so this is not a zero-free result for a source occupying the entire volume.

A useful scoped implication is proved below: **at fixed cutoff, for each selected bounded real local observable A, a common zero-free complex disk for its homogeneous-source partition functions along any unbounded periodic-volume subsequence implies H2 for A.** Boundedness already supplies the extensive upper bound needed for a normal-family argument; no ultraviolet counterterm is needed for that implication. The disk may depend on A and on the fixed coupling. This is a sufficient condition, stronger than differentiability alone, and is not proved by the manuscript estimates inspected here.

H1 is taken as independently proved in the present project: a translation-invariant, gauge-invariant, diagonally reflection-positive Wilson DLR state exists at every finite nonnegative beta. It is not inferred from the manuscript. Thus H2 remains the missing input for the specified pressure route to straight-periodic accessibility.

## 1. Sources, normalization, and exact quantifiers

The source audit inspected commit `785a68fdeef78a1da854c4807fe1f17b597d05e7` of `ethanwsussman/Yang--Mills-LLM-experiment`; all four inspected original-file SHA-256 values were recomputed and matched the source manifest. `SOURCE_MANIFEST.json` records repository paths, pinned URLs, and checks. Printed pages and raw-source line numbers below identify the relevant passages. Downloaded originals and verbatim excerpt files are excluded from this publication. No source-repository code or TeX was executed.

### Main manuscript

Primary source: [pinned main PDF](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/ym4_manuscript_zeroth_draft.pdf).

- Hypotheses (H1)–(H6), printed pp.10–11, fix SU(2), straight cubic tori T_m = R^4/(2 L^m Z^4), bare spacing epsilon = L^(-K), weak bare coupling g_0, a reference coupling g, and K = K(g_0,g). The bare inverse-coupling coefficient is beta = x_0 = g_0^(-2), in the manuscript's normalized-trace convention. This is not a theorem at every finite beta.
- Theorem 3.1, pp.44–45: after the auxiliary constants, fix any source radius rho > 0; then choose a small-coupling ceiling gamma_J depending on rho. For every g <= gamma_J there are b_*(g), C_e and c_vol(s), independent of m and g_0, and the conclusions hold for every sufficiently large m and every 0 < g_0 <= g_-(g), with K = K(g_0,g). Part (c), and hence the vacuum decomposition in (d), uses b_* <= s <= K and K' = K-s. The case K < b_* is handled separately by elementary finite-cutoff bounds in the proof of (e), p.51.
- Increasing rho is therefore not free at fixed g: the quantifier order changes the small-coupling threshold. There is no permission to choose rho growing with volume while keeping the same fixed Wilson theory and all its constants.
- In the fixed-cutoff thermodynamic question, fix g_0, g and K, then let m grow. The bare site count is V_m = (2 L^(m+K))^4; the reference count is (2 L^m)^4. They differ by the fixed factor L^(4K). Uniformity in K for ultraviolet limits does not imply analyticity as m tends to infinity.

### Actual source class

Equations (3.1)–(3.3), p.42, define

    a_p(U) = 1 - Re tr U(partial p),  0 <= a_p <= 2,
    A(w,U) = sum_p w(x(p)) a_p(U),
    Z(w) = integral exp[-x_0 A(1,U) + A(w,U)] dU.

The source w is a scalar coefficient at plaquette barycentres. For a finite family of real Lipschitz functions h_l, it is w = sum_l z_l h_l with

    sum_l |z_l| ||h_l||_sharp < rho,
    ||h||_sharp = max(||h||_infinity, 40 M Lip h).

The Lipschitz constant is in the manuscript's reference units. The intermediate W_j classes, p.43, additionally spell out scale-dependent small amplitude and Lipschitz conditions. Part (d) provides the stated polydisc for the above Lipschitz families. Constant w = t is admissible on |t| < rho and changes the bare Wilson coupling from x_0 to x_0-t. The running-shift functions b_j and zeta_j are holomorphic on |t| < 2rho, but these are coefficients of the finite-depth renormalization construction, **not log partition functions**.

The raw account says the same explicitly: [raw II, lines 681–749](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/theorem_0_complete_account_raw_II.tex#L681-L749), Definition `5.1:def-torus-floor`; Theorem `5.1:thm-correlation-theorem`, lines 2791–2990. Its free N_T is the side count of a cubic torus. It does not introduce an arbitrary local-observable source.

## 2. The global estimate is not pressure analyticity

Theorem 3.1(d) defines local holomorphic vacuum differences e_j(X;w), vanishing at w=0, with

    |e_j(X;w)| <= C_e exp[-(1-delta) kappa d_j(X)].

Write E_m(w) = sum_(j<=K') sum_X e_j(X;w). Equation (3.6), p.44, gives

    |exp[-E_m(w)] Z_m(w)/Z_m(0)|
        <= exp[c_vol(s) |Lambda_(K')|].

This is a one-sided modulus bound. The last block fields and large-field histories have not disappeared: p.48 explicitly writes Z = exp(E) times a remaining last-lattice integral. Neither the locality of E nor its analyticity identifies that remaining integral with the exponential of a controlled analytic extensive function.

At s=b_*, the bound is Q_m = exp[c_vol (2 L^(m+b_*))^4]. Theorem 3.1(e), p.45, and its proof using Lemma 3.6, p.51, guarantee a holomorphic logarithm only on

    sum_i |z_i| ||f_i||_sharp < rho/(Q_m+1).

For c_vol > 0 the guaranteed radius tends to zero exponentially in volume. The theorem allows c_vol >= 0 and does not establish c_vol=0; one cannot insert that special case into the argument. The proof on p.51 expressly describes its global correlation estimate as useless in infinite volume because of this volume factor.

### What can be said about the counterterm at fixed cutoff

The counterterm is not itself the obstacle. Lemma 3.4(v)'s tree sum and (d3) give, on the admitted source disk,

    |E_m(w)| <= C_e C_tree sum_(j<=K') #pi_j,
    #pi_j = V_m / (M^4 L^(4j)).

Thus |E_m(w)|/V_m is bounded independently of m, for fixed cutoff, indeed by

    C_e C_tree / [M^4 (1-L^(-4))].

Counting each domain through all cubes containing it only overcounts, so the displayed upper bound is valid. This makes the normalized counterterms a locally bounded holomorphic family. It supplies no corresponding control of Log[exp(-E_m) Z_m/Z_m(0)]. Multiplication by exp(-E_m) cannot remove any zero of Z_m, since the exponential never vanishes.

Per *reference* volume the above counterterm bound can grow as K increases. The manuscript's re-centering is designed to control selected mixed derivatives without taking a modulus of divergent ultraviolet bulk terms. That is an important cutoff issue, separate from the thermodynamic zero-free issue.

### Exact obstruction to the inference

For V a positive integer let S_V take values +V and -V with equal probabilities. Then

    G_V(z) = E exp(z S_V) = cosh(Vz)

is entire, G_V(0)=1, is positive for real z, and obeys

    |G_V(z)| <= exp(V |Re z|) <= exp(V |z|).

It therefore has every fixed-disk volume-extensive upper bound under discussion, with E_V=0. Nevertheless

    |t| - log(2)/V <= V^(-1) log G_V(t) <= |t|,

so its real limiting pressure is |t|, not differentiable at zero. Its nearest zeros are +/- i pi/(2V), and Var(S_V)/V = V.

This agrees with the independent exact calculation in `ANALYSIS.md`. It disproves the abstract inference from analyticity of partition functions plus extensive upper bounds. It is **not** a Wilson DLR counterexample and does not contradict the manuscript's actual finite-volume estimates.

## 3. The stronger local zero-free result and its exact limitation

The main Theorem 3.10, p.55, and its proof, pp.58–59, use a re-centered holomorphic counterterm E'' and establish

    |h''(z)| <= Q_infinity^n,
    h''(z) = exp[-E''(z)] Z_m(sum_i z_i f_i)/Z_m(0),
    Q_infinity = exp[c_vol L^(4b_*) ell^4 + 2 C_face(R)],
    ell = least power of L at least 8 n(R+1).

Here n is fixed, each f_i has support in a ball of fixed radius R, and different supports are separated by d>0. The mixed correlation constants are independent of the torus volume and of the mutual positions of these fixed balls. The statement says explicitly that no decay in their separation is asserted.

The companion goes further in wording but not in homogeneous-source scope. [Raw II, lines 64285–64346](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/theorem_0_complete_account_raw_II.tex#L64285-L64346), Remark `6.4:rem-complex-sources`, explicitly derives zero-freeness on

    rho(z) <= 1/[2 mathfrak_r (Q_infinity^n+1)],
    rho(z) = r^(-1) sum_i |z_i| ||f_i||_sharp.

The exact hypotheses and constants are in Theorem `6.4:thm-per-ball-bound`, lines 63964–64014. The symbol mathfrak_r is its polydisc-contraction parameter; r is its source radius. This result is genuinely independent of m for a **fixed local source tuple**. It does not state a uniform radius as n or R grows.

Three proposed substitutions fail:

1. **One source filling the torus.** Its support radius grows like L^m. Then ell and Q_infinity grow. A constant source cannot be put into a fixed ball as m grows.
2. **One fixed-radius source per cell, with all parameters equal to t.** The number n grows with volume, while the weighted l1 source norm contains n|t|. Q_infinity also depends on n through ell. Even if one grants a separated decomposition, the displayed radius has no nonzero volume-independent lower bound. A literal decomposition into all plaquette sources has additional support/separation and cell-fitting problems. The theorem's condition L^m >= ell(n,R) already fails for the naive n of order L^(4m) at fixed R.
3. **Use chessboard dissemination backwards.** The proof bounds a local-source expectation by roots of mirror-periodic partition functions. This is an upper bound in one direction. It does not yield a lower bound on those partition functions or zero-freeness for an arbitrary homogeneous complex source. On odd cells dissemination conjugates the source; this must also be distinguished from simply copying one complex t everywhere.

At fixed cutoff, local-source zero-freeness by itself is unsurprising: for a bounded observable B of fixed support,

    |E exp(zB)-1| <= exp(|z| ||B||)-1,

so |z| < log(2)/||B|| gives a zero-free disk independent of the surrounding volume for *any* probability measure. The manuscript's achievement is cutoff-uniform local control after counterterms. That ultraviolet strength does not resolve extensive-source thermodynamic singularities.

Likewise, a volume-independent bound on Cov(B_x,B_y) without decay gives at best order V^2 for Var(sum_x B_x), not the order V susceptibility estimate needed here. The remaining term in (3.15) is independent of d, so the exponentially small localized-counterterm tail cannot be read as decay of the full covariance.

## 4. Which H2 directions belong to the source theorem?

H2 asks about A in a family containing real and imaginary parts of X_i, Theta X_i, and (Theta X_i) X_j, and about

    G_(A,m)(t) = E_(beta,m) exp[t sum_x tau_x A].

Every such A is bounded and depends on finitely many links when the X_i do. A reflected product can have disconnected or widely separated support; it is still a finite-range local interaction for the DLR/pressure argument. Its range may depend on i,j, which is allowed.

The manuscript's sources are **linear combinations of plaquette action densities in the exponent**. This includes the isotropic homogeneous energy direction and more microscopic weight patterns at fixed cutoff. For example, a finite plaquette-linear A has a translated sum which is a plaquette-linear potential with finitely many orientation-dependent coefficients. On the finite-spacing barycentre set, an appropriate periodic Lipschitz scalar interpolation represents those coefficients. Its sharp norm can deteriorate as epsilon tends to zero, but can be bounded independently of volume at a fixed epsilon. Thus the source-class obstruction should not be overstated as excluding every homogeneous first moment beyond the isotropic energy.

It does exclude the general H2 directions as stated:

- A general bounded continuous local observable need not be analytic in complexified link variables, and is not given by A(w,U).
- Even if X_i and X_j are plaquette-linear, their reflected product is a quadratic product of plaquette variables, not another coefficient weight multiplying a single plaquette action.
- Wilson-loop or general finite-support gauge-invariant observables are not included just because their support is bounded. The source theorem is not a theorem for arbitrary small finite-range interactions.
- Differentiating the admitted multi-source partition function can recover finite-volume product moments. That does not insert exp[t sum_x (Theta X_i)X_j]. Expanding the latter requires all orders and volume-summed connected estimates, including repeated/overlapping supports; the separated-source theorem and its n-dependent constants supply no such resummation.

One could choose a countable dense observable family of sufficiently regular gauge-invariant functions rather than arbitrary continuous functions. That could remove a field-regularity mismatch, but does not convert nonlinear product interactions into plaquette coefficient sources. A new source-stability theorem or a direct susceptibility/zero-free estimate in those directions is still required.

## 5. Exact conditional normal-family implication at fixed cutoff

**Proposition.** Fix finite beta, a real bounded finite-support observable A, and the straight periodic volume family, with V_m sites. Suppose that for some r_A>0, the functions

    G_m(z) = Z_(A,m)(z)/Z_(A,m)(0)
           = E_(beta,m) exp[z S_m],
    S_m = sum_x tau_x A,

have no zeros on |z|<r_A for an unbounded subsequence of volumes. Then the real infinite-volume source pressure p_A(t) is real analytic near t=0. In particular it is differentiable there.

**Proof.** The homogeneous finite-range bounded interaction has a real thermodynamic pressure, independently of free/periodic boundary choices. This is the same surface/tiling fact used in the earlier H2 report. The use of a subsequence does not change this real pressure.

Since the disk is simply connected and G_m(0)=1, choose its holomorphic logarithm L_m with L_m(0)=0. Set q_m=L_m/V_m. For real t, G_m(t)>0, and continuity from zero gives q_m(t)=V_m^(-1) log G_m(t). For complex z,

    |G_m(z)| <= E exp[(Re z) S_m]
              <= exp[V_m ||A|| |Re z|].

Thus Re q_m(z) <= r_A ||A|| throughout the disk, while q_m(0)=0. Borel–Caratheodory on smaller disks gives local uniform bounds on |q_m|. Montel supplies subsequential locally uniform holomorphic limits. Every such limit agrees on the real interval with p_A(t)-p_A(0), by real thermodynamic convergence. The identity theorem makes all subsequential limits identical. Hence q_m converges locally uniformly on the disk to a holomorphic function restricting to p_A(t)-p_A(0). This proves the proposition. Derivatives converge as well. QED.

For clarity, the boundedness estimate uses V_m translates, with ||S_m|| <= V_m||A||. An alternative anchoring convention with a fixed number c of terms per site only replaces ||A|| by c||A||.

**Consequences and exact scope.**

- The common zero-free disk is the missing premise. Existing extensive bounds supply no such premise.
- At fixed cutoff no additional counterterm estimate is needed once that premise holds. For an admitted source one could instead combine an extensive counterterm bound with a zero-free corrected partition function; its zeros are exactly those of the original partition function.
- r_A may depend on A, its support, beta, and the cutoff; it need not be uniform as beta tends to infinity, as the cutoff is removed, or across the countable family D.
- Each A may use its own unbounded volume subsequence: real pressure is already unique as a numerical thermodynamic limit. No common analytic subsequence for all A is needed to establish the individual H2 statements.
- Applying the proposition to every A in D gives H2. Together with the independently established H1, the earlier entropy/subgradient proof transfers the selected reflected covariance matrices to every straight-periodic cluster state.
- This is stronger than necessary: H2 asks only differentiability at zero. A volume-uniform susceptibility bound in a real neighborhood, or a suitable weaker second-difference bound, would suffice without complex zero-freeness.

## 6. Stronger-looking results elsewhere do not fill the gap

Theorem 7.2(b), printed pp.114–116, gives holomorphic dependence of selected continuum correlation functions on a tuned bare-coupling offset on **one fixed torus** T_(m_0). Its strip width is upsilon_w = 3rho/[256(Q_w+1)], and m_0 enters through Q_w. It is a cutoff-comparison result, conditional on separately identified inputs; it is not fixed-cutoff infinite-volume analyticity. Holomorphy of running shifts and real-analytic renormalized-coupling charts have the same distinction from a thermodynamic log partition function.

The source itself leaves the thermodynamic question open. [Raw III, lines 75490–75507](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/theorem_0_complete_account_raw_III.tex#L75490-L75507) says its compact-window reduction does not assert the desired infinite-volume properties and points to further last-scale infinite-volume cluster expansions, a volume-uniform gap, or absence of partition-function zeros as possible inputs. Its following non-assertions, lines 75550–75611, include infinite-volume uniqueness, clustering, analyticity at fixed distances, convergence in volume, and conclusions for local observables other than the smeared action density. These disclaimers are corroborative, not substitutes for the quantitative analysis above.

A separate provenance caution: the main PDF's broad proof-status descriptions and the raw account are not perfectly aligned. The main Theorem 0 is explicitly conditional on declared inputs (p.12). Raw II's source theorem itself assumes a preparatory-window statement whose proof is outstanding (lines 2791–2814), and Proposition `5.6:prop-polydisc-holomorphy`, lines 46131–46177, is explicitly followed by “Proof outstanding”; lines 60282–60285 list it among clause (iii)'s unproved inputs. This audit does not resolve those underlying proof obligations. The negative H2 implication survives even if all of them are supplied, so it does not depend on rejecting the source theorem.

## 7. What next estimate would actually close this route?

At each desired finite beta, for every A in the selected first-moment/reflected-product family, prove one of:

1. A common complex zero-free disk for G_(A,m) along an unbounded straight-periodic volume subsequence. The proposition then yields H2.
2. A real-neighborhood estimate

       sup_m sup_(|t|<t_A) Var_(beta,m,t)(sum_x tau_x A)/V_m < infinity.

   Integrating the finite-volume second derivative twice and passing to real pressure proves differentiability at zero. This is exactly the earlier susceptibility criterion, now with the required source identified explicitly.
3. A direct vanishing seam-response comparison for these same observables, which bypasses this pressure route entirely.

A pointwise covariance bound, analyticity of the RG coupling recursion, local per-ball zero-freeness, a zero-source pressure comparison, and an extensive upper stability bound do not supply any one of these estimates. None of the inspected source statements proves the required new input.
