# A boundary-response bridge for diagonal reflection positivity

Date: 2026-10-17. Frozen reference: SHA 785a68fdeef78a1da854c4807fe1f17b597d05e7. This is a finite-lattice lemma and a precise missing estimate, not a proof of the Yang–Mills mass gap or of the missing estimate.

## Finding

It is unnecessary to transfer the entire RG construction, nontriviality proof, or moment bounds to free-boundary boxes in order to prove diagonal reflection positivity of an already constructed periodic two-point limit. It suffices to control a specific integrated boundary response of the connected reflected quadratic form. That response is a third cumulant, with a seam-energy insertion. The estimate needed is uniform in the ultraviolet cutoff and applies to seam-weakened measures, not just the periodic measure. None of the cited periodic per-ball bounds supplies it.

This is a reduction to a narrower analytic target than full boundary-condition or shape independence. It does not establish that target.

## Exact finite-volume construction

Take a four-dimensional periodic lattice T of spacing a and even side 2Na, with representatives {-N,...,N-1} in each coordinate, and SU(2) link variables with product Haar measure. Let C be the induced free cube with vertex set {-N+1,...,N-1}^4. The reflection theta(x0,x1,x2,x3)=(-x1,-x0,x2,x3) preserves both the torus and C. The same construction works on any larger periodic box containing such a reflection-symmetric cube.

Partition the link variables into E_in (links whose two endpoints belong to C, with the ordinary nonwrapping cube interpretation) and E_out (the other links). Let P_seam be the plaquettes containing both an E_in link and an E_out link. Their number is O(N^3). Let P_rest contain all other plaquettes. A plaquette wholly in E_in is exactly a free-cube plaquette. Removing P_seam therefore makes the inside and outside measures independent. One must remove mixed-link plaquettes, not merely plaquettes whose base point is outside C.

Write w_p(U)=(1/2) Re Tr U_p, beta>0, and

  d mu_s = Z_s^{-1} exp[beta sum_{p in P_rest} w_p + s beta sum_{p in P_seam} w_p] dHaar,  0<=s<=1.

Then mu_1 is the original periodic Wilson measure; mu_0 restricted to E_in is the free-cube Wilson measure. Define V=beta sum_{p in P_seam} w_p. Constants in the Wilson action do not affect the calculation. The geometry and every mu_s are theta invariant. This construction uses exactly the original bare coupling and the original torus; there is no retuning of reference coupling.

Let F be any complex continuous function of links on the positive side of the mirror, supported strictly inside C; for the intended application take F=sum_alpha z_alpha O_a(f_alpha), with scalar, reflection-covariant, gauge-invariant local action-density observables and tests supported a positive physical distance from the diagonal plane. Define the antilinear reflection Theta F(U)=overline{F(theta U)}, and

  Q_s(F)=E_s[(Theta F)F]-E_s[Theta F]E_s[F].

All identities below hold exactly at each finite lattice, even if the deterministic normalization of O_a diverges as a goes to zero. F must be held fixed while s is varied. Additive deterministic subtraction constants do not change Q_s or the third cumulant.

## Lemma and proof

1. Q_0(F)>=0.

The SU(2) Wilson plaquette weight has a character expansion with nonnegative coefficients:

  exp[(beta/2) chi_{1/2}(U)] = sum_j c_j(beta) chi_j(U), c_j(beta)>=0.

Indeed the exponential series has positive coefficients, and every tensor power of the fundamental character decomposes with nonnegative integer multiplicities. A plaquette cut by the diagonal mirror consists of a path A and its reflected path B between two fixed vertices. For every unitary irrep,

  chi_j(AB^{-1}) = sum_{r,t} D_j(A)_{rt} overline{D_j(B)_{rt}}.

Thus each crossing plaquette contributes a positive kernel. Plaquettes contained on the mirror give a positive interface weight; plaquettes strictly to either side occur as reflected pairs. Conditional on interface links, integration factorizes into positive and negative halves. This gives E_0[(Theta G)G]>=0. Apply it to G=F-E_0[F]. Reflection invariance gives exactly Q_0(F)>=0. Independent exterior links do not affect this statement.

2. dQ_s(F)/ds = kappa_s(Theta F,F,V).

Differentiation under the finite compact integral gives d E_s[A]/ds=Cov_s(A,V). Differentiate the three terms defining Q_s; expanding yields

  E_s[(Theta F)FV] - E_s[(Theta F)F]E_s[V]
  - E_s[(Theta F)V]E_s[F] - E_s[FV]E_s[Theta F]
  + 2 E_s[Theta F]E_s[F]E_s[V],

which is the joint third cumulant. It is real because the measure and V are reflection invariant. Hence

  Q_1(F)=Q_0(F)+integral_0^1 kappa_s(Theta F,F,V) ds
        >= -[ -integral_0^1 kappa_s(Theta F,F,V) ds ]_+.

The sharper exact lower bound is Q_0 plus the signed integral. Bounding its negative part is only a sufficient criterion, not a necessary one.

