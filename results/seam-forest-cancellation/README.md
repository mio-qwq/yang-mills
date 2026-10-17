# Exact quartic onset of the interior seam response

Exterior integration makes a product of seam traces constant in the selected internal links whenever their distinct-edge graph is a forest. The induced cube has girth4. Along with exterior-center symmetry this cancels the first three orders in normalized bounded interior expectations: the first possible change is order(s beta)^4.

PROOF.md includes the exact normalized covariance identity, finite-volume remainder and fourth-order coefficient. The independent review accepts the final source including the corrected real-part qualification on an ordered reflection bound.

This is an endpoint diagnostic. Its bound contains the number of seam plaquettes and provides no source-distance decay or uniform control up to s=1. It does not establish BRP, an infrared estimate or the Yang–Mills mass gap. No historical novelty or Lean proof is claimed.

Run:

    python check_seam_forest_geometry.py
    python check_cycle_negative_control.py

The second checker uses exact Q8 cubature for a degree-two-in-each-quaternion polynomial. Here its first/second moments agree exactly with SU(2) Haar, so this is an exact integral check, not replacement of the theory by a finite gauge group. The capped-cycle insertion shows why the forest hypothesis matters; it is not a full finite-beta marginal computation.
