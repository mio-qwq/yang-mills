# Conditional centering and finite-box reflection positivity

Local source-only research checkpoint, 19 October 2026.

## Results and exact scope

primary/RESULT.md derives Q(F)=-E[(a-b)^2]/4 for F=X-(a+b)/2 under
conditionally independent half-kernels. The certified three-dimensional finite
free cube and its small-beta mean mismatch yield a bounded real gauge-invariant
negative witness. Mixing the matched-slab marginal with its reflected image keeps
the negative form and centers F conditionally on the fixed-plane links.

A constructive refinement truncates the conditional beta-Taylor centering at
order 24. Its total link-matrix-entry polynomial degree is at most 24, using the
exact one-plane-link-per-half-plaquette count. At each fixed 0<beta<=10^(-14),
the normalized exactly centered polynomial witness has norm at most 1 and form
at most -beta^18/2^46. Its coefficient recursion is specified; the large full
coefficient list is not expanded, and the observable remains beta dependent.

The witness uses the CLOSED positive-half algebra and may depend on all 60
plane links, including transverse-boundary links. The reflected mixture is not the
homogeneous free-slab Wilson measure. This is not a fixed-support arbitrary-depth
obstruction, an all-beta four-dimensional result, or a continuum mass-gap result.

The later boundary-distance comparison is a routine consequence of the recovered
strong-coupling comparison argument, with q=6(d-1) beta<1 (q=18 beta in four
dimensions). It does not provide weak-coupling or all-beta control. The sufficient
condition retains actual norm, support and seam-distance factors.

## Proof and audit map

- primary/: the conditional-centering result and its exact rational/geometric checker.
- audit/: independent geometry, conditioning and centering audit. Its stated audit
  scope is primary/RESULT.md Sections 1–5 including the degree-24 Taylor
  refinement, plus separate geometry/Taylor exact checkers. Later comparison corollaries must not be
  described as independently audited by this report.
- dependency/prior_RESULT.md and prior_AUDIT.md: the complete earlier small-beta
  SU(2) coefficient and remainder argument. dependency/prior_audit_exact.py and
  PRIOR_CHECKS.json replay its 858 explicit checks and both negative controls.
- dependency/strong-coupling-seam-PROOF.md: recovered self-contained comparison proof,
  pinned to commit 4ff17ed90aa40a453129d1d0b9cea0bf483c949a and Git blob
  1a5d84389251c62c7f02cad04fec0d047f37e9db. Its essential incidence constants are
  independently enumerated by the new checker; no prior archive binary is required.
- review/ROOT_REVIEW.md: dated root review. primary/SOURCE_MANIFEST.json records
  historical source references; only necessary proof dependencies are bundled.

The checker does not numerically integrate SU(2) or evaluate unknown conditional
functions. Finite geometry and rational checks supplement the proofs. A common
all-beta/weak-coupling local comparison theorem for reflected cores remains open.
Recovery beyond strong coupling needs an actual verified comparison modulus,
including source normalization and growing support, or a justified blocked model;
failure of q<1 alone does not prove comparison false. The finite-width all-beta
argument is not automatically uniform as transverse width grows.

## Offline verification and deterministic rebuilding

The archive contains UTF-8 source, proofs, exact JSON certificates and verification
scripts only. It contains no nested archives, cached environments, binaries or bytecode.
Use Python 3.12.14, SymPy 1.14.0 and mpmath 1.3.0 for the frozen byte-exact replay.
Dependencies are pinned in requirements.txt; they are not vendored or automatically installed.
The runtime used is recorded in RUNTIME.json. Only Python's standard library and
SymPy/mpmath are needed; no network access is used by the scripts.

From the extracted package directory:

    python -I -B verify_bundle.py
    python -I -B -O verify_bundle.py
    python -I -B rebuild_archive.py ../rebuilt.zip

The verifier checks every file hash and the exact inventory, copies each checker to
a clean temporary directory, and runs every positive replay in BOTH normal and -O
mode. Each generated certificate must equal its frozen JSON byte for byte. It also
checks scientific negative controls and deliberate inventory corruptions. Python
assert statements are not used for verification. No frozen source is modified.
The expected aggregate output is EXPECTED_REPLAY.json. Different software versions
can legitimately change textual symbolic output, so a mismatch requires review.

The rebuild uses lexicographically sorted paths, a fixed 2026-10-19 00:00:00 ZIP
timestamp, fixed Unix regular-file mode 0644 and DEFLATE level 9. Byte-identical
rebuilds were verified after fresh extraction with the recorded Python/zlib runtime.
Output must be outside the extracted package. MANIFEST.json inventories all files
except itself and SHA256SUMS; SHA256SUMS additionally pins MANIFEST.json. The outer
completion manifest pins the ZIP and the internal manifest. Hashes detect altered
bytes; they are not authenticity signatures or mathematical proofs.

## Provenance and recovery

SOURCE_PINS.json maps exact copied files to their frozen local research sources.
The root-review note is an earlier dated snapshot; its then-pending freeze language
is historical. This completed package supplies the later verification evidence.
References in preserved reports to their original sibling folders are provenance;
the bundled mapping below identifies the included dependencies. Current and historical audit receipts are preserved in audit/, including the
initial assertion-based checker, which is never used as current verification.
Optimized duplicates outside that audit record, runtime caches and exploratory
scratch probes are omitted.

If a hash, exact replay, negative-control rejection or deterministic rebuild fails,
retain the failing evidence and suspend the affected claim/package. Restore the
pinned source snapshot or investigate the discrepancy before issuing a replacement.
Do not treat near-zero numerical output as an exact certificate. These checks are
computer-assisted exact algebra/enumeration, not proof-assistant certification or
external peer review. This local checkpoint performs no external publication.

## Outer payload

This directory contains exactly the original source ZIP, this README.md,
VERIFICATION.json and SHA256SUMS. Check the outer hashes before extracting.
VERIFICATION.json records clean exact normal/optimized replays, rejection tests,
root-certificate agreement and byte-identical deterministic rebuilds.
This is the frozen local payload; preparation alone does not publish or merge it.
