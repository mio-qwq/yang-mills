# Independent audit: the shorter tilted-torus construction

18 October 2026. This independently audits the tilted-torus construction, reproduced in `../construction/RESULT.md`, Section 2. The construction is **valid** for every finite β≥0. It is simpler than the valid cylinder construction in `RESULT.md`, because its finite laws already have the required translation invariance.

## 1. Quotient and parity

Let

    L_N=span_Z{N(e₀+e₁),N(e₀−e₁),Ne₂,…,Ne_(d−1)},  N≥3.

The index is 2N^d. The quotient vertices are represented bijectively by

    (u,v,z₂,…,z_(d−1)),
    u,v∈Z/(2N), u≡v (mod 2), z_j∈Z/N,

using u=x₀−x₁ and v=x₀+x₁. Indeed the two generating periods in the 01-plane become (0,2N) and (2N,0), and the inverse integer formulas x₀=(v+u)/2, x₁=(v−u)/2 require exactly the same-parity condition.

The positive basis steps have coordinate increments

    e₀: (u,v)↦(u+1,v+1),
    e₁: (u,v)↦(u−1,v+1),
    e_j: z_j↦z_j+1, j≥2.

Reflection R exchanging x₀,x₁ preserves L_N and becomes (u,v,z)↦(−u,v,z). Its fixed vertices are exactly u=0 and u=N modulo 2N. At u=0 the permitted v are even; at u=N they have the parity of N. Thus **odd N is harmless**: the second plane simply consists of odd-v vertices when N is odd.

Independent variables are positively oriented quotient links (x,i), with reverse orientations defined by inversion. R sends (x,0) to (Rx,1), (x,1) to (Rx,0), and (x,j) to (Rx,j). It preserves positive orientation. There are no additional constraints on the independent link variables.

## 2. Separation and plaquettes

Declare 0<u<N the strict positive half and N<u<2N the strict negative half, with the two fixed planes as their common boundary. Because an edge changes u by at most one on the cycle Z/(2N), and the two fixed levels separate the two open arcs, no edge joins the strict halves. An edge with both endpoints in fixed planes must be a transverse e_j edge lying in one plane: the plane separation is N≥3, and e₀/e₁ change u. Each such oriented edge is fixed pointwise under R. Every other edge belongs to exactly one closed half, and R exchanges the two edge sets.

For a 01 plaquette based at a vertex with u=k, the vertex levels are k,k+1,k,k−1 modulo 2N. This set meets both strict halves if and only if k=0 or k=N. To see the converse, a three-consecutive-level interval can cross between the two open arcs only through a fixed level, and that fixed level must be its middle level. N≥3 prevents the interval from containing both fixed levels. For k=0 or N, the base vertex and the diagonally opposite vertex are fixed individually; the two other vertices are reflected into one another. Every plaquette involving just one of 0,1 has only two adjacent u levels, and every wholly transverse plaquette has constant u. Such plaquettes cannot meet both strict halves.

For a crossing 01 plaquette based at x, set

    P=U_(x,0) U_(x+e₀,1),
    Q=U_(x,1) U_(x+e₁,0).

Both paths run from the fixed vertex x to the fixed vertex x+e₀+e₁, and reflection exchanges them. At u=0, P is the positive path; at u=N, Q is the positive path. The plaquette holonomy is P Q⁻¹. Swapping the two paths changes this to its inverse, but

    ReTr(P Q⁻¹)=ReTr(Q P⁻¹),

so both fixed planes give exactly the same positive kernel exp[κ ReTr(P_+P_-⁻¹)] with κ≥0.

N≥3 also rules out the small-quotient geometric degeneracies relevant here. Since L_N⊂NZ^d, no nonzero vector with all coordinates in {−2,−1,0,1,2} lies in L_N. Thus an elementary edge is neither a loop nor equal to its reverse, distinct coordinate-direction edges do not collapse, and all four vertices of an elementary plaquette are distinct. In particular reflection cannot reverse an e₀ edge by identifying e₁ with −e₀, nor reverse a transverse edge by a period of length two.

## 3. Reflection-positive finite Wilson law

