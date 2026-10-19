# Independent audit: variable-degree spectral extension

19 October 2026. Local mathematical review only. No remote object was changed.

## Verdict

**No substantive mathematical gap found in the audited version.** The theorem is valid under its explicit scalar polynomial-at-each-mass representation, positive locally finite reference measure, finite-stage distributional convergence modulo local contacts, reflection positivity, and the local signed-residue hypothesis. The weaker late-time hypothesis in Section 3.1 also suffices. These are conditional spectral-class conclusions, not a verification of the class for Yang–Mills theory.

Audited source: `/workspace/shared/spectral-degree-boundary-20261019/RESULT.md`, 394 lines.

SHA-256: `ed545ccfe361554df699ec44f01746542927957fbffc85a773b77d676368461a`

The review checked the complete argument, concentrating independently on integration, exceptional sets, topology, local order, and Examples 8.1–8.3. It is an analytic audit, not a computer-assisted formal proof.

## 1. Finite-stage construction and topology

- Bounded mass, bounded degree and integrable coefficient norm on each stage imply integrability of all divided-polynomial and residue coefficients. The multiplier bound by a constant times `(1+|p|)^d/q(p)` is locally integrable in four dimensions and has polynomial growth.
- Polynomial counterterms are origin-supported after inverse Fourier transformation and vanish on every separated reflected correlation test before taking any limit. No convergence of the separate contact series is used.
- Compact-positive-time, tangential-Schwartz tests belong to Schwartz space. Tangential spatial cutoffs approximate them in that topology, preserving a common strictly positive time lower bound. Their correlation tests are Schwartz. Thus both the covariance pairing and the finite-stage identities extend as stated, and the RP inequality passes to the limit.
- Assumption E requires the specified increasing exhaustion to converge in `S'` after its stated local counterterms. The automatic existence of finite coefficient/degree stages alone does not imply this convergence. The source distinguishes these facts correctly; it does not interchange arbitrary cutoff prescriptions.

## 2. Signed-measure extraction and exceptional sets

R gives an absolutely dominated spectral formula on each compact frequency region away from zero. RP then implies nonnegativity of each locally integrable `Q_h` almost everywhere by smooth frequency localization; continuity of `Q_h` is unnecessary.

The time-test family is genuinely countable: finitely many selected delta-approximation bumps, rational real and imaginary coefficients, and countably many approximation indices suffice. After intersecting the resulting full-measure sets and the rational-damping variation sets, each retained momentum has all required inequalities and all required integrability bounds. The delta limit uses one fixed exponential majorant, and extension to arbitrary finite coefficient vectors is finite-dimensional continuity.

The polynomial-square argument is valid. Exponential damping gives a finite signed Borel measure; its pushforward under `x=exp(-omega)` is a finite measure on a compact interval with no newly introduced atom at zero. Uniform approximation of square roots of nonnegative continuous functions proves positivity. Both energy transformations are injective with Borel inverse on their images, so positivity pulls back to the original mass density.

The last change of exceptional-set order is justified by Tonelli on the measurable negative-residue set. Local finiteness makes the reference mass measure sigma-finite. Polynomial continuity then upgrades almost-everywhere tangential positivity to every tangential momentum, including zero. The finite number of representative mirrors creates only a finite union of mass-null sets. There is no uncountable intersection.

## 3. Late-time weakening and recovery of early times

Section 3.1 is correct as written. On `K_l={1/l<=|k|<=l}`, choose `t_l>a_l/2+1`. Bumps of half-width below `1/2` then have squared transforms dominated by a constant times `exp(-a_l omega)`. Localization is performed on the interiors of these annuli, which cover every nonzero momentum. A countable family on each annulus and then a countable union over annuli gives the required common almost-everywhere statement.

Only the single variation bound at `a_l` is needed to make `exp(-2t_l omega) nu_k` finite and run the same polynomial-square proof. Earlier-time absolute convergence is not presumed.

After positivity is established, the original complete finite-stage integrals increase. Monotone convergence plus E therefore identifies their limit with the finite covariance pairing for every compact test, and also for compact-positive-time/tangential-Schwartz tests. This recovers all frequencies and all masses directly, including the massless case. It does not claim that cutoffs excluding zero converge in Schwartz topology.

