# A bad-staple probability counterexample inside the actual seam interpolation

2026-10-17. This is a finite-volume statement for the same mixed-plaquette free-cube interpolation used in DIAGONAL_RP_BRIDGE.md. It disproves uniform low-staple rarity over every link and every interpolation parameter. It does not disprove bulk rarity away from the seam, boundary-response decay, or a mass gap.

## Result

On a four-dimensional periodic lattice of even side 2N with N≥3, cut the induced cube C={-N+1,...,N-1}^4. Let μ_s have Wilson coefficient β on nonseam plaquettes and sβ on the mixed-link seam plaquettes, 0≤s≤1. Fix a link e crossing one flat face from C into the exterior layer, with its transverse coordinates at least two lattice steps from the transverse edges of C. Let S_e be the sum of the six oriented unit-quaternion staples around e, without coupling weights.

At s=0 the six staples are independent SU(2) Haar variables. In particular, for every β≥0,

  E_0 |S_e|² = 6,
  P_0{|S_e|≤4} ≥ 5/8.                                      (1)

For 0<h≤1 define

  c_h = [sqrt(2) h³/(81π)]³ >0.

For all β≥0 and all 0≤s≤1,

  P_s{|S_e|≤h} ≥ exp(-72sβ)c_h.                            (2)

Likewise,

  P_s{|S_e|≤4} ≥ (5/8)exp(-72sβ).                          (3)

Consequently, for every fixed b>0, these probabilities have a positive lower bound independent of β throughout 0≤s≤min(1,b/β), with the β=0 case interpreted directly. No bound tending to zero as β→infinity can hold uniformly over all s and all links for either of these bad-staple events. In particular a putative uniform Ce^(-cβ), or uniform O(logβ/β), estimate fails on this actual seam layer.

The integer 72 is a deliberately conservative local oscillation constant, not an optimal value.

## 1. The geometry and the probability space

Take e from x=(N-1,0,0,0) to x+e_0, whose endpoint is represented by (-N,0,0,0) on the torus. For each nu=1,2,3 and sign ±, let f_(nu,±) be the parallel crossing link based at x±e_nu. Call this six-link set B.

Every plaquette containing any link of B is a mixed-link plaquette: it has a transverse edge on the inside face x_0=N-1, whose endpoints belong to C, and another transverse edge on the outside face x_0=-N, whose endpoints do not. The transverse distance condition ensures the inside edge really is internal, including for plaquettes extending a further step from f_(nu,±). The same property holds for the six plaquettes containing e. Therefore all incident couplings of every link in B vanish at s=0. These links are independent Haar variables, independent of all other links, in the exact finite-volume law μ_0.

The six target staples have disjoint three-link paths. Each contains precisely one member f_i of B and two transverse links outside B. Given all links outside B, its holonomy has the form

  H_i = A_i U_(f_i)^(epsilon_i) B_i,   epsilon_i∈{-1,+1},

where A_i,B_i are fixed SU(2) matrices. Left multiplication, right multiplication and inversion preserve Haar measure. Thus H_1,...,H_6 are conditionally independent Haar variables with a conditional joint law that does not depend on the outside configuration. They are therefore also independent Haar unconditionally. This is a statement about link variables in the actual Gibbs measure, not an independent-plaquette approximation.

The cube and torus may be enlarged without changing this local construction. Plaquettes outside the seam retain their full β coupling throughout.

## 2. Exact second moment and a positive low-sum event

Identify SU(2) with unit quaternions in R^4. For a Haar quaternion H, E H=0 and |H|=1. Independence gives

  E|Σ_(i=1)^6 H_i|²=Σ_i E|H_i|²+Σ_(i≠j) E H_i·E H_j=6.

Markov's inequality gives P{|S_e|>4}≤6/16, proving (1).

For a lower bound at genuinely small magnitude h, first expose H_1,H_2,H_3. Require

  |H_(i+3)+H_i|≤h/3,  i=1,2,3.

The triangle inequality then gives |S_e|≤h. Each of these independent conditional events has the Haar volume v_delta of a Euclidean quaternion ball of radius delta=h/3 centered at a unit quaternion. Rotational invariance makes this volume independent of the center.

For 0<delta≤sqrt(2), write t for the real quaternion coordinate after moving the center to I. Its Haar density is (2/π)sqrt(1-t²), and |H-I|²=2(1-t). Thus

  v_delta=(2/π) integral_0^(delta²/2) sqrt(2u-u²) du
          ≥ [sqrt(2)/(3π)]delta³,

using sqrt(2u-u²)≥sqrt(u) on 0≤u≤1. The probability of all three pairing events is v_(h/3)^3≥c_h. This proves P_0{|S_e|≤h}≥c_h with a fully explicit constant. For h=1 the bound is approximately 1.7×10^(-7); it is intentionally crude but strictly positive and independent of β and volume.

## 3. A local conditional-density comparison for s>0

Condition μ_s on all links outside the six-link set B. Every plaquette that depends on B is a seam plaquette, by the geometry above. There are at most 6×6=36 such plaquettes (in this geometry they are distinct). Write t=sβ. The block conditional log potential is

  L(U_B)=t Σ_(p incident to B) w_p(U_B),   |w_p|≤1.

Hence osc(L)≤72t. Relative to normalized product Haar m_B, its conditional density satisfies

  exp(L)/integral exp(L)dm_B ≥ exp(-osc(L)) ≥ exp(-72t).

For the event |S_e|≤h, its conditional product-Haar probability is the same Haar-sum probability calculated above, regardless of the outside transverse links. Multiplying by the density lower bound and then averaging over the outside conditional law proves (2). Using the second-moment lower bound instead proves (3).

This is a local normalized conditional estimate. No global partition function ratio is omitted: the block normalization is explicitly bounded using osc(L). No comparison of two different outside configurations is used.

## 4. What must change in a plausible weak-coupling estimate

A rarity statement along the interpolation must distinguish the seam layer from bulk regions whose incident couplings remain strong. Even at β→infinity, a layer with sβ=O(1) contains crossing links with a nonconcentrated distribution. The bad-staple event has order-one probability in that local layer; it cannot simply be classified as a uniformly exponentially rare defect.

The interval on which this obstruction persists has width of order 1/β. That fact alone does not make its contribution to the integrated seam response small, because the insertion V_seam=βΣ_p w_p carries a factor β. No lower bound on the actual response is claimed here: the connected cumulant may still be small because its bulk source is far away. The point is that one needs a source-to-layer response estimate, not only a claim that bad staples are rare everywhere.

The event uses the unweighted six-staple magnitude. If one instead defines the staple sum using its actual local coupling weights, the target link's weighted sum is exactly zero at s=0, making an all-links uniform nondegeneracy claim fail even more directly.

## 5. Check

check_seam_haar_geometry.py enumerates all plaquettes on periodic sides 6,8,10 with the corresponding induced free cube. It verifies that the target and its six opposite links are incident only to mixed plaquettes, that each target staple has one private opposite link, and that the opposite links meet exactly 36 seam plaquettes. All assertions pass. The probability argument above is analytic and does not depend on simulation.
