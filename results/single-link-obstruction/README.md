# Actual obstruction to single-link Dobrushin contraction

For the four-dimensional SU(2) Wilson model, every one of a link's 18 plaquette-sharing neighbors has conditional total-variation influence at least max(0,1-6 exp(-β/2)). The actual row sum tends to 18 as β grows, and no positive coordinate weights restore this single-link contraction criterion once the proved lower bound exceeds one.

This strengthens the diagnosis that the earlier sufficient strong-coupling estimate does not reach β tending to infinity: the worst-boundary single-link method itself fails. It does not refute a physical mass gap or rule out block, averaged or typical-background methods.

PROOF.md and separate AI-assisted REVIEW.md state all hypotheses, orientation and essential-supremum conventions. No human review, formalization or novelty claim. Run Python3 standard-library checks:

    python check_staple_geometry.py
    python independent_staple_checker.py

These exact checks test realizability and orientation. The proof supplies the general asymptotic assertion.
