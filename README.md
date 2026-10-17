# Yang–Mills research

Mathematical research on four-dimensional Yang–Mills theory, with explicit proofs, executable certificates and recorded limitations.

**The Yang–Mills existence and mass-gap problem is not solved by this repository.** Current results concern local operator algebra; analytic construction, full rotational invariance and the infinite-volume mass gap remain open research goals here.

## Current results

[Dimension-six antisymmetric SU(2) operators](results/dimension-six/README.md): exact finite certificates establish quotient multiplicities **2 off shell** and **1 on shell** for hypercubic antisymmetric tensor densities modulo gauge-invariant total derivatives. The divergence ranks are **9** and **5**. This supplies an explicit rank proof for a classification already proposed in the cited reference, without assuming a general horizontal-complex exactness theorem.

The proof and executable checks passed a separate AI-assisted mathematical and computational review; see the review record in the result directory. No Lean formalization or human peer review is claimed. See the precise hypotheses and the distinction between symbolic character calculations, certified rank minors and the nonlinear SU(2) interpretation in the result directory.

[SU(N), N>=3 extension](results/su-n-dimension-six/README.md): quotient dimensions **6 off shell** and **5 on shell**, with four explicit additional symmetric-color cubic classes. Constant Cartan-valued exact solutions witness their independence modulo equations and divergences. The four added classes are charge-conjugation odd: the C-even quotient remains **2/1** for every N>=2. They are excluded from symmetry-preserving C-even rotation counterterms; see the charge-conjugation refinement in the theorem.

[Single-pole rotation rigidity](results/single-pole-rigidity/README.md): a degree-at-most-six hypercubic numerator with coordinate/diagonal reflection positivity forces isotropy away from contacts in the stated scalar Gaussian class; degree eight is sharp. Continuous spectra and interacting Yang–Mills are outside this result.

Both extensions have written proofs, separate AI-assisted mathematical reviews and exact computational checks. Historical novelty remains unverified.

[Strong-coupling seam response](results/strong-coupling-seam/README.md): an explicit uniform interpolation bound for 18β<1, with a separately reviewed heat-bath proof. This closes the seam estimate only in that controlled regime, not along the weak-coupling continuum trajectory.

[Single-link method obstruction](results/single-link-obstruction/README.md): explicit realizable boundary configurations force the actual influence row sum toward 18 at weak coupling. Weighted single-link contraction cannot repair this; it is not a mass-gap counterexample. [The staple-energy route note](research/STAPLE_ENERGY_ROUTE.md) separates a deterministic energy cost from the still-missing probability estimate.

## Reproduce

From `results/dimension-six`, with Python3:

```
python characters2.py
python independent_characters.py
python check_certificate.py
python validate_equivariance.py
```

All use the standard library. Actual outputs and SHA256 digests accompany the source. The checker rebuilds matrix entries, checks exact determinants and rejects intentionally corrupted certificates.

## Research direction

The [rotation-invariance checkpoint](research/ROTATION_ROUTE.md) separates established finite calculations from unproved analytic routes. It is not an additional theorem. The [seam-interpolation reduction](research/DIAGONAL_RP_BRIDGE.md) isolates a sufficient boundary-response estimate for diagonal two-point positivity; that estimate remains unproved.

A central reference is [Sussman–Alpöge's Yang–Mills LLM experiment](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/tree/785a68fdeef78a1da854c4807fe1f17b597d05e7). Attribution for its proposed local classification and related operator-basis literature is included with the result. Its raw manuscripts are not redistributed.

AI systems contributed substantially to proof development, programming and checking. No priority claim follows from the available literature search. Releases freeze bounded research milestones rather than imply a solution of the Millennium problem.

## Staple probability estimates

[Finite-volume proofs and independent checks](results/staple-probability/README.md) distinguish a vanishing periodic-measure bad-staple probability from a nonvanishing weakly coupled seam layer. The latter is a counterexample to uniform all-link/all-parameter rarity, not to Yang–Mills existence or a mass gap. The needed bulk-to-seam response estimate remains open.

## Response-route boundary checks

[Audited conditioning and endpoint symmetry](research/response-route-boundaries/README.md) show why frequent seam events do not imply a large connected response. The required distance-sensitive weak-coupling stability estimate remains unproved.

## Averaged worst-replacement obstruction

[Audited finite-volume proof](results/averaged-worst-replacement/README.md): even averaging the reference environment over the periodic Gibbs measure leaves worst-neighbor-replacement total-variation influence tending to1 at weak coupling. This closes that specific single-link comparison route; actual-update averages and physical mixing are not ruled out.
