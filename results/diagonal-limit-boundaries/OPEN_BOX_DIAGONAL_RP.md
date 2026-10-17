# Exact diagonal reflection positivity on free-boundary Wilson subcomplexes

17 October 2026. A local, self-contained proof of a bounded route test. This is not a novelty claim. The frozen manuscript already asserts diagonal reflection positivity on the infinite lattice and failure on straight tori; references and the remaining boundary-comparison gap are recorded below.

## Theorem

Let K be a finite subcomplex of the ordinary nearest-neighbor cubical lattice Z^4, invariant under theta(x0,x1,x2,x3)=(x1,x0,x2,x3). There are no periodic identifications. Choose one positive-coordinate orientation per link. Assign a group variable U_e∈SU(2) to each link, with U_(reverse e)=U_e^(-1), and integrate all links with independent normalized Haar measure. For any chosen set of elementary plaquettes of K, invariant under theta, assign finite real couplings beta_p>=0 with beta_(theta p)=beta_p. Define

    dmu(U)=Z^(-1) exp[sum_p beta_p Tr(U_p)/2] product_e dU_e.

Let A_+ be the algebra of bounded measurable complex functions of links whose two endpoints satisfy x0>=x1. Define (theta U)_e=U_(theta e), with the orientation convention above, and Theta F=conjugate(F(theta U)). Then

    integral (Theta F)F dmu >=0                         (1)

for every F∈A_+. Gauge invariance of F is not required.

In particular (1) holds on every swap-invariant finite open box with free boundary, e.g. [-R,R]^4∩Z^4 with all contained links and plaquettes, at every finite beta>=0. It also holds when F depends only on the strict halfspace.

## 1. Complete geometric classification

Put d(x)=x0-x1. A positive link in direction 0 changes d by +1, a positive link in direction 1 changes it by -1, and links in directions 2,3 leave d unchanged. Because d is integer-valued, no nearest-neighbor edge joins a strictly positive vertex to a strictly negative vertex.

Partition links into:

- E_0: both endpoints lie in d=0. These are exactly spectator-direction links in the fixed plane; theta fixes each oriented link pointwise.
- E_+: both endpoints lie in d>=0, with at least one strictly positive endpoint.
- E_-: both endpoints lie in d<=0, with at least one strictly negative endpoint.

These are disjoint, exhaust all links, and theta bijects E_+ with E_-. No edge is reversed by theta under the positive-coordinate orientation convention.

For a plaquette based at x and spanning two positive coordinate directions, write d=d(x). Its multiset of vertex gaps is:

- (0,1) orientation: d,d+1,d-1,d.
- (0,i), i=2 or 3: d,d+1,d,d+1.
- (1,i), i=2 or 3: d,d-1,d,d-1.
- (2,3): d,d,d,d.

It follows that the ONLY plaquettes containing vertices on both strict sides are (0,1)-plaquettes based at d=0. Each such plaquette is individually invariant under theta. Its two fixed vertices are x and x+e0+e1. Its positive-side two-edge path is

    A_p: x -> x+e0 -> x+e0+e1,

and its other two-edge path is theta A_p. With this orientation the plaquette holonomy is

    U_p=U(A_p) U(theta A_p)^(-1).                        (2)

All remaining plaquettes are either contained in the closed positive half, contained in the closed negative half, or wholly in the fixed plane. The latter are precisely spectator (2,3)-plaquettes based at d=0. Excluding wholly fixed plaquettes, theta pairs positive and negative plaquettes. Some noncrossing plaquettes touch the plane, which causes no problem because their fixed-plane links will be conditioned on.

This classification is inherited by an arbitrary subcomplex K: removing cells does not introduce new types, and every retained plaquette has all its boundary links available.

## 2. The Wilson crossing factor is a positive kernel

For beta>=0 and A,B∈SU(2), set

    k_beta(A,B)=exp[(beta/2)Tr(AB^(-1))].

Let chi_j and D^j denote respectively the character and a unitary matrix representation of spin j, with dimension d_j=2j+1. The character expansion is

    exp[(beta/2)chi_(1/2)(g)]=sum_j c_j(beta) chi_j(g),
    c_j(beta)>=0, sum_j c_j(beta)d_j=e^beta.             (3)

Here is a direct justification, without assuming character-coefficient positivity. Expand the exponential in powers of chi_(1/2). Every power is the character of a tensor power of the fundamental representation; its irreducible multiplicities are nonnegative integers. Therefore all resulting c_j are nonnegative. Evaluating the nonnegative dimension sums at identity gives the last identity by summing the exponential series. Since |chi_j(g)|<=d_j, the series converges absolutely and uniformly. For beta>0 every c_j>0 because spin j occurs in the (2j)-fold tensor power; strictness is not needed for (1).

Unitarity gives

    chi_j(AB^(-1))=sum_(a,b=1)^(d_j) D^j_ab(A) conjugate(D^j_ab(B)),

hence

    k_beta(A,B)=sum_(j,a,b) c_j(beta)
                     D^j_ab(A) conjugate(D^j_ab(B)).     (4)

Every finite spin cutoff is a positive-semidefinite kernel. Its absolute value is at most sum_j c_j d_j<=e^beta: for each j, Cauchy–Schwarz on matrix entries gives sum_ab |D_ab(A)D_ab(B)|<=d_j. The cutoffs converge uniformly to k_beta by (3). These bounds justify the finite-cutoff limit used below; no formal infinite interchange is required.

## 3. Haar factorization and the sum-of-squares identity

