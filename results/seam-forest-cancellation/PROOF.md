# Exact quartic onset of the interior seam response

17 October 2026. Finite-volume statement, with no infrared or mass-gap estimate.

## Setting

On the periodic four-dimensional lattice of side n>=4, let C={1,...,n-1}^4. An internal link has both endpoints in C. A seam plaquette has both internal and exterior links. Every seam plaquette has exactly one internal link and three exterior links. Use normalized Wilson traces w_p=(1/2)Re Tr U_p, and split the zero-seam measure as nu_in times nu_out: these are the normalized Wilson measures containing respectively only all-internal and all-exterior plaquettes, with arbitrary fixed nonnegative beta. Set

    W = sum over seam p of w_p,    m = number of seam plaquettes,
    t = s beta,
    M_k(U_in) = E_out[W^k],
    K_t(U_in) = E_out[exp(t W)].

The exact marginal density relative to nu_in is K_t / E_in K_t. The observables below depend entirely on internal links and do not change with t. Exterior integration uses the fixed, normalized nu_out, not independent Haar unless its action is empty.

## Termwise forest lemma

Fix an ordered list p_1,...,p_k of seam plaquettes, allowing repetitions, and let

    J(U_in) = E_out[ product_j w_(p_j) ].

This depends only on the distinct internal edges appearing in this list. It is invariant under independent SU(2) gauge transformations at every lattice vertex. Indeed, transform all internal variables by h_x U_xy h_y^{-1}, and in the exterior integral make the identical change of variables on exterior links. Product Haar and the exterior-only Wilson action are invariant, and every full plaquette trace is invariant. All unselected internal links may be transformed as well since the integrand does not depend on them. No independence of exterior paths is being assumed.

If the graph of selected distinct internal edges is a forest, its edge configurations form one orbit under vertex gauge transformations. On each component choose a root, assign its gauge transformation, and recursively choose that of each child to send its connecting edge to the identity. There is no consistency condition because there is no cycle. Hence J is constant. Repeated edges or plaquettes do not change this argument: take the graph of distinct edges, not a multigraph in which repetitions are declared cycles.

The induced graph on C is an ordinary open Cartesian grid with coordinate values 1,...,n-1. There are no periodic wrap edges inside C. It is simple and bipartite, so any set of at most three distinct edges is a forest. Expanding W^k as the sum over all ordered lists proves that M_k is constant for k<=3. This expansion automatically includes multiplicities with their correct coefficients.

## Symmetry and normalization

Sending every exterior link to its negative preserves nu_out: every exterior-only plaquette has four such factors. Each seam trace changes sign since it has three exterior factors. Thus M_k=0 for all odd k, and K_t=E_out cosh(tW) pointwise. In particular, M_1=M_3=0, while M_2=c_2 is a nonnegative constant, not generally zero.

Write

    a(t) = 1 + c_2 t^2/2,
    R_t(U_in) = E_out[cosh(tW)-1-t^2 W^2/2].

Then K_t=a(t)+R_t exactly, and

    0 <= R_t <= r(t):=cosh(|t|m)-1-(|t|m)^2/2.

Consequently, for any bounded complex interior observable G,

    E_t G - E_0 G = Cov_0(G,R_t)/(a(t)+E_0 R_t).       (1)

Here covariance is bilinear, without complex conjugation. In particular the quadratic term cancels in the normalized expectation; a quadratic term in the partition function is not a quadratic change of the interior law.

A fully explicit remainder is

    |E_t G-E_0 G| <= ||G||_infinity * r(t)/(2 a(t)).     (2)

For verification, if X lies in [0,r], E|X-EX|<=r/2 (bound it by 2 EX(r-EX)/r); apply this to R_t in (1). The trivial bound 2||G|| may be used when smaller. Equivalently the total-variation distance between the two interior marginals is at most min(1,r(t)/(4a(t))). Also r(t)<= (|t|m)^4 cosh(|t|m)/24, so these are explicit finite-volume fourth-order bounds. If m=0 or t=0 the difference is exactly zero, with no division by r needed.

For bounded interior F, put A=Theta F and B=F, where Theta is the antilinear reflected observable and both supports are internal. Suppose ||F||<=M and reflection preserves the norm. For Q_t=E_t AB-E_t A E_t B, applying (2) to AB,A,B gives

    |Q_t-Q_0| <= 3 M^2 r(t)/(2a(t)).                  (3)

This estimate does not need reflection positivity. A lower bound Re Q_t>=-3M^2 r(t)/(2a(t)) additionally requires the free-cube reflection-positive positive-half algebra hypothesis giving Q_0>=0; arbitrary bounded interior F does not suffice. If the reflection also preserves the full cube/seam measure, as in the intended diagonal reflection, Q_t is real and Re Q_t can be replaced by Q_t. The modulus estimate itself requires neither positivity nor this reality condition.

## First coefficient and the remaining analytic gap

All functions are analytic near t=0 at fixed finite volume. With M_4=E_out W^4,

    E_t G = E_0 G + t^4 Cov_0(G,M_4)/24 + O(t^6),
    Q_t = Q_0 + t^4 kappa_0(A,B,M_4)/24 + O(t^6).

The constants in the O terms can depend on the volume, beta, and observable. Here kappa is the usual third joint cumulant, and beta is held fixed as t varies. For the original parameter s, the first possible nonconstant term is beta^4 s^4 times that coefficient. Thus Q'_s at zero, Q''_s at zero and Q'''_s at zero vanish, while no vanishing of the fourth derivative has been asserted.

Termwise, the only possibly nonconstant summands of M_4 select the four distinct edges of an internal elementary square, each exactly once. All other four-edge sets are forests; a four-cycle in this open grid is an elementary square. These squares must have all four edges incident to seam plaquettes to contribute. This identifies an effective boundary interaction, but does not bound its correlation with a distant source.

Equations (2)-(3) contain m to the fourth power at small t and no source-to-seam distance. They become useful only for |s| beta m small, rather than uniformly across the interpolation to s=1. Even the first coefficient requires a bound on the covariance/cumulant between an interior source and an effective boundary function. The forest cancellation therefore sharpens the exact endpoint diagnostic from even to quartic onset; it does not supply the missing boundary-stability estimate for diagonal reflection positivity in the continuum. This route stops here without a new quantitative mixing input.
