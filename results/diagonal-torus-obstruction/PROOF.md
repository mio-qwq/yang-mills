# Diagonal reflection positivity: exact for free boxes, false for Wilson tori

17 October 2026. Finite lattice results only.

## Decision

The direct finite-torus shortcut is false. On a four-dimensional hypercubic SU(2) Wilson torus, diagonal reflection positivity fails, for sufficiently small positive Wilson coupling, even for a difference of two contractible elementary plaquette traces whose links lie strictly on the positive side of the diagonal in the chosen fundamental cube. The reflected quadratic form is

    - beta^4/512 + O_n(beta^5).

On a reflection-symmetric free box, the diagonal positive-kernel decomposition is exact at every nonnegative coupling. Thus the free-box endpoint in the existing boundary-response bridge is justified, but exact finite-volume periodic diagonal positivity cannot replace the missing boundary-stability estimate. The counterexample's sources approach the periodic seam as volume grows, so it does not disprove the desired fixed-compact-source joint continuum/infinite-volume statement.

## 1. Conventions and positive-half algebra

Let T=(Z/nZ)^4, n>=8, represented by coordinates 0,...,n-1, with one SU(2) variable for each unoriented nearest-neighbor link and U_yx=U_xy^{-1}. All elementary plaquettes, including wrapping plaquettes, occur once in

    d mu_beta = Z^{-1} exp[ beta sum_p w_p ] dHaar,
    w_p = (1/2) Tr U_p.

SU(2) traces are real, so either orientation defines the same w_p. Let

    theta(x0,x1,x2,x3)=(x1,x0,x2,x3),
    Theta F(U)=overline(F(theta U)).

Define A_+ as functions of links whose endpoints both satisfy x0>=x1 in these representatives. The counterexample actually uses only links whose endpoints satisfy x0>x1; none of its observable links wraps. This removes possible ambiguity about including interface or wrapping links in A_+.

The sum-negating reflection (-x1,-x0,x2,x3) is conjugate to this one by reversal of one coordinate; the same phenomenon consequently holds for the corresponding conjugate positive-half algebra. A geometric half-algebra must always be specified: on a torus the diagonal is not a separating hypersurface.

## 2. A local low-order partition-function lemma

Introduce independent real couplings b_p and

    Z(b)=integral exp[sum_p b_p w_p] dHaar,
    z(b)=integral_SU(2) exp[(b/2)Tr U] dU.

At fixed finite n, these functions are analytic near zero, Z(0)=1, and log Z has the multivariate expansion

    log Z(b) = sum_p log z(b_p)
             + (1/1024) sum_cubes c product_{p in boundary c} b_p
             + terms of total degree at least 7.                 (1)

Here a cube is any elementary three-dimensional cell in any three coordinate directions, including cells crossing the periodic seam. Equation (1) is a statement about Taylor coefficients; no infinite-volume cluster expansion or convergence estimate is required.

### 2.1 Peeling proves all the vanishing coefficients

A finite set S of distinct plaquettes is peelable if one can repeatedly remove a plaquette with an edge belonging to no other remaining plaquette. If p has such an edge e, integrate U_e first. For all fixed other link variables, bi-invariance of Haar measure gives

    integral dU_e exp[b_p w_p] = z(b_p).

Remove p and continue. Therefore, when only couplings in a peelable S are switched on,

    Z_S(b) = product_{p in S} z(b_p).                         (2)

Thus every mixed log-Z Taylor coefficient with peelable distinct support vanishes, regardless of repetitions/powers of its couplings. This is stronger and cleaner than merely checking even edge parity in individual moments.

Every set of at most five plaquettes is peelable. Every nonpeelable set of six plaquettes is an elementary cube boundary. A short exact combinatorial certificate is supplied by check_small_cores.py. Its exhaustive reasoning is as follows:

* In a nonempty unpeelable remainder every edge belongs to at least two faces.
* Fix a face p. Each of its four edges needs another face. Two distinct elementary plaquettes share at most one edge, so these are four distinct additional faces.
* In dimension four each edge has exactly five other incident faces. There are therefore 5^4=625 choices for these four faces.
* For each resulting five-face set, list its edges of multiplicity one. A sixth face, if present, must contain every such edge. Intersect the lists of incident faces for these edges and test whether the candidate closes all edges.
* The script finds no five-face core and exactly four six-face cores, precisely the elementary cube boundaries containing p (two transverse axes, two sides each).

This also proves the assertion for a general set of <=6 faces: if peeling stops, its remaining core has >=5 faces; the enumeration rules out five and classifies six. For n>=8 the local incidence configurations tested here cannot acquire extra identifications from periodicity, and the same classification applies at seam-crossing roots by lifting their local neighborhoods to Z^4.

