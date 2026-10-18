# Independent audit of the diagonal-cylinder construction

18 October 2026. Scope: fixed finite Wilson coupling, lattice cutoff fixed, dimension d≥2. This is an independently developed audit of the cylinder construction. The complete construction is reproduced in `../construction/RESULT.md`; the local H1/H2 terminology is explained in `../README.md`.

## Verdict

**The cylinder construction is valid, with the explicit cell decomposition and uniqueness argument below.** At every finite β≥0 it yields a translation-invariant infinite-volume SU(2) Wilson Gibbs state with full uncentered reflection positivity for every integer plane x₀−x₁=a, and hence centered scalar RP. No gauge quotient, Gauss-law constraint, or hard interaction is imposed. The finite-width uniqueness argument is a strictly-positive one-dimensional argument, not an assumption of four-dimensional uniqueness.

This establishes H1 in the earlier criterion for the indicated reflection and scalar sector. It does not establish H2, periodic-boundary accessibility, a continuum limit, or a mass gap. No estimate below is uniform as width or β tends to infinity.

## 1. Exact independent-link cell decomposition

Write u(x)=x₀−x₁ and v(x)=x₀+x₁. The cylinder vertex set is

    V_W={x∈Z^d: |v(x)|≤W and |x_j|≤W for 2≤j≤d−1}.

Take every lattice edge whose two endpoints are in V_W, and every elementary plaquette all of whose vertices are in V_W. For each edge retain one independent variable U_(x,i)∈SU(2), oriented from x to x+e_i. Reverse-oriented variables are defined as U_(x,i)⁻¹, not independently integrated. Reference measure is the product of normalized Haar measures on these independent edges.

Assign U_(x,i) to cell n=floor(u(x)/2). A cell has finitely many edges: its tail u is 2n or 2n+1, v belongs to a fixed finite interval with the appropriate parity, and all transverse coordinates belong to fixed finite intervals. Translation g=e₀−e₁ maps the edge list of cell n bijectively onto that of cell n+1. Consequently the cell space is one fixed finite product X=SU(2)^m, with probability reference measure λ=Haar^m. Every full link configuration corresponds bijectively to one point of X^Z. Shared lattice vertices impose no constraints on link variables.

For an elementary i,j plaquette based at x, the independent positive-edge tails are x, x+e_i and x+e_j (with x repeated). Their u values are:

- i,j=0,1: u, u+1, u−1;
- 0,j with j≥2: u, u+1;
- 1,j with j≥2: u, u−1;
- i,j≥2: u only.

The set {floor((u−1)/2),floor(u/2),floor((u+1)/2)} always consists of precisely two adjacent integers. Therefore **every plaquette uses edges in one cell or in two adjacent cells**. Put the sum of all one-cell plaquette actions in A(s_n), and the sum of all plaquette actions using exactly cells n,n+1 in B(s_n,s_(n+1)). Translation by g identifies the same A and B for every n. Finite width ensures both sums are finite. Wilson trace functions are bounded and continuous, so A and B are bounded continuous real functions.

Thus the cylinder is exactly the unconstrained nearest-neighbor compact-spin Gibbs specification

    Σ_n A(s_n)+Σ_n B(s_n,s_(n+1)).

There is no need to assume B(s,t)=B(t,s).

Define the continuous kernel

    K(s,t)=exp[A(s)/2+B(s,t)+A(t)/2].

There are constants 0<c≤C<∞ with c≤K(s,t)≤C everywhere. They may depend on W and β. All finite cell-interval conditional densities, with endpoints l=s_(L−1) and r=s_(R+1), are exactly

    γ_[L,R]^(l,r)(ds_L⋯ds_R)
      =Z(l,r)⁻¹ [Π_(i=L−1)^R K(s_i,s_(i+1))] Π_(i=L)^R λ(ds_i).

The factors involving A(l)/2 and A(r)/2 are constant in the integrated variables and cancel in normalization. Finite edge-set and finite cell-set DLR formulations are equivalent here: any finite edge set is contained in finitely many cells, and consistent conditioning of the positive product-reference densities gives the smaller-set specification.

## 2. Complete boundary-forgetting proof of 1D uniqueness

Set ε=c/C>0 and δ=1−ε<1. Total variation distance here is sup_E|μ(E)−ν(E)|, at most 1 for probability measures.

Fix L≤p≤q≤R and right endpoint r. Define backward messages by

    h_R(s)=K(s,r),
    h_i(s)=∫K(s,t)h_(i+1)(t)λ(dt),  i=R−1,…,L−1.

Every h_i is positive, continuous, and finite. For i=L−1,…,R−1 define

    P_i(s,dt)=K(s,t)h_(i+1)(t)λ(dt)/h_i(s).

The product of these transitions, starting at s_(L−1)=l, is exactly γ_[L,R]^(l,r): the h factors telescope, leaving the K product including K(s_R,r). Importantly, these P_i depend on r but not on l.

For any positive integrable h, the probability kernel

    P_h(s,dt)=K(s,t)h(t)λ(dt)/∫K(s,z)h(z)λ(dz)

