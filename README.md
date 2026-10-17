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

## Quartic seam-endpoint cancellation

[Exact forest/gauge argument and audit](results/seam-forest-cancellation/README.md): normalized interior expectations have no first-, second- or third-order seam response. The fourth-order term still contains the missing source-to-boundary covariance, so no new distance estimate is claimed.

## Finite-torus half-algebra qualification

[Diagonal torus obstruction](results/diagonal-torus-obstruction/README.md) records a negative small-coupling reflected form for the coordinate-swap half x0>x1 in representatives 0,...,n-1. This precise seam-dependent finite-geometry result is not a counterexample to every torus half-algebra or to the bridge’s fixed compact sources, and has no continuum reflection-positivity or mass-gap conclusion.

## Boundary-depth checkpoint

[Finite-volume seam locality](results/seam-locality/README.md) shows why the quartic elementary-plaquette obstruction disappears after one full coordinate layer and gives a necessary connected-support criterion with a finite-volume Cauchy bound.

[Remote-boundary obstruction](results/remote-boundary-obstruction/README.md) proves failure of the original representative-half diagonal form at every prescribed integer 0/1 seam depth L >= 0, for n >= max(8,6L+5) and suitable k. Its leading term is -2^(-(16L+9)) beta^(8L+4), with an explicit rational small-positive-beta negativity interval. Frozen proofs, separate AI-assisted reviews, and portable exact controls accompany both results. The corrected L=1 proof supersedes an earlier negative-beta positivity overstatement.

These are finite-volume microscopic results; neither fixed-physical-source continuum failure nor a mass gap nor a refutation of the original continuum conjecture is claimed. No human peer review, Lean formalization, or established novelty is claimed.

## All-positive-coupling sign and limit boundaries

[All-beta finite-torus sign](results/diagonal-allbeta/README.md) extends the prescribed-depth representative-half obstruction to every finite beta>0, without a uniform negative margin. [Limit and boundary qualifications](results/diagonal-limit-boundaries/README.md) show unrescaled weak-coupling disappearance and a fixed-compact-support obstruction, and record the known free-boundary diagonal reflection-positivity mechanism. The periodic/free limit comparison remains open; no continuum or mass-gap resolution follows.
