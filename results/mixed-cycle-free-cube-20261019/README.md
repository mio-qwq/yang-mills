# Three-dimensional SU(2) free-cube reflection obstruction

Source-only research archive, 19 October 2026.

## Result

For the free-Haar SU(2) Wilson measure on all links and plaquettes of the cube with vertices {0,...,5}³, let p be the (1,2)-plaquette based at (3,2,2), and q the one based at (1,2,2). The off-center site reflection x₀ ↦ 4 − x₀ interchanges them. Both plaquettes are strictly interior, but the reflection does not preserve the whole cube.

The exact small-coupling expansion is

    Eβ[w_p] − Eβ[w_q] = β⁹ / 2¹⁸ + O(β¹¹).

The difference is positive throughout 0 < β ≤ 10⁻¹⁴. The explicit remainder certificate applies to the unnormalized numerator; positivity of the partition function then transfers its sign to the normalized mean difference.

On the reflection-invariant slab {0,...,4} × {0,...,5}², equipped with the marginal of the full-box measure, F = 1 + i w_p has reflected form

    Eβ[(ΘF)F] = 1 + Eβ[w_pw_q] + i(Eβ[w_p] − Eβ[w_q]).

It is nonreal, so complex reflection positivity fails for this slab marginal. This refutes the proposed exact finite-box shortcut that fitting both reflected supports inside a free box suffices. It is not a demonstrated negative real reflected form, and it does not contradict Wilson reflection positivity on reflection-invariant volumes. There is no four-dimensional, infinite-volume, continuum, or mass-gap conclusion.

## Contents and proof boundaries

- `primary/RESULT.md`: the full author-frozen readable proof and research-scope discussion.
- `audit/AUDIT.md`: independent readable mathematical audit, including the exhaustive character-label classification through total degree 10.
- `primary/check_cube_incidence.py`: exact cube/domino incidence and rational remainder checks.
- `primary/check_tube.py`: supplementary exact character-transfer checks for fixed-width tubes; these do not replace the full-cube proof.
- `audit/audit_exact.py`: independently implemented geometry, sphere, parity, and symbolic-series checks.
- Adjacent `CHECKS.json` / `CUBE_CHECKS.json`: frozen outputs of those checks.
- `SOURCE_PINS.json`: source-file SHA256 pins and provenance. `primary/SOURCE_MANIFEST.json` retains the original pinned repository URLs and Git blob identities for background/deduplication material.
- `verify.py`: optimization-resistant check runner, output comparisons, explicit geometric scope checks, and deliberately corrupted-input negative controls.
- `CHECKPOINT_VERIFICATION.json`: deterministic validation report. `SHA256SUMS` covers every other packaged file.
- `rebuild.py`: byte-deterministic ZIP builder.

The mathematical argument for exhaustiveness is a proof in the two Markdown reports. The scripts verify specified finite geometry and exact algebra; they are not a formal proof checker or an exhaustive spin-foam search. No Monte Carlo evidence is used.

The original reports are preserved byte-for-byte. The primary report's relative audit reference `../free-cube-rp-audit-20261019-1320/AUDIT.md` corresponds to `audit/AUDIT.md` here. Background repository source files referenced by `primary/SOURCE_MANIFEST.json` are intentionally not copied: they are not dependencies of this self-contained theorem or of its verification scripts. The historical assertion-only files mentioned in the audit are also intentionally omitted; only the hardened verifier is included. No older large archive is included.

## Reproduce

Tested with CPython 3.12.14 and SymPy 1.14.0. Python 3.10 or later is required by the scripts; only the independent symbolic audit requires SymPy. The exact dependency is listed in `requirements.txt`.

From this directory, with SymPy installed:

    python verify.py
    python -O verify.py
    python rebuild.py ../rebuilt.zip

The verifier checks hashes, rejects missing/unlisted files (ignoring only interpreter bytecode caches), runs every checker in normal and optimized Python, compares its JSON output to the frozen output, and runs negative controls in both modes. All check conditions use explicit exceptions, so Python optimization cannot remove them.

The rebuild uses sorted paths, a fixed archive prefix and timestamp, fixed Unix file modes, no comments, and ZIP_STORED (no compressor-version dependence). The archive contains only inventory-listed files plus `SHA256SUMS`. Rebuilding from an unchanged extracted package yields identical bytes. The ZIP is unsigned; SHA256 pins detect corruption or change but are not an authenticity signature.

## Additive source archive verification

This directory contains exactly the original ZIP, README.md, SHA256SUMS and
VERIFICATION.json. Check the outer SHA256SUMS before extraction. All source file
paths discussed above refer to paths inside the ZIP. VERIFICATION.json records
the frozen checkpoint, fresh clean full replay in normal and optimized Python,
byte-identical deterministic rebuilding, and agreement with an additional root
replay of the primary certificate. No prior source or archive is replaced.
No PR, merge, tag or release is created by this source archival operation.
Local-only provenance in the frozen package describes preparation before this
commit. Hash pins detect changes and are not authenticity signatures.
