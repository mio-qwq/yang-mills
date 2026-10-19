# A translation-invariant diagonally RP Wilson Gibbs state

18 October 2026. Fixed lattice spacing; SU(2); finite nonnegative Wilson coupling. This note proves the existence premise H1 from the preceding boundary audit. It does **not** identify a cluster point of the stipulated straight cubic periodic volumes, prove the source differentiability premise H2, or address a continuum limit or mass gap.

## Result

**The proposed cylinder construction is valid.** At every fixed transverse width, disjoint two-level link blocks give a compact one-dimensional nearest-neighbor model with a uniformly strictly positive transfer kernel. Its unique Gibbs state is the limit of free longitudinal cutoffs centered at every integer diagonal plane, and therefore is reflection positive at all those planes. A transverse-width limit retains every such inequality. Full translation averaging is now legitimate because each translate is already RP for the same fixed plane.

There is also a shorter construction, checked below: **tilted tori with two fixed diagonal planes.** Their finite-volume Wilson laws are translation invariant and diagonally RP. Their local limits immediately give the required state. These are different periodic geometries from the prescribed straight tori; replacing one family with the other would be an additional step, not a consequence of this proof.

### Precise theorem

Let d>=2 and 0<=b<infinity. Put independent SU(2) variables on the positively oriented nearest-neighbor links of Z^d, with normalized product Haar reference measure. The Wilson specification has plaquette weight

    exp[b w_p],     w_p(U) = (1/2) Re Tr(U_p).

There exists a probability measure rho_b on all link variables such that:

1. rho_b satisfies the infinite-volume Wilson DLR equations;
2. rho_b is invariant under every lattice translation and under the coordinate-interchange reflection theta_0;
3. for every integer a, every bounded continuous cylinder function F depending only on links with both endpoints in x_0-x_1>=a satisfies

       rho_b((Theta_a F) F) >= 0,

   where theta_a(x_0,x_1,z)=(x_1+a,x_0-a,z) and Theta_a F=overline(F composed with theta_a);
4. rho_b can also be chosen gauge invariant.

The statement extends to bounded measurable cylinder functions by L2 approximation. In particular all finite connected reflected covariance matrices in a chosen scalar positive-side sector are positive semidefinite. Thus it supplies H1, with stronger full-algebra positivity, for every finite nonnegative coupling. The assertion concerns this fixed parallel family of diagonal planes.

## 1. Local factorization, including fixed-plane links

Use the oriented-link convention U_(y,x)=U_(x,y)^(-1). Reflection acts on configurations by pullback on oriented edges. In the present reflection, positive coordinate directions 0 and 1 are interchanged; directions j>=2 are fixed. The complex conjugation in Theta acts on scalar observables.

First consider any finite reflection-invariant induced subcomplex of Z^d with free boundaries, reflected through

    u=x_0-x_1=a,     a an integer.

No nearest-neighbor link has endpoints strictly on opposite sides: its u-increment is 0, +1, or -1. Links whose endpoints are both on the plane are exactly links in directions j>=2; reflection fixes these links pointwise. Call their variables U_0. Partition all other link variables into U_+ and U_-, interchanged by reflection. The reference measure is

    dHaar(U_0) dHaar(U_+) dHaar(U_-).

For an oriented (i,j) plaquette based at x, its vertex u-values are

    k, k+delta_i, k+delta_j, k+delta_i+delta_j,
    k=u(x), delta_0=1, delta_1=-1, delta_j=0 for j>=2.

Consequently a plaquette has vertices on both strict sides if and only if it is a (0,1) plaquette with k=a. Its vertices on the plane are x and y=x+e_0+e_1. Let

    P_+ = U_(x,x+e_0) U_(x+e_0,y),
    P_- = U_(x,x+e_1) U_(x+e_1,y).

Then P_- is the reflection of P_+, and the oriented plaquette holonomy is P_+ P_-^*. In particular

    Re Tr(P_+ P_-^*)
      = sum_(i,j) [Re(P_+)_(ij) Re(P_-)_(ij)
                   + Im(P_+)_(ij) Im(P_-)_(ij)].

