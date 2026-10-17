# Independent audit: averaged worst-single-neighbor replacement

## Verdict and binding versions

PASS, with no blocking mathematical gap found, for the finite-volume claim and its stated scope.

Audited source: `AVERAGED_WORST_REPLACEMENT.md`

SHA-256: `41c3698b820a3905bd7fbbc444d44421c8b89a4078b472e86881999ee6d33586`

Dependency: `../staple-probability/PERIODIC_BAD_STAPLE_BOUND.md`

SHA-256: `a686ae8cec03e9712f3e6c93e61b4f48692a3b71b0abddc92dd8674c45d0249a`

Earlier audit: `../staple-probability/independent-review.md`

SHA-256: `142405b3a0a708b44f53d80ba3142490fe2aab7ecbe471de3903aad6f4072332`

The conclusion is that averaging the reference environment does not make the supremum-over-arbitrary-replacement TV influence small: its expectation tends to one, uniformly over the specified cubic volumes. It does not concern a replacement drawn from the actual Gibbs update, nor establish failure of physical mixing, a spectral-gap statement, or any mass-gap conclusion.

## Conditional density and orientation

Choose the six staples as oriented three-link paths from the endpoint of target link e back to its starting point. With S their quaternion sum, the incident normalized traces sum to Re(U_e S). The conditional density with respect to normalized Haar is therefore proportional to exp(beta Re(U_e S)). If a=|S|>0 and v=S/a, then Re(U_e S)=a <U_e, conjugate(v)> in Euclidean R^4. Thus the actual maximizing center is conjugate(v), rather than v under this particular orientation convention. Quaternion conjugation is a fixed orthogonal map, independent of the environment, so it preserves both center separations and cap probabilities. The source explicitly allows this convention and uses no false orientation-dependent conclusion. The conditional remains smooth as a function of the unnormalized S even at S=0.

## Independent cap estimate and constants

For chord radius d<=sqrt(2), the Haar cap probability on S^3 equals

(2/pi) integral from 0 to d^2/2 of sqrt(2u-u^2) du.

On this interval u<=1, sqrt(2u-u^2)>=sqrt(u). Integration gives at least sqrt(2)d^3/(3pi). Setting d=r/2 yields sqrt(2)r^3/(24pi), as claimed. The hypothesis r<=1 is more than sufficient.

For a density proportional to exp(beta a <U,v>), the integrand on the radius r/2 cap is at least exp(beta a(1-r^2/8)); on the complement of the radius r cap it is at most exp(beta a(1-r^2/2)). Since Haar has total mass one, comparison gives the asserted tail bound

24pi/(sqrt(2)r^3) exp(-3 beta a r^2/8).

At r=1/12 and a>=3, the prefactor is exactly 41472pi/sqrt(2), and the exponent is at most -beta/128. For centers farther apart than 2r, take one of the caps as the TV witness: the first measure assigns it at least 1-epsilon, and the second at most epsilon because it lies outside the second cap. Hence normalized TV is at least 1-2epsilon. Negative lower bounds at moderate beta cause no logical problem.

## Local geometry, arbitrary replacement, and separation

On a cubic torus with side L>=4, write e=(x,mu). For each transverse direction nu and sign s, the staple is the path from x+mu with steps s nu, -mu, -s nu. These six paths have distinct parallel middle links based at x+s nu; their remaining links run in distinct transverse directions or have bases differing in the mu coordinate or the sign of the nu displacement. For L>=4 none of these base-coordinate differences is zero modulo L. Thus the 18 unoriented stored links are distinct, and none equals e. Each belongs to exactly one target staple. The six closed loops obtained by prepending e are precisely its six incident elementary plaquettes. The hypothesis L>=4 safely excludes small-period identifications.

With every other conditioning link fixed, any occurrence of f in a staple is A g B or A g^{-1} B, with A,B unit quaternions fixed. To obtain desired unit quaternion w, take g=A^{-1}wB^{-1} in the first case and g=(A^{-1}wB^{-1})^{-1} in the second. These are elements of SU(2). Changes to other plaquettes involving f are irrelevant: the definition permits arbitrary replacement of a conditioning coordinate, without requiring that it be likely or energetically favorable under its own conditional law.

On G, a>=1199/200=5.995. Since sum |V_i-v|^2=12-2a<=1/100, each |V_i-v|<=1/10. For any unit w perpendicular to v, write V_i=c v+z with z perpendicular to v. Then 0.9<=c<=1, |z|<=0.1, and

S'=(a-c)v+(w-z).

