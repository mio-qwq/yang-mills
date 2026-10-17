# Verification record

All three commands in README.md were run from this portable package on 17 October 2026 and exited zero. Their unedited stdout is recorded in discovery-check.txt, independent-check.txt, and haar-check.txt.

- Discovery: 625 root-neighbor choices; zero five-face cores; four six-face cores, all cube boundaries.
- Independent enumeration: six root orientations, 625 choices each, four cube cores per orientation; witness matrix [[0,1],[1,0]], quadratic coefficient -1/512.
- Independent exact Haar calculation: normalized cube-face product 1/1024 using 32,768 samples.

The root Haar checker SHA256 is c2ce40a8f10e60442767b6d8d5c50111f4492cf5f35b486d86758e8ade81ce68, unchanged from the independently supplied source. The proof was copied with only its obsolete workspace-status sentence removed. The independent audit and all three programs are otherwise byte-identical to the reviewed source artifacts. Reviews are AI-assisted, not human peer review or Lean/formal verification. Numerical display of -1/512 is exact in binary; the written audit supplies the rational derivation and explicit beta range.
