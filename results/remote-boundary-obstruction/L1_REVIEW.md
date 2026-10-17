# Independent audit: remote L=1 transfer proof

Reviewed 2026-10-17. Reviewed source: `/workspace/scratch/477a3dcb7024/remote-prism-L1-20261017/TRANSFER_PROOF.md`.

Source SHA-256: `9ef6f6cbbf19d809e85257ea0535bdf13ddc87d007044cf6a52f3a0df8874ad1`.

## Verdict

The finite-volume leading coefficient and eventual strict negativity for small positive beta are supported by the transfer proof. I found no substantive gap in the positive-beta theorem. There is one literal false auxiliary sentence, easily repaired: positivity of T for all sufficiently small *real* beta. Positivity holds for beta >= 0, but not generally for negative beta on odd-length tori. Replace that phrase by “for sufficiently small nonnegative beta,” or retain only self-adjointness and the positive principal eigenvalue for real beta. No continuum or mass-gap conclusion follows.

I independently checked the representation coefficients, trace-class convergence, rank-one subtraction, finite-period covariance normalization and source geometry. This is an analytic audit, not a full independent lattice-integral expansion to order 12.

## 1. Exact transfer identity

Take one representative of every unoriented spatial link and one canonical orientation of every spatial plaquette. A single time-step kernel before integrating temporal links has the product of normalized temporal plaquette factors. Temporal links form one independent spatial gauge transformation per vertex. Integrating them yields the orthogonal gauge projector Q acting on the product convolution C. Central convolution commutes with each left/right endpoint action, hence Q commutes with C. Spatial multiplication A also commutes with Q. The full-space step is A C Q A; its restriction to the invariant Hilbert space is A K A and its orthogonal complement is killed. Taking the periodic trace therefore integrates all temporal links, including the final step. There is no discarded periodic holonomy.

Every temporal plaquette contributes a removed factor z(beta). There are 3 n^4 temporal plaquettes, agreeing with the stated scalar. The two factors A give each spatial plaquette its full exp(beta w) weight. Multiplication insertions commute with A, so the trace insertion formula has the correct time placement.

## 2. Trace-norm analyticity and multiplicities

On a single link the spin-j Peter–Weyl block has dimension d_j^2, and convolution eigenvalue c_j/(d_j c_0). Its trace-norm contribution is therefore d_j |c_j|/|c_0|, exactly as claimed. Missing a d_j here would have invalidated the argument; it is not missing.

A more explicit analyticity proof is available. Write chi_(1/2)^m = sum_j N_(m,j) chi_j with nonnegative integer tensor multiplicities. The unnormalized convolution Taylor coefficient at order m has nonnegative eigenvalues N_(m,j)/(2^m m! d_j). Its trace norm is

  sum_j d_j N_(m,j)/(2^m m!) = 1/m!,

because sum_j d_j N_(m,j)=2^m. Thus the unnormalized convolution series converges absolutely in trace norm for every complex beta, with bound exp(|beta|). Dividing by c_0=z is analytic on a neighborhood of zero since z(0)=1. Finite tensor products remain trace-norm analytic; compression/restriction by the fixed gauge projector is trace-norm continuous. Multiplication A is operator-norm entire because there are finitely many bounded spatial plaquettes. Consequently all operator Taylor remainders used in the proof are justified in trace norm.

## 3. Complete low-order invariant spectrum

Peter–Weyl decomposes each physical link into a *single* irrep label. At a vertex with only one occupied incident link, its nontrivial irrep has no invariant vector. Therefore every occupied support vertex has degree at least two. A finite nonempty support contains a graph cycle. For n>=11 the nearest-neighbor spatial graph is simple, has no loops or parallel edges, has girth four, and its four-cycles are precisely elementary squares.

Each occupied link contributes at least one to the leading beta degree (2j>=1). Hence degree at most four forces exactly the four edges of one elementary square, all with j=1/2. Bivalent invariant intertwiners on that loop are one-dimensional. The normalized invariant function is chi_p=Tr U_p, with Haar norm one. Different unoriented plaquettes have a free edge in their symmetric difference and are orthogonal. Canonical orientation should be understood to avoid naming the same SU(2) trace twice.

Repeated traversal of an edge is not an extra graph edge or an additional low mode: its tensor product decomposes into the single-link Peter–Weyl irreps already considered. Immediate backtracking cancels, while higher irreps only increase degree. Fundamental cycles winding around the torus have length at least n, so cannot enter the degree-four coefficient. Branching invariant networks similarly cannot fit into the degree-four budget.

An independent exact rational tensor-product recurrence gave:

- t_(1/2) = beta/4 - beta^3/96 + beta^5/1536 - beta^7/23040 + ...
- t_1 = beta^2/24 - beta^4/384 + beta^6/5760 + ...
- t_(3/2) = beta^3/192 - beta^5/2560 + ...
- t_2 = beta^4/1920 - beta^6/23040 + ...

Thus the coefficient on each fundamental square is (1/4)^4=1/256, with no other nonconstant coefficient at that order or earlier. Numerical rational output is in `representation_check.txt`.

## 4. Principal-mode subtraction

Let B_beta=A_beta P0 A_beta. For real beta, B has the single nonzero eigenvalue s_beta=<1,A_beta^2 1> and projector onto A_beta 1. Its complementary remainder is identically zero. Since

  T_beta = B_beta + beta^4 P4/256 + O_1(beta^5),

the only possible order-four contribution to the complementary spectral part is obtained by first-order spectral perturbation at B_0=P0. There P4 P0=P0 P4=0. Its principal-eigenvalue derivative <1,P4 1> vanishes and its off-diagonal projector derivative vanishes. Therefore neither principal normalization nor principal-projector subtraction removes or changes beta^4 P4/256. This yields the asserted R_beta expansion. Merely saying that A=I+O(beta) would not by itself suffice, but the rank-one argument in the source supplies the needed justification.

Trace-norm analyticity gives R=O_1(beta^4), and multiplication of these remainders gives R^D = beta^(4D) P4/256^D + O_1(beta^(4D+1)) for every fixed positive integer D. The constants can depend on n and D, as allowed.

## 5. Finite periodic trace and connected covariance

The exact denominator after dividing by lambda^n is 1+Tr R^n = 1+O(beta^(4n)). For bounded insertions, the term with two complementary propagators is bounded in absolute trace by a constant times ||R^D||_1 ||R^(n-D)||, hence O(beta^(4n)). One-point corrections are also O(beta^(4n)). The denominator-induced correction to the disconnected principal means is of that same order. Thus the displayed connected-covariance formula has the stated error; no disconnected cap survives as an unaccounted low-order contribution.

The two single-propagator terms have orders 4D and 4(n-D). Both are needed on a periodic lattice. For D=3 and n>=11 the reverse term starts at order at least 32. No reverse-path multiplicity doubles the short-path coefficient. At equal half-period there would be two equally short terms, but that case is absent here.

For the same spatial plaquette, w=chi/2 and <1,M_w P4 M_w 1>=1/4. Thus D=3 gives

  (1/256)^3 (1/4) = 1/2^26.

The observable normalization is consequently correct.

## 6. Four source pairs and seam depth

The same-spatial-location cross pair theta p, q has short coordinate-1 separation three; the other cross pair has short coordinate-0 separation three. Each has covariance beta^12/2^26+O_n(beta^13).

For theta p, p, the coordinate-1 separation n-2-k is at least four and its reverse k+2 at least seven. For theta q, q, the separation k-1 is at least four and its reverse n-k+1 at least seven. The universal transfer bound therefore gives O_n(beta^16) for each self-pair, even without using their distinct spatial positions. Spatial insertions cannot introduce a lower mode after the principal mode is subtracted.

The source plaquettes vary only in coordinates 2 and 3. Their 0/1 coordinates are fixed at (n-2,k) and (k,1), respectively, so all endpoints are in the coordinate-depth-one belt [1,n-2]^2 and in the strict representative half x0>x1. This agrees with the explicit depth convention in the preceding locality certificate. Reflection preserves the spectator plaquette orientation. Translation invariance gives identical one-point means and E F=0; likewise E Theta F=0. Consequently the uncentered reflected form is exactly the signed sum of the four covariances.

The total coefficient is -2/2^26 = -1/2^25, as claimed. Fixed-volume analyticity gives an actual sufficiently small positive interval of strict negativity.

## 7. Exact wording correction about positivity

For odd n (including n=11), a straight fundamental Wilson loop winding once around a spatial coordinate is a gauge-invariant eigenvector of K with eigenvalue t_(1/2)(beta)^n. For small negative beta, t_(1/2)<0, so this eigenvalue is negative. Multiplication by the strictly positive invertible A preserves the existence of a negative quadratic direction under congruence: if K f has negative quadratic form, choose h=A^(-1)f and <h,T h>=<f,K f><0. Therefore T is not a positive operator for all sufficiently small real beta.

This does not threaten the argument. For nonnegative beta all c_j are nonnegative, so K and T are positive. For either sign T is self-adjoint, its isolated eigenvalue near one remains positive, and its simple spectral projector is orthogonal. The theorem only needs beta>0. Correcting the sentence avoids an actual false auxiliary claim without changing any coefficient or conclusion.

## Limits

No quantitative small-beta threshold, uniformity in n, growing source depth, continuum limit, or mass-gap statement has been established or inferred. No source file or external service was changed.