This is a finite sum of terms (Theta_a f) f with real bounded positive-half functions f. Each coefficient in b w_p is b/2>=0. Therefore exp[b w_p] is the uniformly convergent positive-cone series obtained by expanding the exponential. This is a scalar entrywise argument; no matrix-order convention is needed.

All remaining plaquettes lie in one closed half or entirely in the fixed plane. The full exponent consequently has the form

    S = S_+ + S_+ composed with theta_a + S_0
        + sum_alpha c_alpha (Theta_a f_alpha) f_alpha,
    c_alpha>=0,

where S_0 depends only on U_0 and S_+ only on U_0,U_+. Plane plaquettes can alternatively be split equally between the two half-actions. For any positive-half F, expanding the last exponential yields terms

    coefficient * integral dHaar(U_0) exp[S_0(U_0)]
       * | integral dHaar(U_+) F exp[S_+] product_alpha f_alpha^(n_alpha) |^2.

Every coefficient is nonnegative. Uniform absolute convergence permits integration term by term. Division by the positive partition function proves RP. Conditioning on U_0 is important: one must not claim that the two closed halves have disjoint link variables.

Only the reflection-invariant incidence structure was used. Free tangent boundaries omit whole plaquettes and preserve this argument; no boundary plaquette is silently restored.

## 2. Short proof using tilted tori

### 2.1 The quotient and its fixed sets

For N>=3 let

    L_N = span_Z { N(e_0+e_1), N(e_0-e_1), N e_j : 2<=j<d },
    T_N = Z^d / L_N.

Use the usual quotient nearest-neighbor links and elementary plaquettes and put the ordinary Wilson action on all of them. The quotient has 2 N^d vertices. A convenient coordinate description is

    u=x_0-x_1 mod 2N,
    v=x_0+x_1 mod 2N,
    z_j=x_j mod N,
    u congruent to v modulo 2.

This parity condition describes exactly the quotient; u and v are not independent unrestricted residues. A step e_0 sends (u,v) to (u+1,v+1), while e_1 sends it to (u-1,v+1). A tangent v wrap changes no u-coordinate.

The reflection theta_0 descends because it preserves L_N and acts by

    (u,v,z) -> (-u,v,z).

Its fixed vertices are exactly the two planes

    u=0 and u=N modulo 2N.

Let the positive open half have 0<u<N and the negative open half have N<u<2N. Include both fixed planes in the closures of both halves. Reflection interchanges the open halves and fixes the common boundary pointwise.

No link joins the two open halves. The fixed links are the tangent j>=2 links on either fixed plane. The only plaquettes meeting both open halves are (0,1) plaquettes based at u=0 or u=N. At u=0 use the positive path e_0 then e_1; at u=N use the positive path e_1 then e_0. In both cases the other path is its reflection and both endpoints are fixed. The local factorization in Section 1 applies unchanged, simultaneously at the two planes. It includes every plaquette, including all tangent wraparound plaquettes. Thus the finite Wilson measure mu_N is RP for this split.

This is the essential difference from using an ordinary straight torus: on this quotient the reflection has two separating fixed planes and there are no nonlocal seam-crossing terms left outside the cone decomposition.

### 2.2 Local limits and DLR

The finite measure mu_N is invariant under every translation of T_N. Lift it to a periodic probability measure on all links of Z^d by assigning each link its quotient-link variable. This lifted measure is exactly invariant under every translation of Z^d and under theta_0.

The full link configuration space is a countable product of compact metric spaces, hence compact and metrizable. Choose any local weakly convergent subsequence of these lifted measures with N tending to infinity, and denote its limit by rho_b.

For every fixed positive-half cylinder F on the infinite lattice, all links in its support and its reflection embed without identification in T_N for sufficiently large N, with its positive support lying in the torus closed positive half. Therefore mu_N((Theta_0 F)F)>=0 eventually, and weak convergence gives the same inequality for rho_b. Translation invariance and reflection invariance pass to the limit. Translating the test function gives RP at every integer plane u=a.

To justify DLR, fix a finite set A of links, a continuous function f supported in A, and a bounded continuous local function g supported outside A. For sufficiently large N the finite union consisting of their supports and all plaquettes meeting A embeds injectively in T_N. The finite-torus conditional expectation on A is then exactly the usual full-lattice Wilson kernel gamma_A, evaluated on that local neighborhood. Consequently

    mu_N(g f) = mu_N(g gamma_A f)

