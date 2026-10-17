# Yang–Mills research

Mathematical research on four-dimensional Yang–Mills theory, with explicit proofs, executable certificates and recorded limitations.

**The Yang–Mills existence and mass-gap problem is not solved by this repository.** Current results concern local operator algebra; analytic construction, full rotational invariance and the infinite-volume mass gap remain open research goals here.

## Current result

[Dimension-six antisymmetric SU(2) operators](results/dimension-six/README.md): exact finite certificates establish quotient multiplicities **2 off shell** and **1 on shell** for hypercubic antisymmetric tensor densities modulo gauge-invariant total derivatives. The divergence ranks are **9** and **5**. This supplies an explicit rank proof for a classification already proposed in the cited reference, without assuming a general horizontal-complex exactness theorem.

The proof and executable checks passed a separate AI-assisted mathematical and computational review; see the review record in the result directory. No Lean formalization or human peer review is claimed. See the precise hypotheses and the distinction between symbolic character calculations, certified rank minors and the nonlinear SU(2) interpretation in the result directory.

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

The [rotation-invariance checkpoint](research/ROTATION_ROUTE.md) separates established finite calculations from unproved analytic routes. It is not an additional theorem.

A central reference is [Sussman–Alpöge's Yang–Mills LLM experiment](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/tree/785a68fdeef78a1da854c4807fe1f17b597d05e7). Attribution for its proposed local classification and related operator-basis literature is included with the result. Its raw manuscripts are not redistributed.

AI systems contributed substantially to proof development, programming and checking. No priority claim follows from the available literature search. Releases freeze bounded research milestones rather than imply a solution of the Millennium problem.
