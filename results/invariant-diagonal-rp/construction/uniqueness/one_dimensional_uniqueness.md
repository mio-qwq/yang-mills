# Finite-width Wilson cylinder: exact one-dimensional uniqueness lemma

## Result

For each fixed finite transverse width and every finite real coupling, the ungauge-fixed SU(2) Wilson specification on the infinite longitudinal cylinder has exactly one DLR Gibbs measure, provided its link variables have been assigned to finite longitudinal slices and the resulting interaction has finite range and uniformly bounded local energy. Two-periodic slice geometry causes no problem: use an even block length at least the interaction range. The statement concerns all DLR measures, including non-translation-invariant ones.

The argument below is direct, and does not require a high-temperature inequality or reflection positivity. In particular, the positivity used here means pointwise positivity of the transfer kernel; it is not positivity of an operator quadratic form.

## Precise general hypothesis

Let the original single-slice spaces be standard Borel probability spaces (S_i, nu_i), with compact finite products of SU(2), equipped with product normalized Haar measure, as the intended case. Assume a measurable interaction Phi with range R and

J = sup_i sum_{A containing i} ||Phi_A||_infinity < infinity.

The coupling is included in Phi. For a periodic finite-range continuous model on compact slice spaces this bound is automatic. Mere boundedness of each individual Phi_A, without a uniform bound in i, is not the claimed hypothesis.

Choose a block length L >= max(R,1). If the slices have period two, choose L even. Divide Z into disjoint consecutive blocks of length L. Any interaction support meets at most two adjacent blocks. Thus the blocked energy consists of bounded one-block terms V_i(x_i) and adjacent-block terms W_i(x_i,x_{i+1}), with, for example,

||V_i||_infinity <= LJ,   ||W_i||_infinity <= LJ.

Define

k_i(x,y) = exp[-V_i(x)/2 - W_i(x,y) - V_{i+1}(y)/2].

There are constants 0 < m <= M < infinity, independent of i, such that

m <= k_i(x,y) <= M.

For instance m = exp(-2LJ), M = exp(2LJ) work. Up to a constant depending only on the exterior endpoints, the Gibbs density on blocks [a,b], with x_{a-1}=ell and x_{b+1}=r, is

Z^{-1} product_{i=a-1}^{b} k_i(x_i,x_{i+1}) product_{i=a}^{b} nu_i(dx_i).

The blocks must be disjoint. Using overlapping block states introduces artificial compatibility zeros and obscures this simple strict-positivity argument.

## Boundary contraction, with explicit constants

Fix the right endpoint r. Set

h_b(x) = k_b(x,r),

h_i(x) = integral k_i(x,y) h_{i+1}(y) nu_{i+1}(dy),   i < b.

These functions are positive and integrable. Under the finite-interval Gibbs law, the forward transition from block i to block i+1 is

P_i(x,dy) = k_i(x,y) h_{i+1}(y) nu_{i+1}(dy) / h_i(x),

for a-1 <= i <= b-1. Put

eta_i(dy) = h_{i+1}(y) nu_{i+1}(dy) / integral h_{i+1} dnu_{i+1}.

Then, uniformly in x and the entire right boundary message,

P_i(x,dy) >= (m/M) eta_i(dy).

Consequently the total-variation contraction coefficient of P_i is at most

rho = 1 - m/M < 1.

Here total variation means sup_A |mu(A)-nu(A)|. Indeed, each transition is (m/M) eta_i plus a nonnegative remainder of mass 1-m/M, and the common part cancels in differences.

If only the left endpoint is changed, the resulting laws on an interior window [c,d] differ in total variation by at most rho^(c-a+1): couple the two forward chains and use the contraction up to c; their continuation from c to d uses the same kernels. The same argument in the reverse direction controls a change of right endpoint by rho^(b-d+1). Therefore, for arbitrary endpoint pairs xi and xi',

