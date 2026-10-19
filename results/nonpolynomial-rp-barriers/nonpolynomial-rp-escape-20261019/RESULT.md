# Two no-escape results beyond polynomial-at-each-mass numerators

19 October 2026. Local mathematical research only. No repository, PR, release, or external publication was changed.

## Executive result

Two natural alternatives to a polynomial numerator over a radial massive resolvent fail to produce the sought anisotropic reflection-positive covariance:

1. **Finite positive ellipsoidal-resolvent mixtures are rigid.** If

       F(p) = sum_{j=1}^N w_j / (p^T A_j p + m_j^2),
       w_j > 0, A_j real symmetric positive definite, m_j >= 0,

   is reflection invariant and reflection positive at a mirror with unit normal n, then **every A_j has n as an eigenvector**. Therefore W_4 invariance and RP at the coordinate and diagonal mirrors force every A_j to be a scalar matrix. No ultraviolet hypothesis is needed. A shifted complex pole cannot disappear: all residues at a common upper-half-plane pole have the same phase and add with strictly positive magnitude.

2. **Bounded separable Laplace-mixture covariances always fail diagonal RP unless constant.** Let sigma be a finite nonzero positive measure on [0,infinity), put

       h(t) = integral exp(-lambda |t|) sigma(dlambda),
       C(x) = product_{i=0}^3 h(x_i).

   These are ordinary positive, W_4-invariant, bounded continuous Gaussian covariances, and they satisfy complex RP at every coordinate mirror. They obey the very mild reflected ultraviolet bound O(d^8), hence o(d^-2). Nevertheless, if sigma((0,infinity))>0, a single explicit three-point test at a diagonal mirror has a strictly negative reflected form. This covers arbitrary finite Laplace mixtures, including genuinely nonrational examples, without assumptions about compact spectral support, analytic continuation, or finite polynomial degree.

Both obstructions survive adding arbitrary origin-supported contact distributions. They do not classify general nonseparable covariances or continuous mixtures of ellipsoids, and they do not establish a representation theorem for interacting Yang–Mills fields.

## 1. Conventions and the actual positivity being tested

Work on R^4 with signed-permutation group W_4. Its sixteen mirror hyperplanes have normals

    e_i,                         0 <= i <= 3,
    (e_i + e_j)/sqrt(2),
    (e_i - e_j)/sqrt(2),         0 <= i < j <= 3.

For a unit normal n, write x=tn+z, p=un+k, with z,k perpendicular to n. Reflection is theta_n(tn+z)=-tn+z. The covariance reflection form is

    Q_n(f) = integral integral conjugate(f(x)) C(theta_n x-y) f(y) dx dy,

for complex smooth compactly supported f in {n dot x>0}; in the distributional case use the corresponding distribution pairing. The placement of the complex conjugate is material. Positivity means Q_n(f)>=0 for every such complex test.

The covariances below are real and reflection invariant at the mirrors under discussion. Ordinary covariance positivity is separate from RP. For a reflection-invariant centered real Gaussian field, covariance RP gives Gaussian RP: the cross-covariance matrices of positive-side linear observables are positive, and their Gaussian exponential kernel is positive by the power-series/Schur-product argument. Conversely, Gaussian RP includes the covariance test.

The spatial Fourier convention used in the pole calculation is

    K_k(t) = (2pi)^(-1) integral_R exp(iut) F(un+k) du.

The reflected form after tangential Fourier transformation contains K_k(t+s), with positive t,s.

## 2. Finite positive ellipsoidal mixtures: statement

Let

    F(p) = sum_{j=1}^N w_j / D_j(p),
    D_j(p) = p^T A_j p + m_j^2,

with finite N, w_j>0, A_j real symmetric positive definite, and m_j>=0. This is a nonnegative locally integrable tempered multiplier on R^4, including at p=0 when a mass vanishes, and hence is a stationary Gaussian covariance.

### Theorem A

Fix n. Assume that the aggregate F is invariant under reflection across n-perpendicular and its covariance has complex RP at that mirror. Then

    A_j n is a scalar multiple of n for every j.

If F is W_4-invariant and has RP at all sixteen W_4 mirrors, then

    A_j = a_j I,    a_j>0,    for every j,

and

    F(p) = sum_j (w_j/a_j) / (|p|^2+m_j^2/a_j).

