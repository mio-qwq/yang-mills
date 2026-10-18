# Fixed-cutoff translation-invariant diagonal-RP Wilson Gibbs states

This research note proves existence of a translation-invariant, gauge-invariant SU(2) Wilson DLR state with reflection positivity at every integer plane parallel to x_0=x_1, for d>=2 and every finite nonnegative Wilson coupling. The lattice cutoff is fixed.

Start with [the complete proof](construction/RESULT.md). Two constructions are given: tilted periodic quotients and finite-width cylinders with an explicit one-dimensional uniqueness proof. Independent proof audits are in [the cylinder audit](independent-audit/RESULT.md) and [the tilted-torus audit](independent-audit/TILTED_TORUS_ADDENDUM.md).

The local labels used in these notes are H1 for this existence premise and H2 for differentiability at zero of the homogeneous-source pressure in the selected first-moment and reflected-product directions. They are not the identically named numbered hypotheses in the separately audited manuscript.

No identification with a cluster state of prescribed ordinary straight-periodic volumes is proved. H2 remains unproved. There is no continuum-limit, full-dimensional uniqueness, correlation-decay, or mass-gap conclusion. The independent audits are computational-assistant research checks, not human peer review or Lean verification. No novelty claim is made.

## Reproduction

From the repository root, using Python 3 without optimization (`-O`):

```sh
python results/invariant-diagonal-rp/construction/check_geometry.py
python results/invariant-diagonal-rp/construction/check_tilted_torus.py
python results/invariant-diagonal-rp/independent-audit/check_tilted_torus.py
python results/invariant-diagonal-rp/additional-check/check_geometry.py
python results/verify_research_2026_10_18.py
```

The first two checkers write their JSON results beside their scripts. The latter two print JSON. The aggregate verifier runs all checks in a fresh temporary staging directory, compares full generated output hashes and case counts with `../EXPECTED_OUTPUTS_2026-10-18.json`, validates publication hashes, and confirms rejection of deliberately false finite-geometry assertions. Detailed output JSON files are intentionally untracked and excluded from the archive. These finite checks supplement the written proofs; they do not mechanically verify the analytic arguments.
