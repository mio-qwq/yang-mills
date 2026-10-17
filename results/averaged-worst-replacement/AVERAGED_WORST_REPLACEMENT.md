# Averaging the reference environment does not rescue worst-replacement influence

2026-10-17. Root derivation for independent audit. This is a finite-volume obstruction to a particular comparison criterion, not a physical mixing or mass-gap statement. No novelty claim.

## Definition

Use the fully coupled periodic four-dimensional SU(2) Wilson measure at beta>=1, on a cubic torus of side at least four. For a target link e let eta denote all other links. Write gamma_e(.|eta) for its single-link conditional distribution. If f is one of its 18 distinct neighboring links lying on its six three-link staple paths, define

    c_ef(eta)=sup_(g in SU(2)) TV(gamma_e(.|eta),gamma_e(.|eta[f<-g])).

TV is normalized to lie in [0,1]. The supremum permits an arbitrary replacement of f while every other conditioning link stays fixed. We average c_ef over the actual Gibbs marginal of eta. This is NOT a random heat-bath replacement of f and not a claim about a Glauber spectral gap.

Let

    e(beta)=[1+log(8beta)+(2/3)log(3pi^3/8)]/beta,
    C=41472pi/sqrt(2).

Then

    E_beta c_ef >= max(0,1-1200e(beta)-2C exp(-beta/128)).

In particular this expected worst-replacement influence tends to one as beta tends to infinity, uniformly in the cubic torus volume. The expected sum over all18 neighbors tends to18. This rules out contraction of this particular averaged row-sum criterion in the weak-coupling limit.

## 1. Heat-bath concentration with explicit constants

Identify SU(2) with the unit sphere in R^4. A single-link conditional has density proportional to exp(beta a <U,v>), where a is the magnitude of the staple sum and v is its maximizing direction (a quaternion conjugation may enter depending on orientation; it preserves all distances).

For chord radius0<r<=1, the Haar probability of a chord ball of radiusr/2 is at least sqrt(2)r^3/(24pi). This follows from the cap integral in the previously reviewed seam probability proof. On that smaller cap, <U,v>>=1-r^2/8. Outside the radiusr cap, <U,v><=1-r^2/2. Comparing numerator with the normalized partition function gives

    P(|U-v|>=r) <= [24pi/(sqrt(2)r^3)] exp(-3beta a r^2/8).

Take r=1/12. For a>=3 this is at most C exp(-beta/128). If two centers are separated by more than2r, their radiusr caps are disjoint. Two such conditional distributions therefore have TV at least1-2C exp(-beta/128).

## 2. A worst replacement creates separated centers even when staples are aligned

Let V_1,...,V_6 be the six oriented unit-quaternion staples for e, S=sum V_i, a=|S| and v=S/a. Consider the event

    G={a>=6-1/200}.

Since all V_i have unit norm,

    sum_i |V_i-v|^2=12-2a<=1/100.

Hence every |V_i-v|<=1/10. A neighboring link f belongs to exactly one staple path, say the i-th. Its contribution is A U_f^(+/-1) B with other factors fixed, so changing U_f can replace V_i by any desired unit quaternion while leaving the other five staples unchanged. Choose a unit quaternion w perpendicular to v. Then

    S'=a v-V_i+w.

Its component along v is positive and at most5.1; its orthogonal component has norm at least0.9. Its magnitude satisfies |S'|>=a-2>3. Also a>3. Thus the angle theta between S and S' has tan(theta)>=3/17 and

    |v-S'/|S'||^2 >= 2-34/sqrt(298) > 1/36.

The final strict inequality is equivalent to 298*71^2>1224^2 (the integer difference is4042). The two centers are therefore separated by more than1/6=2r. Section1 gives c_ef(eta)>=1-2C exp(-beta/128) on G.

Attainability uses distinct staple-path links, valid for the stated torus size. A pointwise choice of w suffices for the supremum. The coefficient is measurable because the conditional density varies continuously with the compact finite-dimensional conditioning variables and replacement.

## 3. The aligned event is typical under the periodic measure

The previously independently audited periodic entropy bound gives E_beta H/N_p<=e(beta), with H=sum_p(1-w_p). Cubic symmetries identify all plaquette expectations. For the six plaquettes incident to e, pointwise

    sum_(p contains e)(1-w_p)=6-Re(U_e S)>=6-|S|.

Thus G^c implies incident energy deficit greater than1/200. Markov's inequality gives

    P_beta(G^c)<=200*6e(beta)=1200e(beta).

Although the incident energy uses U_e, G depends only on eta, so this is a bound for the same conditioning marginal used in the definition of c_ef. Combining sections1--2 and c_ef>=0 gives

    E_beta c_ef >= P_beta(G)-2C exp(-beta/128)
                >=1-1200e(beta)-2C exp(-beta/128).

All constants are volume-independent. Since c_ef<=1 and e(beta)->0, the stated limit follows. Summing the finite18 terms gives the row-sum limit.

## 4. Scope and stop condition

Unlike the earlier cancellation construction, this obstruction occurs with high probability over the reference environment: nearly aligned staples suffice. It still optimizes over an arbitrary neighboring-link replacement, which can be atypical for the Gibbs distribution. Therefore it does not rule out a coupling that averages over actual updates, a block argument, a suitable gauge-invariant metric, or physical mass-gap behavior.

The result specifically prevents using rarity of small |S|, even combined with averaging the base environment, to justify contraction of E[sup_replacement TV]. Exchanging that supremum for an expectation over an actual replacement law changes the mathematical problem and requires its own proof.

Dependencies: the elementary SU(2) cap-volume bound, the periodic entropy estimate in results/staple-probability/PERIODIC_BAD_STAPLE_BOUND.md, and the exact local staple geometry. No continuum hypothesis is imported.
