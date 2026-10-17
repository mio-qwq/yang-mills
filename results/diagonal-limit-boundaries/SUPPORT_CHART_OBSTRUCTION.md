# The two-plaquette witness cannot become a fixed compact Euclidean halfspace source

17 October 2026. Exact geometry of the existing witness only. This does not exclude other lattice witnesses, other smearings, or any continuum theory. No frozen proof or repository was modified.

## Setup

Suppress spectator coordinates 2,3, which have no effect on the following normal-coordinate argument. On (Z/nZ)^2 let

    p=(a,k), q=(k,L), a=n-1-L, D=2L+1,
    theta(x0,x1)=(x1,x0),
    3L+2<=k<=n-3L-3, n>=max(8,6L+5).

Define h_p=a-k and h_q=k-L. Then

    0<h_p<n, 0<h_q<n,
    h_p+h_q=n-D,
    3D=6L+3<=n-2, so D<n/3.                            (1)

Let epsilon>0 be lattice spacing and ell=n epsilon the physical period. Allow ANY lifts of p,q to the covering Euclidean plane:

    P=epsilon(a+rn, k+sn),
    Q=epsilon(k+tn, L+un),                 r,s,t,u in Z. (2)

Allow also any involutive affine Euclidean lift of the specified swap reflection that projects to the original torus swap. Every such lift has the form

    R_m(X0,X1)=(X1+m ell, X0-m ell),        m in Z.       (3)

Its fixed line is H_m={X0-X1=m ell}, and choose the positive halfspace H_m^+={X0-X1>m ell}. Formula (3) is exhaustive: a lift of swap has the form swap plus an integer-period vector; the condition R^2=id forces that vector to be (m ell,-m ell). The plane can equivalently be written through the point (m ell/2,-m ell/2); thus half-period shifts of its coordinate intercepts are included. Tangential changes of origin do not change the argument. The same argument in four dimensions uses the fixed hyperplane with spectator coordinates arbitrary.

A reflection-compatible Euclidean realization uses R_m P and R_m Q as the lifts of the reflected observables. Independently choosing unrelated lifts for the reflected points would not describe a single Euclidean reflection quadratic form.

## Theorem 1: positive-halfspace lifts necessarily have macroscopic depth

If P,Q both belong to H_m^+, then

    dist(P,H_m)+dist(Q,H_m) >= epsilon(n-D)/sqrt(2),
    max(dist(P,H_m),dist(Q,H_m))
                         >= epsilon(n-D)/(2 sqrt(2))
                         > ell/(3 sqrt(2)).              (4)

These bounds hold for every allowed L,k,n, all lifts (2), and every reflection lift (3).

### Proof

The signed normal gaps, before division by sqrt(2), are

    g_P=P0-P1-m ell=epsilon[h_p+(r-s-m)n],
    g_Q=Q0-Q1-m ell=epsilon[h_q+(t-u-m)n].

Each h lies strictly between 0 and n. Therefore positivity of a gap forces its integer multiple of n to be nonnegative. Consequently g_P>=epsilon h_p, g_Q>=epsilon h_q. Sum and use (1). Division by sqrt(2) converts a coordinate gap to Euclidean distance; the maximum is at least half the sum. Finally n-D>2n/3. This proves (4).

The plaquettes themselves extend only in coordinates 2,3. Every endpoint of each lifted plaquette therefore has exactly its basepoint's normal gap. There is no O(epsilon) support correction in (4).

## Corollary: no fixed compact positive-halfspace support as ell→infinity

Consider ANY sequence of admissible n_j,L_j,k_j and spacings epsilon_j with ell_j=n_j epsilon_j→infinity. It is impossible to lift the two source plaquettes reflection-compatibly so that both remain in one fixed compact subset of a Euclidean positive halfspace, even after translating each fixed hyperplane H_(m_j) to the reference diagonal plane and applying isometries preserving that plane.

