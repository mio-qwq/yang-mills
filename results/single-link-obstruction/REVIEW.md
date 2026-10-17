# Independent review: actual single-link influence obstruction

## Verdict

Final mathematical PASS for the exact source SHA-256 c3822dc3c05538b315b555118b441cbed932fb5a6a5a129cccf45146a0ad0b02. This hash was reverified and both checker programs were rerun successfully on 2026-10-17 at 05:12 UTC. The source is unchanged from the version read in full during the initial audit. This approval is tied to those exact bytes; any later revision requires checking its changes. No blocking gap found. This result rules out the specified worst-case single-link total-variation Dobrushin contraction at sufficiently large Wilson beta. It is not a counterexample to a physical mass gap, does not disprove a continuum Yang–Mills theory, and does not exclude alternative comparison or multiscale methods.

## Geometry and global realizability

For a target link in direction mu, the six adjacent plaquettes give paths through plus/minus each of the other three directions. For n>=4 all 18 links in those paths are distinct. In particular each staple has a private parallel link and none of its transverse links occurs in another target staple. Translation and coordinate permutation extend the origin calculation to every target link. Periodic wrapping is included in both the explicit construction and the checkers.

Setting transverse links to I lets each staple attain any prescribed SU(2) holonomy through its private parallel link, with inversion when orientation requires it. The five values I,I,-I,W,W^2 sum to zero because W+W^2=-I. The selected sixth staple is I. Replacing any of its three links by its negative changes that staple to -I, including when the link is traversed inversely, since -I is central. No other target staple changes.

These are actual assignments to global link variables, not arbitrary assignments to plaquette holonomies. Other plaquettes automatically take whatever values the link assignment imposes. Changes to plaquettes not containing the target link contribute only constants to that target's conditional log density and cancel under normalization. There is no neglected Bianchi constraint or incompatibility between the six assigned staples.

The conditional laws are therefore exactly proportional to exp(plus/minus beta t(U)), with t=(1/2)ReTr U and equal normalizers. Each influence coefficient has its own optimizing pair; the supremum definition does not require one boundary to optimize all 18 entries at once.

## Haar integral, total variation, and threshold

Normalized SU(2) Haar is uniform measure on S^3 in quaternion coordinates, so t has density (2/pi)sqrt(1-t^2). Its cap probability is p=P(t>=1/2)=1/3-sqrt(3)/(4pi), approximately 0.195501109478, strictly greater than 1/6.

The two conditional densities cross at t=0. Consequently TV=1-2 mu_plus(t<=0). The numerator of mu_plus(t<=0) is at most 1/2; its denominator is at least p exp(beta/2). Thus TV>=1-p^(-1)exp(-beta/2)>=1-6exp(-beta/2), and taking the positive part is valid.

At beta=4, L=1-6exp(-2) is approximately 0.187988300580. Thus 6L is approximately 1.12792980348 and 18L is approximately 3.38378941045, both strictly above one. The elementary sixth-order exponential-series argument in the source proves the strict threshold without relying on floating-point checks. All neighboring influences are at least L and at most one; nonneighbor influences are exactly zero by locality. Hence every row sum converges to 18 as beta tends to infinity.

At every finite beta the Gibbs density is positive and continuous on the full compact configuration space. Conditional densities are continuous in their outside coordinates in total variation. Therefore the constructed influence values can be approximated on positive-measure neighborhoods in the common conditioning variables and the two possible values of the changed coordinate. The same lower bound applies to the customary essential-supremum definition. The fact that the exact displayed configuration itself has measure zero is not a loophole.

## Weighted contraction and interpretation

For arbitrary positive coordinate weights, choose a minimum-weight target link. Each of its 18 neighboring weights is at least its own, so its weighted row sum is at least 18L. This directly excludes any weighted sup-norm contraction with the same matrix when 18L>1. Equivalently, entrywise domination of L times the 18-regular adjacency matrix gives spectral radius at least 18L. No symmetry assumption on the actual influence matrix is needed.

The construction concerns the uniform-coupling periodic endpoint. It is therefore enough to rule out a criterion required to hold uniformly throughout the whole seam interpolation. It does not assert the same lower bound at a deleted-interaction endpoint, and the source does not need such a claim.

The source appropriately distinguishes failure of a worst-case comparison method from failure of the desired physical statement. Typical-background estimates, gauge-invariant blocks, other metrics, and genuinely multiscale arguments are not excluded. Any beta threshold is normalization-specific; the source states the normalized-trace convention explicitly.

## Independent checks executed

The supplied check_staple_geometry.py passes for n=4,5,6,8. It checks geometry and exact diagonal sixth-root arithmetic for all 18 possible flipped neighbors.

The separate independent_staple_checker.py passes for n=4 and n=5. It constructs oriented plaquette loops and actual global link assignments, tests both signs for all 18 neighbors, and evaluates the conditional potential at 15 independently chosen noncommuting SU(2) target-link probes. This confirms that the total incident-plaquette potential is exactly plus/minus t(U), up to numerical roundoff, including plaquettes in which the target link originally occurs inversely. It also checks the cap probability and threshold margins.

The algebraic proof, not those finite computations, establishes the result for all n>=4 and beta>=4. No source file was edited during this review.