Consequently every mixed term of total degree <=6 vanishes except a degree-six term using the six faces of one cube, each once. Setting all other couplings to zero identifies each coefficient individually; unused plaquettes do not affect Taylor coefficients.

### 2.2 Exact cube coefficient

For the six distinct faces of a cube, every nonempty proper subset has zero product Haar expectation (peel a face with an unpaired edge). Hence its squarefree log-Z coefficient is simply

    integral product_{six faces p} w_p dHaar.

Orient the six faces outward. Each of the twelve edges appears once as U and once as U-dagger. The identity

    integral U_ab conjugate(U_cd) dU = delta_ac delta_bd / 2

gives a factor 2^{-12}. Contracting the trace indices leaves one free index at each of the eight cube vertices, giving 2^8. The six normalized traces contribute 2^{-6}. The result is

    2^{-12} 2^8 2^{-6} = 2^{-10} = 1/1024.

This proves (1), including its sign and normalization.

Differentiating (1) with respect to two distinct plaquette couplings, then setting every b_p=beta, yields

    Cov_beta(w_p,w_q)
      = (number of elementary cubes having both p,q as faces)
        * beta^4/1024 + O_n(beta^5).                         (3)

In particular the coefficient is 1 for parallel opposite faces one lattice step apart, and 0 for the more distant pairs used below. The remainder is at fixed n and is not claimed uniform in n or cutoff.

## 3. Explicit local counterexample

Let p and q be oriented (2,3)-plaquettes with respective base points

    p: (n-1,2,0,0),       q: (2,0,0,0).

Let P=w_p, Q=w_q, F=P-Q. Every vertex of p has x0-x1=n-3>0; every vertex of q has x0-x1=2>0. All eight observable links lie strictly in the positive half and do not wrap. These are local gauge-invariant and center-neutral observables.

Their reflected plaquettes are at

    theta p: (2,n-1,0,0), theta q: (0,2,0,0).

The pair (theta p,q) is the pair of opposite (2,3)-faces of the elementary (1,2,3)-cube that wraps from x1=n-1 to x1=0. Similarly (theta q,p) consists of opposite faces of a wrapping (0,2,3)-cube. Each pair belongs to exactly one elementary cube.

Neither (theta p,p) nor (theta q,q) belongs to an elementary cube: their base points differ in both coordinates 0 and 1, with cyclic distances at least two in each coordinate. Consequently (3) gives

    Cov(Theta P,P)=O_n(beta^5),
    Cov(Theta Q,Q)=O_n(beta^5),
    Cov(Theta P,Q)=beta^4/1024+O_n(beta^5),
    Cov(Theta Q,P)=beta^4/1024+O_n(beta^5).

Translation invariance implies E P=E Q and therefore E F=0; reflection invariance gives E Theta F=0. Thus the centered and uncentered reflected forms agree:

    E[(Theta F)F] = -beta^4/512 + O_n(beta^5).               (4)

Analyticity at finite volume implies that for every fixed n>=8 this is strictly negative throughout some interval 0<beta<epsilon_n. This is an exact existence statement about the finite Wilson measure, not a Monte Carlo inference or an asymptotic claim at large beta.

The formula applies to the definition w=(1/2)Tr U. A convention with another normalization rescales the coefficient but not its sign.

### 3.1 An explicit positive coupling, without an unspecified remainder constant

Let M=6 n^4 be the number of elementary plaquettes and S=sum_p w_p, so |S|<=M and |(Theta F)F|<=4. Since E_beta F=0, the numerator of the reflected form is

    N(beta)=E_Haar[(Theta F)F exp(beta S)].

Equations (1)-(4) imply that its Taylor coefficients below degree four vanish and its degree-four term is -beta^4/512 (Z(0)=1). The exponential-series tail therefore gives, for beta>=0,

    |N(beta)+beta^4/512| <= exp(beta M) beta^5 M^5 / 30.

Choose the explicit rational coupling

    beta_* = 1 / (128 M^5).

Then beta_* M<=1/128 and exp(beta_* M)<=128/127, using exp(x)<=1/(1-x) for 0<=x<1. Consequently the tail is at most beta_*^4/3810, which is smaller than beta_*^4/1024. Thus

    N(beta_*) <= -beta_*^4/1024,
    E_beta_*[(Theta F)F] <= -beta_*^4/(1024 exp(beta_* M)) < 0.

This is a conservative finite-volume certificate, not a useful physical-coupling threshold. The same estimate holds for every 0<beta<=beta_*. It requires no unproved uniform strong-coupling expansion.


## 4. Exact free-box decomposition

