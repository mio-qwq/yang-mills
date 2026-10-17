# Independent review: exact separator identities and rarity-route limits

## Verdict

PASS, tied to these exact source hashes:

- separator-route-stop.md: 8152201ce5fcd3733f4fe7c49ef1eb3788fd8da57655233cc6be7d4f515d5b31
- INTEGRATED_RARITY_OBSTRUCTION.md: 51a9121e8a4be8b00111f99b4339f4c3b6869876b0cda715012ab32b9d0b92dd

No blocking gap found. These are exact finite-volume reductions, a symmetry cancellation, and carefully delimited statements about an insufficient bounding strategy. They establish no new distance-sensitive estimate or continuum result. Neither source was edited or published during review.

## Separator identities

The explicit condition that no plaquette contain both an I link and an O link suffices: conditioned on all links in Gamma, product Haar and the Gibbs density split into separate I and O factors. Mere pictorial separation without this interaction-graph condition would not suffice, but the manuscript states the needed condition.

Since H_s=(A-E_s A)(B-E_s B) is measurable on I union Gamma and V on O union Gamma, their conditional covariance vanishes. The law of total covariance yields Cov(H_s,V)=Cov(E[H_s|Gamma],E[V|Gamma]). Expanding E[H_s|Gamma] into the conditional covariance of A,B plus the product of their conditional means gives equation (2) exactly. The unconditional means are constants at the chosen s, so centering creates no additional random variables or derivative terms.

The interior conditional operator is independent of s precisely under the stated exclusion of seam-coupled plaquettes from those depending on I. The displayed oscillation inequality follows by expanding H_s and using the triangle inequality. The marginal score identity follows by differentiating the finite-volume marginal density. None of these identities supplies a strict contraction or a source-distance gain. The manuscript correctly stops at that missing estimate rather than assuming one.

## Exterior-center symmetry

For the induced vertex cube C={1,...,n-1}^4, a plaquette's internal vertices form a Cartesian product in its two varying directions (or are absent due to a fixed exterior coordinate). Therefore the possibilities are four vertices, two adjacent vertices, one vertex, or none. Their numbers of internal links are respectively 4,1,0,0. In particular every mixed plaquette has exactly three exterior links.

Multiplying every exterior link by the central SU(2) element -I preserves product Haar. It multiplies a plaquette trace by (-1) to the number of its exterior links, including inversely traversed links. Hence only mixed plaquette terms change sign; both interior-only and exterior-only terms are unchanged. This is an actual globally defined link transformation and respects all induced plaquette identities.

Integrating over exterior links with fixed interior links therefore produces the same interior density at s and -s, with equal normalization. All bounded interior expectations are even in s. The finite-volume dependence is real analytic, so all odd derivatives at zero vanish. In particular Q_s is even and its derivative kappa_s at zero vanishes provided both F and Theta F depend only on interior links. This is the support hypothesis established in section 1 and is automatic when the reflection preserves the chosen cube. Merely saying F is interior without preservation or without interior reflected support would not be sufficient in a different geometry.

The alternative conditional identity E_0[V|interior]=0 is also correct: the exterior s=0 measure is invariant under this sign transformation and V is odd. These observations require no reflection positivity at negative s and provide no uniform bound on higher Taylor coefficients.

## Integrated rarity interpretation

Integrating c_h exp(-72s beta) gives exactly

beta integral_0^1 P_s(B) ds >= c_h(1-exp(-72beta))/72.

At beta=0 the weighted integral is zero and the same limiting formula is consistent. At beta tending to infinity its lower bound tends to c_h/72>0; threshold 4 uses c_h=5/8. Thus the proposed probability-only bounding quantity does not vanish merely because the parameter layer narrows. This is not a lower bound on the actual error, connected cumulant, or physical response. The source explicitly preserves that distinction.

Likewise the periodic O(log(beta)/beta) upper bound, when multiplied by beta, is not itself a vanishing upper bound. It does not prove that the actual beta-weighted probability stays large. The abstract majorant criterion correctly includes the sum over seam plaquettes, parameter integral, beta factor, chosen cutoff/volume diagonal, and source distance. It is presented as a missing sufficient estimate rather than a theorem already obtained.

## Checks

The author's parity checker passed periodic sides 4,6,8. An independent enumeration checked sides 4,5,6 and verified both the internal-edge counts {0,1,4} and the resulting transformation sign for every plaquette. The proof covers all permitted lattice sizes; the checks are corroborative only. Source hashes were verified before and after review.
