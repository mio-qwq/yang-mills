# Exact local operator certificates for four-dimensional SU(2)

This research packet proves a bounded local-algebra statement: the multiplicity of the antisymmetric hypercubic representation in engineering-dimension-six pure SU(2) gauge-invariant densities, modulo gauge-invariant total derivatives, is **2 off shell** and **1 on shell**. The divergence ranks are **9** and **5**, respectively.

The dimensions were already proposed in Sussman–Alpöge's reference material. The contribution here is an explicit finite rank certificate replacing its unprovided character computation and general exactness assumption. The packet does not prove Yang–Mills existence, rotational invariance of its continuum limit, or a mass gap.

## Verification

Python 3 standard library only, from this directory:

```
python characters2.py
python independent_characters.py
python check_certificate.py
python validate_equivariance.py
```

The two character implementations use equivalent but separately implemented jet formulas. The determinant checker reconstructs entries from wave parameters and uses integer Bareiss elimination, unlike the generator's modular elimination. Corrupted entries and zero determinant claims are rejected. The last check independently verifies the parity/stabilizer transformation of every stored tensor candidate.

`divergence.py` regenerates the two JSON certificates. Exact modular minors prove characteristic-zero lower bounds; representation dimensions and independent curls prove matching upper bounds. See `PROOF.md` for the semantic bridge to nonlinear SU(2) jets, including on-shell jet surjectivity.

## Sources and limitations

Reference snapshot: [Yang--Mills-LLM-experiment, commit 785a68f](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/tree/785a68fdeef78a1da854c4807fe1f17b597d05e7), raw companion III, proposition `10.1:prop-antisymmetric-channel`, approximately lines 78191–78335. The 153-page manuscript is conditional and explicitly does not claim the mass gap. Its broader analytic assumptions have not been discharged here.

Related methodology includes [Husung's opbasis](https://nikolai-husung.github.io/opbasis/), [Henning et al.](https://arxiv.org/abs/1706.08520), and [Lüscher–Weisz](https://doi.org/10.1007/BF01206178). No historical-priority claim is made. Upstream manuscripts are referenced, not redistributed.

AI systems made substantial contributions to derivation, code and checking. The lead assistant independently reran the checks and implemented the second character calculation and tensor-equivariance check. A separate AI-assisted mathematical and computational review resumed after an interruption and passed; it regenerated the certificates byte-for-byte and checked the nonlinear jet and on-shell interpretation. See `REVIEW.md`. There is no Lean formalization or human peer review in this packet.
