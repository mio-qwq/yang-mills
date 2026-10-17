# Actual single-link Dobrushin failure at large Wilson coupling

2026-10-17. This is a diagnostic of a known comparison method's scope, not evidence against a physical mass gap and not a novelty claim for strong/weak-coupling behavior. It strengthens the previous observation that our sufficient upper bound 18β becomes unusable: the actual single-link total-variation influence matrix fails the contraction criterion.

## Result

Consider SU(2) Wilson theory on a periodic four-dimensional lattice of side n≥4 with density

  Z^(-1) exp(β Σ_p (1/2) Re Tr U_p) dHaar,   β>0.

Let c_ef(β) be the supremum total-variation change in the conditional law at link e when only another link f is changed. Let e and f be adjacent when they share a plaquette. Then every link has exactly 18 such neighbors and

  c_ef(β) ≥ L(β) := max{0,1-6 exp(-β/2)}   for every adjacent e,f;   (1)
  c_ef(β) = 0                             for nonadjacent e,f.

Consequently, for every e,

  Σ_f c_ef(β) ≥ 18 L(β),
  lim_(β→infinity) Σ_f c_ef(β) = 18.                            (2)

Already β≥4 makes L(β)>1/6, and so even the six private parallel neighbors alone force the row sum above one. β≥6 is a looser threshold with an immediate numerical margin. No weighted sup-norm version of the same single-link total-variation matrix can restore contraction when 18L(β)>1.

The Wilson parameter β is the coefficient of normalized trace in this statement. Other action normalizations must convert this threshold accordingly. The asymptotically-free bare trajectory eventually leaves this method's possible contraction regime. This failure concerns the periodic endpoint s=1, so an interpolation-uniform application of the same criterion also cannot work there.

## 1. Realizable six-staple geometry

Fix the positive link e=(0,e_mu). There are six plaquettes containing e, one for each ±nu with nu≠mu. Orient each loop so that it starts by traversing e. Its remaining three links form a path from e_mu back to 0; write its ordered holonomy H_p. Since the trace of an SU(2) matrix is real and invariant under inversion, plaquettes originally written with the opposite orientation have the same Wilson weight in this convention. The conditional density at e is therefore

  μ(dU_e | outside) ∝ exp[(β/2) Re Tr(U_e H)] dHaar(U_e),
  H = Σ_(p containing e) H_p.                                  (3)

For n≥4, the six three-link paths are pairwise link-disjoint: their only common vertices that matter are the endpoints of e, and sharing a vertex imposes no constraint on link variables. Explicitly the plus-nu path uses the transverse links at 0 and e_mu in direction nu and the private opposite parallel link (e_nu,e_nu+e_mu). The minus-nu path uses the corresponding links at -e_nu and e_mu-e_nu, with private parallel link (-e_nu,e_mu-e_nu). These links are distinct for different signs and transverse directions modulo n. Thus there are 18 distinct neighbors, each occurring in exactly one target staple.

Set all transverse links in these paths to I. Each H_p can then be assigned an arbitrary SU(2) value by choosing its private parallel link to that value or its inverse, according to orientation. Other lattice links may be set to I. This defines a genuine global link configuration; there is no independent-plaquette assignment or ignored plaquette constraint.

## 2. Two boundary configurations differing at one prescribed neighbor

Choose any neighboring link f, and let p_* be its unique target staple. Set H_(p_*)=I. For the remaining five staples choose

  I, I, -I, W, W²,
  W=diag(exp(2πi/3),exp(-2πi/3)).

They sum to zero because W+W²=-I. Hence H=I. Now replace only U_f by -U_f. The center element -I commutes with every matrix, and replacing an inverse link by its negative has the same effect. Therefore only H_(p_*) changes, from I to -I, and H changes to -I.

If f is a transverse link, this operation also changes some plaquettes not containing e. Such plaquettes contribute constants to the conditional log density as a function of U_e; these constants cancel from its normalization. They do not spoil (3). No other target staple contains f.

Thus the two conditional laws at e are exactly

  dμ_+(U)=Z_β^(-1) exp(β t(U)) dHaar(U),
  dμ_-(U)=Z_β^(-1) exp(-β t(U)) dHaar(U),
  t(U)=(1/2) Re Tr U.                                          (4)

