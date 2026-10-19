# Fiber/angular source archive checkpoint

Source-only additive research snapshot, 19 October 2026. Existing repository
files and earlier archive bytes are preserved. No release, merge, tag or PR is
part of this checkpoint. Historical statements inside unchanged source ZIPs
about their local-only status describe the time they were prepared, not the
current location of this copy. Original local paths in provenance manifests
are historical identifiers; the portable commands below use only included files.

## Scoped results

- Finite-harmonic continuous ellipsoid mixtures: in the stated scalar class,
  reflection positivity at one invariant mirror forces a finite even angular
  density to be constant; the nonnegative constant converse is radial RP.
- Positive infinite-angular axial examples: for b,tau>0 and 0<beta<1, the
  smooth normalized nonconstant ACG density yields one-mirror RP. beta=1 is
  radial. This disproves dropping finite harmonic degree in that one-mirror
  setting; it does not settle the W4 coordinate/diagonal-mirror question.

The new positive-family ZIP contains only the accepted theorem, positive-only
audit, root review, frozen exact checkers and receipts, plus documented copy
clarifications. Broader beta>1 classification manuscripts and numerical search
caches are excluded. Five auxiliary identities remain in the unchanged checker
only to preserve exact regression receipts, without claiming a beta>1 theorem.
Archive bytes are not also duplicated as expanded source files.

Requires Python 3.10+ and SymPy; the finite-harmonic archive itself uses only the
standard library. This is scalar two-point/Gaussian mathematics, not an interacting
Yang-Mills construction or a proof of existence or mass gap.

## Extracted proof map

Each ZIP extracts to the directory of the same name without .zip:

- ym-continuation-20261019/continuous-ellipsoid-mixtures-20261019/RESULT.md,
  AUDIT.md and ROOT_REVIEW.md in the same module. The self-contained stronger
  one-mirror theorem is in RESULT.md Section 6.
- ym-positive-infinite-angular-20261019/RESULT.md, AUDIT_POSITIVE.md and
  ROOT_REVIEW.md. COPY_EDITS.json records the two documented wording edits.

## Reproduce and verify integrity

From this directory, run:

    python verify_archives.py
    python -O verify_archives.py

The wrapper verifies this directory's manifest, all ZIP hashes, safe member paths,
CRC, sorted paths and fixed metadata, clean-extracts each source archive, checks
its internal SHA256SUMS, and runs every entrypoint under both ordinary Python and
-O. Source trees are checked again afterward and temporary copies are discarded.
Inner wrappers replay exact certificates, the indicated C++ exhaustive checks,
and negative controls. The stored REPRODUCTION.json is the fresh clean-extraction
receipt from preparing this snapshot. No network or solver is used.

SHA256SUMS covers every other file in this directory. ARCHIVES.json records exact
sizes, hashes, entrypoints and the pinned single parent. Finite computation and
AI-assisted reviews complement written arguments; neither human peer review,
historical originality nor proof-assistant formal verification is claimed.
