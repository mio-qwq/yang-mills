# Independent mathematical audit

Result: PASS. No substantive gap found, conditional on the finite-torus all-beta theorem as expressly assumed by the audited document.

Audited file: `ym-limit-next/LIMIT_THEOREMS.md`
SHA-256: `dc1c05c2a100fea9ba9544cc8ef65c00398de350c5da3a892e689ac408a12970`
Date: 2026-10-17 UTC

## Checks

- Normalized SU(2) Haar radial density is (2/pi)sin²(theta). Concavity of sine on [0,1] gives sin(theta)>=theta sin(1), hence the stated c=2sin²(1)/(3pi).
- Bi-invariant distance and inversion invariance bound the plaquette angle by 4r. The global inequality 1-cos(t)<=t²/2 yields the asserted deficit bound even when 4r exceeds pi.
- For f=-log Z_0, f'=E S and f''=-Var(S). Concavity with f(0)=0 gives beta f'(beta)<=f(beta), in the correct direction.
- The all-links ball has probability at least (cr³)^(4n⁴), and N_e/N_p=2/3. Substitution r=(8beta)^(-1/2) gives exactly 1+(2/3)log(1/c)+log(8beta), with no omitted volume term.
- Translations and coordinate permutations equate plaquette deficit expectations; changes of canonical orientation do not affect the real normalized SU(2) trace. Thus division by N_p is justified.
- (d_p-d_q)²<=d_p²+d_q²<=2(d_p+d_q) gives factor 4. Measure preservation and Cauchy–Schwarz suffice for the reflected bound; reflection positivity is not assumed. Antilinear Theta gives |a|² for complex normalization. All vanishing and necessary-normalization conclusions follow, uniformly over varying volume and geometry.
- At s=0 the spectral series sums to Tr(B²T^n)/Z and remains absolutely summable. Pairing unequal eigenvalues gives exactly the displayed cosh ratio and mK contribution. Equal eigenvalues and diagonal elements contribute zero decrement. Pairwise monotonicity gives total m mass <= C(D)/V <=1.
- For D<d_a<=floor(n/2), each attenuation factor lies strictly between 0 and 1, so 0<K<2 (the stated <=2 is valid). The sufficient spectral-band condition and its converse use only total mass <=1 and K<=2. The converse threshold gamma/2 yields mass >=gamma/4 as claimed. The distinction between A and the possibly larger magnitude -Q is correctly maintained.
- In the two-state example the eigenvalues are 1,r, B swaps eigenvectors, V=1, the periodic mean of B is zero, and [B,T] is nonzero. Closing gap r_j=exp(-1/n_j²) gives uniform convergence C_n(s)->1 because both exponents have magnitude <=1/n_j. For fixed r, the chosen D_j and n_j-D_j both diverge, giving the claimed exponential disappearance.
- For n_j=8j,L_j=j,k_j=4j, n>=6L+5 and 3L+2<=k<=n-3L-3 hold for j>=3. The circular self-distances are 3j-1 and 3j, both strictly larger than D=2j+1 exactly for the stated range j>=3.

## Optional exposition clarification

Section 2 inherits noncommutation from the all-beta theorem. If its opening operator assumptions were read as a standalone abstract theorem, positivity/injectivity and nonconstant centered multiplication alone would not establish strict A>0 without the relevant noncommutation/strict-decrease hypothesis. The explicit inheritance and reference to that theorem make the present statement valid. Adding '[B,T] != 0' there would make that dependence even clearer.

No file in the proof directory was modified; no external publication or repository mutation was performed.
