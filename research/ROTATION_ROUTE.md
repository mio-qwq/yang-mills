# Rotation-invariance route: current obligations

Research checkpoint, not a completed Yang–Mills theorem.

The reference repository also contains a separate 18-page manuscript, `QED3_slop/YM_Rotation_Invariance_simplified.pdf`. Its Theorem A concerns a translation- and hypercubic-invariant probability law of **ordinary closed two-forms**, with Gaussian domination in the **L2 test norm** and coordinate/diagonal reflection positivity. It claims full Euclidean covariance.

These hypotheses cannot simply be applied to SU(2) curvature: its Bianchi identity is covariant, D_A F=0, not dF=0; curvature components are not gauge-invariant scalar observables; tr(F)=0; the action density is a scalar composite and the required Gaussian L2 domination is not supplied. Proving an analogous theorem for suitable gauge-invariant observables requires new arguments.

A possible abstract route is to quantify imaginary-angle continuation of correlation defects. The reference argument uses growth exp(c*N*|beta|) with c=2, positive Gram kernels in coordinate and pi/4-tilted frames, and recovery from ordered/disjoint planar test supports. Its arithmetic elimination suggests a threshold c<4. This has not been independently proved here and supplies no missing YM hypotheses by itself.

Generalizing the closed-two-form argument to arbitrary tensor fields is unsafe. Contact-supported covariances can satisfy positivity on disjoint half-spaces without rotational covariance; the reference's closedness and contact-removal step are substantive assumptions.

## Separate Gaussian route under investigation

For a finite positive sum of scalar covariances (p^T A_j p+m_j^2)^(-1), coordinate and diagonal reflection positivity should force all metrics A_j to be scalar. A finite-exponential Hankel argument has been drafted. This is a restricted model result only. Infinite positive mixtures require a different argument; finite exponential interpolation does not extend automatically.

For a single-pole hypercubic scalar covariance P(p)/(p^2+m^2), a polynomial numerator of degree at most six appears to force isotropy away from contact terms under the same mirror positivity. Degree eight has potential counterexamples. This is a candidate, not an accepted theorem in this packet; full proof and novelty review remain to be completed.

## Unresolved main objectives

- Rigorous verification of the analytic RG inputs on which the reference construction depends.
- Exact full rotational invariance for the relevant nonabelian continuum observables without assuming it indirectly.
- A uniform infinite-volume infrared estimate establishing a positive mass gap.

The local operator certificate in this directory does not resolve any of these objectives by itself. No unverified RG statements are promoted to axioms or hidden in the certificate.
