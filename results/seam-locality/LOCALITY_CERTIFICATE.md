# A finite-order seam-locality criterion and the failed quartic relocation route

2026-10-17. Local work only. Reference: pristine v0.7 proof at `/tmp/ym-torus-remote-audit-20261017/results/diagonal-torus-obstruction/PROOF.md`. No repository files changed. No continuum claim.

## Result in brief

The published negative quartic mechanism cannot be moved even one full coordinate layer away from the artificial 0/1 seam while retaining elementary-plaquette linear sources in the original strict half-algebra. Its entire quartic reflected covariance matrix becomes zero there. This is a theorem about the degree-four mechanism, not a theorem that all remote sources have positive reflected norm.

For general bounded interior sources there is an exact, all-orders *necessary dependency-graph criterion* for a Taylor coefficient to feel the seam. It supplies a computable finite-volume error bound against a reflection-positive cylinder. It does not supply the sign of the first allowed coefficient.

## 1. Geometry and conventions

Keep exactly T=(Z/nZ)^4, representatives 0,...,n-1, n>=8, theta swapping coordinates 0 and 1, and the half-algebra consisting of links whose endpoints obey x0>=x1. Strict half support means both endpoints obey x0>x1. Use w_p=Tr(U_p)/2 and exp(beta sum_p w_p).

Here 'L layers from the seam' means every endpoint of every source link satisfies L<=x0,x1<=n-1-L. This is a precisely declared coordinate depth; it is not distance from the diagonal mirror. Periodic spectator directions 2 and 3 are retained, and no assumption on their coordinate depths is needed. L is an integer, and the interior strict half must be nonempty.

Delete all plaquettes containing a wrapping link in direction 0 or 1. Call that set W. The retained model is a free square in directions 0/1 times a periodic spectator 2-torus; unused wrapping links have independent Haar law. Its diagonal RP follows by exactly the free-box proof: the 0/1 cut plaquettes split into paths with fixed endpoints, all spectator links on the interface have positive weights, and spectator periodicity never joins opposite strict halves. This works for every beta>=0. Let Q_T and Q_C be connected reflected forms for the full torus and this cylinder.

## 2. Exact connected-support Taylor criterion

Let F be bounded, fixed independently of beta, supported on a specified set of nonwrapping half-links. Put A=Theta F and B=F. For any action plaquette multiset p1,...,pk, create an intersection graph with vertices A,B,p1,...,pk. Join two vertices when their underlying link-variable supports intersect; repeated plaquette occurrences are separate intersecting vertices.

Define r(F) to be the minimum k for which such a graph is connected and at least one pi belongs to W. If no such graph exists set r=infinity. Using a superset of F's true support gives a valid, potentially weaker bound.

**Theorem.** Every Taylor coefficient of Q_T(beta)-Q_C(beta) of order k<r(F) is zero.

**Proof.** At product Haar measure, joint cumulants of variables split into independent groups vanish. Differentiating the log generating function gives

  [beta^k] Q_T = (1/k!) sum_(p1,...,pk in P) kappa_H(A,B,w_p1,...,w_pk).

For Q_C restrict every pi to P\W. Subtracting leaves precisely the tuples with a seam occurrence. An intersection graph which is disconnected splits functions into disjoint independent link families, so its joint cumulant is zero. All remaining tuples have k>=r(F). This proves the result. Complex A and B cause no change: use formal source parameters in the finite compact integral.

**Coordinate-depth corollary.** If the source endpoints have depth at least L, then r(F)>=L+1, hence Q_T-Q_C=O(beta^(L+1)). A path from a source vertex to a seam vertex in the connected graph uses at most k plaquette vertices. The first nonwrapping plaquette can extend the source's 0/1 coordinate range by at most one; each subsequent shared-link step can extend it by at most one. A wrapping plaquette shares only boundary-coordinate links or other wrapping links. At least L nonwrapping plaquettes, followed by a seam plaquette, are required. Reflection preserves the coordinate-depth belt.

The graph test is necessary, not sufficient. Gauge/Haar integration and cumulant cancellations can postpone the actual first nonzero term substantially. In particular no leading sign follows from graph connectivity.

## 3. Explicit finite-volume error bound

