# Independent audit: seam forest cancellation

Date: 2026-10-17. Verdict: PASS for the stated finite-volume cancellation and quantitative modulus estimates. No distance decay, boundary reflection positivity bridge, or continuum conclusion follows.

## Final-proof amendment

The final `PROOF.md` has SHA-256 `a1e96b1b33c396a4317ecf0f0e2c546b3c35df70e6c7c3df42344bb947eb8f0f`. I independently verified its hash and reviewed its diff against the original frozen source. The only change states the ordered bound for Re Q_t and explains that reflection invariance of the full measure makes Q_t real. This resolves the reality caveat in item 7 below. Final verdict: APPROVED, with no remaining mathematical correction requested. The original frozen source remains unchanged.

The portable negative-control checker now verifies this final proof hash and loads the sibling geometry checker. Both checkers passed again after this change. Its frozen SHA-256 is `a9429582cacba9013a1befb986307482f53c915e721ce3fe14bbb83d932eabdf`.

## Frozen inputs

- `SEAM_FOREST_CANCELLATION.md`
  SHA-256 `3b93c7bd48f464ad015cc7e73ec3a874c494021db92e1cd7a4a335f084accfdc` (verified before audit).
- `check_seam_forest_geometry.py`
  SHA-256 `ac974a3a4b10d13435a9d3b5a541d407d02872456ae5ab63e0ceb07971f088b6`.
- Context read: `separator-route-stop.md`.

## Independent mathematical checks

1. **Termwise gauge invariance:** The exterior-only Wilson action is gauge invariant at every vertex, including vertices belonging to C. Changing exterior variables with the same vertex transformations applied to internal links leaves each full seam trace invariant. Integration therefore makes each ordered-product term a gauge-invariant function only of its selected distinct internal edges. This does not require exterior links or paths to be independent.

2. **Forests, including repetitions:** Rooting each selected tree and solving the gauge equations recursively sends every selected edge to identity. Reverse orientations cause no difficulty. Repeated plaquettes and repeated edges leave the distinct-edge graph unchanged, so their terms are constant too. The relevant graph is not a multigraph with duplicate-edge cycles.

3. **Cube geometry:** For n>=4, internal vertices form the open Cartesian grid {1,...,n-1}^4, with no periodic internal wrap edge or parallel edge. It is bipartite and simple, hence a set of at most three distinct edges is acyclic. Every four-cycle is an elementary coordinate square. Plaquette internal-edge counts are exactly among 0,1,4, so mixed plaquettes have one internal edge. The supplied exact checker passes n=4,5,6,8; the geometric argument, rather than these finite checks alone, establishes the general statement. Seam counts are 432,1152,2400,7056 respectively; elementary internal-square counts are 216,864,2400,10584.

4. **Odd moments:** SU(2)'s central -I can multiply every exterior link without changing its normalized measure. All-exterior plaquettes have four factors; seam plaquettes have three. Thus all odd conditional moments vanish pointwise, including M1 and M3. M2 is constant by item 2 and nonnegative, not generally zero.

5. **Normalization:** K_t=a+R_t with a=1+c2*t^2/2 and 0<=R_t<=r is exact. Dividing by E K_t gives the displayed covariance identity. There is no order-t^2 change of normalized expectations even when the partition function has a nonzero quadratic term.

6. **Explicit bounds:** For X in [0,r] and mu=EX, convexity gives E|X-mu|<=2*mu*(r-mu)/r<=r/2. Applied to R, this yields |delta E G|<=||G||*r/(2a) for complex G as well. Under TV=sup_events |P-Q|=one-half L1 density distance, TV<=r/(4a), capped by 1. The cosh Taylor remainder gives r<=x^4*cosh(x)/24, x=|t|m. Zero r is handled directly. These constants are correct.

7. **Connected quantity:** Expanding the product difference as (E_t A-E_0 A)E_t B+E_0 A(E_t B-E_0 B), each factor mean is bounded by M. Together with the AB estimate this gives 3*M^2*r/(2a). No reflection positivity is used in this modulus estimate. For the additional ordered lower bound, Q0>=0 is necessary and Q_t must be real. Reality is automatic when the intended reflection preserves the full cube/seam measure; if the statement is read as allowing an arbitrary norm-preserving reflection, this symmetry/reality assumption should be stated explicitly. Equivalently the same lower bound always applies to Re Q_t when Q0 is real nonnegative.

8. **Fourth coefficient:** Since K_t=1+c2*t^2/2+M4*t^4/24+O(t^6), quotient expansion gives Cov(G,M4)/24. The connected derivative is Cov(AB,M4)-EA*Cov(B,M4)-EB*Cov(A,M4), precisely the bilinear third joint cumulant. The factor beta^4 for derivatives in s is correct when beta and the observables are fixed. The assertion is first *possible* nonconstant order four, not guaranteed nonzero order four for each observable or beta.

9. **Term classification at order four:** Nonforest ordered lists of length four necessarily select four distinct edges exactly once. In this grid these are elementary squares. Each selected edge must be available to a seam plaquette. No other list can produce a nonconstant term.

## Exact negative control

`check_cycle_negative_control.py` reruns the frozen checker and computes a four-seam capped-disk polynomial using exact rational arithmetic. Place an internal square in a coordinate boundary face of C, its parallel exterior square at coordinate zero, and the four seam strip plaquettes between them. Gauge-fix the four radial exterior links to identity using transformations at the four exterior vertices, keeping internal links fixed. Let internal edges in cyclic orientation be U_i and outer square edges V_i. The polynomial is

    integral product_i w(U_i V_i^{-1}) * w(V_1 V_2 V_3 V_4) dV.

This equals w(U_1 U_2 U_3 U_4)/256. The check obtains 1/256 for all U_i=I, -1/256 with one U_i=-I, zero with one U_i=i, and 1/256 with all four U_i=i.

The computation averages over Q8 rather than sampling continuous Haar, but is exactly an SU(2) Haar integral here: each independent quaternion enters only at degree two, and uniform Q8 has precisely the S^3 Haar first and second coordinate moments (zero and delta_ab/4). Thus this is exact cubature, not a finite-group approximation or Monte Carlo test. The exterior cap factor is an allowed first-order Wilson-action insertion. It demonstrates concretely why a cycle can retain internal holonomy and why the forest hypothesis cannot be dropped. It does not claim a full finite-beta evaluation or uniform spatial estimate.

## Scope and stopping point

The estimates grow as m^4 at small t and give no distance factor. The coefficient remains a covariance/cumulant with a boundary interaction. No uniform interpolation estimate to s=1, mixing theorem, BRP theorem, or continuum result is established. The note explicitly respects this limit. No external state was modified; this review and checks are local audit artifacts.

## Reproduction

    python check_cycle_negative_control.py

Place `PROOF.md`, `check_seam_forest_geometry.py`, and `check_cycle_negative_control.py` together. The command works from any working directory when the checker is invoked by its path. Output is preserved in `check_results.txt`.