The normalizers agree by U↦-U. This construction is made separately for each f, as permitted by the supremum defining c_ef; simultaneous optimizing boundary configurations are not required.

If the definition uses an essential supremum rather than a pointwise supremum, the same bound holds. At every finite β the Wilson measure has strictly positive continuous density relative to product Haar, and the conditional distributions vary continuously in total variation with their outside links. Neighborhoods of the constructed configurations have positive measure and approximate their influence values arbitrarily well.

## 3. Exact SU(2) integral and explicit lower bound

Under normalized SU(2) Haar measure, t has density

  ρ(t)=(2/π)sqrt(1-t²),   -1<t<1,

because SU(2) is the unit three-sphere in quaternion coordinates. Set

  p = Haar{t≥1/2} = 1/3 - sqrt(3)/(4π) > 1/6.

The two densities in (4) cross exactly at t=0. Consequently their total variation is exactly

  TV(μ_+,μ_-)
  = [integral_0^1 (exp(βt)-exp(-βt))ρ(t)dt]
    /[integral_(-1)^1 exp(βt)ρ(t)dt]
  = 1-2μ_+{t≤0}.                                              (5)

The numerator of μ_+{t≤0} is at most 1/2, whereas Z_β≥p exp(β/2). Thus

  TV(μ_+,μ_-) ≥ 1-p^(-1)exp(-β/2) ≥ 1-6exp(-β/2).

Taking the nonnegative part gives (1). This also proves TV→1 without an informal concentration argument. For β≥4, exp(2)>36/5 implies 1-6exp(-2)>1/6. One elementary proof is to truncate the positive exponential series for exp(2) after the sixth-order term. Hence the six parallel neighbors alone give Σ_f c_ef>1, and using all 18 gives a stronger failure. Since each c_ef≤1 and nonneighbors have zero influence, (2) follows by squeezing.

## 4. Positive weights cannot rescue the same matrix

Let w_e>0 be any finite collection of coordinate weights. Select a link e_* with minimal weight. The graph is 18-regular, so

  [Σ_f c_(e_*f) w_f]/w_(e_*) ≥ 18L(β).

Thus max_e w_e^(-1)Σ_f c_ef w_f≥18L(β), regardless of the weights. Equivalently, the actual influence matrix dominates L(β) times the regular adjacency matrix and has spectral radius at least 18L(β). Reweighting the same single-link total-variation criterion therefore cannot bypass the obstruction.

This does not exclude block dynamics, a different metric/influence notion, estimates restricted to typical backgrounds, or a genuinely multiscale comparison. The worst-case boundary configurations are deliberately non-generic. A successful alternative would have to control their role rather than assert that the supremum criterion remains small.

## 5. Consequence for the seam program

The previous strong-coupling seam estimate uses a resolvent (I-C)^(-1) with a contracting single-link influence matrix. The failure at large β is now intrinsic to that chosen method, rather than just an artifact of replacing tanh(β) by β. Even the sharp actual conditional influences approach their maximal values on every neighboring link.

Accordingly, improving the elementary numerical coefficient 18 or replacing β by tanh(β) cannot extend that argument along the continuum bare-coupling trajectory. A valid next estimate must change the comparison objects (for example gauge-invariant blocks or controlled effective interactions), or exploit cancellations specific to the seam third cumulant. No such replacement or uniform infrared estimate is established here.

## 6. Checks and attribution

check_staple_geometry.py enumerates the target plaquettes on n=4,5,6,8 periodic lattices and checks six pairwise link-disjoint three-link paths, 18 unique neighboring links, and one private parallel link per path. It also represents the diagonal SU(2) matrices by sixth-root phases and checks, using exact integer arithmetic, the oriented staple sums H=+I and H=-I for each of the 18 possible single-neighbor flips. All checks pass. These checks supplement the explicit coordinate argument, rather than substitute for the proof.

The Dobrushin influence criterion and its use in covariance comparison are standard; see the primary comparison framework in Rebeschini–van Handel, Comparison Theorems for Gibbs Measures, https://arxiv.org/abs/1308.4117. The explicit SU(2) boundary configurations and constants above are independently derived for this diagnostic. No priority claim is made for this observation.