## The missing estimate in the actual joint-diagonal setting

Let (a_j,T_j) be an existing periodic joint diagonal from Theorem 0, with a_j->0 and physical side(T_j)->infinity; choose the above centered cube C_j. Fix any finite collection of positive-half-space compactly supported tests and coefficients, and let F_j denote its lattice representative.

A sufficient estimate, with precisely the relevant order of limits, is

  lim_{j->infinity} [ - integral_0^1 kappa_{j,s}(Theta F_j,F_j,V_j) ds ]_+ = 0.  (BRP)

If BRP holds for every such collection, and the periodic two-point pairings converge as in the reference, their limit is diagonally reflection positive on one-field vectors. Proof: Q_{j,1} converges to the required quadratic form, Q_{j,0}>=0, and the displayed finite-lattice lower bound applies. No limit of Q_{j,0}, tightness of mu_{j,0}, free-boundary continuum construction, or uniqueness theorem is required.

A more practical but stronger sufficient estimate is

  integral_0^1 sum_{p in P_seam,j} beta_j
       |kappa_{j,s}(Theta F_j,F_j,w_p)| ds <= epsilon_F(R_j),
  epsilon_F(R)->0,

uniformly in the cutoff, where R_j is the physical distance to the seam. Cancellation in the signed sum can make BRP much weaker than this absolute estimate. For real basis observables the quadratic-form statement is equivalently positivity of the Hermitian matrix of connected reflected pairings; complex coefficients require no extra assumption.

One can instead cut a physical cube of fixed radius R in each sufficiently large torus, retaining all exterior plaquettes, and then require lim_{R->infinity} limsup_{j->infinity} of the negative response to vanish. That version again compares to the same periodic state and does not exchange a free-boundary thermodynamic limit with a continuum limit. The seam itself always has a finite physical distance from the sources before R is sent to infinity.

## Why the currently quoted bounds do not prove BRP

- Raw I, lines 2608–2621 approximately: clause (iii-b) is a per-ball volume-free bound for separated smeared curvature correlations in the periodic model. It explicitly asserts no decay in separation. It does not cover mu_s with spatially varying plaquette coupling down to zero at a seam.
- A seam has O((R/a)^3) plaquettes. A cutoff-independent bound on each insertion would not make the summed response small; beta_j and the observable normalization must also be retained. A bare plaquette insertion cannot silently be replaced by a unit-normalized continuum density.
- Cutting is not a small perturbation in total variation. Since |w_p|<=1, the elementary likelihood-ratio estimate costs exp[2 beta |P_seam|]. This diverges both with cutoff removal and with boundary size. Standard bounded-density transfer of periodic bounds is therefore useless here.
- Localized large-field/polymer boundary terms are not automatically external free-box boundary conditions. The free-boundary response operator appearing elsewhere in Raw I is a linear response/minimizer object, not a theorem giving the needed nonlinear Gibbs-measure estimate.
- Even a mass gap for one limiting periodic state would not, by itself, control all mu_s at every cutoff. Invoking uniform exponential clustering throughout this interpolation is a new hypothesis and would import a major part of the desired infrared result.
- Translation invariance need not be proved for free-boundary limits: this reduction transfers positivity to the already translation-invariant periodic limit. Thus it avoids another common unproved step in the exhaustion argument.

## Relation to the claimed main target

Raw III 79931–79989 states that diagonal RP plus the listed existing assumptions yields two-point O(4) invariance, and explicitly says diagonal RP is unproved. The lemma above gives an exact microscopic object whose smallness would establish that missing assumption. It proves neither its smallness nor a spectral gap. Even successful BRP supplies only the two-point rotation bridge; it does not establish all higher-point Euclidean covariance, uniqueness of vacuum, or a mass gap.

Raw I 2688–2712 explicitly excludes uniqueness/clustering and a mass gap. Raw III 108223 onwards uses clustering or a mass gap only as sufficient hypotheses for reflected decay; 109214 states that a cutoff-uniform gap is not asserted. Reading these implications backwards would be circular.

## A justified next analytic experiment

Derive a multiscale expansion with one seam-energy derivative and two fixed bulk source derivatives, retaining the derivative's signed sum. The quantity to estimate is the integrated third cumulant above. A sufficient coarse-grained estimate would be: after grouping seam plaquettes into unit physical patches D, uniformly in s and cutoff,

  |kappa_s(Theta F,F, beta sum_{p in D} w_p)| <= C_F (1+dist(D,supp F union supp Theta F))^{-3-delta}, delta>0.

There are O(R^3) such patches for a cubic seam at radius R, giving O(R^{-delta}). This is a conditional bookkeeping criterion, not a proved RG bound. Patch normalization includes beta and all microscopic plaquettes, so it avoids losing ultraviolet factors. The endpoint s=0 and spatially inhomogeneous running couplings are the main additional analytic difficulties. Polynomial decay at this threshold would suffice for this bridge; exponential decay and a mass gap are not logically required.