for all sufficiently large N. Both integrands are continuous cylinder functions because the interaction is bounded, continuous and finite range. Passing to the limit and then extending from local test functions gives the DLR conditional expectation identity. This proves that rho_b is a Gibbs measure.

One should not say that a periodic lift is itself a full-space DLR measure at finite N: its distant periodic copies determine interior links. The argument above uses local exterior tests before taking the limit, which is sufficient and avoids that error.

Gauge invariance follows in the same way from finite-torus gauge invariance, testing any finitely supported full-lattice gauge transformation on fixed local observables. This completes the theorem.

## 3. Independent proof using finite-width cylinders

This section verifies the construction proposed in the assignment, without relying on the tilted-torus shortcut.

### 3.1 Exact free geometry

For W>=1 define the vertex cylinder

    D_W = {x in Z^d : |v(x)|<=W and |x_j|<=W for j>=2}.

Keep exactly the nearest-neighbor links with both endpoints in D_W and exactly the elementary plaquettes whose four vertices lie in D_W. The longitudinal coordinate u is unbounded. The cylinder is invariant under

    theta_a, for every integer a,
    g=e_0-e_1, which sends u to u+2 and fixes v and z.

The inverse coordinate formulas x_0=(u+v)/2, x_1=(v-u)/2 show the parity condition u congruent v modulo 2. Under theta_a, u becomes 2a-u, so that parity is preserved for every integer a. Half-integer a is neither needed nor asserted.

For each a and T>=1 use the finite vertex set

    D_(W,a,T)=D_W intersect { |u-a|<=T }

with its induced free links and plaquettes. It is reflection invariant under theta_a. Section 1 proves full RP for its free Wilson law. In particular, the free transverse boundary introduces no unmatched crossing interactions.

### 3.2 A disjoint compact block alphabet

Assign each positively oriented cylinder link to the u-level of its tail. Group the levels into disjoint pairs

    B_n = {links with tail u in {2n,2n+1}}.

Translation by n g identifies B_n with B_0. Each B_n is finite, so its configuration space is a fixed compact product

    S_W = SU(2)^(M_W),

with product normalized Haar probability lambda_W. Every original link appears in exactly one block. In particular there are no artificial compatibility constraints between neighboring blocks and no gauge fixing.

The positively oriented link tails around a plaquette based at level k have levels among

    {k, k+delta_i, k+delta_j}.

For a (0,1) plaquette this is {k-1,k,k+1}. If k=2n it meets only B_(n-1),B_n; if k=2n+1 it meets only B_n,B_(n+1). The other plaquettes have smaller spans. Thus every Wilson plaquette belongs to one block or two adjacent blocks, never three blocks.

Assign each within-block plaquette to V(s_n), and each spanning plaquette to W_1(s_n,s_(n+1)). Here V and W_1 are contributions to the exponent, not the negative Hamiltonian. Translation by g makes these functions independent of n. They are continuous and bounded, because at fixed W only finitely many plaquettes occur and |b w_p|<=b.

Define

    K(s,t)=exp[V(s)/2 + W_1(s,t) + V(t)/2].

There are finite constants 0<m_W<=M'_W<infinity such that

    m_W <= K(s,t) <= M'_W for every s,t.

For example, if |V|<=A and |W_1|<=B, then m_W=exp[-A-B] and M'_W=exp[A+B] work. No width-uniform bound is claimed. Pointwise positivity here is distinct from reflection positivity.

### 3.3 Direct all-DLR uniqueness proof

For clarity, here is the exact one-dimensional statement needed. Let a chain with compact alphabet S and probability reference lambda have nearest-neighbor kernel K with 0<m<=K<=M<infinity. On blocks [l,r], conditioned on endpoints s_(l-1),s_(r+1), its density is proportional to

    product_(n=l-1)^r K(s_n,s_(n+1)) product_(n=l)^r lambda(ds_n).

For the Wilson kernel above this equals the DLR density exactly, up to a factor depending only on the exterior endpoints.

Fix the right endpoint. Integrating sites to the right produces positive messages h. Each forward transition takes the form

    P_h(s,dt)=K(s,t) h(t) lambda(dt) / integral K(s,z)h(z)lambda(dz).

