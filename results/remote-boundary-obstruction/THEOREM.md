# Finite-torus diagonal-RP obstruction at every prescribed coordinate depth

2026-10-17. Local theorem and explicit small-coupling certificate. Novelty has not been checked. No continuum or mass-gap conclusion.

## Theorem

Let L>=0 be an integer, n>=max(8,6L+5), and choose an integer k with

  3L+2 <= k <= n-3L-3.

On the four-dimensional SU(2) Wilson torus T=(Z/nZ)^4, use representatives 0,...,n-1, the measure proportional to exp(beta sum_p w_p), and w_p=Tr(U_p)/2, with every elementary plaquette counted once. Let theta swap coordinates 0 and 1, and let Theta act antilinearly on observables by reflection. The positive algebra is exactly the original representative-half algebra, with link endpoints x0>=x1.

Take (2,3)-plaquettes p,q at

  p=(n-1-L,k,0,0), q=(k,L,0,0),

and F=w_p-w_q. Set

  D=2L+1, h=4D=8L+4, c=2^(-(16L+9)).

Then all source endpoints have x0>x1 and lie in the coordinate belt

  L <= x0,x1 <= n-1-L.

No source link wraps. The source depth from the artificial 0/1 seam is exactly L, according to this belt convention; this is not a statement about distance from the diagonal mirror. Spectator coordinates remain periodic and are not subject to a depth requirement.

At fixed n,L,k,

  E_beta[(Theta F)F] = -c beta^h + O_(n,L,k)(beta^(h+1)).   (1)

Since k ranges over a finite set, the remainder can equally be written O_(n,L). In particular diagonal RP fails at each such depth for sufficiently small positive beta.

An explicit rational interval is available. Put M=6n^4, r=1/(4M), and

  beta_* = c r^(h+1)/48.

For every 0<beta<=beta_*,

  E_beta[(Theta F)F] <= -(c/2) beta^h < 0.                (2)

The coupling and estimates depend on n and L; no fixed-coupling uniformity, fixed-physical-source continuum transfer, or novelty claim is made.

## 1. Complete coordinate-transfer coefficient

Choose any coordinate direction as time. The spatial lattice is the 3-torus of side n. Let H be the gauge-invariant subspace of product-Haar L^2 of its 3n^3 unoriented links. On each link use central convolution with exp(beta Tr(U)/2)/z(beta), where z is its Haar integral. Its spin-j Peter-Weyl eigenvalue is

  t_j(beta)=c_j(beta)/[(2j+1)c_0(beta)],

where exp(beta chi_(1/2)/2)=sum_j c_j(beta) chi_j. Thus t_0=1, t_(1/2)=beta/4+O(beta^2), and t_j=O(beta^(2j)). Product convolution commutes with spatial gauge transformations; call its restriction K_beta.

In a gauge-invariant spin-network basis, any occupied vertex has at least two occupied incident edges, because a lone nontrivial irreducible representation has no invariant vector. Hence a nonempty occupied support contains a cycle. For n>=8 the spatial nearest-neighbor graph has girth four, and every four-cycle is an elementary plaquette. A network of total leading beta-degree at most four must therefore be one elementary four-edge cycle, each edge in spin 1/2. Its invariant function is chi_p=Tr U_p=2w_p; these functions are orthonormal for distinct elementary unoriented plaquettes. If P4 projects onto their span and P0 onto constants, then the complete expansion is

  K_beta=P0+(beta^4/256)P4+O_1(beta^5),                   (3)

where O_1 is trace norm. There are no other nonconstant modes of lower or equal degree. Repeated link traversals are already resolved into the single-link Peter-Weyl irreps; they are not additional low-order modes. Winding loops have length at least n and do not enter (3).

Here is a direct trace-norm analytic justification. If chi_(1/2)^m=sum_j N_(m,j)chi_j, then N_(m,j)>=0 and sum_j(2j+1)N_(m,j)=2^m. The order-m coefficient of unnormalized single-link convolution is positive with trace norm

  sum_j (2j+1)N_(m,j)/(2^m m!)=1/m!.

Its Taylor series is therefore entire in trace norm. Division by c_0, which equals 1 at zero, is analytic locally. Finite tensor products, restriction by the fixed gauge projector, and bounded multiplication preserve the required analyticity.

Set A_beta=exp[(beta/2)sum_(spatial p)w_p] as a multiplication operator, and T_beta=A_beta K_beta A_beta. Integrating temporal links supplies the spatial gauge projection between successive slices. Taking the trace includes the final temporal link layer, so no periodic holonomy is omitted. Apart from the scalar z(beta)^(3n^4), the partition function is Tr_H(T_beta^n). Spatial multiplication insertions have the exact trace formula

  E[a(0)b(s)]=Tr(M_a T^s M_b T^(n-s))/Tr(T^n).            (4)

For sufficiently small nonnegative beta the operator is positive self-adjoint. Its simple eigenvalue lambda_beta near 1 and associated rank-one projector P_beta are analytic near zero. Define R_beta=T_beta/lambda_beta-P_beta. Then

  P_beta R_beta=R_beta P_beta=0,
  R_beta=(beta^4/256)P4+O_1(beta^5).                      (5)

To justify the subtraction, A_beta P0 A_beta is exactly rank one for every beta. The first perturbation away from it is beta^4 P4/256. At beta=0, P4 is orthogonal to P0, so this term changes neither the principal eigenvalue nor its projector at order four. Thus its full leading complementary coefficient survives normalization and subtraction. This excludes disconnected principal-mode contributions rather than treating them as propagation.

