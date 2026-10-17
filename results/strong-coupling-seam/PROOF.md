# An explicit, uniform seam-response bound at strong coupling

2026-10-17. Scope: finite four-dimensional SU(2) Wilson lattices, including the whole free-to-periodic seam interpolation. This applies standard Dobrushin comparison and Föllmer covariance machinery to prove the previously isolated seam estimate in an explicit strong-coupling regime. No novelty is claimed for that machinery or for strong-coupling mixing. It does not cover the weak-bare-coupling continuum trajectory required for the Yang–Mills problem.

## 1. Statement

Let the finite periodic lattice have side at least four lattice spacings. On its positively oriented links E, put product SU(2) Haar measure and

  dμ_s = Z_s^(-1) exp(Σ_p β_p(s) w_p) dHaar,
  w_p = (1/2) Re Tr U_p,
  0 ≤ β_p(s) ≤ β,
  β_p(s) = sβ for p in P_seam, and β otherwise.

The seam set is the mixed-link plaquette set of DIAGONAL_RP_BRIDGE.md: deleting it separates the interior free cube from the remaining link variables. Define

  V = β Σ_(p in P_seam) w_p.

Let F be a real bounded bulk observable, and let θ be the diagonal reflection on link configurations. Define the antilinear reflection on observables by ΘF(U)=overline{F(θU)}. Put M=||F||∞, A=ΘF, B=F, and let S contain every link on which A or B depends. Let B_seam be the set of links belonging to seam plaquettes. Put an adjacency edge between two different links when they belong to a common plaquette, and let

  r = dist_graph(S,B_seam).

This is the graph distance on the full periodic lattice, including all wrapping plaquettes, rather than distance in the cut cube. Periodic shortcuts must therefore be included.

For the nontrivial case assume 0<q=18β<1 and S,B_seam are nonempty. If β=0 or the seam is empty, V=0 and its third cumulant is identically zero. If S is empty, F is constant and the third cumulant and Q_s vanish. These cases are handled directly, without interpreting 0^0 or q^infinity. Then, uniformly in s∈[0,1], lattice size and placement of the seam,

  |κ_s(ΘF,F,V)| ≤ 24 β M² |S| q^r/(1-q).                  (1)

More generally, with H_s=(A-E_s A)(B-E_s B) and δ_e the single-link oscillation seminorm,

  |κ_s(A,B,V)| ≤ [3β q^r/(1-q)] Σ_(e in S) δ_e H_s.       (2)

Consequently, for any bounded F under the preceding covariance hypotheses,

  |Q_1(F)-Q_0(F)| ≤ 24 β M² |S| q^r/(1-q).               (3a)

Here Q_s=E_s[(ΘF)F]-E_s[ΘF]E_s[F]. The additional lower bound

  Q_1(F) ≥ -24 β M² |S| q^r/(1-q)                        (3b)

requires the following additional RP hypotheses: the interior cube and cut are compatible with θ, their s=0 marginal is the free-cube Wilson measure, and F belongs to its reflection-positive half-algebra, with its link support strictly in the positive half of that cube (and away from the seam). These conditions imply Q_0(F)≥0. The lower bound is not claimed for an arbitrary bounded bulk observable: for example F=X−ΘX can have Q_0(F)<0 even at β=0. In the zero cases above, (3b) is asserted only under these same RP hypotheses. For complex F with ||F||∞≤M, assume the seam family and V are invariant under Θ. Writing F=u+iv, reflection invariance and symmetry of cumulants cancel the two imaginary cross terms, and

  κ_s(ΘF,F,V)=κ_s(Θu,u,V)+κ_s(Θv,v,V).

Thus the complex version of (1), (3a) and, under its additional RP hypotheses, (3b) holds with 48 in place of 24, with S covering both real and imaginary supports. This avoids applying the real covariance inequality directly to complex oscillation seminorms. Alternatively, for a fixed finite collection of real scalar sources, the reflected covariance matrix is real symmetric; positivity for all real coefficients implies positivity for complex coefficients.

