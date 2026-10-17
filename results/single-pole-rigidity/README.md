# Low-degree single-pole rotation rigidity

For d>=3, a hypercubic scalar Gaussian covariance P(p)/(p²+m²), with m>0 and deg(P)<=6, which is reflection positive across a coordinate and a diagonal mirror is rotationally invariant away from contact terms. Degree8 admits an explicit anisotropic reflection-positive example.

This is a restricted rational-covariance theorem, not a statement about arbitrary interacting Yang–Mills limits. The constant free-field coefficient can be zero. See PROOF.md for exact positivity, distributional and contact-term conventions.

`REVIEW.md` records a separate AI-assisted mathematical review. `check_algebra.py` verifies the polynomial reductions and sign witnesses using exact SymPy arithmetic, including four negative controls. It does not verify the analytical proof in a proof assistant. Run:

```
python check_algebra.py
```

The tested SymPy version is pinned in requirements.txt; actual output is in VERIFICATION.txt. No human peer review, historical priority or Millennium-problem solution is claimed.
