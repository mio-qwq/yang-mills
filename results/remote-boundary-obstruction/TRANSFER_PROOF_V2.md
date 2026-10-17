# Remote L=1 obstruction from the coordinate transfer operator

2026-10-17. Corrected V2 after independent analytic review; the original file is preserved. No external writes. The earlier locality certificate is unchanged.

## Claim

Use exactly the reference SU(2) Wilson measure on T=(Z/nZ)^4, w_p=Tr(U_p)/2, theta(x0,x1,x2,x3)=(x1,x0,x2,x3), and the strict representative half-algebra x0>x1. Let n>=11, 5<=k<=n-6, and let p,q be (2,3)-plaquettes based at

  p=(n-2,k,0,0), q=(k,1,0,0).

Then F=w_p-w_q has all source endpoints at least one coordinate layer from the 0/1 seam, lies in the original strict half-algebra, has mean zero, and satisfies

  E_beta[(Theta F) F] = - beta^12 / 2^25 + O_n(beta^13).

In particular it is negative at sufficiently small positive beta for each fixed n and admissible k. This is a finite-volume strong-coupling assertion. It does not establish a fixed-physical-source continuum obstruction.

The proof computes full transfer-operator coefficients; it does not infer a covariance from a selected surface diagram. Repeated plaquettes, branching supports, and cumulant subtraction are included by the exact transfer identity.

## 1. Exact coordinate transfer operator

Choose coordinate 1 as time, leaving the spatial 3-torus with coordinates 0,2,3. Let E_s be its unoriented links, |E_s|=3n^3, and let H=L^2(SU(2)^(E_s),Haar)^G be the subspace invariant under independent gauge transformations at spatial vertices. Denote the normalized constant vector by 1 and P0=|1><1|.

Set z(beta)=int_SU(2) exp(beta Tr(U)/2)dU, and let C_beta be the product over spatial links of central convolution with

  k_beta(U)=exp(beta Tr(U)/2)/z(beta).

Product convolution commutes with the spatial gauge action, so restrict it to H and call the restriction K_beta. Equivalently, insert the orthogonal gauge projector in the convolution kernel. Define the bounded multiplication operator

  A_beta(U)=exp[(beta/2) sum_(spatial plaquettes p) w_p(U)],
  T_beta=A_beta K_beta A_beta.

This is the ordinary coordinate-axis transfer construction, obtained by integrating temporal links as the spatial gauge transformations between slices. Each spatial plaquette receives its two half-weights, and each temporal plaquette receives k_beta. Thus, apart from a scalar z(beta)^(3n^4) that cancels in normalized expectations,

  Z_beta = Tr_H(T_beta^n).

For bounded gauge-invariant spatial multiplication observables a,b inserted D time steps apart,

  E_beta[a(0)b(D)]
   = Tr(M_a T_beta^D M_b T_beta^(n-D)) / Tr(T_beta^n).

A one-point insertion is Tr(M_a T_beta^n)/Tr(T_beta^n). No gauge fixing with an unaccounted periodic holonomy is used: temporal-link integration is the gauge projection, including at the trace closure.

## 2. The complete degree-four nonconstant transfer coefficient

Write exp(beta chi_(1/2)/2)=sum_j c_j(beta) chi_j. On the Peter-Weyl subspace of a single link with spin j, convolution has eigenvalue

  t_j(beta)=c_j(beta)/[(2j+1)c_0(beta)].

Consequently t_0=1, t_(1/2)=beta/4+O(beta^2), and t_j=O(beta^(2j)). A gauge-invariant spin-network basis diagonalizes K_beta; its eigenvalue is the product of these t_j over occupied edges.

Every nonconstant gauge-invariant network has a nonempty occupied-edge support with no degree-one vertex: an isolated nontrivial irreducible representation at a vertex admits no invariant vector. A finite graph with no leaves contains a cycle. The spatial nearest-neighbor torus for n>=11 has girth four, and every four-cycle is an elementary plaquette. Therefore:

- There are no nonconstant eigenvectors whose eigenvalue begins below beta^4.
- At degree four, exactly four edges can be occupied, their support is an elementary plaquette, and each edge has spin 1/2.
- The invariant intertwiner space around that loop is one-dimensional. Its normalized basis function is chi_p=Tr(U_p)=2w_p.

Distinct chi_p are orthogonal under Haar (integrate a free edge), and each has norm one. If P4 is their orthogonal span projector, the *complete* expansion is

  K_beta = P0 + (beta^4/256) P4 + O(beta^5).                 (1)

This is valid in trace norm, not merely weak matrix elements. One justification: for a single edge, the absolute trace-norm series is bounded by

  sum_j (2j+1)|c_j(beta)|/|c_0(beta)|
   <= exp(|beta|)/|c_0(beta)|.

The inequality follows by coefficientwise domination |c_j(beta)|<=c_j(|beta|) from the nonnegative tensor-power multiplicities; sum_j (2j+1)c_j(r)=exp(r). The finite tensor product and its gauge-invariant restriction preserve local analytic trace-class convergence. Thus the degree classification above identifies the full trace-norm Taylor coefficient.

