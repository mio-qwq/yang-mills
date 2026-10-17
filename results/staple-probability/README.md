# Finite-volume probabilities of small unweighted staple sums

Two complementary analytic results, both independently AI-audited:

1. Fully coupled periodic SU(2) Wilson measure: on cubic four-dimensional tori the probability |S_e|<=h<6 is at most min(1,6e(beta)/(6-h)), with e(beta)=[1+log(8beta)+(2/3)log(3pi^3/8)]/beta for beta>=1. On rectangular tori the stated bound is link-averaged. This follows from a product Haar-ball partition-function estimate and relative entropy.
2. Actual free-cube seam interpolation: a flat-face crossing link has six independent Haar staples at s=0. Hence P(|S_e|<=4)>=5/8; positive small-radius lower bounds persist multiplied by exp(-72s beta). Uniform rarity over every link and every interpolation parameter is false.

The results concern unweighted staple sums. They coexist because seam couplings weaken with s. They do not establish a mixing or block-contraction estimate, nonzero bulk response, continuum existence, or a mass gap. Historical novelty has not been established. General Gibbs/entropy facts are standard; no claim of a new general probability method is made.

See both proof files and independent-review.md. The periodic proof's frozen initial status line says pending audit; the accompanying hash-specific report records its completed audit without changing the reviewed source.

Run Python 3 standard-library checks:

    python check_seam_haar_geometry.py
    python independent_geometry_check.py
    python negative_geometry_test.py

Geometry assertions use exact finite combinatorics. Floating-point constant comparisons are regression checks only; the probability bounds follow from the analytic proofs. No simulation or Lean proof is claimed.