The a posteriori recovery of R is also valid: take a smooth frequency cutoff equal to one on the desired compact set and a nonzero nonnegative time bump supported below `a/2`. Its Laplace transform is bounded below by its mass times `exp(-a omega/2)`. The finite positive full formula bounds precisely the desired `exp(-a omega)` residue integral. Thus R and R_late are equivalent once the other theorem hypotheses have supplied positivity and global recovery, although R_late is a weaker standalone assumption.

## 4. Quotient degrees, scaling and local order

Finite algebraic quotient operations on countably many degree strata preserve coefficient measurability. The highest canonical quotient part cannot be divisible by `q`. Evenness in the normal variable ensures that an identically zero null-cone residue would force precisely that forbidden divisibility. The top residue is therefore a nonzero homogeneous polynomial of the same degree, and it is nonnegative by scaling the full positive residue.

The fixed-mass scaling dominator is integrable, including at zero in three tangential dimensions. Its constant may depend on mass because this dominated-convergence step occurs before mass integration. The common nonnegative profile has a nonzero transform near zero, which gives a strictly positive leading coefficient at every nonzero quotient mass. No uniform cone or coefficient lower bound is needed. Countability of finite degrees and Fatou then give the asserted stratum lower bound; masswise cancellation cannot defeat it.

For local distribution order `m`, the correlation scales as `psi_d=d^4 psi(./d)`, so the common compact-support order estimate is `O(d^(4-m))`. Combining it with a degree-D stratum's `d^(6-D)` lower bound gives exactly `D<=m+2`. This conclusion does not use UV. For each fixed d the correlation vanishes near the origin, so contacts still pair to zero even though the separation shrinks. A single fixed compact neighborhood supplies the order estimate. Anisotropic contacts can enlarge an order bound but cannot invalidate the argument.

The degree-eight threshold, UV contradiction, and closure of origin-supported distributions under distributional limits give the stated rotation conclusion modulo contacts. The proof does not assert complete distributional rotational invariance.

## 5. Boundary examples

### 8.1

`H_j=4^(-j)Q_4^j` has coefficient norm one. All coefficients are nonnegative, so `P_(j^2)` has norm exactly `j^2+5`, and its numerator degree is `4j+2`. Stagewise subtraction leaves the convergent positive radial multiplier sum. Residues are one. The total spectral weight is finite and the scaled reflected kernels are uniformly bounded after removing `d^6`, proving the stated `O(d^6)` behavior. This is a valid nonempty example of unbounded contact-representative degrees.

### 8.2

`16^(-j)Q_4^(2j)` has coefficient norm one and degree `8j`. At the coordinate mirror its residue is at least `16^(-j)j^(8j)`. On a fixed annulus the weighted terms are bounded below by a positive constant times `j^(8j)exp(-aj)/(32^j j)`, so they fail even to tend to zero. A nonzero nonnegative time bump and a nonnegative even spatial bump with Fourier transform positive on a sufficiently small annulus produce divergent positive reflected pairings. Contacts cannot alter these pairings. This rules out the required distributional convergence, not merely one attempted subtraction prescription.

### 8.3

An explicit bound verifies the stated gamma-integral estimate. For any considered mirror, with `omega=sqrt(|k|^2+j^2)`,

`|Q_4(i omega n+k)| <= (omega^2+|k|^2)^2 <= 4 omega^4`,

and therefore `0<=R_n(k,j^2)<=omega^(8j)`. If a test has time support above `delta>0`, its per-mass form is bounded by

`C_g Gamma(8j+2)/(2delta)^(8j+2)`.

Indeed radial integration followed by the energy substitution bounds the integral by a constant times `integral_0^infinity omega^(8j+1)exp(-2delta omega) d omega`. Its logarithm is `O(j log j)`, so weighting by `exp(-j^3)` makes the sum finite. R follows similarly, or directly on compact annuli.

Every atom still has genuine quotient degree `8j`. Any distributional extension through coincidence would have finite order on a compact neighborhood; positivity and the original finite-stage identities would give the same full reflected forms there. One sufficiently large fixed j then contradicts that order bound. Thus the failure of a local extension is established independently of any uniform asymptotic in j.

## Remaining boundary

The audit finds no repair needed. The substantive remaining assumptions are the masswise finite-polynomial scalar ansatz, identifiable signed-measure Laplace representation, and genuine local distributional extension E. Infinite-degree fixed-mass numerators, merely conditional spectral sums without an appropriate inversion argument, and actual interacting/tensor field applicability remain outside the result. Publication would still warrant ordinary external mathematical review.