Write the link variables as (X,Y,z), where X are E_+ variables, z are E_0 variables, and Y are the E_- variables identified with their reflected E_+ partners. Product Haar measure becomes

    dX dY dz,

with dX and dY identical product Haar measures. Reflection swaps X,Y and leaves z fixed. Thus

    F(U)=F(X,z), (Theta F)(U)=conjugate(F(Y,z)).

Let S_+(X,z) be the Wilson action sum over nonfixed plaquettes contained in the positive half, and S_0(z) the sum over fixed-plane plaquettes. Reflection symmetry gives the negative-side sum S_+(Y,z). Let C be the finite set of crossing plaquettes. By (2), the full density is

    exp[S_0(z)] exp[S_+(X,z)] exp[S_+(Y,z)]
       product_(p∈C) k_(beta_p)(A_p(X),A_p(Y)).          (5)

The crossing paths do not use fixed-plane links; allowing harmless z-dependence would not change the argument.

Replace each crossing kernel by a finite character cutoff in (4), expand the FINITE product, and put W(X,z)=exp[S_+(X,z)]. The corresponding unnormalized reflected form equals

    integral dz exp[S_0(z)]
      sum_alpha c_alpha
        | integral dX F(X,z) W(X,z)
                         product_(p∈C) D^(j_p)_(a_p b_p)(A_p(X)) |^2,
                                                               (6)

where alpha selects one retained triple (j_p,a_p,b_p) for every crossing plaquette and c_alpha=product_p c_(j_p)(beta_p)>=0. Formula (6) is nonnegative for each cutoff.

All functions are bounded, there are finitely many links and plaquettes, and the kernels are uniformly bounded by e^(beta_p). Uniform convergence of the finite product and dominated convergence therefore show that the exact unnormalized reflected form is the limit of these nonnegative numbers. Finally Z>0 because the original Wilson density is strictly positive. Division by Z proves (1).

This proof includes functions depending on fixed-plane links: the square is formed at each fixed z, and is then integrated against the positive plane weight. No unjustified assertion that the positive and negative halves are independent under the Wilson measure is made; only their underlying Haar variables are independent, and their interactions are accounted for by the crossing kernels.

## 4. What this rules out, and what it does not

### Free-boundary counterexample route

No bounded positive-halfspace observable on these finite free-boundary complexes has a negative diagonal reflected norm. This includes any finite linear combination or smearing of plaquettes supported in that halfspace and any deterministic scalar normalization. Therefore switching the old straight-torus witness to genuinely Euclidean free-boundary halfspace geometry cannot retain its negative sign.

### Limit inheritance within this family

If F_j are supported in the corresponding positive half-algebras and their reflected moments have a limit, that limit is nonnegative, even if the lattice spacing, volume, couplings, smearing, and normalization vary with j. This is simply closure of [0,infinity) under limits; it is not an existence or moment-convergence theorem.

At fixed lattice spacing and coupling, any subsequential local weak limit of growing swap-invariant free boxes is diagonally reflection positive for bounded continuous fixed local halfspace observables. Their reflected products are also fixed bounded continuous local observables, so convergence passes (1) to the limit. At least one subsequential local weak limit exists by compactness of the countable product of compact link groups (one can extend box measures by identity variables outside). This does not identify all Gibbs states or prove uniqueness.

### Remaining comparison gap

Nothing here proves that a periodic-box limit equals a free-box limit at weak coupling, or that a simultaneous continuum/infinite-volume periodic construction has boundary-shape independence. It does not establish uniqueness, uniform mixing, a mass gap, renormalized moment convergence, continuum rotation invariance, or any continuum construction. Reflection-invariant boundary conditions alone are NOT claimed sufficient if they introduce additional nonlocal couplings or identifications across the halfspaces; the theorem's free Haar/subcomplex factorization is an essential hypothesis.

## 5. Primary-source and prior-assertion check

The frozen source `ethanwsussman/Yang--Mills-LLM-experiment`, commit `785a68fdeef78a1da854c4807fe1f17b597d05e7`, raw III lines 79973–79978, explicitly asserts infinite-lattice diagonal Wilson positivity, contrasts straight-torus failure, and identifies the relevant periodic continuum comparison as unproved box-shape independence. The local source was read directly. Its explicit statement is: “Diagonal reflection positivity holds for the Wilson weight on $\mathbb{Z}^4$ and fails on every straight torus”. This free-boundary proof verifies the stated positivity mechanism; it does not newly refute or newly discover that mechanism.

https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/theorem_0_complete_account_raw_III.tex#L79973-L79978

Primary scholarly context inspected through publisher/institutional records:

- K. Osterwalder and E. Seiler, “Gauge field theories on a lattice,” Annals of Physics 110 (1978), 440–471. Publisher abstract describes rigorous lattice-gauge positivity and transfer construction. https://doi.org/10.1016/0003-4916(78)90039-8
- P. Menotti and A. Pelissetto, “General proof of Osterwalder-Schrader positivity for the Wilson action,” Communications in Mathematical Physics 113 (1987), 369–373. Authors' institutional record describes extension to site-containing reflection planes. https://iris.uniroma1.it/handle/11573/458456 ; DOI https://doi.org/10.1007/BF01221251

These inspected abstracts do not by themselves establish their exact coordinate-swap scope; no such attribution is made here. A targeted search did not locate a primary full-text diagonal theorem during this bounded pass. The argument above is self-contained, uses the standard positive-kernel/sum-of-squares mechanism, and carries no novelty claim.