This is an absolute estimate, stronger than the one-sided estimate needed for the bridge. No mass gap, clustering hypothesis, or uniqueness assumption is imposed; the mixing estimate below is derived directly from the bounded local Wilson interactions.

## 2. Single-link influence bound

For distinct links e,f let k_ef be the number of plaquettes containing both. Condition on all links except e, and compare the conditional law when only f is changed. The difference of the two unnormalized conditional log densities, as a function of U_e, has oscillation at most 4β k_ef: each w_p lies in [-1,1], so its change lies in [-2,2].

For two normalized densities whose log likelihood ratio has oscillation D, their total variation distance is at most tanh(D/4). This follows by maximizing over a two-point distribution at the extreme likelihood ratios; equivalently, if the likelihood ratio ranges in [a,b], normalization gives a≤1≤b and TV≤(1-a)(b-1)/(b-a), whose maximum under b/a≤exp(D) is tanh(D/4).

Thus the conditional influence is bounded by

  C_ef = β k_ef,  C_ee=0.

A link lies in six plaquettes in d=4, and each plaquette has three other links. Counting with multiplicity gives

  Σ_f C_ef = 18β = q.

The same bound applies at s=0 and to arbitrary inhomogeneous couplings in [0,β]. It does not require the seam-interpolated law to retain translated reflection symmetries. Set

  D = (I-C)^(-1) = Σ_(n≥0) C^n.

Since C only joins adjacent links, for every e at distance at least r from B_seam,

  Σ_(f in B_seam) D_ef
  ≤ Σ_(n≥r) Σ_f (C^n)_ef
  ≤ q^r/(1-q).                                          (4)

This row-sum estimate is why no factor proportional to the seam's total area is needed in (1).

## 3. Covariance comparison, including its constant

For bounded real functions h,g of the links,

  |Cov_μ(h,g)| ≤ (1/4) Σ_(e,f) δ_e h D_ef δ_f g.          (5)

Here is a direct derivation of the comparison inequality used in (5). Tilt μ to ν_ε proportional to exp(εg)μ. Its conditional law at link f differs from the μ conditional law at the same outside configuration by at most

  b_f ≤ tanh(|ε|δ_f g/4) ≤ |ε|δ_f g/4.

Here is a finite-iteration proof that requires no stationary coupling theorem. Let m=|E|. Couple random-scan single-link heat-bath updates of μ and ν_ε, choosing the same uniformly random link in each copy and using a maximal coupling of its conditional laws. Such a coupling is explicit: couple the pointwise minimum of their Haar densities on the diagonal and use the product of their remaining normalized densities on the residual event. Let p_e(n) be the probability that the two copies disagree at e after n updates. Telescoping changes of outside links and the influence bound imply

  p(n+1) ≤ A p(n)+b/m,    A=(1-1/m)I+C/m.

The nonnegative matrix A has row sum 1-(1-q)/m<1. Since p(0)≤1,

  p(n) ≤ A^n 1 + (1/m) Σ_(k=0)^(n-1) A^k b,
  limsup_(n→∞) p(n) ≤ (I-C)^(-1)b=Db.

Each marginal heat-bath chain converges in total variation to its prescribed Gibbs law. Indeed its conditional densities are uniformly bounded below by a positive constant relative to Haar, since the finite local Wilson potential and the tilt εg are bounded. In m updates there is positive probability of choosing a specified ordering that updates every link once. This event minorizes the entire m-step transition kernel by a positive constant times product Haar, proving convergence and uniqueness in finite volume. Telescoping h over disagreeing links at time n and passing to the marginal limits therefore gives

  |ν_ε(h)-μ(h)| ≤ Σ_(e,f) δ_e h D_ef b_f.

Division by |ε| and differentiation at ε=0 prove (5). Boundedness justifies the derivative. This argument applies to bounded measurable h and g, as well as continuous lattice observables.

## 4. Applying the comparison bound to the third cumulant

