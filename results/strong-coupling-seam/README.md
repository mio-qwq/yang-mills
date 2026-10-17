# Uniform seam response at strong coupling

For finite four-dimensional SU(2) Wilson lattices with q=18β<1, the mixed third cumulant controlling the free-to-periodic seam interpolation is bounded by 24β‖F‖∞²|S|q^r/(1−q) for real bounded F, and by twice that for complex F. The bound is uniform over the interpolation and volume. A positivity lower-bound corollary additionally requires the positive-half free-cube reflection-positivity hypotheses.

See PROOF.md for all assumptions, zero cases and distance conventions. The proof derives a finite heat-bath comparison bound and explicitly credits standard Dobrushin–Föllmer theory; no historical novelty is claimed. This is a controlled-regime application, not a continuum Yang–Mills construction or mass-gap result: β→∞ is outside the regime.

Separate AI-assisted review in REVIEW.md detected and led to correction of a missing positive-half hypothesis. Its counterexample is a negative test of the original draft, not a counterexample to Yang–Mills. Neither human review nor Lean verification is claimed.

Run Python3 standard-library checks:

    python check_link_influences.py
    python independent_checker.py

These validate incidence, propagation and comparison constants; the analytical proof supplies the all-volume theorem. The earlier analytic target is [the seam bridge](../../research/DIAGONAL_RP_BRIDGE.md).
