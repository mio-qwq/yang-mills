# Independent review: strong-coupling seam bound

## Current verdict

PASS for the frozen revised artifact, SHA-256 55703932aecdf8388a79c124e52a0f30b44688b1d57ae1e65579b24310053424, read in full after revision. The seam-response estimates (1), (2), the absolute-difference estimate (3a), and the conditional positivity corollary (3b) are mathematically sound under their now-explicit hypotheses. No blocking gap remains in this finite-volume strong-coupling result.

The initial version omitted the RP-positive-half hypothesis for its positivity corollary. The revised version fixes that omission, explicitly specifies anti-linear reflection, handles degenerate cases directly, includes periodic wrapping in its distance, and retains the actual joint-limit prefactor. The negative control recorded below explains why the hypothesis matters; it is not a counterexample to Yang–Mills theory. Attribution to standard comparison machinery is now explicit. The review below preserves the detailed audit and the reasons for each correction; its requested clarifications are satisfied in the revised artifact.

Reviewed initial SHA-256: db9262fd6c0f9d3ce652f400ba15c86a835785cc8e7abeaca472b94d62623a5d. Reviewer did not edit the source artifact.

## Proof audit

- On a periodic four-dimensional lattice of side at least four, each positive-oriented link occurs in six distinct plaquettes. Each plaquette contributes three off-diagonal incidences. Thus the symmetric matrix C_ef = beta k_ef has row sum 18 beta. Counting multiplicity, rather than distinct neighbors, is sufficient and correct.
- Changing one conditioning link changes the conditional log potential by a function of oscillation at most 4 beta k_ef. The sharp normalized-density bound TV <= tanh(osc(log ratio)/4) gives C_ef <= beta k_ef. The normalization contributes only a constant to the log ratio and does not change its oscillation.
- The random-scan coupling recurrence is valid using the original measure's influences and the tilted conditional law's discrepancy at a common exterior configuration. No influence bound for the tilted law is needed. A maximal coupling exists for the positive Haar densities, including the zero-residual convention when they coincide.
- The finite-iteration recurrence contracts with row sum 1-(1-q)/m. The stationary-limit disagreement bound is Db. Uniformly positive conditional densities and a prescribed full sweep give a genuine finite-volume Doeblin minorization. The minorization need not be uniform in volume; only convergence is used here. Bounded measurable observables are allowed, with pointwise conditional densities supplied by the bounded Gibbs potentials.
- A tilt by epsilon g has conditional TV discrepancy at most |epsilon| delta_f g / 4. Differentiation therefore gives the covariance factor 1/4. Matrix orientation agrees with the recurrence and the final row-sum estimate. The underlying C is symmetric in any case.
- The exact identity kappa(A,B,V) = Cov((A-EA)(B-EB),V) holds with centering constants fixed at the chosen interpolation parameter. There is no illegal differentiation of the centered product.
- delta_f V <= 12 beta; delta_e H <= 2M(delta_e A + delta_e B) <= 8M^2. Multiplying gives constants 3 in (2) and 24 in (1). The distance support of C^n and its row sum q^n remove the seam-area factor without dropping any source-support factor.
- Differentiating the connected quadratic form produces the third cumulant with the displayed positive sign for exp(S_rest+sV). Integrating proves the absolute response bound without any reflection-invariance assumption.

## Required positivity hypothesis and negative control

For the lower bound on Q_1, require a reflection-invariant free cube, F supported in the RP-positive half and belonging to the positive-side observable algebra of the invoked free-cube RP theorem, and Q_0 computed in the factorized free-cube measure. The reference to a seam file alone does not establish these hypotheses. Centering F preserves the positive algebra because constants belong to it.

At beta=0 choose a plaquette p and its reflected plaquette with disjoint link sets. Set X = (1/2) Tr U_p and Y = Theta X. Products of independent Haar links are Haar. The SU(2) fundamental character has Haar mean zero and squared Haar integral one, so Var(X)=Var(Y)=1/4. Their disjoint supports make them independent. For F=X-Y, Theta F=-F, and Q_0=Q_1=-Var(F)=-1/2. The seam response is exactly zero. This refutes the unrestricted lower bound while confirming that it is the RP-positive-side hypothesis, rather than the seam-response proof, that is missing. F is gauge invariant as well as bounded.

## Complex reflection

Specify Theta F = conjugate(F composed with the reflected link configuration). Anti-linearity is essential. Assuming the full interpolated measure and V are reflection-invariant, the imaginary cross cumulants cancel by reflection invariance, involutivity and cumulant symmetry. Both real diagonal contributions obey the real bound, giving 48. Seam-set invariance together with uniform bulk coupling ensures invariance of the full family. The same positive-side requirement is necessary for the complex positivity corollary. If Theta instead denotes only a linear pullback, the displayed complex identity is false: F=i u changes the sign of the quadratic form.

## Degenerate cases and geometry

- beta=0: V=0, so the third cumulant and Q_1-Q_0 vanish identically. Handle directly, rather than relying on 0^0 or 0^infinity.
- Empty seam: V=0, with the same exact conclusions. Define distance to the empty set as infinity and the tail as zero, or state the case separately.
- Empty support: both observables are constant, so centered products vanish; treat directly to avoid an undefined empty-set distance.
- r=0 is allowed. For beta>0 the geometric tail is 1/(1-q), and the estimate remains valid for supports touching the seam.
- Graph distance must be computed on the actual periodic lattice, including wrapped plaquettes. Unwrapped coordinate distance can be arbitrarily larger: links at second coordinates 0 and n-1 may be adjacent. The physical-distance consequence must use periodic geometric distance to all seam-link supports, or an explicitly proved protected interior-cube distance. Also include both F and Theta F in the source support; a far-away F alone does not imply the reflected support is far away.
- A plaquette-adjacency step moves link midpoints by at most one lattice spacing in the periodic Euclidean metric. Hence a properly defined positive physical distance supplies the claimed lower bound on r, up to harmless conventions for link versus plaquette support.

## Normalization and limits

The bound retains M_a^2 |S_a| and requires uniform q <= q_0 < 1. Polynomial growth in a^(-1) of this actual norm/support factor, together with fixed positive physical separation, is enough for vanishing error. A simultaneous volume limit also requires control of this same prefactor along the chosen diagonal; growing separation alone does not compensate for arbitrary volume-dependent normalization or support growth. The safe fully general condition is beta_a M_a^2 |S_a| q_a^(r_a)/(1-q_a) -> 0.

These estimates do not construct a continuum theory, prove convergence of renormalized observables, prove a physical mass gap, or cover asymptotic freedom. In the stated Wilson normalization asymptotic freedom has beta -> infinity, outside beta < 1/18. The manuscript appropriately says so. A coarse-grained version requires a newly verified influence bound for the induced interactions.

## Executed checks

Both the supplied incidence checker and independent_checker.py ran successfully. The independent checker covers n=4 and n=5, checks symmetric shared-plaquette multiplicities and row sum 18, verifies finite-power propagation and row sums 18^k, explicitly tests a wrapped adjacency, and checks sharp two-point attainment of the TV factor 1/4. It records the beta=0 RP negative control using exact SU(2) character moments. These are finite combinatorial/algebraic checks, not numerical evidence for a continuum theorem.
