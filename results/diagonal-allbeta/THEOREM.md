# Exact finite-torus diagonal-RP obstruction at every positive Wilson coupling

2026-10-17. Separate local proof, submitted for independent review. All earlier proofs remain unchanged. Novelty is unverified.

## Theorem

Let L>=0 be an integer, n>=max(8,6L+5), and choose an integer k satisfying

  3L+2 <= k <= n-3L-3.

On the four-dimensional SU(2) Wilson torus T=(Z/nZ)^4, use representatives 0,...,n-1, plaquette normalization w_p=Tr(U_p)/2, and the probability measure proportional to exp(beta sum_p w_p), with every elementary plaquette counted once. Let theta swap coordinates 0 and 1, and let Theta act antilinearly on observables by reflection. The positive-half algebra is the original one defined by link endpoints x0>=x1.

Let p,q be the (2,3)-plaquettes based at

  p=(n-1-L,k,0,0), q=(k,L,0,0),

and put F=w_p-w_q. Then, for every finite real beta>0,

  E_beta[(Theta F)F] < 0.                                (1)

All source links are nonwrapping and their endpoints satisfy x0>x1. Every source endpoint belongs to the belt L<=x0,x1<=n-1-L, with minimum 0/1 coordinate depth exactly L. The depth is measured from the artificial 0/1 seam in the declared representatives, not from the diagonal mirror. No spectator-coordinate depth is asserted.

This is an exact finite-volume sign theorem for every positive coupling. It supplies no uniform negative margin and no continuum, infinite-volume fixed-source, or mass-gap conclusion.

## 1. Exact transfer operator at arbitrary beta>0

Choose coordinate 1 as time. The spatial lattice is the 3-torus of side n with coordinates 0,2,3. Let H0 be product-Haar L^2 of its 3n^3 unoriented links, and let H be its closed subspace invariant under independent gauge transformations at spatial vertices. Use one canonical orientation per link; inverses represent the other orientation.

For one link let C_beta be central convolution with

  k_beta(U)=exp(beta Tr(U)/2)/z(beta),
  z(beta)=int_SU(2) exp(beta Tr(U)/2)dU.

On the spin-j Peter-Weyl block, its eigenvalue is

  t_j(beta)=c_j(beta)/[(2j+1)c_0(beta)],

where exp(beta chi_(1/2)/2)=sum_j c_j(beta)chi_j. For every beta>0 and every j, c_j(beta)>0. Indeed all coefficients in every tensor-power character decomposition are nonnegative, and spin j appears in the power 2j, which occurs with a strictly positive exponential coefficient. Thus every single-link eigenvalue is strictly positive.

The single-link operator is trace class: the spin-j multiplicity is (2j+1)^2, and

  Tr C_beta=sum_j (2j+1)c_j(beta)/c_0(beta)
            =exp(beta)/z(beta)<infinity.

The finite tensor product over spatial links is consequently positive, injective and trace class. Central convolution commutes with endpoint gauge transformations, so H reduces this product operator. Denote the restriction by K_beta; it remains positive, injective and trace class.

Let A_beta be multiplication by

  exp[(beta/2)sum_(spatial plaquettes r)w_r].

For fixed finite volume and finite beta, A_beta is bounded, strictly positive, has a bounded inverse, and preserves H. Set

  T_beta=A_beta K_beta A_beta on H.

Then T_beta is self-adjoint, positive, injective and trace class. Positivity here means nonnegative quadratic form, and injectivity additionally makes every eigenvalue strictly positive; no uniform positive lower spectral bound is asserted.

Temporal-link integration gives the spatial gauge projector between successive slices. The periodic trace includes its final slice, so no periodic holonomy is removed. Apart from the positive scalar z(beta)^(3n^4), the partition function is

  Z=Tr_H(T_beta^n)>0.

For bounded gauge-invariant spatial multiplication observables a,b inserted s time steps apart, 1<=s<=n-1,

  E_beta[a(0)b(s)]
    =Tr(M_a T_beta^s M_b T_beta^(n-s))/Z.                 (2)

The scalar omitted from the partition function cancels in (2). Spatial translations commute with T_beta and preserve H.

## 2. The plaquette multiplication operator does not commute with T

Fix a spatial (2,3)-plaquette at any specified spatial location, and write w(U)=Tr(U_p)/2. It is real, gauge invariant, bounded, and nonconstant. Its finite-torus mean is

  mu=Tr(M_w T^n)/Z.

Let B=M_w-mu I. We will need [B,T] != 0, which equals [M_w,T] != 0.

This holds on the gauge-invariant Hilbert space itself, not just before gauge projection. To see it, write the restricted operator using a kernel on full configuration space. The full convolution kernel is a product of strictly positive continuous factors k_beta(U_e V_e^{-1}). Averaging over a gauge transformation of V gives a gauge-invariant kernel. Multiplying by A_beta(U)A_beta(V) gives a continuous kernel t(U,V)>0 everywhere that represents T on H with respect to full product Haar measure.

Take the gauge-invariant function f(V)=1_{w(V)<0}. For U with w(U)>0,

  ([M_w,T]f)(U)
    =int (w(U)-w(V)) t(U,V) 1_{w(V)<0} dV >0.            (3)

Both sets {w>0} and {w<0} have positive Haar measure: integrating any one plaquette edge makes its holonomy Haar distributed. Thus (3) proves that the commutator is a nonzero operator on H. Centering by mu I does not change it.

This argument avoids any need to choose a gauge-orbit quotient measure or to assume that a nonconstant function survives projection without proof.

## 3. Strict temporal decrease of the centered plaquette autocorrelation

Suppress beta from notation and define

  C0(s)=Tr(B T^s B T^(n-s))/Z,  1<=s<=n-1.              (4)