|| (gamma_[a,b]^xi)_[c,d] - (gamma_[a,b]^xi')_[c,d] ||_TV
  <= rho^(c-a+1) + rho^(b-d+1).                         (1)

For a bounded measurable F supported in [c,d], multiply the right side of (1) by 2||F||_infinity to bound the difference of expectations. No restriction on the size of J or on the finite coupling appears.

## Existence and uniqueness

Uniqueness: the DLR equation expresses the restriction of any infinite-volume Gibbs measure to [c,d] as a mixture of the restrictions of gamma_[a,b]^xi. The diameter bound (1), followed by a -> -infinity and b -> +infinity, shows that any two Gibbs measures agree on every finite window. They are therefore equal.

Existence can be proved without adding continuity: finite-volume measures with fixed exterior configurations have Cauchy finite-window marginals in total variation. To compare two different volumes, condition the larger-volume measure on the boundary of the smaller interval and use (1). Their consistent limiting marginals define a probability measure by the countable-product extension theorem. For every finite set Delta and bounded local F, both F and gamma_Delta F depend on finitely many block coordinates, so local total-variation convergence passes the finite-volume DLR identity to the limit. This gives the DLR measure. For Wilson's continuous compact setting, the usual weak compactness/quasilocality existence proof is also sufficient.

Free longitudinal boundary conditions have the same limit: end factors are positive boundary messages, and the same contraction works away from the ends. Alternatively, any subsequential free-boundary limit is DLR, hence is the unique state. The finite-width constant rho may approach one as the width increases; no width-uniform mixing bound is asserted or needed to take the longitudinal limit first.

## Specialization to SU(2)

For the conventional plaquette factor exp[(beta/2) Re Tr(U_p)], |(beta/2) Re Tr(U_p)| <= |beta|. Each finite-width block and adjacent pair of blocks contains only finitely many relevant plaquettes. Thus m>0 and M<infinity hold for every finite beta. Product Haar reference measures have full support. No gauge fixing, quotient constraints, or zero-temperature limit is needed. Free transverse boundaries simply omit interactions and preserve the argument.

The unique cylinder Gibbs state is invariant under every symmetry of that cylinder specification: pushing it forward by such a symmetry gives another Gibbs state, which uniqueness identifies with the original state. This is the justification for exact longitudinal translation/reflection invariance whenever the geometry itself has those symmetries.

## Checked literature support and scope

1. Leandro Cioletti, Artur O. Lopes, Manuel Stadlbauer, "Ruelle operator for continuous potentials and DLR-Gibbs measures," Discrete and Continuous Dynamical Systems 40(8) (2020), 4625-4652, DOI 10.3934/dcds.2020195. Publisher: https://www.aimsciences.org/article/doi/10.3934/dcds.2020195 . Author preprint: https://arxiv.org/pdf/1608.03881 . The preprint's Theorem 5.2 (printed p. 13, PDF page 13) proves uniqueness of their DLR/eigenprobability under the Bowen bounded-boundary-variation condition for a compact metric alphabet with fully supported probability reference; Theorem 2.2 records the compact-alphabet Ruelle-Perron-Frobenius theorem. A bounded finite-coordinate potential satisfies that Bowen condition directly. Important scope caveat: their DLR formulation is one-sided. The two-sided all-DLR conclusion needed here is established by the explicit endpoint-contraction proof above, rather than being silently attributed to that theorem.

2. S. Friedli and Y. Velenik, Statistical Mechanics of Lattice Systems, Chapter 6, author-hosted text: https://www.unige.ch/math/folks/velenik/smbook/Infinite-Volume_Measures.pdf . Theorem 6.40 and Corollary 6.41, printed p. 275, give the bounded-boundary-energy criterion and one-dimensional finite-range uniqueness. Section 6.10.2, printed pp. 307-308, explicitly says the relevant uniqueness results extend to compact spin spaces. This is a useful rigorous textbook cross-check, not an original research source.

3. D. Ruelle, "Statistical mechanics of a one-dimensional lattice gas," Communications in Mathematical Physics 9 (1968), 267-278: https://www.ihes.fr/~ruelle/PUBLICATIONS/%5B21%5D.pdf . This is the historical primary-source transfer-operator result, but its state space is {0,1}; it should not be cited alone as if it states the full compact-SU(2) version.

All estimates and the two-sided proof above are derived explicitly here; they are not quotations from the sources.