Let B={0,...,m}^4 with ordinary nonwrapping edges and free Wilson action, invariant under theta swapping coordinates 0,1. Define E_+ by both endpoints x0>=x1, E_- by both endpoints x0<=x1, and E_0=E_+ intersect E_-.

Every link is in one of these sets. The only interface links E_0 point in spectator directions 2,3 and lie in x0=x1. The links strictly on opposite sides are independent under product Haar conditional on U_E0.

Classify plaquettes:

1. Entirely on one closed side: they occur as reflected pairs, except those entirely in the interface, whose weight is positive and can be kept in the interface measure.
2. Crossing the mirror: necessarily (0,1)-plaquettes with opposite vertices (k,k) and (k+1,k+1) on the mirror. Their boundaries consist of a two-link positive path A between those fixed vertices and the reversed reflected path. Thus U_p=A (theta A)^{-1} up to conjugation.

For every irreducible unitary representation j,

    chi_j(A B^{-1}) = sum_rt D_j(A)_rt conjugate(D_j(B)_rt).

The SU(2) Wilson weight has a uniformly convergent character expansion

    exp[(beta/2) chi_{1/2}(U)] = sum_j c_j(beta) chi_j(U),
    c_j(beta)>=0, beta>=0.

Positivity follows directly from the exponential series and nonnegative tensor-product multiplicities. Thus every crossing weight is a sum of terms c_j (Theta f_jrt)f_jrt. Products preserve this cone. The side action is exp(S_+)Theta(exp(S_+)); conditional integration over reflected sides gives a sum of squared moduli. The remaining integral against positive interface weight preserves nonnegativity. Hence

    E_B[(Theta F)F]>=0

for every bounded continuous F of positive-half links. Centering F proves connected positivity. This is exact for all beta>=0.

On the torus, periodic seam plaquettes supply additional cross-side interactions which are not diagonal-mirror cuts into paths with pointwise fixed endpoints. The wrapping cubes in Section 3 identify how those interactions actually produce a negative reflected form; merely classifying the near-mirror plaquettes misses them.

## 5. Original literature and recent formulations

The relevant original oblique-plane proof is Evertz, Jansen, Kastrup, Fredenhagen and Marcu, Physics Letters B 194 (1987), 277-282, DOI 10.1016/0370-2693(87)90542-9. Their setup on p.278 is a reflection-invariant box in Z^D. Equations (9)-(13), pp.278-279, use half-space-supported functions and exactly the positive-cone split above. They then discuss infinite-volume Gibbs states obtained by suitable thermodynamic limits. This does not assert that arbitrary periodic hypercubic tori have the same diagonal half-space factorization.

Original author-hosted scan:
https://itp.tugraz.at/~evertz/Pubs/1987_PLB_194_277_Proof_of_Perimeter_Law_in_Nonabelian_Higgs.pdf

Osterwalder and Seiler, Annals of Physics 110 (1978), 440-471, DOI 10.1016/0003-4916(78)90039-8, is the original Wilson physical-positivity reference. The accessible abstract verifies that this is the general lattice physical-positivity/transfer-matrix paper; it does not settle the torus geometry above by itself.
https://doi.org/10.1016/0003-4916(78)90039-8

The recent paper Bootstrapping SU(3) Lattice Yang-Mills Theory, JHEP 03 (2025) 099, arXiv:2502.14421, Section 3.2, equations (3.9)-(3.13), explicitly presents diagonal reflection and the cut-plaquette cone argument. Its discussion on p.29 describes local regions of the infinite lattice. That argument likewise needs the declared geometric split and cannot erase periodic seam terms.
https://d-nb.info/137049159X/34
https://arxiv.org/abs/2502.14421

## 6. Scope and the next justified route

Established:

* Exact diagonal RP of the reflection-symmetric free-box Wilson measure.
* Failure of diagonal RP for finite hypercubic periodic Wilson measures, including a strictly-positive-half local plaquette-algebra witness at sufficiently small beta.
* A precise seam mechanism, already visible in the degree-six cube contribution to log Z.

Not established or refuted:

* Diagonal RP for a prescribed fixed compact collection of renormalized action-density sources after a joint UV/infinite-volume limit.
* A large-beta counterexample, or cutoff-uniform quantitative boundary response.
* Failure or validity for every other choice of torus subalgebra.
* Continuum Euclidean covariance, vacuum uniqueness, or a Yang-Mills mass gap.

The witnesses in (4) sit next to the artificial periodic seam; one source moves outward when n grows. The coefficient is a diagnostic of why exact microscopic periodic RP cannot be invoked, not an obstruction that survives the target limit. The boundary-response bridge (or another argument controlling removal of remote seams for fixed sources) remains necessary as a route unless replaced by a different rigorously justified thermodynamic-limit construction. Quartic endpoint cancellation alone does not supply that control.
