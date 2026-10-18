# Extensive analytic partition bounds do not imply differentiable pressure

18 October 2026. Exact test-family and normal-family analysis of a possible bridge; this is not a Wilson counterexample.

## Exact test family

Let V be a positive integer, let a random variable S_V equal V or -V with probabilities 1/2, and define the normalized partition function

Z_V(z) = E exp(z S_V) = cosh(Vz).

This is entire, Z_V(0)=1, and for every complex z,

|Z_V(z)| <= exp(V |Re z|) <= exp(V |z|).

Thus every fixed disk has a volume-extensive upper bound with a constant independent of V, even without any counterterm. Z_V(t)>0 on the real axis. For real t,

|t| - (log 2)/V <= V^(-1) log Z_V(t) <= |t|.

The limiting pressure is |t| and is not differentiable at zero. Its exact zeros are z=i*pi*(j+1/2)/V, j integer. No volume-independent disk supports a holomorphic logarithm. At t=0 the per-volume susceptibility is V, since Var(S_V)/V=V. This is a two-phase finite probability model, not a positive-temperature Wilson DLR example.

## Precise normal-family repair

If normalized pressures q_V(z)=V^(-1) Log Z_V(z) admit holomorphic branches on one fixed disk |z|<r, q_V(0)=0, and are locally uniformly bounded there, and the real thermodynamic limit exists on an interval about zero, then the limit is analytic near zero. Montel gives convergent subsequences on compact subdisks. Each subsequential limit agrees on the real interval; the identity theorem makes the limit unique. Therefore the pressure is differentiable at zero. This criterion needs uniform control of Log Z, not merely of Z.

A uniform upper bound Re q_V <= C on a slightly larger fixed disk, together with q_V(0)=0 and a zero-free holomorphic branch, also suffices by the Borel–Carathéodory estimate on smaller disks. The zero-free fixed disk is an essential additional input.

## Pinned manuscript comparison

Source: ethanwsussman/Yang--Mills-LLM-experiment, commit 785a68fdeef78a1da854c4807fe1f17b597d05e7, ym4_manuscript_zeroth_draft.pdf, printed pp.44–45, Theorem 3.1(d4),(e).

The displayed estimate (3.6) bounds |exp(-E(w)) Z(w)| by exp(c_vol(s)|Lambda_(K')|) Z(0). It is an upper bound for an analytic partition function with local counterterms. The stated logarithm domain in (e) has radius rho/(Q+1), Q=exp(c_vol*(2L^(m+b_*))^4), in the weighted source norm. For positive c_vol this guaranteed radius shrinks as the volume parameter m grows. The estimate does not by itself provide the fixed disk needed above. If c_vol vanishes, the displayed issue may disappear, but the theorem does not establish that vanishing and source-domain coverage remains a separate question.

The exact cosh family disproves the generic inference from an entire normalized partition function and an extensive modulus bound to differentiability of its thermodynamic pressure. It does not refute any Wilson-specific theorem or the manuscript's stated finite-volume conclusions. The companion `RESULT.md` audits whether the inspected source statements supply the missing uniform zero-free estimate and the necessary reflected-product source directions.