For eta_h(dt)=h(t)lambda(dt)/integral h dlambda,

    P_h(s,dt) >= (m/M) eta_h(dt), uniformly in s and h.

It follows by subtracting the common measure that P_h contracts total variation by at most q=1-m/M<1. Change the left endpoint while keeping the right endpoint fixed. The transitions are the same; contraction until site i, followed by the same conditional continuation, shows that the laws of an interior block [i,j] differ by at most q^(i-l+1). Reverse the argument to change the right endpoint. The triangle inequality gives, for arbitrary endpoint pairs eta,eta',

    || (gamma_[l,r]^eta)_[i,j] - (gamma_[l,r]^eta')_[i,j] ||_TV
       <= q^(i-l+1) + q^(r-j+1).

Here TV is sup over events. The restriction of any infinite-volume DLR law to [i,j] is a mixture of these finite-interval laws. Letting l tend to minus infinity and r to plus infinity forces any two DLR laws to agree on every finite block. Hence the DLR law is unique. Existence follows by compactness and finite-range continuity of the specification. This proves uniqueness among **all** Gibbs measures, not merely the translation-invariant ones.

The estimate is valid at every fixed finite W and finite b. It supplies no estimate uniform in W or in b tending to infinity; neither is needed for the ordered limits below.

### 3.4 One cylinder law is RP at every integer plane

Extend each finite free law on D_(W,a,T) to all cylinder links with independent Haar variables on omitted links. Any weak limit as T tends to infinity satisfies the cylinder DLR equations: a fixed finite set of links and all its interaction neighbors lie inside the free cutoff for sufficiently large T. By the uniqueness just proved, every such limit is the same cylinder law nu_W, regardless of a. Compactness and uniqueness also show convergence of each complete free-cutoff sequence.

For each fixed integer a, its centered free laws are theta_a invariant and RP. Passing to the limit gives theta_a invariance and RP for nu_W. Since the limit law is the same for every a, this is one law with all the required parallel-plane inequalities. No uncountable or incompatible subsequence choice is being made.

### 3.5 Width limit and legitimate full translation averaging

Extend nu_W to full-lattice link variables using independent Haar variables outside the cylinder. Along a subsequence W tending to infinity, compactness gives a local weak limit nu. For every finite link set A, its entire plaquette interaction neighborhood is inside D_W eventually. Thus the full-space DLR equation for A passes to the limit. Likewise, every fixed positive-half F and its reflection lie inside D_W eventually; hence nu is RP and invariant under theta_a for every integer a.

Now let T_z be spatial translation by z, and write u(z)=z_0-z_1. The elementary geometric identity is

    T_z theta_a T_(-z) = theta_(a+u(z)).

Thus translating a measure RP at every integer plane preserves RP at every integer plane. In particular every translate of nu is RP for theta_0 and is theta_0 invariant. Every translate is also a Gibbs measure for the same homogeneous Wilson specification.

For a cubic lattice Følner set Q_R define the convex average

    nu_R = (1/|Q_R|) sum_(z in Q_R) (T_z)_*nu.

The RP inequalities are linear in the measure, so each nu_R is RP. Gibbs measures are convex; therefore each nu_R is Gibbs. A local weak cluster point rho_b is Gibbs by quasilocality and RP by continuity. For any fixed shift h and bounded cylinder F, the translation-invariance error is at most

    2 ||F||_infinity |(Q_R+h) symmetric_difference Q_R| / |Q_R|,

which tends to zero. Hence rho_b is fully translation invariant. Reflection invariance and gauge invariance also persist. This proves the theorem a second way.

The previous three-periodic counterexample to arbitrary translation averaging does not apply: its starting state was RP only at one selected plane. The present construction establishes all-plane RP **before** averaging.

## 4. Centered covariance consequence and exact scope

For positive-half functions F_1,...,F_n, reflection invariance gives

    rho_b(Theta_a F_i) = overline(rho_b(F_i)).

Apply full RP to F=sum_i c_i(F_i-rho_b(F_i)). Then

    sum_(i,j) overline(c_i)c_j
      [rho_b((Theta_a F_i)F_j)
       - rho_b(Theta_a F_i)rho_b(F_j)] >= 0.

This is the connected reflected covariance matrix in H1. Continuous local scalar observables are covered directly. Bounded measurable cylinder functions follow by approximating in the marginal L2 norm; reflection invariance controls the reflected approximation, and ordinary Cauchy-Schwarz controls the product error.

The proofs establish existence for every finite b>=0. They do not establish uniqueness of the infinite four-dimensional theory. Cylinder uniqueness is a finite-width intermediate fact only. They do not prove that rho_b belongs to the cluster set of a specified straight cubic periodic sequence. Tilted periodic quotients and straight periodic quotients are different finite-volume families, even when their bulk pressures agree. Nor do they prove differentiability in the selected source directions. Thus the earlier H1-H2 criterion now has H1 supplied; H2 or another local-state bridge remains a substantive separate input.

## 5. Literature and verification

The proofs above are explicit arguments in this note. The following sources support their ingredients, with their actual scopes kept separate.

- H. G. Evertz, K. Jansen, H. A. Kastrup, K. Fredenhagen, M. Marcu, *Proof of universal perimeter law behaviour of the Wegner-Wilson loop in nonabelian lattice gauge theories with Higgs fields*, Physics Letters B 194 (1987), 277-282. Printed pp. 278-279, equations (7)-(13), give the free-volume oblique-reflection cone argument, including terms wholly on the reflection plane. The local pure-gauge factorization in Section 1 is an explicit specialization. This source does not identify our limiting state with a specified straight-periodic cluster state. Author-hosted primary PDF: https://itp.tugraz.at/~evertz/Pubs/1987_PLB_194_277_Proof_of_Perimeter_Law_in_Nonabelian_Higgs.pdf

- V. Kazakov, Z. Zheng, *Bootstrap for Finite N Lattice Yang-Mills Theory*, arXiv:2404.16925v4, Section 3.2, printed pp. 19-20, equations (3.8)-(3.13), gives the diagonal crossing-plaquette factorization in contemporary notation. The displayed PDF version is dated 4 December 2024; later published pagination differs. It is not used as a boundary-condition transfer theorem. Primary PDF: https://arxiv.org/pdf/2404.16925

- L. Cioletti, A. O. Lopes, M. Stadlbauer, *Ruelle operator for continuous potentials and DLR-Gibbs measures*, DCDS 40(8) (2020), 4625-4652, Theorem 5.2, is a primary compact-alphabet uniqueness result under a bounded-boundary-variation condition. Its DLR formulation is one-sided. Our Section 3.3 gives the needed two-sided all-DLR argument directly instead of silently identifying the formulations. https://arxiv.org/pdf/1608.03881 ; https://www.aimsciences.org/article/doi/10.3934/dcds.2020195

- L. Chayes, J. Machta, *Graphical representations and cluster algorithms I. Discrete spin systems*, Physica A 239 (1997), 542-601, Section 4.1, printed pp. 574-575, defines precisely the two-dimensional diagonal quotient by identifying both x+y and x-y modulo an even L. Equation (4.1) identifies the two separating fixed lines x-y=0 and L/2. Taking L=2N gives the first two directions of our quotient. This is a primary geometry precedent, in a discrete spin/bond setting. The Wilson plaquette extension and the full-space Gibbs construction are proved above, rather than attributed to that paper. Author-hosted primary PDF: https://www.math.ucla.edu/~lchayes/lchayes_website_folder/old_publications_folder/graph_rep_1.pdf

Additional exact finite combinatorial checks, not substitutes for the proof:

- check_geometry.py: 60 cylinder cases in d=2,3,4, widths 1,2, centers -2 through 2, longitudinal cutoffs 1,3. Checks vertex/link/plaquette reflection invariance, no strictly crossing links, exact crossing-plaquette classification, reflected paths, and disjoint block adjacency. Result: PASS.
- check_tilted_torus.py: 18 quotient cases in d=2,3,4 and N=3 through 8. Checks parity, quotient size, both fixed planes, absence of strictly crossing links, all crossing-plaquette classifications and paths. Result: PASS.
- uniqueness/one_dimensional_uniqueness.md: expanded direct uniqueness proof and primary-source scope audit.

Only public literature was read/downloaded; original local audit code was written and run. No unknown code, external communications, or public writes were used.
