# Remote-boundary diagonal reflection-positivity obstruction

The [frozen theorem](THEOREM.md) proves a finite-volume failure of the original coordinate-representative half-algebra at every prescribed integer coordinate depth L >= 0. For n >= max(8, 6L+5) and 3L+2 <= k <= n-3L-3, take spectator plaquettes at p=(n-1-L,k,0,0), q=(k,L,0,0), and F=w_p-w_q. All source endpoints are strictly in x0>x1 and have 0/1 seam depth L. This is not distance from the diagonal mirror.

The reflected form has leading term -2^(-(16L+9)) beta^(8L+4). With h=8L+4, c=2^(-(16L+9)), M=6n^4, r=1/(4M), and beta_star=c*r^(h+1)/48, it is at most -(c/2) beta^h < 0 for every 0 < beta <= beta_star. The interval is explicit, rational, and volume/depth dependent.

## Proof and review status

- [General-depth theorem](THEOREM.md), frozen SHA-256 `67e19b1dcd4ebe037f9ea0deba0ef43c9c983c759f04ba1b789331475fdfa626`.
- [Corrected L=1 transfer proof](TRANSFER_PROOF_V2.md), frozen SHA-256 `282792ef8a56d4cc34b66c4b9d573a776d363f4485cc79e33ca9d4b7c354a227`.
- [Fresh independent AI-assisted review](REVIEW.md) verifies V2 and the general theorem, including the rational interval endpoint.
- [Historical L=1 review](L1_REVIEW.md) identified an auxiliary overstatement: positivity near zero must be restricted to nonnegative beta. Odd winding loops give negative directions for negative beta on odd tori. V2 supersedes the original proof. The original erroneous proof is not distributed as a current proof here.

The general theorem's final paragraph requesting a separate review is historical frozen text; that review is now present above. Likewise the historical L=1 review's lack of a quantitative threshold describes the earlier L=1 scope, superseded by the general theorem's explicit interval. Reviews are AI-assisted, not human peer review or Lean formalization. Exact controls support the analytic proofs; they do not enumerate every arbitrary-order lattice integral.

## Reproduce

From this directory, run `python3 check_geometry_threshold.py`, `python3 check_controls.py`, and `python3 check_representation.py`. All use exact arithmetic and the Python standard library. The controls script rewrites CONTROL_RESULTS.txt deterministically with identical bytes. The representation script is a newly reconstructed portable control, independently deriving character coefficients and matching the preserved historical output. Commands, script hashes and full outputs appear in [VERIFICATION.md](VERIFICATION.md).

## Provenance and scope

[SOURCE_MAP.json](SOURCE_MAP.json) records original paths and frozen hashes for copied material. Absolute paths in preserved proofs/reviews are historical citations, not runtime dependencies. The historical `/tmp/ym-remote-prism-review-20261017/REVIEW.md` maps to L1_REVIEW.md here; its representation output maps to L1_representation_check.txt. The local general-L and corrected L=1 paths map to THEOREM.md and TRANSFER_PROOF_V2.md here. The [preceding seam-locality certificate](../seam-locality/README.md) and [v0.7 torus obstruction](../diagonal-torus-obstruction/README.md) provide the earlier context. Original SHA256SUMS and SOURCE_SHA256 records are retained as provenance, not portable shell manifests.

This result does not establish a continuum or fixed-physical-source obstruction, a volume-uniform fixed-coupling statement, or a mass gap. It does not refute the original continuum conjecture or the bridge's fixed compact-source hypothesis. Historical novelty has not been established.