## 3. Subtracting the principal mode before taking separations

At beta=0, T_0=P0. There is a unique analytic simple eigenvalue lambda_beta near 1 and its analytic rank-one spectral projector P_beta near P0. For nonnegative beta sufficiently small, T_beta is positive self-adjoint, P_beta=|v_beta><v_beta| with ||v_beta||=1, and lambda_beta>0. Define

  R_beta=T_beta/lambda_beta-P_beta.

Then P_beta R_beta=R_beta P_beta=0 and v_beta=1+O(beta). Equation (1) and A_beta=I+O(beta) give

  R_beta=(beta^4/256)P4+O(beta^5)                           (2)

in trace norm.

For clarity, the possibly lower-order spatial action terms do not invalidate (2): A_beta P0 A_beta is exactly rank one at every beta. Its complement vanishes identically. The first perturbation away from that rank-one operator is beta^4 P4/256; at beta=0, P4 is orthogonal to P0, so its leading coefficient changes neither the principal eigenvalue nor its projector. Projecting off the principal mode therefore leaves exactly that degree-four coefficient. This is the step that removes disconnected caps and their dressing rather than counting them as propagation.

It follows that for each positive integer D,

  R_beta^D=(beta^(4D)/256^D)P4+O(beta^(4D+1)).              (3)

## 4. Finite periodic trace and connected subtraction

Because (T/lambda)^m=P+R^m,

  Tr((T/lambda)^n)=1+Tr(R^n)=1+O(beta^(4n)).

Expand the two-point trace into four terms:

  Tr(M_a P M_b P)
  + Tr(M_a P M_b R^(n-D))
  + Tr(M_a R^D M_b P)
  + Tr(M_a R^D M_b R^(n-D)).

The first term is <v,M_a v><v,M_b v>. The one-point traces equal these principal-mode means up to O(beta^(4n)). Accordingly the connected covariance obeys

  Cov_beta(a(0),b(D))
   = <v,M_a R^D M_b v>
     + <v,M_b R^(n-D) M_a v>
     + O(beta^(4n)),                                      (4)

where swapping a,b in the displayed first term, according to the trace ordering convention, gives the same conclusions below. Bounded multiplication operators and the trace-norm bound on R control the mixed remainder and mean corrections. In particular,

  Cov_beta(a(0),b(D))=O(beta^(4 min(D,n-D))).               (5)

If a=b=w_p is the same spatial plaquette and D<n-D, equations (3)-(4) yield

  Cov_beta(w_p(0),w_p(D))
   = beta^(4D)/256^D * <1,M_wp P4 M_wp 1>
     + O(beta^(4D+1))
   = beta^(4D)/2^(8D+2)+O(beta^(4D+1)),                   (6)

because w_p=chi_p/2 and its Haar norm squared is 1/4. The longer periodic propagation path is included and is higher order. These are full Wilson-model covariances, not an isolated tube weight.

## 5. Apply to the four entries

The reflected sources are theta p=(k,n-2,0,0) and theta q=(1,k,0,0), still oriented (2,3).

- theta p and q have the same spatial location x0=k, x2=x3=0. In time coordinate 1, their short separation is 3, through n-2,n-1,0,1. Equation (6) gives beta^12/2^26+O(beta^13).
- theta q and p have the same spectator coordinates and time x1=k. Choose coordinate 0 as time instead. Their short separation is likewise 3, so the other cross covariance has the same coefficient.
- theta p and p have coordinate-1 time separation h_p=n-2-k. Our k range gives h_p>=4 and n-h_p>=7. Equation (5) bounds this self covariance by O(beta^16), irrespective of their different spatial positions.
- theta q and q have coordinate-1 time separation h_q=k-1>=4, with n-h_q>=7. Their self covariance is likewise O(beta^16).

Translation invariance gives E(w_p-w_q)=0, exactly at every beta. Therefore the uncentered reflected norm equals the corresponding four connected entries, and

  E[(Theta F)F]
   = O(beta^16)+O(beta^16)
     -2(beta^12/2^26+O(beta^13))
   = -beta^12/2^25+O(beta^13).

All coordinates remain in the original representatives and both original source plaquettes are strictly in x0>x1, with coordinate-depth one. Their spectator coordinates 0 do not alter the stated 0/1 seam depth.

## Scope and checks still desirable

The transfer proof establishes a higher-order route around the failure of the quartic mechanism, subject to independent review of the exact trace normalization and analytic rank-one subtraction. It does not assert a useful numerical coupling threshold, uniformity as n or source depth grows, or any continuum consequence. An explicit small-beta threshold could be extracted from a separately quantified remainder, but finite-volume analyticity already yields existence.

## V2 review record

Independent review: `/tmp/ym-remote-prism-review-20261017/REVIEW.md`. The original reviewed SHA-256 is `9ef6f6cbbf19d809e85257ea0535bdf13ddc87d007044cf6a52f3a0df8874ad1`. The reviewer supported the positive-beta theorem and identified only the positivity wording above: on an odd spatial torus, negative beta can give a negative eigenvalue for an odd winding loop. V2 restricts that assertion to nonnegative beta; no coefficient or conclusion changes.