Let M=6 n^4 and rho=log(3/2)/M. For complex |z|<=rho, either model has |Z(z)-1|<=1/2 and |Z(z)|>=1/2. Each normalized moment of a bounded observable H is at most 3||H||. Thus |Q_T(z)| and |Q_C(z)| are each at most 12||F||^2; their difference is at most 24||F||^2. Cauchy's coefficient estimate and Section 2 give, for 0<=beta<rho and any integer r<=r(F),

  |Q_T(beta)-Q_C(beta)|
    <=24 ||F||^2 (beta/rho)^r / (1-beta/rho).

Consequently

  Q_T(beta) >= -24 ||F||^2 (beta/rho)^r / (1-beta/rho),

because Q_C(beta)>=0. One may use r=L+1 without computing the graph invariant. This is a rigorous finite-volume estimate; rho deteriorates as n^-4, and it is not a uniform thermodynamic or continuum boundary-stability result. For r=infinity the two analytic germs agree.

## 4. A sharper no-go for the original quartic mechanism

Take any finite linear combination F=sum_i c_i w_pi of elementary plaquettes all of whose vertices are strictly positive and at coordinate depth at least one. Centering is optional when defining Q, and no translation-invariance cancellation is needed.

The existing exact cube coefficient gives

  Cov(w_(theta pi),w_pj)= N(theta pi,pj) beta^4/1024+O_n(beta^5),

where N counts elementary cubes containing both faces; all lower mixed coefficients vanish. Distinctness holds because the two faces belong to opposite strict halves.

**Claim:** N(theta pi,pj)=0 for every i,j.

1. Any cube wrapping in direction 0 or 1 has each face touching coordinate 0 or n-1, or containing a wrapping edge. It cannot contain any depth-one source face.
2. A nonwrapping cube cannot contain both a wholly strict-positive and a wholly strict-negative plaquette face. If the cube contains at most one of directions 0/1, the range of delta=x0-x1 has width at most one, whereas having both signs requires width at least two. If it contains both 0 and 1, its delta range has width two; every face varies in at least one of those directions and therefore has delta-width at least one. A positive face would require maximum delta>=2 and a negative face minimum delta<=-2, requiring cube width at least four, contradiction. (More precisely the extrema argument uses positive integer minimum >=1 and negative integer maximum <=-1.)

Therefore Q_T(F)=O_n(beta^5), with identically zero quartic matrix. The reference coefficient -1/512 cannot survive this relocation, for any choice of coefficients or number of such interior plaquettes. This proves a sharp failure of the literal quartic construction; it does not prove RP at higher orders.

`check_quartic.py` independently enumerates all cubes for n=8,9, verifies that no nonseam cube has strict +/- faces, and recovers the original reflected cube matrix [[0,1],[1,0]]. The proof above applies to every n>=8 and does not depend on those finite checks.

## 5. Precise remaining route and recovery conditions

A natural relocated pair is p=(n-1-L,k,t,t), q=(k,L,t,t), both oriented (2,3), with L<k<n-1-L. Their reflected cross pair is separated through the seam by 2L+1 steps in one coordinate. A straight prism joining these two unit plaquettes has 4(2L+1) lateral plaquettes. This suggests a higher-order tube contribution, but it is NOT a proved leading term: one must classify all connected nonpeelable supports, repeated coupling powers, higher link incidences, and competing self-pair surfaces at that order. A single positive surface diagram does not establish the connected covariance coefficient or its sign after subtraction.

Recovery conditions for a valid negative remote-source result are:

- Prove all lower connected Taylor coefficients vanish for all four reflected pairs, rather than inspecting just one tube.
- Compute the *full* first nonzero 2x2 coefficient matrix and show a negative eigenvalue, accounting for diagonal terms and every competing wrapping/nonwrapping support.
- Control the finite-volume analytic remainder at fixed n,L; no uniformity follows automatically.
- For any fixed-physical-source/continuum assertion, additionally control L growing like physical distance divided by cutoff and the actual bare coupling/normalization. Neither the graph bound nor a fixed-order tube coefficient supplies that control.

The completed bounded obligation is the exact locality criterion, explicit finite-volume bound, and a precise certificate that the original quartic route fails after even one layer of relocation. The higher-order sign problem remains open here.