Indeed, the distances of points in such a fixed compact set to the reference plane have a finite common upper bound, contradicting (4). The conclusion also applies to a family of source supports contained in a uniformly bounded-distance region relative to the reflection plane. It is independent of scalar normalization of the observables.

Thus multiplying this precise two-plaquette witness by a diverging scalar cannot, by itself, turn it into a discretization of a fixed compact Euclidean positive-halfspace test in a growing-physical-volume limit. If a coefficient is set identically to zero, that is a different witness and the original two-term sign proof does not apply. Weak-limit mechanisms in which one source escapes to infinity and decouples would require separate observable/limit arguments; they are not a representation by the same fixed compact source.

The result covers n→infinity at fixed lattice spacing and continuum/infinite-volume sequences with epsilon→0 and n epsilon→infinity. It does NOT assert a support obstruction merely from n→infinity if n epsilon remains bounded: a fixed-size physical torus is not Euclidean infinite volume.

## Theorem 2: preserving the short cross-pair geometry conflicts with positivity

The cross pair p,theta q has torus displacement (n-D,0), whose unique shortest Euclidean representative is (-D,0), since D<n/2. If a reflection-compatible choice of lifts retains this short displacement, namely

    P-R_m Q=(-epsilon D,0),                             (5)

then P,Q cannot both lie in H_m^+. More generally, every choice with both in H_m^+ satisfies

    |P-R_m Q| >= epsilon(n-D)/sqrt(2) > sqrt(2)ell/3.     (6)

Thus the short cross-correlation used by the finite-torus proof cannot remain a bounded Euclidean reflected separation in positive-halfspace charts as ell→infinity.

### Proof

For arbitrary P,Q and R_m,

    (P-R_m Q)_0-(P-R_m Q)_1 = g_P+g_Q.                  (7)

Under (5) the left side is -epsilon D<0, whereas positivity of both source gaps makes the right side positive. This is impossible.

For positive lifts, Theorem 1 gives g_P+g_Q>=epsilon(n-D). For every Euclidean vector v, |v0-v1|<=sqrt(2)|v|. Apply this to v=P-R_m Q and use (7) to obtain (6). Extra spectator-coordinate displacements can only enlarge the distance.

In fact this conflict is exact at every finite n; it is not an asymptotic estimate. Under (5), the opposite cross pair satisfies R_m P-Q=(0,-epsilon D), since its displacement is the coordinate swap of P-R_m Q. It gives the same contradiction after the corresponding choice of normal orientation.

## Natural unwrapped chart

Take m=0 and the usual short-wrap choices

    P=epsilon(-1-L,k), Q=epsilon(k,L).

Then

    P-theta Q=(-epsilon D,0),
    theta P-Q=(0,-epsilon D),
    P0-P1=-epsilon(k+L+1)<0,
    Q0-Q1=epsilon(k-L)>0.

This chart retains the very cross separation whose covariance dominates the proof, but it places the two source plaquettes on opposite sides of the true Euclidean diagonal plane. The general theorems show this is not a removable defect of that particular chart.

## Scope relative to the fixed-source continuum requirement

The audited source's infinite-volume formulation requires fixed compact separated physical source tuples transported to sufficiently large tori. For this exact two-plaquette witness, the following are distinct obstacles:

1. Raw amplitudes vanish uniformly as beta→infinity, by LIMIT_THEOREMS.md.
2. The two elementary shrinking plaquettes are not yet a fixed smooth test-function observable.
3. Even allowing arbitrary scalar normalization, reflection-compatible positive-halfspace lifts cannot keep their supports in a fixed compact physical region when the physical torus extent grows.

Item 3 is purely geometric and does not depend on Wilson dynamics, spectral gaps, beta scaling, convergence rates, or smoothness. It excludes a direct normalization-only conversion of this witness into the required fixed compact Euclidean halfspace source. It does not exclude a newly designed smeared or differently located witness, nor prove or disprove continuum diagonal reflection positivity.
