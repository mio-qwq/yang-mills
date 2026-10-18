# Period-lattice geometry and tilted-volume compatibility

Start with [the compatibility audit](RESULT.md), [the period-lattice theorem](LATTICE-THEOREM.md), and its [independent verification](independent-verification.md). [The raw-account scope audit](RAW_PERIOD_AUDIT.md) gives pinned source locations.

The geometric result says that a period lattice preserved by a coordinate reflection and the corresponding coordinate interchange cannot give separating fixed loci for both. The relevant fixed locus is the union of all its components. This obstructs simultaneous standard geometric cut arguments, not all possible reflection-positive inequalities.

The tilted Wilson geometry has a twisted transfer trace and a useful real zero-source comparison. The inspected source statements do not already supply the complex-source comparison, full finite-volume symmetries, or local-state transfer required to replace their prescribed straight-volume family. This is a scoped compatibility analysis, not a verdict on the full construction.

These are fixed-cutoff results. No ordinary straight-periodic accessibility, source-pressure H2, continuum limit, or mass gap is proved. The independent audit is a computational-assistant research check, not human peer review or Lean verification. No novelty claim is made.

## Reproduction

From the repository root, with Python 3 and assertions enabled:

```sh
python results/tilted-volume-compatibility/check_indices.py
python results/verify_research_2026_10_18.py
```

The checker covers 32 exact two-dimensional lattice examples. Its detailed JSON output is regenerated in temporary staging and checked against the expected byte hash and case count in `../EXPECTED_OUTPUTS_2026-10-18.json`; that output is not tracked or archived. The general topological and transfer statements are written arguments, not consequences of finite enumeration. Downloaded source PDFs and raw TeX are excluded; `SOURCE_MANIFEST.json` retains pinned public source URLs and hashes.
