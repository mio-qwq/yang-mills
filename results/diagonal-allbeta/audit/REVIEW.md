# Independent audit: all-positive-coupling finite-torus obstruction

Date: 2026-10-17.

Frozen source: `../THEOREM.md`

Verified SHA-256: `201bce70620fd3984956190a207e49bec5f5539666f2dfb149df162904ef4688`.

## Verdict

The argument supports strict negativity for every finite beta>0 under its stated L,n,k hypotheses. I found no substantive gap or required correction. In particular, the proof does not silently require a spectral gap bounded away from zero, a finite-dimensional transfer matrix, or a diagonal-reflection-positivity assumption.

The decisive strengthening beyond the previous small-coupling proof is valid: noncommutation of the centered plaquette observable with a positive injective transfer operator forces its finite-period temporal autocorrelation to be strictly decreasing with circular separation, and a Hilbert–Schmidt inequality bounds displaced correlations by that same autocorrelation.

This is an analytic review supplemented by exact finite-matrix controls, not an independent symbolic evaluation of the full lattice integral. No novelty, uniform negative margin, or continuum conclusion is endorsed.

## 1. Strictly positive coefficients and the arbitrary-beta transfer operator

For SU(2), tensor powers of the fundamental character decompose with nonnegative integer multiplicities. The spin-j irrep occurs in power 2j, so c_j(beta)>0 for every beta>0, without needing beta to be small. Character-series convergence at fixed beta is justified by the dimension sum: the trace-norm Taylor coefficient of unnormalized single-link convolution is 1/m!. Thus the sum of trace-norm coefficients is exp(beta), finite at every finite beta. Division by z(beta)>0 is harmless on the positive real axis.

The Peter–Weyl multiplicity is d_j^2 and its eigenvalue is c_j/(d_j c_0), giving total trace sum_j d_j c_j/c_0=exp(beta)/z(beta). Every block eigenvalue is strictly positive. The full link-product operator is therefore positive and injective, although its eigenvalues tend to zero. Endpoint gauge actions commute with central convolution. The invariant subspace reduces the product operator, so its restriction K remains positive, injective and trace class.

A is bounded and boundedly invertible at every fixed finite volume and finite beta. Consequently T=A K A is positive self-adjoint and trace class. Injectivity follows either from A K A f=0 and invertibility of A, or from <f,Tf>=||K^(1/2)A f||^2. No lower spectral bound is needed. At beta=0 injectivity fails; the theorem correctly excludes that value.

The coordinate transfer construction and periodic trace were already audited in the previous proof. All steps are exact at arbitrary finite beta, not just in a local analytic expansion. The removed scalar z(beta)^(3n^4) is positive and cancels from all normalized traces. Calling the remaining trace Z introduces no normalization error.

## 2. Gauge-invariant positive kernel and noncommutation

Let c(U,V) denote the product of positive central one-link kernels. Under the same gauge transformation on U and V, each U_e V_e^(-1) changes by conjugation at an endpoint; therefore c is invariant under simultaneous gauge transformations. Averaging c(U,gV) over the gauge group makes the kernel separately invariant in V and, by simultaneous invariance and Haar invariance, separately invariant in U. It still represents the same convolution when acting on invariant functions. The average remains continuous and strictly positive because its integrand is strictly positive on the compact configuration and gauge spaces. Multiplication by the invariant positive factors A(U)A(V) preserves these properties.

This kernel on full Haar configuration space represents T restricted to H. It need not be injective on the entire noninvariant space; the proof only needs injectivity on H, already established spectrally. No quotient measure or gauge-fixing assumption is hidden in this construction.

The sign indicator f=1_{w<0} is bounded, measurable and gauge invariant. Both {w<0} and {w>0} have positive full Haar measure: a source plaquette has four distinct physical links for n>=8, and conditioning on three of them makes its holonomy Haar as the remaining link varies. SU(2) half-traces take both signs on positive-measure open sets.

For U with w(U)>0 the commutator integrand (w(U)-w(V))t(U,V)1_{w(V)<0} is nonnegative and strictly positive throughout the negative-sign set. Its integral is positive. The commutator therefore sends an element of H to a nonzero element of H. This proves noncommutation on the required Hilbert space. Subtracting the scalar mean leaves the commutator unchanged.

## 3. Infinite-dimensional spectral expansion and strictness

H is separable. The compact self-adjoint spectral theorem decomposes it into eigenvectors together with the kernel. Since the kernel is zero, the eigenvectors with positive eigenvalues form a complete orthonormal basis. Accumulation at zero does not invalidate completeness or introduce missing zero-eigenvalue terms.

B is bounded and self-adjoint. For 1<=s<=n-1, the matrix-element expansion of the trace equals

  sum_(i,j) |B_ij|^2 lambda_i^s lambda_j^(n-s).