has the common minorization

    P_h(s,dt) ≥ ε ν_h(dt),
    ν_h(dt)=h(t)λ(dt)/∫h dλ.

Indeed the numerator is bounded below by c h(t) and the denominator above by C∫h. Hence P_h=ε ν_h+(1−ε)Q_h for another probability kernel Q_h, and for arbitrary probability distributions α,α′,

    ||αP_h−α′P_h||_TV ≤ δ ||α−α′||_TV.

Apply this successively from L−1 to p. For two left endpoints l,l′ and the same right endpoint r, the laws of s_p differ by at most δ^(p−L+1). Given s_p, the rest of the block s_(p+1),…,s_q is generated by the same transitions regardless of l, so applying that common kernel cannot increase distance. Therefore

    ||γ_[L,R]^(l,r)|_[p,q]−γ_[L,R]^(l′,r)|_[p,q]||_TV
      ≤ δ^(p−L+1).

Repeat the identical argument in reverse order with transposed kernel K^rev(s,t)=K(t,s). It obeys the same bounds c,C. For fixed l and varying r,r′,

    ||γ_[L,R]^(l,r)|_[p,q]−γ_[L,R]^(l,r′)|_[p,q]||_TV
      ≤ δ^(R−q+1).

The triangle inequality now gives the uniform boundary-diameter bound

    sup_(l,l′,r,r′)
      ||γ_[L,R]^(l,r)|_[p,q]−γ_[L,R]^(l′,r′)|_[p,q]||_TV
      ≤ δ^(p−L+1)+δ^(R−q+1).                 (1)

For any two infinite-volume DLR states μ,ν, their [p,q] marginals are mixtures of the displayed finite-interval marginals, using their respective endpoint distributions. The diameter of the convex hull cannot exceed the original diameter: integrating the difference under the product of the two endpoint distributions proves this directly. Thus their [p,q] distance is bounded by (1). Sending L→−∞ and R→∞ gives zero. Equality of all finite interval marginals proves μ=ν.

Existence follows from compactness of X^Z and any sequence of finite free cell-interval Gibbs laws, extended outside by λ. Their local weak limits satisfy DLR because the interaction is finite range and the local conditional kernels send continuous cylinder functions to continuous cylinder functions. Thus the cylinder has exactly one Gibbs state, among **all** DLR states, not only invariant or extremal states.

This proof does not invoke an eigenfunction theorem or an assertion that every DLR state is automatically a stationary Markov chain. It uses only the finite-interval densities, their elementary message-factorization, and DLR. At β=0 the action vanishes, K=1 and δ=0, giving the product-Haar state directly.

## 3. Exact diagonal reflection and finite-domain geometry

For integer a, define

    θ_a(x₀,x₁,x₂,…)= (x₁+a,x₀−a,x₂,…).

Then u(θ_ax)=2a−u(x), v(θ_ax)=v(x), and θ_a exchanges e₀ and e₁ while fixing every e_j, j≥2. In particular θ_a maps the retained cylinder edges and plaquettes bijectively to themselves. It maps positively oriented retained edges to positively oriented retained edges. On configurations define (R_aU)_(x,i)=U_(θ_ax,σ(i)), where σ swaps 0 and 1, and extend the convention to reversed edges by inversion. For a complex observable, Θ_aF(U)=overline{F(R_aU)}.

Take the finite induced vertex domain

    V_(W,T,a)=V_W∩{|u−a|≤T}.

For integer T≥0 it is finite and θ_a-invariant. The induced edge and plaquette sets are also invariant. No retained edge joins u<a directly to u>a: an edge changes u by 0, +1, or −1, while these two strict integer half-spaces are separated by a gap of two.

Partition independent edges into E_+, E_0, E_−: E_0 contains the edges lying wholly in u=a; E_+ consists of all remaining edges whose endpoints satisfy u≥a; E_− is analogous. E_0 consists only of transverse j≥2 edges. Reflection fixes each E_0 variable pointwise and bijects E_+ with E_−. Thus product Haar factorizes with a common plane variable z and two reflected independent side variable sets.

Every non-01 plaquette has its u values in a set {u}, {u,u+1}, or {u,u−1}, so cannot meet both strict halves. A 01 plaquette based at x has vertex u values u,u+1,u−1,u; it meets both strict halves exactly when u(x)=a. In that case the vertices x and x+e₀+e₁ are fixed by θ_a, and the other two vertices are exchanged. Define the two paths, both oriented from x to x+e₀+e₁,

    P=U_(x,0) U_(x+e₀,1),
    Q=U_(x,1) U_(x+e₁,0).

P uses only E_+ edges; Q uses only E_− edges; Q is the reflected path P. The standard plaquette holonomy is P Q⁻¹. Neither path uses an E_0 edge. The induced-domain rule causes no additional issue: a crossing plaquette is included if and only if all four vertices (hence both full paths) are included, and the domain symmetry never retains only a purported half-plaquette action.