Consequently the covariance is O(4)-invariant. The conclusion is already forced by the four coordinate normals and any three diagonal normals connecting the four coordinate indices, for example (e_i+e_{i+1})/sqrt(2), i=0,1,2.

No numerator-degree, mass-disintegration, or ultraviolet hypothesis is used. The proof also permits an additional reflection-invariant polynomial multiplier, because its origin-supported inverse Fourier transform never contributes to a strictly separated reflected pairing. With such a term added, the rotational conclusion concerns the displayed resolvent part and the covariance away from the origin; an anisotropic W_4-invariant contact term need not itself become O(4)-invariant.

### Why this family genuinely tests a different route

Before the theorem is applied, the poles lie on anisotropic quadrics p^T A_j p+m_j^2=0, rather than the radial quadrics |p|^2+s=0 used in the earlier polynomial-at-each-mass representation. A finite signed-permutation orbit of any diagonal anisotropic A gives a W_4-invariant positive mixture. Such an orbit is coordinate-RP, but Theorem A shows that it fails the required diagonal RP.

The mild ultraviolet condition would not exclude these candidates by itself. If a_* is the minimum of the least eigenvalues of the finitely many A_j, then

    0 <= F(p) <= (sum_j w_j/a_*) / |p|^2.

For f_d(x)=f(x/d), ordinary covariance positivity, Cauchy–Schwarz, and the Fourier change of variables give

    |Q_n(f_d)| <= const_f d^6,

whenever the aggregate covariance is invariant at that mirror. The same estimate follows by bounding the two ordinary covariance norms even without mirror invariance. Thus the obstruction is truly reflection positivity, not an excessive ultraviolet singularity.

## 3. The shifted poles and why cancellation is impossible

Fix a real tangential k!=0. For each j write

    a_j = n^T A_j n > 0,
    b_j = n^T A_j k,
    c_j = k^T A_j k + m_j^2,
    beta_j = b_j/a_j,
    omega_j = sqrt(c_j/a_j - beta_j^2) > 0.

The final strict inequality follows from the positive-definite Schur complement on n-perpendicular, since k!=0. Thus

    D_j(un+k) = a_j [(u+beta_j)^2+omega_j^2].

Its poles are

    u = -beta_j +/- i omega_j.

The residue of w_j/D_j at its upper-half-plane pole is exactly

    w_j/(2 i a_j omega_j) = -i w_j/(2 a_j omega_j).

Every term with a pole at that same point contributes another strictly negative imaginary residue. Hence **no upper pole can cancel in a finite positive mixture**, even when several denominators have coincident poles. No genericity argument, resultant, irreducibility claim, or separation of masses is needed.

If A_j n is not parallel to n, there exists k perpendicular to n with b_j!=0. Such k is automatically nonzero. The aggregate then has an uncancelled pole with nonzero real part.

It remains to prove directly that such a pole violates complex RP. This is done next without assuming a general Stieltjes representation theorem.

## 4. A self-contained finite-exponential RP obstruction

The inverse normal Fourier transform at positive time is

    K_k(t) = sum_j B_j exp(-lambda_j t),
    B_j = w_j/(2 a_j omega_j) > 0,
    lambda_j = omega_j+i beta_j.

Aggregate identical lambda_j first. Their coefficients remain positive real. Reflection invariance makes F(un+k) real and even in u, and therefore K_k(t) real. Linear independence of distinct exponential functions implies that the set of distinct exponents is closed under conjugation and the coefficients at conjugate exponents agree.

Assume that one exponent lambda is nonreal, with coefficient B>0. Select a time step r>0 such that the numbers

    z_j = exp(-r lambda_j)

are pairwise distinct and the selected conjugate pair consists of two nonreal nodes. Such r exists: excluded coincidences and real-node conditions form at most a countable set of positive r. Fix any t_0>0.

By ordinary finite polynomial interpolation, there is a polynomial P with real coefficients such that

    P(exp(-r lambda)) = i exp(t_0 lambda),
    P(exp(-r conjugate(lambda))) = -i exp(t_0 conjugate(lambda)),
    P(z_j) = 0 at every other node.

Indeed, the interpolation nodes and assigned values are both conjugation symmetric, so uniqueness of the interpolating polynomial makes its coefficients real. Write

    P(z) = sum_{a=0}^M q_a z^a,    q_a real.

Use point-time coefficients q_a at positive times t_a=t_0+a r. Their Hankel quadratic form is

    sum_{a,b} q_a q_b K_k(t_a+t_b)
      = sum_j B_j exp(-2t_0 lambda_j) P(z_j)^2
      = -2B < 0.