The weighted arithmetic-geometric mean bound in the source is correct. Summing it uses both row and column square sums of B, each bounded by ||B||^2, giving an upper bound ||B||^2 Tr(T^n). This proves finite absolute sum and legitimizes all index interchanges and unordered-pair regroupings. The same expansion also follows as the squared Hilbert–Schmidt norm of T^(s/2) B T^((n-s)/2), avoiding any conditional trace manipulation.

For each unordered pair of distinct eigenbasis indices the two terms combine into the displayed cosh expression. Equal eigenvalues contribute a constant in s. Unequal positive eigenvalues with nonzero B_ij contribute a strictly decreasing function as s moves from 1 toward floor(n/2). The infinite sum preserves strictness: every pairwise decrement is nonnegative, at least one is strictly positive, and both sums are finite. No termwise differentiation or uniform convergence of derivatives is required.

Such an unequal-eigenvalue pair exists. If every matrix element (lambda_j-lambda_i)B_ij vanished, the bounded commutator would have zero matrix elements in a complete orthonormal basis and would be the zero operator, contradicting the kernel argument. Degenerate eigenvalues cause no obstruction to this reasoning.

Hence strict decrease holds also at the final integer step into n/2 when n is even, and into floor(n/2) when n is odd. Symmetry in s and n-s is exact. Centering changes diagonal entries but not the decisive off-diagonal commutator entries.

## 4. Hilbert–Schmidt displacement bound

For any integer s>=1, T^(s/2) is Hilbert–Schmidt because Tr(T^s)<=||T||^(s-1)Tr(T)<infinity. The other power and each B_x are bounded. The proposed X_x is therefore Hilbert–Schmidt. Its adjoint product with X_y has trace

  Tr(B_x T^s B_y T^(n-s)),

by cyclicity for the trace-class product; all factors and powers have the needed Schatten properties. Its squared norm is the corresponding same-location trace. Spatial translations are unitary, preserve H and commute with T, so that norm is the same for all translated plaquettes. Hilbert–Schmidt Cauchy–Schwarz gives |C(x,y;s)|<=C0(s) exactly.

The correlators are real because the insertions are real Wilson observables in a real positive probability measure, even though their operator expressions need not display that immediately. Thus the absolute-value bound implies the one-sided bound used later. No diagonal reflection positivity has been assumed; coordinate-axis transfer positivity is sufficient.

## 5. Geometry, centering, and axis interchange

All four plaquettes have the same (2,3) orientation and equal one-point means by translations. Therefore replacing each w by w-mu leaves F and Theta F unchanged and expresses their product as the signed sum of connected entries.

The two cross entries are same-spatial-plaquette correlations at circular distance D=2L+1. One uses coordinate 1 as time and the other coordinate 0; the coordinate permutation is an exact symmetry of the isotropic torus action and preserves the spectator orientation, so their autocorrelation functions are identical. Each cross entry is exactly C0(D).

The self distances are h_p=n-1-L-k and h_q=k-L. The given inequalities imply

  h_p,h_q>=D+1,
  n-h_p,n-h_q>=4L+3>D.

Therefore both circular self distances exceed D. Also n-D>=4L+4>D. Applying strict temporal decrease at those integer circular distances gives C0(h_p),C0(h_q)<C0(D). Their respective spatially displaced covariances are bounded above by those values. Adding yields a strict negative total, irrespective of whether either self covariance itself is positive or negative.

The minimal case L=0,n=8 is valid: k=2,3,4,5; D=1; self circular distances are at least two. The largest allowed L at each n also satisfies the same inequalities. Sources vary only from 0 to 1 in coordinates 2 and 3, so all links are nonwrapping. Their fixed 0/1 coordinates lie in the belt, attain its boundary depth L, and have strictly positive x0-x1. Reflection is antilinear, but these observables and coefficients are real and the reflection preserves their plaquette orientation.

## 6. Independent controls

`check_spectral_controls.py` uses an exact-rational positive four-dimensional diagonal transfer matrix with a degenerate positive eigenvalue, a noncommuting self-adjoint observable centered separately for each period n, and a commuting sign-unitary translation. It checks symmetry, strict temporal decrease, equality of translated autocorrelations, and the mixed displacement bound for n=8,...,44. It then checks a strict negative geometric upper bound in 2,269 admissible (L,n,k) combinations. All checks passed; results are in `CONTROL_RESULTS.txt`.

These controls help detect indexing, centering and finite-period mistakes; the infinite-dimensional justification is the analytic argument above, not the numerical samples.

## Scope and preservation

Every finite positive beta is covered without perturbation theory. Constants such as the inverse bound on A and the size of the strict decrement may deteriorate without limit as beta, volume or depth changes. The theorem supplies no uniform quantitative negative margin and does not establish a negative continuum limiting quadratic form, a continuum failure/restoration result, or a mass-gap claim. No claim of novelty has been checked. Earlier frozen proofs and the current source remain unchanged; no external service was accessed or modified for this audit.
