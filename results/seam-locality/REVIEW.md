# Independent review of the finite-volume seam-locality certificate

Date: 2026-10-17. Verdict: **PASS within its expressly finite-volume, finite-order scope.** No substantive mathematical correction found. This review does not establish a remote-source negative coefficient, all-orders RP, continuum control, or a mass gap.

## Inputs and preservation

Reviewed the complete `LOCALITY_CERTIFICATE.md`, its `check_quartic.py`, and the frozen `PROOF.md` dependency named in the task. Exact paths and initial SHA-256 digests are in `SOURCE_SHA256.txt`. No source was changed. The supplied checker was inspected before execution; the independent checker uses only Python's standard library and imports no source-project code.

## Analytic findings

1. **Connected coefficient identity is correct.** For a fixed bounded observable F, take A=Theta F and B=F as fixed random variables, even at complex coupling. The two-source derivative of log of the finite-volume generating integral is E(AB)-E(A)E(B). Its kth beta derivative at zero is the joint cumulant with k action insertions. Expanding the action sum gives exactly the ordered tuple sum divided by k!. Restricting action indices to retained plaquettes computes the cylinder on the same product-Haar probability space, so subtraction leaves precisely tuples with a removed plaquette. Disconnected link-intersection graphs give independent blocks and hence zero cumulants. Complex conjugation is already part of the fixed random variable A; one must not conjugate the complex coupling. The certificate uses the correct convention.

2. **Arbitrary source unions are allowed.** A and B may each depend on many disconnected link subsets. Treating each whole observable as one vertex permits artificial connections inside that vertex and therefore can underestimate the necessary order, but cannot invalidate vanishing below the bound. The graph test remains necessary rather than sufficient. Using an explicit superset of support is likewise safe and weaker. Constants or observables with empty true support produce no covariance obstruction.

3. **The depth index is L+1, not L.** Assign to a nonwrapping link the minimum coordinate depth among both endpoints in directions 0 and 1. Two links of a retained plaquette have depths differing by at most one. Every nonwrapping link shared with a seam plaquette has depth zero; a retained plaquette cannot share a wrapping link with it. Starting with depth at least L therefore requires at least L retained plaquette steps before the final seam plaquette, hence at least L+1 action vertices. In a graph path that visits another source vertex, start instead from the last source vertex before the first seam vertex: all its links still have depth at least L. Reflection preserves depth. Thus agreement includes order L, and the first possibly different order is L+1. This is coordinate depth, not mirror distance.

4. **The periodic-spectator cylinder is RP.** After deleting plaquettes containing direction-0 or direction-1 wrapping links, the active geometry is a free square times a periodic spectator two-torus. Spectator links preserve x0-x1, including at their own periodic seams, and never connect strict opposite halves. Retained links in directions 0 and 1 change that integer by one, so cannot jump across the interface. The only retained plaquettes with both positive and negative vertices are (0,1) squares based at (k,k), with two mirror-fixed opposite vertices. Their two half-paths yield the character positive-kernel decomposition in the frozen proof. Interface spectator plaquettes merely give a positive conditional weight. Unused wrapping variables integrate out of the stipulated nonwrapping source functions. Continuous-source RP extends to bounded measurable sources by L2 approximation in this finite compact model. Centering uses a constant in the same half-algebra and yields connected positivity for real beta >= 0.

5. **Conjugation and centering are consistent.** For F=sum c_i w_pi, Q(F)=sum conjugate(c_i)c_j Cov(w_theta(pi),w_pj). Opposite strict halves ensure the two faces are distinct, allowing the frozen mixed-coupling covariance formula. The vanishing quartic matrix therefore holds for arbitrary complex coefficients and arbitrary finite numbers of source plaquettes. Q is connected by definition; optional centering does not claim that the uncentered norm has the same low-order expansion. Reflection invariance ensures Q is real on real coupling, so the final lower bound is meaningful.

6. **All cube geometries satisfy the exclusion.** A cube wrapping in direction 0 or 1 has every face either containing the relevant wrapping direction or fixed on coordinate 0 or n-1. It has no depth-one face. This includes cubes wrapping in both coordinates and cubes also wrapping in a spectator direction. A cube not wrapping in directions 0 or 1 has delta=x0-x1 width at most one if it uses at most one of these axes, ruling out strictly opposite-sign faces. If it uses both, the total width is two, but each two-dimensional face varies in at least one of these axes. A wholly positive face forces maximum delta >= 2 and a wholly negative face forces minimum delta <= -2, impossible in that cube. Spectator wrapping cannot change this argument. The frozen degree-six log-Z lemma then yields a zero quartic reflected covariance matrix, with all lower mixed terms zero and fixed-volume remainder O(beta^5).

7. **Cauchy estimate and constants check.** M=6n^4 bounds the action's absolute value in both models, including the cylinder with fewer terms. With rho=log(3/2)/M, |Z(z)-1|<=exp(rho M)-1=1/2 on the closed disk. Each normalized moment is <=3 times the observable norm. Each connected form is bounded by (3+9)||F||^2=12||F||^2; their difference is bounded by 24||F||^2. Analyticity on a neighborhood of this closed disk and the coefficient cancellations give the stated geometric tail for 0<=beta<rho and nonnegative integer r<=r(F). The useful application r=L+1 is positive. If r(F)=infinity, all Taylor coefficients agree, so the germs agree. This is not a claim about arbitrary complex coupling or volume-uniform analytic radii.

8. **Nonuniformity is adequately disclosed.** The radius shrinks as n^-4; neither this estimate nor the fixed-volume quartic remainder controls a continuum or thermodynamic scaling. The suggested longer tube is correctly labeled unproved as a leading coefficient. A possible higher-order sign requires the complete matrix and all competing connected contributions.

## Independent executable checks

`check_geometry.py` independently builds canonical positive-direction links, every plaquette, and every cube for n=8,9,10. It checks:

- Every retained plaquette crossing strict signs is exactly a diagonal (0,1) cut square.
- Retained links do not jump between strict signs; wholly interface plaquettes have spectator orientation.
- Breadth-first distances through shared-link plaquette adjacency to the seam give source-link path length at least depth+1, for every nonwrapping link, without assuming a positive-half condition.
- Every seam cube lacks a depth-one face.
- No nonseam cube has both strictly positive and strictly negative faces.
- No cube pairs a depth-one strictly positive face with a strictly negative face.
- The frozen original reflected cube-count matrix is [[0,1],[1,0]].

All assertions passed. Full machine-readable outputs are in `geometry_results.jsonl`. Across n=8,9,10, 82,628 cubes and 123,942 plaquettes were inspected. Minimum source-link path lengths by exact endpoint depth were respectively {0:1,1:2,2:3,3:4}, {0:1,1:2,2:3,3:4,4:5}, and {0:1,1:2,2:3,3:4,4:5}. These finite checks support, but do not replace, the general geometric arguments above.

The supplied checker also passed for n=8,9; output is preserved in `original_checker_output.txt`. Its stated coverage is narrower than the independent checker: it does not directly test the general depth-BFS or cylinder classification. Its claims about nonseam cubes and the original matrix are accurate.

## Conclusion

The locality and failed-quartic-relocation certificate is sound with the frozen local cube coefficient as its dependency. No requested correction is necessary. Keep the existing qualifications: graph connectivity alone determines neither first nonzero order nor sign, depth refers specifically to the 0/1 coordinate seam, and all quantitative estimates are finite-volume and nonuniform.