At a fixed s, hold H_s as a function of the links fixed when applying (5). The identity

  κ_s(A,B,V)=Cov_s(H_s,V)

is exact. It does not require differentiating H_s or treating its s-dependent centering constants as observables.

Each link is in at most six seam plaquettes, so

  δ_f V ≤ 12β,
  δ_f V=0 if f is outside B_seam.

Moreover H_s depends only on S. Combining (4) and (5) proves (2). Finally,

  δ_e H_s ≤ 2M(δ_e A+δ_e B) ≤ 8M²,

which proves (1). Differentiating the connected quadratic form with the convention exp(S_rest+sV) gives Q'_s=κ_s(A,B,V); integrating gives (3a). Under the additional positive-half-algebra hypotheses, free-cube reflection positivity gives Q_0≥0 and hence (3b).

## 5. Cutoff and physical-distance content

The graph distance r is measured in plaquette adjacency steps, not physical units. Each such step moves link locations only a bounded number of lattice spacings. Thus if the shortest periodic physical distance from S to B_seam is at least R, r≥cR/a-O(1), with a positive geometric constant c. Distance only within the displayed fundamental cube is not sufficient. In particular, for a uniform q≤q0<1,

  M_a² |S_a| q0^(cR/a)/(1-q0) → 0

whenever M_a²|S_a| grows at most polynomially in a^(-1). This retains the actual deterministic normalization of lattice sources; it does not drop ultraviolet factors. For an arbitrary joint cutoff/volume diagonal, the sufficient condition is explicitly

  [β_a/(1-q_a)] M_a² |S_a| q_a^(r_a) → 0.

A uniform q_a≤q0<1 and polynomial growth of M_a²|S_a| in a^(-1) imply this when the shortest periodic physical source-to-seam distance is bounded below by a positive constant, or grows. No assertion is made for faster-growing normalization or support prefactors without checking this displayed condition. The same condition with a harmless factor two handles complex sources.

The failure on the target Yang–Mills trajectory is explicit. In the Wilson normalization used here β is proportional to inverse bare coupling squared; along asymptotic freedom β tends to infinity. The sufficient contraction q=18β<1 is then unavailable. Failure of this sufficient condition does not show that the desired covariance bound or physical mass gap is false; single-link influence is a deliberately coarse criterion. One cannot restart the argument at a coarse RG scale unless the induced action has a verified summable influence bound there. Such an action need not remain a nearest-plaquette Wilson action, and its multibody interactions and large-field terms must be controlled. Proving that infrared input would be substantive new work, not a consequence of this calculation.

The result does establish that the seam interpolation and order-of-limits criterion are analytically nonvacuous for the actual compact gauge model. The remaining obstruction is the regime of the estimate, rather than a flaw requiring all free-boundary RG estimates or an independently constructed free-boundary continuum limit.

## 6. Exact incidence check

check_link_influences.py enumerates a 5^4 periodic lattice and verifies that all 2500 links belong to six plaquettes and have total off-diagonal shared-plaquette multiplicity 18. With β=1/36 the bound gives q=1/2. This checks the finite incidence constant only; it is not a numerical proof of a continuum statement.

## 7. Attribution and scope of the application

The covariance estimate (5) is standard Dobrushin/Föllmer comparison theory. Relevant primary references are Hans Föllmer, “A Covariance Estimate for Gibbs Measures,” Journal of Functional Analysis 46 (1982), 387–395, listed in the author's [publication bibliography](https://www2.mathematik.hu-berlin.de/~foellmer/publications.html), and Patrick Rebeschini and Ramon van Handel, [Comparison Theorems for Gibbs Measures](https://arxiv.org/abs/1308.4117). The self-contained proof above specifies the convention and constant needed here. The contribution of this note is the explicit application to the connected reflected quadratic form throughout the gauge-theory seam interpolation, with its geometry, source normalization, and restricted coupling regime stated. It is not a new general covariance theorem or a solution of the weak-coupling Yang–Mills problem.