## 4. Positive-kernel factorization and plane variables

Write the Wilson plaquette Boltzmann factor as exp[κ ReTr(U_p)] with κ≥0 (κ=β or β/2 depending on the normalization). For SU(2), Tr(G) is real. Since Q⁻¹=Q*,

    Tr(PQ⁻¹)=Σ_(i,j=1)^2 P_ij overline{Q_ij}.

The crossing factor therefore has the explicit positive expansion

    exp[κTr(PQ⁻¹)]
      =Σ_(n≥0) κ^n/n! Σ_((i₁,j₁),…,(i_n,j_n))
         [Π_(k=1)^n P_(i_k j_k)]
         overline{[Π_(k=1)^n Q_(i_k j_k)]}.

Every coefficient is nonnegative. The series converges absolutely and uniformly, since matrix entries have absolute value ≤1 and its termwise absolute sum is at most exp(4κ). A finite product over crossing plaquettes likewise has a uniformly absolutely convergent expansion Σ_α c_α B_α Θ_aB_α with c_α≥0 and each B_α a bounded continuous positive-side function.

Split the remaining action as H_+(z,U_+)+H_−(z,U_−)+H_0(z), assigning every noncrossing non-plane plaquette to its unique closed half and every entirely plane plaquette to H_0. Reflection invariance gives H_−=H_+∘R_a. For any bounded positive-side observable F, allowed also to depend on z, direct integration yields

    ∫ (Θ_aF)F exp(H) dHaar
      =∫ exp[H_0(z)] Σ_α c_α
         |∫ F(z,U_+) B_α(U_+) exp[H_+(z,U_+)] dHaar_+(U_+)|²
         dHaar_0(z)
      ≥0.

Shared plane vertices are harmless because the independent variables are edges; gauge transformations do not impose constraints. Plane edges are integrated once, outside the squares. Positivity of exp(H_0), rather than any character expansion for H_0, is sufficient. Normalizing by the positive partition function proves full uncentered RP of every finite free law, together with exact reflection invariance.

## 5. Infinite limits and translation averaging

For fixed W and a, extend each finite free law on V_(W,T,a) to the whole cylinder by independent Haar on omitted edges. Compactness gives subsequential local weak limits. For any fixed finite edge set, all plaquettes meeting it are included for all sufficiently large T; the finite law then satisfies the cylinder DLR identity for that set. Finite range, continuity, and boundedness let the identity pass to the limit. Section 2 makes every such limit the same unique cylinder state ρ_W, independently of a. RP and reflection invariance for θ_a pass through expectations of continuous cylinder functions. Since this works for each a, the **same** ρ_W has RP and invariance for every integer θ_a.

The independent-Haar extension also preserves RP: omitted edges come in reflected pairs or fixed plane edges, and their product measure has the same conditional-product square factorization. It is enough, however, to test observables eventually supported entirely in the finite domain.

Next extend ρ_W by independent Haar outside the infinite cylinder and take a local weak subsequence as W→∞. For any finite full-lattice edge set and all incident plaquettes, the entire interaction neighborhood belongs to the cylinder once W is large. The same continuous-kernel argument proves that the limit ρ is a full-lattice Wilson DLR state. Every fixed positive-side cylinder observable and its reflection belong to sufficiently large cylinders, so ρ is RP and invariant for every θ_a.

For lattice translation t_z, direct computation gives

    t_z θ_a t_(−z)=θ_(a+u(z)).

Thus every translated measure t_zρ is RP for every θ_a, and invariant under every θ_a: the conjugated plane is still one of the integer planes already established. Take finite averages over cubic Følner sets of translations. Each average remains DLR (linearity of the DLR identity), reflection invariant, and RP for every θ_a (linearity of each uncentered quadratic inequality). Any local weak subsequential limit is translation invariant by the Følner symmetric-difference bound. It remains DLR because this bounded finite-range compact-spin specification is Feller, and remains RP and reflection invariant by the same local expectation limits.

Finally, for the invariant limit μ and a positive-side F, test the full RP inequality with F−μ(F). Reflection invariance ensures μ(Θ_aF)=overline{μ(F)}, giving the centered inequality

    μ((Θ_aF)F)−|μ(F)|²≥0.

Linear combinations give the corresponding positive semidefinite reflected covariance matrices. Continuous cylinder observables suffice for the stated scalar sector. If bounded measurable local observables are desired, the inequality extends by L² approximation on each finite compact-coordinate marginal and Cauchy–Schwarz, using reflection invariance.

## 6. What has and has not changed

The earlier objection to averaging translates of an arbitrary single-plane RP state remains correct. This construction repairs precisely that missing prerequisite by proving all parallel integer planes before averaging.

H1 is supplied at each finite β≥0. Nothing in the argument proves equality with limits of a prescribed sequence of straight periodic boxes, source-direction pressure differentiability H2, width-uniform correlation decay, a continuum limit, or a mass gap. The 1D contraction constant can tend to 1 as W or β grows, so the width limit supplies existence and RP, not a usable full-dimensional mixing estimate.