Its parallel component is positive (indeed at least 4.995) and at most 5.1, while its perpendicular component is at least 0.9. Also |S'|>=a-|V_i|-|w|=a-2>=3.995>3. Thus the angle theta lies in (0,pi/2) and tan(theta)>=0.9/5.1=3/17. It follows that cos(theta)<=17/sqrt(298), and the squared chord distance of the centers is at least 2-34/sqrt(298).

The strict comparison with 1/36 is analytic, not numerical: 2-34/sqrt(298)>1/36 is equivalent, by multiplication and squaring positive quantities, to 71^2*298>1224^2. The integer difference is exactly 4042. The center distance consequently exceeds 1/6=2r. Both conditional concentrations have a>=3, so the same error epsilon applies before and after replacement.

## Measurability

For each fixed finite volume and beta, the conditional density is a continuous function of the conditioning configuration, replacement g, and target U. Its normalizer is strictly positive. Compactness gives uniform continuity, and integrating the absolute density difference shows that the normalized TV distance is continuous in (eta,g). Maximization over compact SU(2) therefore yields a continuous, in particular measurable, coefficient c_ef(eta). There is no need for a measurable choice of an optimizing replacement, because the pointwise witness only lower-bounds this well-defined supremum. If desired, a measurable perpendicular witness can even be taken as w=v i, with i a fixed unit imaginary quaternion; real inner product <v,vi>=0.

## Energy dependency and typicality of G

I independently rechecked the dependency algebra. The product geodesic ball with radius delta has Haar mass at least c delta^3 per link, c=8/(3pi^3). On that product event, a plaquette has chord distance at most 4delta from identity, hence energy deficit at most 8delta^2. Therefore Z>= (c delta^3)^{N_l} exp(-8 beta N_p delta^2). Nonnegative relative entropy gives E H<=-log Z/beta, with the sign as used in the source. Since N_l/N_p=2/3, choosing delta^2=1/(8beta) proves exactly the displayed e(beta) for beta>=1.

Equal torus side lengths and homogeneous couplings make all elementary plaquette expectations equal by translations and coordinate symmetries; reversal does not affect the SU(2) real trace. Thus each incident plaquette has expected deficit at most e(beta). Pointwise their sum is 6-Re(U_e S)>=6-|S|. On G-complement, |S|<6-1/200, so the incident deficit exceeds 1/200. Markov gives P(G-complement)<=200*6e(beta)=1200e(beta). G depends solely on the conditioning links eta, even though the auxiliary energy contains U_e; integrating over the full Gibbs measure is exactly the desired conditioning-marginal probability.

The stated good-event bound may be negative at moderate beta, but is still a valid lower bound. No claim of positivity at all beta is needed.

## Averaging, uniformity, and scope

Pointwise one may write c_ef>=1_G-2epsilon: on G this is the cap bound, and off G it follows from c_ef>=0. Consequently

E c_ef >= 1-1200e(beta)-2C exp(-beta/128),

and nonnegativity supplies the maximum with zero. This argument avoids any issue with multiplying a possibly negative intermediate lower bound by a possibly negative estimate of P(G).

Every constant is independent of L, target e, and its selected neighbor f. Together with c_ef<=1 and e(beta)->0, this proves uniform convergence to one over cubic L>=4, as well as convergence of the expected 18-term row sum to 18. No independence among the 18 coefficients is required. Cubicity is used for an individual-direction plaquette expectation; rectangular extensions should not simply inherit this step without a separate bound or averaging argument.

The meaningful obstruction is specifically to a criterion requiring this averaged worst-replacement row sum to be below one. Averaging over actual replacement laws, a different metric, blocks, or physical long-distance correlations is a different mathematical quantity. The proof correctly makes no inference about those alternatives.

## Exact checker

The independent script `independent_averaged_geometry_check.py` verifies the source hash; enumerates every target link for L=4,5,6; constructs staple paths independently; compares them against independently enumerated incident plaquettes; and checks all 18 occurrences are private to their staple. It passed all 1024, 2500, and 5184 target links respectively. It also checks rational quaternion replacement constructions and all rational/integer constants exactly. These finite checks supplement the general analytic arguments above and are not used as proof of an inequality via floating-point approximations. No audited source was edited.

The final portable checker resolves its proof input with `Path(__file__).with_name('AVERAGED_WORST_REPLACEMENT.md')`; place the unchanged proof beside it and run with Python 3. The checker was rerun successfully after this portability change. Its frozen SHA-256 is `613a096c9e7e537ea550aa6b80f889c6f64cfa4b538e953fe8fc2ce7f342ebd0`.