The product-Haar variables split into positive, negative, and fixed-plane groups. The noncrossing plaquette actions split as H_++H_−+H_0, where reflection exchanges H_+ and H_− and H_0 is a function only of fixed-plane links. Crossings have the positive kernels just identified.

For SU(2), Tr(PQ⁻¹) is real and equals Σ_ij P_ij overline{Q_ij}. Expanding the exponential in nonnegative powers gives a uniformly absolutely convergent sum of products b(P) overline{b(Q)} with nonnegative coefficients. The explicit expansion and its exp(4κ) absolute bound appear in Section 4 of `RESULT.md`. Products over the finitely many crossing plaquettes preserve this form, including crossings at both fixed planes.

For every complex bounded positive-half function F, condition on all plane links z. Integrating the reflected independent side variables gives

    ∫ (ΘF)F exp(H) dHaar
      =∫ exp[H_0(z)] Σ_α c_α
         |∫ F(z,U_+) B_α(U_+) exp[H_+(z,U_+)] dHaar_+|²
         dHaar_0(z)
      ≥0.

This permits F to depend on either set of plane links. Shared plane vertices cause no dependence in the independent link Haar measure. There are no hidden fixed non-plane edges or reversed-link variables. Division by the partition function proves full uncentered RP. Reflection invariance follows directly from invariance of Haar and the Wilson plaquette action.

All quotient translations permute the positively oriented independent links and the set of plaquettes. Consequently each finite Wilson law is exactly invariant under the full quotient translation group.

## 4. Infinite-volume limit: the DLR qualification

Lift the quotient law to an L_N-periodic probability law μ_N on the infinite positively oriented link variables. These laws are invariant under every Z^d translation. Compactness gives a local weak subsequential limit μ as N→∞. The shortest nonzero period has sup norm at least N, since L_N⊂NZ^d, so every fixed finite link/plaquette neighborhood injects into the quotient for all sufficiently large N.

**The periodic lift μ_N is not itself an infinite-lattice DLR state.** Conditioning on its entire exterior can reveal an interior variable through a periodic copy. The correct limit argument is local:

1. Fix a finite link region Λ, a continuous function f of its variables, and a continuous cylinder test G using only links outside Λ.
2. Include the support of G and every plaquette meeting Λ in one fixed finite edge set S.
3. Once S injects into the quotient, the finite-torus conditional density of the Λ links given the other torus links is precisely the infinite-lattice Wilson conditional density γ_Λ, because the complete list of plaquettes meeting Λ is the same and no outside test variable has been identified with an inside variable.
4. Therefore μ_N(Gf)=μ_N(Gγ_Λ f) for all sufficiently large N. Both integrands are continuous cylinder functions: the denominator of the finite local conditional density is positive and continuous.
5. Passing to the local weak limit gives μ(Gf)=μ(Gγ_Λ f). Extending from continuous local tests to all bounded exterior-measurable tests by the usual approximation/monotone-class argument establishes the full DLR identity.

Translation invariance passes immediately to μ. For any fixed continuous positive-half observable F of the infinite lattice, choose N large enough that its support and reflected support inject and its positive u levels lie in [0,N]. Then its torus version belongs to the positive half for the finite RP inequality. Passing the inequality to the limit proves μ((ΘF)F)≥0. Reflection invariance passes likewise. Translation invariance then conjugates the inequality to every integer plane u=a. Testing F−μ(F) gives centered scalar RP.

## 5. Verified conclusion and limits

This supplies H1 directly at every finite β≥0, without a finite-width uniqueness theorem or a subsequent translation average. The cylinder proof remains an independent valid alternative.

The tilted period lattice is different from the specified straight cubic period lattice. No step identifies the resulting state with a cluster point of that prescribed straight-periodic sequence. H2, or an appropriate direct comparison estimate, is still needed for that further conclusion. No continuum or mass-gap conclusion follows.

As supplemental checks only, `check_tilted_torus.py` exhaustively verifies quotient geometry for N=3,…,7 and d=2,3,4; all 15 cases pass. The output is `tilted-torus-geometry.json`. It checks vertex and edge nondegeneracy, oriented reflection covariance, absence of strict-side crossing edges, exact crossing-plaquette classification, fixed diagonal endpoints, opposite-side middle vertices, and fixed-plane plaquettes. The general proof above does not depend on these finite checks.
