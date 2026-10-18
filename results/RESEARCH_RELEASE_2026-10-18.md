# Fixed-cutoff Wilson geometry and scoped pressure implications

Research notes dated 18 October 2026:

1. [Invariant diagonal reflection positivity](invariant-diagonal-rp/README.md): two existence constructions for a translation-invariant, gauge-invariant SU(2) Wilson DLR state at each fixed finite nonnegative coupling.
2. [Tilted-volume compatibility](tilted-volume-compatibility/README.md): a period-lattice separating-cut obstruction, an exact twisted-transfer comparison, and a pinned-source compatibility audit.
3. [Source-pressure scope](source-pressure-scope/README.md): a supplementary implication audit, an exact cosh obstruction to an abstract analytic-pressure inference, and a conditional zero-free-disk criterion.

The scope is fixed cutoff. These notes do not prove accessibility from the prescribed ordinary straight-periodic volume family, unconditional source-pressure differentiability H2, a continuum limit, or a mass gap. The audits are computational-assistant research checks, not human peer review or Lean verification. No novelty claim is made.

## Provenance and verification

The original research archives remain frozen. `PROVENANCE_2026-10-18.json` records their hashes, included file mappings, prepublication hashes, and the restricted publication changes. Mathematical arguments and original checkers are preserved; edits only remove nonpublication editorial wording, replace absolute paths with relative references, or update publication metadata. Downloaded raw source/PDFs, verbatim excerpt files, and regenerable detailed geometry-output JSON files are excluded. `EXPECTED_OUTPUTS_2026-10-18.json` stores only expected full-output SHA-256 values, case counts, and generator locations.

From the repository root, run:

```sh
python results/verify_research_2026_10_18.py
```

Use Python 3 without `-O`. The verifier checks `SHA256_2026-10-18.json`, runs the five original checkers in clean temporary staging, compares the full generated output byte hashes and case counts against that compact summary, and tests negative controls. Finite combinatorial checks do not replace the general analytic or topological proofs. `VERIFICATION_2026-10-18.json` records the publication run.
