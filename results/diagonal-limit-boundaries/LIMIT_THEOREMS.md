# Exact weak-coupling limitation and spectral survival criteria

17 October 2026. Local mathematical continuation of `remote-prism-all-beta-20261017/THEOREM.md`. No claim about continuum Yang–Mills, mass gaps, or literature novelty. The finite-torus theorem is taken as established; the additional estimates below are proved directly.

## 1. The raw witness necessarily vanishes at weak coupling, uniformly in volume

Use normalized SU(2) trace w_p, Wilson probability proportional to exp(beta sum_p w_p), and a four-dimensional periodic lattice of side n>=8. Set

    c = 2 sin(1)^2 / (3 pi),
    C = 1 + log 8 + (2/3) log(1/c).

For every beta>=1 and every plaquette p,

    0 <= E_beta[1-w_p] <= (log beta+C)/beta.                 (1)

In particular, for any two plaquettes p,q of the same orientation, F=w_p-w_q, and any measure-preserving involutive reflection theta,

    |E_beta[(Theta F)F]| <= E_beta[F^2]
                          <= 4(log beta+C)/beta.           (2)

The estimate is uniform in n and in the plaquette positions. Consequently the specific strictly negative witness in the all-beta theorem has limit zero along EVERY sequence beta_j→infinity, regardless of the admissible choices n_j,L_j,k_j. This is stronger than saying its limit is uncontrolled: its unrescaled limit is controlled and zero.

### Proof of (1)

Write d_p=1-w_p>=0 and S=sum_p d_p. There are N_e=4n^4 independent links and N_p=6n^4 plaquettes. Let

    Z_0(beta)=integral exp(-beta S(U)) dU,
    f(beta)=-log Z_0(beta).

Haar measure is normalized, so f(0)=0. Differentiation under the finite-dimensional compact integral gives f'(beta)=E_beta S and f''(beta)=-Var_beta S<=0. Concavity implies

    beta E_beta S <= f(beta).                              (3)

Represent the conjugacy angle of an SU(2) element by theta∈[0,pi], so Tr(U)/2=cos theta. Normalized Haar measure assigns the angle interval [0,r] mass

    (2/pi) integral_0^r sin^2(theta) dtheta >= c r^3,

for 0<r<=1, since sin theta>=theta sin 1 there. The angle is the bi-invariant geodesic distance from identity. If all four links around a plaquette lie in this ball, the plaquette angle is at most 4r by the triangle inequality (inversion preserves the distance). Thus

    1-w_p <= (4r)^2/2 = 8r^2.

Restrict the product Haar integral to the event that EVERY link has angle at most r. Its measure is at least (c r^3)^{N_e}, and S<=8r^2 N_p on it. Therefore

    f(beta) <= 8 beta r^2 N_p + N_e log(1/(c r^3)).

For beta>=1 choose r=(8 beta)^(-1/2)<=1. Division by N_p and N_e/N_p=2/3 gives

    f(beta)/N_p <= 1+(2/3)log(1/c)+log(8 beta).

All plaquettes have equal expectation by translations and coordinate permutations. Combining this with (3) proves (1). This uses no infinite-volume Gibbs limit or gauge fixing.

### Proof of (2)

For d_p,d_q∈[0,2],

    F^2=(d_p-d_q)^2 <= d_p^2+d_q^2 <= 2(d_p+d_q).

Taking expectations gives E F^2<=4 E d_p. Measure-preserving reflection and ordinary Cauchy–Schwarz give |E[(Theta F)F]|<=E|F|^2. This does not assume reflection positivity. Together these prove (2).

### Rescaling consequence

For G_j=a_j F_j, with deterministic complex scalars a_j,

    |E[(Theta G_j)G_j]| <= 4 |a_j|^2 (log beta_j+C)/beta_j.

Hence even a rescaled negative witness vanishes if |a_j|^2 log(beta_j)/beta_j→0. Conversely, this bound does NOT guarantee survival for any faster normalization. To maintain a magnitude at least epsilon along a subsequence one necessarily has

    |a_j|^2 >= epsilon beta_j / [4(log beta_j+C)]

on that subsequence. Normalizations dictated by physical field scaling may exceed this bound; (1) does not decide their limits or their tightness.

## 2. An exact quantitative spectral sufficient condition

At each finite stage retain the transfer notation of the all-beta theorem: positive injective trace-class T, bounded self-adjoint centered multiplication B, eigenvalues lambda_i>0, Z=Tr(T^n), and

    C(s)=Z^(-1) sum_ij |B_ij|^2 lambda_i^s lambda_j^(n-s).

The same formula is valid at s=0; define V=C(0)=E B^2>0. Let 1<=D<d_1,d_2<=floor(n/2), where d_1,d_2 are the two self-pair circular distances. The theorem gives

    Q := E[(Theta F)F] <= -A,
    A := [C(D)-C(d_1)]+[C(D)-C(d_2)] >0.                  (4)

