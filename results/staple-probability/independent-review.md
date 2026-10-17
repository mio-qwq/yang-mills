# Independent review: seam-layer and periodic bad-staple probabilities

## Verdict and exact versions

PASS for both scoped finite-volume results:

- Seam source: seam-layer-bad-staple-counterexample.md, SHA-256 9c93b65a66884f688cd42697a980001a65175dbff0688ed9e49f59524ea8895f. The author confirmed this version is frozen.
- Periodic source: PERIODIC_BAD_STAPLE_BOUND.md, SHA-256 a686ae8cec03e9712f3e6c93e61b4f48692a3b71b0abddc92dd8674c45d0249a.

No blocking mathematical gap was found. Neither result proves or disproves a physical mass gap or the required bulk-to-seam covariance estimate. Their distinction between the fully coupled periodic measure and the weakly coupled seam layer is essential.

## Seam geometry

In centered coordinates on side 2N, N>=3, the cube excludes the coordinate layer -N. A positive link from N-1 to -N crosses its flat boundary. Each private parallel link displaced by plus/minus one transverse unit also crosses that boundary. The two-step margin ensures that every plaquette touching any private link contains an internal transverse edge at normal coordinate N-1 and an exterior transverse edge at -N. Thus all these plaquettes are genuinely mixed and their coefficients are s beta.

There are six private links, each with six incident plaquettes. The 36 incident plaquettes are distinct here, although the upper bound 36 alone suffices. The target's six three-link paths are pairwise link-disjoint and each contains exactly one private link. The same assertions hold for the other face orientations by symmetry. Periodic wrapping is accounted for; there is no hidden open-boundary approximation.

At s=0 the Gibbs density does not depend at all on the six private links. Consequently they are independent Haar variables independent of every outside link. Conditional on all outside links, each staple is a fixed left/right translate of a private link or its inverse. Its joint conditional law is therefore product Haar and is independent of the outside configuration. This correctly establishes unconditional independent Haar staples despite interactions among the remaining lattice links.

## Seam probability constants

For independent unit Haar quaternions H_i, E H_i=0 and E|sum H_i|^2=6. Markov at radius 4 gives P(|S|<=4)>=1-6/16=5/8. The strict/non-strict threshold convention creates no issue.

For a quaternion chord ball of radius delta<=sqrt(2), its Haar probability is (2/pi) integral_0^(delta^2/2) sqrt(2u-u^2) du. Since sqrt(2u-u^2)>=sqrt(u) on [0,1], this is at least sqrt(2) delta^3/(3pi). Pairing three independent opposite pairs within delta=h/3 ensures |S|<=h and gives [sqrt(2)h^3/(81pi)]^3. The stated h<=1 safely satisfies the ball restriction; at h=1 the constant is approximately 1.716e-7.

For s>0, conditioning on all outside links leaves at most 36 incident seam terms, each bounded in [-s beta,s beta]. Their summed log-potential has oscillation at most 72s beta. The normalized block density is pointwise at least exp(-72s beta) relative to product Haar. Multiplying this by the conditional Haar event probability and integrating over the outside law is valid. No global partition-function comparison or independence under the interacting law is assumed.

The estimates remain valid at beta=0 and s=0 directly. For fixed b, restricting s beta<=b gives a beta-independent positive lower bound. Here “order one” means nonvanishing as beta grows with b,h fixed; it does not imply a large numerical probability for the conservative small-h bound.

## Seam interpretation and limitations

These statements concern the unweighted staple sum S. All target incident couplings equal s beta, so the dimensionless weighted staple sum is sS, or the full conditional field is beta sS depending on convention. At s=0 the actual conditional field is exactly zero. At s beta=O(1), the crossing link is locally weakly coupled; it is not an example of cancellation of six uniformly strong incident interactions.

Thus a bound tending to zero uniformly over every link and every interpolation parameter is impossible. This does not rule out a bound for links or blocks a positive distance inside the bulk, where couplings remain beta, or an estimate that explicitly treats the seam separately. Nor does it establish a nonzero density of bad blocks in a large-volume spatial average: the displayed construction is localized at the boundary.

The layer has parameter width O(1/beta), and the seam insertion carries beta, so width alone cannot certify a small integrated response. Equally, this argument supplies no lower bound on the connected source-to-seam cumulant. A bulk observable and its reflected support can remain far from the seam, and correlations connecting them to these locally disordered links may decay or cancel. The manuscript makes this limitation explicit. Boundary localization or a direct source-to-layer response estimate remains a viable requirement for a future approach; no general averaged/block method is ruled out.

## Periodic energy estimate

For beta>=1, use the geodesic Haar ball theta<=delta<=1. Haar angle density is (2/pi)sin^2(theta), and sin(theta)>=2theta/pi yields ball mass at least c delta^3 with c=8/(3pi^3). Quaternion chord distance is at most theta. Product telescoping and norm invariance give |U_p-I|<=4delta for any four-link oriented plaquette, hence d_p=|U_p-I|^2/2<=8delta^2.

The product-ball event gives Z>= (c delta^3)^(N_l) exp(-8 beta N_p delta^2). Relative entropy has the correct sign: D(mu_beta||Haar)=-beta E H-log Z>=0, hence E H<=-log Z/beta. Since N_l/N_p=2/3, this yields E H/N_p<=8delta^2+(2/(3beta))log(1/(c delta^3)). Taking delta^2=1/(8beta) gives exactly e(beta)=[1+log(8beta)+(2/3)log(3pi^3/8)]/beta. Constants and normalization check out. The estimate is uniform in finite volume and does not require gauge fixing.

Configurationwise, sum of incident plaquette deficits equals 6-Re(U_e S_e)>=6-|S_e|. Thus the event |S_e|<=h<6 costs at least 6-h incident deficit. Markov gives the stated probability estimate. On a cubic torus, translations and coordinate permutations identify plaquette expectations, giving the individual-link upper bound 6e(beta)/(6-h), capped at one. For rectangular tori, summing over links counts each plaquette four times and 4N_p/N_l=6, proving the same link-averaged bound. The source correctly avoids an unjustified individual directional estimate on rectangular tori.

This establishes fixed-threshold unweighted cancellation probability O(log(beta)/beta) in the fully coupled periodic measure. It does not bound directional sensitivity, conditional worst cases, bad-event correlations, weighted covariances, spectral gaps, or a contraction coefficient. In particular it does not negate the separate worst-case influence obstruction or the seam-layer lower bound.

## Checks executed

The author's seam checker passed sides 6,8,10. The separate independent_geometry_check.py uses centered coordinates and checked all eight face orientations on sides 6 and 8, including mixed classification, 36 distinct incident plaquettes, and 18 disjoint staple links. It also checks the small-h numerical constant and the periodic entropy-bound algebra at several beta values. These checks supplement the analytic proofs; they are not continuum evidence. Neither source artifact was edited.
