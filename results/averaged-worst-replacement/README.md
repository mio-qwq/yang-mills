# An averaged worst-replacement obstruction

Under the fully coupled periodic cubic SU(2) Wilson measure, average the total-variation influence after taking a supremum over arbitrary replacements of one neighboring link. That expected coefficient tends to1 as beta grows, uniformly in torus volume; the eighteen-neighbor expected row sum tends to18.

AVERAGED_WORST_REPLACEMENT.md gives the full finite-volume proof and explicit constants. It combines typical near-alignment from the preceding periodic entropy estimate with an attainable one-staple rotation and elementary heat-bath concentration. The reference environment is averaged over the Gibbs law, but the replacement is still chosen adversarially.

This sharpens the earlier rare-cancellation example: rarity of small staple sums cannot rescue this particular averaged supremum criterion. It does not rule out couplings using actual random updates, block comparisons, gauge-invariant metrics, or physical mass-gap behavior. No historical novelty, continuum solution or general mixing obstruction is claimed.

The accompanying independent AI-assisted audit checks the exact source hash. There is no Lean formalization or human peer review.

Run Python3 standard-library checks:

    python check_generic_neighbor_replacement.py
    python independent_averaged_geometry_check.py
    python negative_control.py

The first two use exact finite combinatorics and rational quaternion arithmetic. They corroborate geometry and constants; the probability estimates follow from the analytic proof, not numerical simulation.

The entropy dependency is ../staple-probability/PERIODIC_BAD_STAPLE_BOUND.md, with its existing audit. The prior source/seam qualifications remain in ../../research/response-route-boundaries/.
