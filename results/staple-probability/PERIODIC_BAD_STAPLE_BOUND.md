# Periodic Wilson-measure bad-staple bound by a product-ball estimate

Status: root derivation, 2026-10-17; pending independent audit. No novelty claim.

Let the finite periodic four-dimensional hypercubic lattice have side lengths at least four, normalized product SU(2) Haar measure, N_l=4V links and N_p=6V plaquettes. Set d_p=1-(1/2)ReTr U_p in [0,2], H=sum_p d_p and dmu_beta=Z_beta^{-1} exp(-beta H)dHaar. Assume beta>=1. The measure is translation invariant; directional symmetry additionally requires equal side lengths (or a direction-averaged conclusion).

## Entropy estimate

Use quaternion distance |U-I| and geodesic angle theta in [0,pi]. The Haar angle density is (2/pi)sin(theta)^2. For 0<delta<=1, sin(theta)>=2theta/pi for theta<=delta, hence the ball theta<=delta has Haar probability at least c delta^3, c=8/(3pi^3). On this ball |U-I|=2sin(theta/2)<=theta<=delta. Quaternion norm is bi-invariant and subadditive under products relative to I. If every link lies in this ball, each oriented four-link plaquette has |U_p-I|<=4delta. Therefore d_p=|U_p-I|^2/2<=8delta^2.

Independence of reference Haar measure gives

    Z_beta >= (c delta^3)^(N_l) exp(-8 beta N_p delta^2).

Relative entropy of mu_beta with respect to product Haar is

    D(mu_beta || Haar) = -beta E_beta H - log Z_beta >= 0.

Consequently

    E_beta H/N_p <= 8delta^2 + (2/(3beta))log(1/(c delta^3)).

Taking delta=(8beta)^(-1/2), which is <=1, gives the uniform energy-density estimate

    E_beta H/N_p <= [1+log(8beta)+(2/3)log(3pi^3/8)]/beta =: e(beta).

This is a finite-volume estimate uniform in all side lengths; the right side tends to zero. It uses only the elementary entropy inequality and a product set of near-identity links. It does not require gauge fixing or a mass-gap assumption.

## Consequence for staple cancellation

For an oriented link e let S_e be the sum of its six unit-quaternion staples, with orientation chosen so that the sum of the six plaquette traces involving e equals Re(U_e S_e). For every configuration,

    sum_(p contains e) d_p = 6-Re(U_e S_e) >= 6-|S_e|.

Thus on |S_e|<=h<6 the incident energy is at least 6-h. Markov's inequality yields

    P_beta(|S_e|<=h) <= E_beta[sum_(p contains e)d_p]/(6-h).

On a cubic periodic torus, lattice symmetries identify every plaquette expectation, so

    P_beta(|S_e|<=h) <= min(1, 6 e(beta)/(6-h)).

For rectangular tori without directional symmetry the same bound holds after averaging over all links: each plaquette is counted four times and 4N_p/N_l=6. No unjustified individual directional bound is asserted.

## What this does and does not supply

This proves a vanishing O(log(beta)/beta) probability of fixed-threshold unweighted staple cancellation under the fully coupled periodic Gibbs measure, uniformly in volume. It complements the worst-boundary example by showing such small-staple events need not be typical in this measure. The bound is far weaker than an exponential estimate.

It does not control changes of staple direction, correlations of bad events, a quenched supremum over boundary conditions, a spectral gap, or an averaged/block contraction theorem. It is not uniform over the seam interpolation: at s=0 the deleted crossing links may be independent Haar, and the agent's separate seam computation must be checked. No continuum Yang--Mills construction follows.