Since T is compact, self-adjoint and injective, it has a complete orthonormal eigenbasis with eigenvalues lambda_i>0. The spectral expansion is

  C0(s)=Z^(-1) sum_(i,j) |B_ij|^2 lambda_i^s lambda_j^(n-s).  (5)

The series is finite in sum and nonnegative. For example weighted arithmetic-geometric mean yields

  lambda_i^s lambda_j^(n-s)
    <=(s/n)lambda_i^n+(1-s/n)lambda_j^n,

and summing with |B_ij|^2 bounds the total by ||B||^2 Tr(T^n). This also justifies regrouping into unordered eigenvalue pairs. Equation (5) gives C0(s)=C0(n-s).

For i!=j the combined pair is

  2 |B_ij|^2 (lambda_i lambda_j)^(n/2)
    cosh[(n/2-s) log(lambda_i/lambda_j)] / Z.             (6)

As s increases toward n/2, each term (6) is nonincreasing. If lambda_i!=lambda_j and B_ij!=0, it is strictly decreasing. Such a pair exists because [B,T]!=0 by Section 2: in the complete eigenbasis, the commutator has entries (lambda_j-lambda_i)B_ij.

Consequently, for integer separations satisfying 1<=a<b<=floor(n/2),

  C0(a)>C0(b).                                          (7)

Equivalently, C0(s) strictly decreases as the circular distance min(s,n-s) increases from 1 toward floor(n/2). There is no claim of a lower bound on the amount of decrease uniform in beta or volume.

## 4. Spatially displaced correlations are bounded by C0

Let B_x be a spatial translate of B. Translation invariance makes its mean equal to mu and gives

  Tr(B_x T^s B_x T^(n-s))/Z=C0(s).

For two spatial locations x,y, define

  C(x,y;s)=Tr(B_x T^s B_y T^(n-s))/Z.

The Hilbert-Schmidt operators

  X_x=T^(s/2) B_x T^((n-s)/2),
  X_y=T^(s/2) B_y T^((n-s)/2)

satisfy

  Tr(X_x^*X_y)=Tr(B_x T^s B_y T^(n-s)),
  ||X_x||_HS^2=||X_y||_HS^2=Z C0(s).

These operators are Hilbert-Schmidt because s,n-s>=1, T is positive trace class, and each B_x is bounded. Cauchy-Schwarz therefore gives the exact bound

  |C(x,y;s)|<=C0(s).                                    (8)

The traces equal ordinary real Wilson-measure correlations by (2), so in particular C(x,y;s)<=C0(s). No reflection positivity for the diagonal theta is assumed in this argument; the transfer operator uses a coordinate-axis time direction.

## 5. Apply the exact inequalities to the source geometry

Set a=n-1-L and D=2L+1. The original and reflected bases are

  p=(a,k,0,0),       q=(k,L,0,0),
  theta p=(k,a,0,0), theta q=(L,k,0,0).

Translation invariance gives E w_p=E w_q=mu and E F=0. All four plaquettes have the same (2,3) orientation. Center each by this common mean, so the reflected norm is exactly the signed sum of four covariances.

**Cross entry theta p,q.** With coordinate 1 as time, the spatial plaquette positions agree, and the short periodic time separation is D. Thus this covariance is C0(D), using the symmetry C0(s)=C0(n-s).

**Cross entry theta q,p.** Use coordinate 0 as time. The same-spatial-plaquette separation is again D. Interchanging coordinate axes 0 and 1 preserves the action, the lattice, and the (2,3) observable, so the autocorrelation function is the same C0. This entry also equals C0(D).

**Self entry theta p,p.** Use coordinate 1 as time. Its temporal separation is

  h_p=a-k=n-1-L-k,

and its spatial positions may differ. Equation (8) bounds this covariance above by C0(h_p).

**Self entry theta q,q.** Again use coordinate 1 as time. Its temporal separation is h_q=k-L. Equation (8) bounds it above by C0(h_q).

The k bounds give

  h_p>=2L+2=D+1,       n-h_p=k+L+1>=4L+3>D,
  h_q>=2L+2=D+1,       n-h_q=n-k+L>=4L+3>D.

Also n-D>=4L+4>D, from n>=6L+5. Both self-pair circular distances are therefore strictly larger than D. By (7),

  C0(h_p)<C0(D),       C0(h_q)<C0(D).

Combining these facts,

  E[(Theta F)F]
    <= C0(h_p)+C0(h_q)-2C0(D)
    <0,

which proves (1) for every beta>0.

The source gaps x0-x1 are h_p and h_q, both positive. Their 0/1 coordinates lie in [L,n-1-L], with p at its upper boundary and q at its lower boundary. Since their only varying coordinates are 2 and 3, from 0 to 1, no source link wraps. The original strict positive-half hypothesis and declared depth are therefore unchanged.

## 6. Relation to the small-coupling proof and limits

The separately derived strong-coupling expansion gives, for this same F,

  E[(Theta F)F]
    =-2^(-(16L+9)) beta^(8L+4)+O_(n,L)(beta^(8L+5)).

The current proof does not use that expansion or its explicit tiny coupling interval. It strengthens the sign conclusion to every finite beta>0 by exact transfer inequalities. In particular no enumeration of higher-order surface diagrams is needed for the sign.

The spectral decrease in Section 3 can become arbitrarily small along varying beta, n, or L. Moreover these source locations and their support geometry vary with the torus and chosen seam. Strict negativity at every finite stage does not imply a nonzero negative limiting quadratic form for fixed compact physical sources. No continuum failure, continuum restoration, vacuum statement, or mass-gap conclusion follows here.

This is a local proof awaiting independent review, not a claim of literature novelty. No prior proof file, repository state, or external service was changed.