For every fixed positive integer s,

  R_beta^s=(beta^(4s)/256^s)P4+O_1(beta^(4s+1)).          (6)

## 2. Connected covariance on the finite periodic time circle

Write P=|v><v| for nonnegative beta, with ||v||=1 and v=1+O(beta). Orthogonality gives

  (T/lambda)^m=P+R^m,
  Tr((T/lambda)^n)=1+Tr R^n=1+O(beta^(4n)).

Expanding (4), subtracting the product of the one-point trace formulas, and using boundedness of the insertions gives

  Cov(a(0),b(s))
    = <v,M_a R^s M_b v>
      + <v,M_b R^(n-s) M_a v>
      + O(beta^(4n)),                                   (7)

up to an immaterial interchange of a,b from the choice of trace ordering. The term with two complementary propagators, the one-point corrections, and the denominator corrections are all O(beta^(4n)). In particular,

  Cov(a(0),b(s))=O(beta^(4 min(s,n-s))).                  (8)

For the same spatial plaquette a=b=w, if s<n-s, equations (6)-(7) and w=chi_p/2 give the full leading covariance

  Cov(w(0),w(s))
    = beta^(4s)/(4*256^s)+O(beta^(4s+1))
    = beta^(4s)/2^(8s+2)+O(beta^(4s+1)).                (9)

The source factor is exactly <1,M_w P4 M_w 1>=1/4. The reverse path on the time circle is explicitly present in (7) and is higher order in (9). These identities automatically include all Wilson-action Taylor terms, including repeated plaquettes and branching supports.

## 3. Geometry of the four reflected entries

The reflected bases are theta p=(k,n-1-L,0,0) and theta q=(L,k,0,0).

For theta p,q, choose coordinate 1 as time. They have the same spatial plaquette, and their short periodic separation is D=2L+1. The reverse separation is n-D. Our n bound gives n-D>=4L+4>D. Thus (9) yields

  Cov(Theta w_p,w_q)=beta^(4D)/2^(8D+2)+O(beta^(4D+1)).

For theta q,p, choose coordinate 0 as time. The same calculation gives the identical cross coefficient.

For theta p,p, choose coordinate 1 as time. Their forward separation is

  s_p=n-1-L-k >= 2L+2=D+1,

and the reverse separation is

  n-s_p=k+L+1 >= 4L+3 >= D+1.

For theta q,q, again use coordinate 1. The separations are

  s_q=k-L >= 2L+2=D+1,
  n-s_q=n-k+L >= 4L+3 >= D+1.

Equation (8) bounds each self covariance by O(beta^(4D+4)). Different spatial positions do not weaken that bound. The source gaps x0-x1 equal s_p and s_q, respectively, so both sources are strictly in the original positive half. Their fixed coordinates belong to [L,n-1-L], and their spectator links do not wrap since they begin at 0 and n>=8.

Translation invariance gives E w_p=E w_q exactly, hence E F=E Theta F=0. Adding the two self entries and subtracting the two cross entries proves

  E[(Theta F)F]
    = -2 beta^(4D)/2^(8D+2)+O(beta^(4D+1))
    = -2^(-(16L+9)) beta^(8L+4)+O(beta^(8L+5)),

which is (1). At L=0 it recovers -beta^4/512; at L=1 it gives -beta^12/2^25.

## 4. Explicit rational positive interval

Let H=(Theta F)F. Pointwise |H|<=4 and |S|<=M for S=sum_p w_p. For complex z with |z|<=r=1/(4M),

  |Z(z)-1|<=exp(|z|M)-1<=exp(1/4)-1<1/2.

Indeed exp(1/4)<=1/(1-1/4)=4/3, so |Z(z)|>=2/3. Also

  |E_Haar[H exp(zS)]|<=4 exp(1/4)<=16/3,

hence the normalized analytic function g(z)=E_z[H] satisfies |g(z)|<=8, and in particular |g(z)|<=12, throughout this closed disk. Translation symmetry remains valid in the disk and yields E_z F=0, so (1) is also the Taylor expansion of this uncentered g. Its coefficients below degree h vanish, and its degree-h coefficient is -c.

Cauchy's estimate with the deliberately conservative bound 12 gives, for 0<=beta<r,

  |g(beta)+c beta^h|
    <=12 (beta/r)^(h+1)/(1-beta/r).                      (10)

Now beta_* = c r^(h+1)/48 is positive and rational. Since c<=1/512 and r<1,

  beta_*/r=c r^h/48 <1/2.

For 0<beta<=beta_*, use 1/(1-beta/r)<=2 in (10) to get

  |g(beta)+c beta^h|
    <=24 beta^(h+1)/r^(h+1)
    <=24 beta^h [c r^(h+1)/48]/r^(h+1)
    =(c/2) beta^h.

This proves (2), including the endpoint beta_*. It does not rely on unspecified transfer-operator remainder constants.

## Provenance and boundary of the conclusion

The L=1 transfer argument was independently audited at `/tmp/ym-remote-prism-review-20261017/REVIEW.md`; its original frozen source SHA-256 is `9ef6f6cbbf19d809e85257ea0535bdf13ddc87d007044cf6a52f3a0df8874ad1`. The corrected L=1 version restricts operator positivity to nonnegative beta; odd winding loops can violate positivity at negative beta on odd tori. The analytic expansions near zero remain valid.

This document extends the geometry to each fixed integer L and adds a direct finite-volume rational threshold. The general-L extension and threshold require their own independent review. All sources and couplings are microscopic finite-volume objects. In particular, the growing exponent and rapidly shrinking certified interval prevent inferring any continuum limit or a negative result at fixed physical source locations. No literature-based novelty claim is made.