The square here is P(z_j)^2, not |P(z_j)|^2: the same complex exponential appears at both positive times in K_k(t+s). The resulting sum is real because conjugate exponents occur in pairs. This distinction is precisely why an oscillatory decay mode cannot be an RP contribution.

Replace each point-time mass by a common smooth unit-mass bump supported in a small neighborhood of t_a. Since K_k is continuous, the negative value persists for sufficiently small bumps, producing a real h in C_c^infinity((0,infinity)) with a negative scalar reflected form.

### From a fixed frequency to a legal four-dimensional test

For this fixed h, its scalar form Q_h(k') varies continuously with k' in a neighborhood of the chosen nonzero k. This follows directly from the finite formula and the smooth positive omega_j(k'). It is therefore strictly negative on a nonempty open tangential neighborhood.

Choose a nonzero smooth compactly supported Fourier cutoff chi inside that neighborhood. With g the inverse tangential Fourier transform of chi, the test f(t,z)=h(t)g(z) has reflected form proportional to

    integral |chi(k')|^2 Q_h(k') dk' < 0.

It is compactly supported in positive time and Schwartz in z. Smooth tangential spatial cutoffs approximate it in Schwartz topology. The covariance is tempered, so its reflected form is continuous under this approximation; a sufficiently large cutoff gives an actual C_c^infinity positive-half-space test with negative form.

Thus an off-imaginary normal pole violates the stipulated complex RP. The construction already starts from real time coefficients; no numerical matrix-eigenvalue claim is being used.

### Completion of Theorem A

Section 3 shows that any cross-block n^T A_j|_{n-perpendicular} produces such a pole, and Section 4 rules it out. Hence every A_j has n as an eigenvector.

Apply this first to n=e_i. Every A_j is diagonal in the common coordinate basis. Apply it to n=(e_i+e_l)/sqrt(2). The corresponding two diagonal entries of A_j must agree. A connected set of coordinate pairs makes all four entries equal. This proves the theorem. Conversely, positive radial massive-resolvent mixtures have RP at every mirror by their ordinary nonnegative one-dimensional exponential formulas.

### An explicit four-ellipsoid example and a two-time witness

Consider the W_4-invariant multiplier

    F(p) = sum_{j=0}^3 1/(|p|^2+p_j^2+1).

Every matrix I+e_j e_j^T is diagonal, so coordinate RP holds term by term. At n=(e_0+e_1)/sqrt(2) and k=(e_0-e_1)/sqrt(2), its normal slice is

    F(un+k) = 1/((3/2)u^2+u+5/2)
              + 1/((3/2)u^2-u+5/2)
              + 2/(u^2+2).

The off-axis upper poles are +/-1/3+i sqrt(14)/3. Its positive-time kernel is exactly

    K_k(T) = (2/sqrt(14)) exp(-sqrt(14)T/3) cos(T/3)
             + (1/sqrt(2)) exp(-sqrt(2)T).

Let

    r=3pi/2,
    t=exp(-pi sqrt(14)/2),
    s=exp(-3pi sqrt(2)/2).

Use times r and 3r with real coefficients (-s^2,1). The nonoscillatory mode cancels exactly, because -s^2 exp(-sqrt(2)r)+exp(-3sqrt(2)r)=0. The oscillatory part gives the exact value

    Q_time = -(2/sqrt(14)) t^2 (s^2+t^2)^2 < 0.

The smoothing and frequency-localization argument above turns this into a legal compact smooth four-dimensional witness. This is an explicit finite positive W_4 orbit with mild ultraviolet behavior and coordinate RP, but failed diagonal RP.

## 5. Arbitrary finite separable Laplace mixtures

Here the covariance is defined directly in position space. Let sigma be any finite nonzero positive Borel measure on [0,infinity) and put

    h(t) = integral_[0,infinity) exp(-lambda |t|) sigma(dlambda),
    C(x_0,x_1,x_2,x_3) = h(x_0)h(x_1)h(x_2)h(x_3).

There is no finite-support, rationality, spectral-gap, or finite-moment assumption on sigma.

### Theorem B

The kernel C is a bounded continuous, stationary, ordinary positive-type, W_4-invariant scalar covariance. Its centered Gaussian field has complex RP at the four coordinate mirrors.

It has RP at a diagonal mirror if and only if sigma is supported at {0}. In that exceptional case h and C are constant. If sigma((0,infinity))>0, a universal explicit three-point witness proves failure at (e_0+e_1)/sqrt(2), and W_4 conjugacy transfers failure to all twelve diagonal mirrors.

### Ordinary positivity and coordinate RP

Each t -> exp(-lambda |t|) is positive definite on R for lambda>=0: for lambda>0 its Fourier measure has density 2lambda/(u^2+lambda^2), up to the Fourier normalization; for lambda=0 it is the constant covariance. Positive integration makes h positive definite. Products in separate coordinates make C positive definite on R^4. Dominated convergence gives continuity, and |C(x)|<=h(0)^4.

At a coordinate mirror, the reflected normal factor is

    h(t+s) = integral exp(-lambda t) exp(-lambda s) sigma(dlambda),

a positive kernel for positive t,s. Every tangential factor h(z_i-w_i) is an ordinary positive kernel. Their pointwise product is positive by the Schur product theorem, or directly by the tensor product of their positive-kernel feature representations. Integrating against complex tests yields coordinate covariance RP, and hence Gaussian RP. This verifies the full complex inequality, not merely positivity for real point values.

### Ultraviolet bound

For every compactly supported test f and f_d(x)=f(x/d), boundedness gives

    |Q_n(f_d)| <= h(0)^4 ||f_d||_1^2
                 = h(0)^4 ||f||_1^2 d^8.

Thus these anisotropic candidates satisfy O(d^8), which is much stronger than o(d^-2). The diagonal failure cannot be blamed on singular behavior at coincidence.

## 6. One exact three-point diagonal witness for the whole class

Assume sigma((0,infinity))>0. Fix any L>0 and let

    x_1 = ( L/2,   L/2, 0,0),
    x_2 = (3L/2,  -L/2, 0,0),
    x_3 = (5L/2, -3L/2, 0,0).

All three points lie strictly in the positive half-space of n=(e_0+e_1)/sqrt(2), with n dot x_i=L/sqrt(2). The reflection acts on the first two coordinates as

    theta_n(x_0,x_1) = (-x_1,-x_0).

Write h_j=h(jL), including h_0=h(0). The reflected matrix is exactly

    [C(theta_n x_i-x_j)]_{i,j=1}^3
      = h_0^2 [ [h_1^2,  h_0 h_2, h_1 h_3],
                 [h_0 h_2,h_1^2,  h_0 h_2],
                 [h_1 h_3,h_0 h_2,h_1^2] ].

With the fixed real coefficient vector v=(1,-2,1), the quadratic form equals

    Q_point = h_0^2 [6 h_1^2 - 8 h_0 h_2 + 2 h_1 h_3].

Cauchy–Schwarz in L^2(sigma) gives

    h_1^2 <= h_0 h_2.

Because sigma has positive mass on strictly positive lambda, h is strictly decreasing on [0,infinity). In particular h_1<h_0 and h_3<h_2. Every h_j is positive. Consequently

    Q_point <= 2 h_0^2 [h_1 h_3 - h_0 h_2] < 0.

This is an exact symbolic inequality for every admissible nonconstant h. It has no cancellation qualification and no smallness condition on the nonconstant spectral component. It includes a positive atom at lambda=0 mixed with any nonzero positive-mass component.

### A genuine smooth compactly supported witness

Let phi be a nonnegative smooth compactly supported unit-mass bump on R^4. Set phi_epsilon(x)=epsilon^(-4)phi(x/epsilon) and

    f_epsilon(x) = phi_epsilon(x-x_1)
                   - 2 phi_epsilon(x-x_2)
                   + phi_epsilon(x-x_3).

For sufficiently small epsilon, all supports remain strictly in the positive half-space. Continuity and boundedness of C imply

    Q_n(f_epsilon) -> Q_point < 0.

Therefore sufficiently small positive epsilon gives a legal real smooth compact test violating RP. A real test is also a complex test, so failure of the required complex inequality follows immediately.

### Single-exponential check

For h(t)=c exp(-m|t|), c,m>0, put a=exp(-2mL). The matrix calculation reduces to

    Q_point = 2 c^4 a(a-1) < 0.

This is a useful elementary sanity check, but the general proof does not split into atomic and non-atomic cases.

### Nonradiality away from the origin

These nonconstant kernels cannot be O(4)-invariant: coordinate RP plus O(4) invariance would transport RP to the diagonal mirror, contradicting the explicit witness. The obstruction uses only nonzero separated arguments theta_n x_i-x_j, whose normal component is -sqrt(2)L. Thus it is genuinely an off-origin distinction.

## 7. A concrete genuinely nonrational subclass

Take a nonzero finite positive measure mu supported on a compact interval [a,b] with 0<a<=b<infinity, and define

    g(z) = integral_[a,b] mu(ds)/(z+s),
    F(p) = product_{i=0}^3 g(p_i^2).

The one-dimensional inverse Fourier transform is

    h(t) = integral_[a,b] exp(-sqrt(s)|t|)/(2sqrt(s)) mu(ds).

This is a special case of Theorem B under the positive finite measure obtained by pushing mu(ds)/(2sqrt(s)) forward by lambda=sqrt(s). All the covariance, coordinate-RP, mild-UV and exact diagonal-failure conclusions therefore apply.

For example, mu(ds)=1_[a,b](s) ds with a<b gives

    g(z) = log((z+b)/(z+a)),
    F(p) = product_i log((p_i^2+b)/(p_i^2+a)).

The multiplier is not rational, and its per-coordinate logarithmic branch structure is not a polynomial numerator over a single radial resolvent. Its real-space covariance is bounded, continuous, W_4-invariant and coordinate-RP, yet the same three-point coefficients (1,-2,1) give a strictly negative diagonal reflected form for every L>0.

For mu=delta_(m^2), F(p)=product_i (p_i^2+m^2)^(-1), and h(t)=exp(-m|t|)/(2m). This supplies the simplest rational separable check.

## 8. Contacts, recovery conditions, and exact limits of the result

### Contacts cannot repair either obstruction

Any distribution supported at the spatial origin contributes zero when a test supported strictly in one open half-space is paired with its reflection. In the three-point construction, even the limiting pairwise arguments stay a fixed positive normal distance from the origin. Thus adding an arbitrary local contact term cannot change either negative witness.

For the finite ellipsoid theorem, polynomial contacts can simply be removed before taking the normal inverse Fourier transform: they contribute only derivatives of delta at normal time zero and hence vanish from K_k(t+s) for positive t,s.

### What these routes would have to change

- A finite positive mixture of ellipsoidal resolvents can recover all-mirror RP only by making every participating quadratic form isotropic.
- A separable product of identical bounded Laplace-mixture factors can recover diagonal RP only by making the factor constant, equivalently placing all sigma at zero.
- Adding more positive terms of the same finite ellipsoidal-resolvent type cannot cancel an existing shifted pole. The common-pole residues have the same phase.
- Increasing the spectral complexity of a separable factor, even to arbitrary continuous finite measures, does not help. The fixed three-point inequality remains strictly negative.

### What remains open here

- General stationary W_4-invariant scalar Gaussian covariances with all sixteen mirror RP conditions are not classified.
- Continuous mixtures over ellipsoidal matrices are not covered by the finite-pole proof. In particular, one must not conclude that every matrix in a continuous rotational average is isotropic; a rotation-averaged anisotropic ellipsoid can produce a radial covariance.
- Nonseparable nonpolynomial kernels are not covered by Theorem B.
- The finite-mixture theorem does not claim that signed mixtures have the same noncancellation property. Strict positivity of the weights is used exactly at that step.
- No conclusion is drawn for tensor-valued fields, gauge-invariant Yang–Mills observables, a continuum construction, a mass gap, or the applicability of any scalar spectral ansatz to an interacting theory.

These results eliminate two concrete escape routes. They neither prove a universal scalar rigidity theorem nor solve the actual Yang–Mills problem.

## 9. Relation to established pole criteria

The known rational reflection-positivity criterion excludes nonreal poles, repeated poles, and negative residues for rational functions of the Laplacian. Theorem A uses a direction-dependent pole calculation and a finite-exponential interpolation proof, so it does not assume global rotational invariance or apply that radial theorem outside its hypotheses.

Primary reference: F. Arici, D. Becker, C. Ripken, F. Saueressig, W. D. van Suijlekom, “Reflection Positivity in higher derivative scalar theories,” arXiv:1712.04308, Theorem 3.7 and Sections 3.2–3.3.

https://arxiv.org/abs/1712.04308
https://arxiv.org/html/1712.04308

The proofs in Sections 3–6 above are supplied explicitly and do not rely on a missing general spectral representation theorem.
