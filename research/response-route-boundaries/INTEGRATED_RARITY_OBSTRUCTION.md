# Why rarity alone cannot close the seam response estimate

2026-10-17. Direct corollary of the independently reviewed finite-volume seam probability bound; no claim about the actual connected response.

Let B_s={|S_e|<=h} for the flat-face crossing link, 0<h<=1, and c_h=[sqrt(2)h^3/(81pi)]^3. The proved bound P_s(B_s)>=c_h exp(-72s beta) implies, for beta>0,

    beta integral_0^1 P_s(B_s) ds >= c_h(1-exp(-72beta))/72.

Thus the beta-weighted integrated occupation of this local bad event does not tend to zero as beta tends to infinity. The same conclusion with c_h=5/8 holds at threshold h=4. This is an exact integration of a finite-volume inequality, uniform over allowed torus sizes.

It is therefore insufficient to bound a seam-response error by a constant times beta integral P_s(B_s) ds and then assert that this bound vanishes solely because the weakly coupled interval has width O(1/beta). The insertion supplies the cancelling factor beta. A lower bound on the right-hand bounding quantity does NOT imply a lower bound on the actual error or connected cumulant: cancellation, spatial separation and covariance structure can still make the physical response small.

For the fully coupled periodic measure, the root entropy estimate only gives P_beta(B)<=O(log(beta)/beta) for fixed h<6. Multiplication by beta does not itself produce a vanishing upper bound either. Stronger decorrelation or a distance-sensitive weight is needed; this is not disproved by the entropy estimate.

A sufficient abstract replacement would be a bound on the actual connected local insertion K_p(s), not only on bad-event probability. For an error sum of plaquettes, a usable uniform majorant W_p(s,a,R) must satisfy

    beta(a) sum_p integral_0^1 W_p(s,a,R(a)) ds -> 0,
    |K_p(s)| <= W_p(s,a,R(a)).

The required quantifiers include the chosen continuum/volume diagonal and the source-to-seam distance R(a). No such weak-coupling majorant is established here. The point of this note is a stop condition for the rarity-only route, not a substitute for the missing theorem.