For each unordered pair i<j with unequal eigenvalues set

    r_ij = |log(lambda_i/lambda_j)|,
    m_ij = |B_ij|^2 [lambda_i^D lambda_j^(n-D)
                    +lambda_j^D lambda_i^(n-D)] / (Z V),
    K_ij = sum_(a=1,2) {1 - cosh[(n/2-d_a)r_ij]
                            /cosh[(n/2-D)r_ij]}.

Then

    m_ij>=0, 0<K_ij<=2, sum_(i<j, unequal) m_ij<=1,
    A/V = sum_(i<j, unequal) m_ij K_ij.                   (5)

The total-mass bound uses C(D)<=C(0)=V, obtained from the same pairwise cosh expression, now including endpoint s=0. Equal-eigenvalue pairs and diagonal entries have zero decrement. Absolute summability follows from the boundedness estimate in the original theorem, also valid at s=0. Thus (5) is exact with no limiting interchange.

### Uniform spectral-band criterion

For a varying sequence of lattices and couplings, suppose there are eta,delta>0 such that eventually

    sum_{i<j: lambda_i!=lambda_j, K_ij>=eta} m_ij >= delta. (6)

Then A/V>=eta delta, and the variance-normalized witness G=F/sqrt(V) obeys

    E[(Theta G)G] <= -eta delta.                          (7)

More generally a normalization a_j has a uniform negative margin whenever (6) holds and liminf |a_j|^2 V_j>0. This suffices for negativity of a convergent limiting quadratic form. It does not prove that G_j represents a fixed physical source, that its moments converge, or that its limit is a continuum observable.

Conversely (6), with some eta,delta>0, is equivalent to a positive eventual lower bound on A/V. Indeed, if A/V>=gamma>0 eventually, take eta=gamma/2. Since total mass<=1 and K<=2,

    A/V <= eta + 2 sum_{K>=eta} m,

so the displayed mass is at least gamma/4. Thus a uniform decrement requires both spectral weight and attenuation; noncommutation only supplies a positive term separately at each finite stage.

This equivalence concerns the certified transfer decrement A, not necessarily the actual magnitude -Q. The spatial Cauchy–Schwarz inequalities used to establish (4) can be strict, and their additional negative contribution is not measured by A.

## 3. Finite two-state countermodels to unjustified limiting inferences

These are elementary transfer-operator examples, NOT SU(2) Wilson theories or continuum counterexamples. They demonstrate precisely why positivity, injectivity, a strictly positive kernel, a nonconstant multiplication observable, and strict autocorrelation decrease alone do not supply (6).

For 0<r<1, work on two configurations with counting-measure Hilbert space and define

    T_r = (1/2) [[1+r, 1-r], [1-r, 1+r]],
    B   = [[1,0],[0,-1]].

The transfer kernel is strictly positive, with eigenvalues 1,r; B is nonconstant multiplication, centered in every periodic length-n state. In the transfer eigenbasis B interchanges the two eigenvectors. Direct calculation gives

    Z=1+r^n,
    C_n(s)=(r^s+r^(n-s))/(1+r^n),
    V=C_n(0)=1,
    [B,T_r]!=0.

C_n(s) strictly decreases for integer s from 0 toward n/2.

### A. Closing spectral gap destroys the decrement at fixed variance

Let n_j→infinity and r_j=exp(-1/n_j^2). For EVERY choice 0<=s_j<=n_j, both r_j^(s_j) and r_j^(n_j-s_j) tend to 1; hence C_(n_j)(s_j)→1 uniformly in s_j. Therefore any two-distance strict decrement tends to zero although V_j=1, every finite kernel is strictly positive, and every finite commutator is nonzero.

For example n_j=8j, L_j=j, k_j=4j satisfies the geometric admissibility for j>=3, with D_j=2j+1, d_1=3j-1, d_2=3j (strict for j>=3). The decrement A_j>0 tends to zero.

### B. A fixed spectral gap and fixed nonzero commutator still do not suffice

Keep r∈(0,1) fixed and use the same admissible n_j,L_j,k_j for j>=3. Then D_j→infinity and n_j-D_j→infinity. Since

    0<A_j<=2 C_(n_j)(D_j),

A_j→0 exponentially. Here V_j=1 and both T_r and [B,T_r] are fixed. The missing condition is surviving spectral weight at the first separation D_j: the m-mass tends to zero. Thus a bare transfer spectral gap, even one uniformly separated from zero, is not a sufficient quantitative condition in growing-depth geometry.

## 4. What is and is not now settled

Settled exactly: at weak coupling the unrescaled Wilson plaquette-difference witness tends to zero uniformly in all its admissible finite-torus geometry. A normalization slower than sqrt(beta/log beta) cannot rescue its reflected quadratic form. For variance-normalized transfer decrements, (6) is the exact uniform mass/attenuation criterion, and strict positivity/noncommutation do not imply it.

Still unproved: a physically prescribed renormalized observable, any identification with fixed smooth compact source functions, uniform spectral-band estimates for actual SU(2) Wilson transfer operators, convergence of normalized reflected moments, or a negative continuum reflected norm. No such conclusion follows from these finite-stage statements.
