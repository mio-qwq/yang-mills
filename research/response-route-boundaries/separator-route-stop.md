# Source–seam conditioning: exact reduction, endpoint cancellation, and route stop

2026-10-17. This note checks the proposed spatial-Markov reduction. It does not supply a new source-to-seam decay estimate. The route stops at the missing boundary-stability estimate rather than promoting that estimate into a theorem.

## 1. What conditioning actually proves

Use the finite SU(2) Wilson seam family μ_s and V=βΣ_seam w_p. Let A=ΘF and B=F, with both supports inside a region separated from all seam plaquettes. Choose a set Γ of link variables separating the two regions in the graph whose vertices are links and whose adjacency means belonging to a common plaquette. Partition the remaining links into I and O, with A,B measurable on I∪Γ and V measurable on O∪Γ. No plaquette may contain both an I link and an O link.

Conditioned on Γ, the product-Haar Gibbs density factors into an I factor and an O factor. Thus the two sets of random variables are conditionally independent. With

  H_s=(A-E_s A)(B-E_s B),
  h_s=E_s[H_s|Γ],   v_s=E_s[V|Γ],

one obtains exactly

  κ_s(A,B,V)=Cov_s(H_s,V)=Cov_s(h_s,v_s).             (1)

In terms of the conditional covariance and conditional means this is equivalently

  κ_s(A,B,V)
  = Cov_s(Cov_s(A,B|Γ), v_s)
    + κ_s(E_s[A|Γ], E_s[B|Γ], v_s).                (2)

If Γ lies strictly inside the seam and no plaquette depending on I has a seam coupling, the conditional expectation operator K_{I,β}(·|Γ) for the interior is independent of s. Only its boundary argument and boundary marginal vary with s. This is a genuine separation of the roles of the bulk specification and the seam perturbation, but not a quantitative decay statement.

## 2. Where the useful bound would have to enter

For real variables Cauchy–Schwarz gives

  |κ_s(A,B,V)| ≤ sqrt(Var_s(h_s)) sqrt(Var_s(v_s)).   (3)

Neither factor is known to decrease with the distance between the source and Γ. Conditional expectation is an L2 contraction, but its contraction constant is at most one, with no strict or distance-dependent gain from the Markov property alone.

For example a worst-boundary oscillation estimate could be expressed through

  osc_Γ h_s ≤ osc K_{I,β}(AB)
              + |E_s A| osc K_{I,β}(B)
              + |E_s B| osc K_{I,β}(A).

Bounding these oscillations by something tending to zero as Γ recedes is a boundary-stability/mixing assertion. It is not a consequence of writing the conditional expectation. Likewise using a weighted L2 boundary law merely replaces the missing uniform estimate by a missing averaged estimate.

The seam score v_s-E_s V is the derivative of the log marginal density of Γ along the interpolation. Its existence and exact score interpretation do not bound its variance or its correlation with h_s. A naive bound retains the seam area and β, with no suppression by source distance.

Therefore this conditioning route alone yields no non-tautological distance estimate beyond the previously proved strong-coupling regime. Applying strong-coupling Dobrushin control here would only repeat that result; assuming a new contracting block kernel would assume the missing input. This is the stopping point for the proposed route.

## 3. A useful exact endpoint check: interior marginals are even in the seam parameter

The actual induced cube has an extra elementary symmetry. In the periodic coordinate representation {0,...,n-1}^4 its vertex set is C={1,...,n-1}^4. A plaquette has either four internal links, exactly one internal link, or no internal links. To see this, its internal vertices are the product of the allowed coordinate values in its two varying directions. They therefore number four, two adjacent vertices, one vertex, or zero vertices. The corresponding counts of internal edges are four, one, zero, zero. Thus every mixed plaquette has exactly one interior link and three exterior links.

Apply the map U_e→-U_e to every exterior link, leaving all interior links fixed. Haar measure is preserved. Each exterior-only plaquette has four transformed factors, hence unchanged Wilson weight. Interior-only plaquettes are unchanged. Every seam plaquette has three transformed factors and its normalized trace changes sign. This remains true for inverse link factors because (-U)^(-1)=-U^(-1).

It follows, by change of variables in the exterior integral, that for every bounded observable G depending only on interior links,

  E_s[G]=E_(-s)[G].                                 (4)

Here the finite-volume family is extended to negative real s only as an analytic identity; no reflection-positivity assertion for negative seam couplings is needed. The normalization also agrees under s↦-s.

Consequently, for interior F,

  Q_s(F)=Q_(-s)(F),
  κ_0(ΘF,F,V)=Q'_0(F)=0.                            (5)

The same conclusion follows directly from E_0[V|all interior links]=0: at s=0, the exterior variables factor from the interior, and the exterior sign transformation makes V odd while leaving their measure invariant.

All odd derivatives of an interior expectation at s=0 vanish. This is an exact finite-volume cancellation; the observable and its deterministic normalization are held fixed during differentiation.

## 4. Why the endpoint identity does not close the bridge

Equation (5) is compatible with the large probability of low unweighted staple magnitude in the seam layer. A frequent local configuration is not a lower bound on a distant connected response. In particular the rarity-based lower bounds must not be read as lower bounds on κ_s.

Evenness implies that Q_s-Q_0 starts at even order in the finite-volume Taylor series. Its coefficients involve additional seam insertions, however; they can carry powers of β and the number of seam plaquettes. No uniform cutoff/volume bound on those coefficients has been derived here. A zero derivative at one endpoint gives no control on the integral from s=0 to s=1, nor on the layer s=O(1/β), without a quantitative estimate.

The appropriate next mathematical input would still be a proven distance-sensitive stability estimate for K_{I,β} or a controlled effective boundary interaction. This note supplies neither and therefore records a route stop, not a new infrared bridge.

## 5. Exact geometry check

check_mixed_plaquette_parity.py enumerates periodic sides 4,6,8 and verifies that internal-edge counts are only 0,1,4. The proof above explains why this holds generally. This is solely a check of the endpoint symmetry; no numerical mixing inference is made.
