# Root derivation: why the worst-boundary obstruction does not settle typical response

For a target link U in SU(2), write its six oriented staples as unit quaternions V_j. Put S=sum_j V_j and identify SU(2) with unit quaternions. The six incident normalized Wilson terms sum to the real inner product of U with S (up to conjugating S according to orientation). Hence

max_U sum_j (1/2) Re Tr(U V_j) = |S|.

The local action deficit relative to six identity plaquettes therefore satisfies

sum_j (1 - (1/2) Re Tr(U V_j)) >= 6 - |S|,

with equality after aligning U with S when S is nonzero. The checked large-influence construction has S=+I or -I, so its incident action deficit is at least 5, and the local Boltzmann penalty relative to a fully aligned six-plaquette configuration is exp(-5 beta).

This is a deterministic energy comparison, NOT a probability estimate for the bad boundary event. Conditional on that boundary, the link law is normalized and the comparison does not reduce its influence. In the full Gibbs measure, changing the boundary to make all staples align also changes neighboring plaquettes and the partition function. Therefore no inequality P(bad staples)<=exp(-5 beta) follows from this calculation alone.

The meaningful next requirement is a quantitative distributional estimate on low-staple-magnitude/rough boundary regions along the seam interpolation, with entropy, compatibility and source normalization included. Such an estimate could support an averaged or block comparison even though worst-boundary single-link Dobrushin contraction is impossible. It is not supplied by the current proof.

A further warning: worst-case influence can also use small orientation changes of a large staple sum. At large beta the conditional width shrinks, so small boundary changes may separate the conditional laws without requiring |S| near zero. A successful averaged comparison must control the whole kernel, not only the cancellation example. No general weak-coupling bound is proved here.

This note was derived directly by the root researcher as a route analysis. It is not a new historical claim, a mass-gap result, or a bound on event probabilities.
