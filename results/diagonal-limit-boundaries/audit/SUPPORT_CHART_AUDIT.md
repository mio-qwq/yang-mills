# Independent support-chart audit

Result: PASS. No substantive mathematical gap found.

Audited file: `ym-limit-next/SUPPORT_CHART_OBSTRUCTION.md`
SHA-256: `7cd662ea435e7d41bae659d5156a830713e3af1536c7955be85560ad8ac90d8f`
Date: 2026-10-17 UTC

The reflection lift classification is correct: any lift differs from coordinate swap by a constant period vector, and involutivity forces its first two entries to be opposite (and spectator shifts to vanish). Translating a coordinate chart and its reflection plane together does not alter signed normal distances. No unrelated mirror is tacitly permitted.

The individual positive gaps have residues epsilon h_p and epsilon h_q, each strictly between zero and ell. Positivity therefore forces each added integer period to be nonnegative. Their sum is at least epsilon(n-D). Admissibility implies 3D<=n-2, so the stated strict lower bound on maximum physical normal depth follows. Spectator plaquette edges change no normal coordinate, so there is no endpoint correction.

The compactness quantifier is correctly restricted to growing physical period ell, and remains valid after transporting the same reflection plane to a reference plane and applying plane-preserving isometries. Uniformly bounded normal distance alone already contradicts the inequality. This is not an obstruction on bounded-size physical tori, or to other witnesses, escape/decoupling arguments, or general continuum reflection positivity.

For the second theorem, (P-R_m Q)_0-(P-R_m Q)_1=g_P+g_Q exactly. The short displacement (-epsilon D,0) has negative normal component, contradicting two positive source gaps. The reflected separation lower bound follows directly from Cauchy–Schwarz in the two normal coordinates; additional spectator displacement can only increase its norm. The other cross-pair displacement is indeed the coordinate swap of this one. The exhibited unwrapped chart gives opposite-sign source gaps as claimed.

All shifts, lifts, geometric quantifiers, and strict constants checked. The conclusion excludes a direct scalar-normalization-only representation of this exact two-term witness by a common fixed compact positive-halfspace source; it does not claim to exclude alternative source constructions.
