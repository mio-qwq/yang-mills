# Strong-coupling collar/block source checkpoint

19 October 2026. This additive source archive records a scoped Yang–Mills research checkpoint. The separate arbitrary-collar comparison requires a common high-temperature buffer and uses `18 beta < 1`. The actual elementary signed-diagonal Gaussian factors have disjoint two-link support, giving the local block comparison under `22 beta < 1` in four dimensions. The two hypotheses must not be conflated.

For the actual Gaussian blocks, with a fixed bounded physical test supported on a deterministic set `S_F`, the tested marginal total variation is bounded by `epsilon = min(1, |S_F| q^r/(1-q))`, where `q = 22 beta < 1`. The finite-half expectation mismatch is at most `2 ||F|| epsilon`, uniformly in the Gaussian values. Complete padded halves retain all bounded ordinary physical tail plaquettes; arbitrary multiblock collar or terminal interactions are not part of this special block theorem. The distance is to differing ordinary factors. The proof gives `r >= max(0, L - |k| - R)` along isotropic free cubes and the stated common-exhaustion reflection-positivity consequence.

This is an explicit strong-coupling conditional-Gaussian comparison. It does not establish an all-coupling result, a weak-bare-coupling limit, a continuum construction, full Euclidean rotational invariance, or a Yang–Mills mass gap. It does not make a Millennium-problem solution, historical-priority, human-peer-review, or formal-verification claim. Independent AI-assisted proof audits and finite executable certificates have the scope stated in the enclosed documents.

## Files

- `ym-strong-coupling-collar-block.zip`: complete minimal source checkpoint, including both comparison proofs, the arbitrary-collar obstruction and its scope, independent reviews and checkers, minimal prior gluing/strip/seam documents, frozen expected outputs, portable replay, deterministic rebuild, provenance and an inner SHA-256 manifest.
- `VERIFICATION.json`: clean-extraction replay and deterministic rebuild evidence, the parent snapshot, and the archive digest.
- `SHA256SUMS`: outer SHA-256 manifest for these three files.

The archive has 29 files, including its own manifest. It is 78,474 bytes and has SHA-256 `f7e638427c7861d6dc20b86e43e8b1b8e56bd7b877761e013298f64fbd01d236`.

## Reproduce

First run `sha256sum -c SHA256SUMS` here. Extract the ZIP into an empty directory. In the extracted `ym-strong-coupling-collar-block` directory run:

```
python replay.py --receipt ../replay-receipt.json
python -O rebuild.py ../rebuilt.zip
```

The replay runs five checkers in normal and optimized Python, compares full outputs, checks ten intended fault rejections, and verifies all payload hashes before and after execution. CPython 3.12.14 and NumPy 2.3.5 were used. Only `comparison/check_collar.py` requires NumPy. The finite hypergraph checks use explicitly bounded floating-point tolerances; the geometric and obstruction checks use exact integer/rational arithmetic. These finite checks supplement the written analytic arguments.

The rebuild output is outside the extracted payload and must not already exist. Its byte-identical digest must equal the archive digest above. Existing source wording, original local-path provenance and historical status phrases inside the frozen ZIP have been preserved; they describe source snapshots, not additional current publication actions.

## Additive archive scope

This checkpoint is based on `research-posterior-strip-20261019` at commit `266c1ee15da7e0e497431f19fab603162eb3c8aa` (tree `2c15362ef1b235c306dff2188bc6d7291e7af1e8`). Its intended placement is a new research branch with only this new directory added; every existing blob and ref is preserved. No PR, merge, tag or release is included in this archival action. The existing parent tree has no GitHub Actions workflow; local replay evidence must not be described as passing remote CI.
