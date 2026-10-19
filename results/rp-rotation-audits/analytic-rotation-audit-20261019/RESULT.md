# Analytic rotation claim: exact hypotheses and applicability audit

Date: 2026-10-19. Upstream repository pinned throughout at commit `785a68fdeef78a1da854c4807fe1f17b597d05e7`.

## Result

1. The scalar two-point implication in raw III, Remark `10.1:rem-diagonal-positivity`, is conditional on one-field diagonal reflection positivity, a separated-support bound, and a specific logarithmically improved small-scale upper bound. It is **not** a deduction from the finite reflection group alone. Nothing here refutes that implication.
2. The exact scalar theorem named without a number in that remark, and the separately named bounded-kernel theorem, were **not located in the searched pinned raw I–III or the four pinned QED3 PDFs**. This is a bounded source-location result, not a claim that no proof exists elsewhere.
3. A substantial, explicit analytic rotation proof **was** located: Theorem A of the pinned 18-page *Rotation invariance from lattice symmetry and reflection positivity*, plus §18 of the pinned *QED3 manuscript*. These prove results for globally Gaussian-dominated laws of **closed distributional two-forms**, with reflection positivity of the characteristic functional. They are not the scalar theorem referred to in the raw YM4 remark.
4. There is a precise obstruction to directly substituting Theorem 0's scalar action density into that available theorem. Its global Gaussian (L^2) domination would imply a covariance bound (O(d^4)) for explicit admissible fixed-height bumps, whereas the lower witness bound of Theorem 0(iv), if assumed, is at least (c/(1+\log(1/d))^2\). Therefore those two assumptions are incompatible for this scalar density. This is **conditional on the stated lower bound** and rules out that direct shortcut. It is not a claim that Theorem 0 is inconsistent, and it does not allege that an author made this substitution.

## 1. What the YM4 observable actually is

Raw I, lines 696–705, defines

\[
\mathcal O(f)=\sum_p f(x(p))[1-\operatorname{Re}\operatorname{tr}U(\partial p)].
\]

The sum includes all six plaquette orientations. This is a **scalar Wilson action density**, which the manuscript also calls its curvature field. The same paragraph explicitly distinguishes it from tensor components. In particular it is not the distributional two-form (F\) of Theorem A below.

Raw I, lines 724–746, defines the connected Schwinger functions as ordinary derivatives of \(\log Z\), hence ordinary connected expectations. At order two the centred moment and connected covariance agree. There is no additional factor of (d\), a test normalization by its integral, or a scale-dependent rescaling in this definition.

Sources: [observable and norm, raw I lines 696–713](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/theorem_0_complete_account_raw_I.tex#L696-L713), [covariance definition, lines 724–746](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/theorem_0_complete_account_raw_I.tex#L724-L746).

## 2. Exact hypotheses used by the scalar remark

The remark takes a subsequential infinite-volume continuum limit \(\sigma\) of Theorem 0(ii–\(\mathbb R^4\)), at a sufficiently small reference coupling \(g\le\gamma_W^{\mathbb T}(\vartheta_0)\), for an unspecified pure \(0<\vartheta_0\le1\). Its assumptions are:

- (a) Translation and \(W_4\) invariance, plus reflection positivity **on one-field vectors** at coordinate mirrors.
- (b) The per-ball position-uniform bound (iii-b).
- (c) The **upper** member of (iv), including its logarithmic factor, for the approximating family.
- (d) Reflection positivity **on one-field vectors** at the one diagonal mirror normal to \((e_0+e_1)/\sqrt2\), in the same scalar sense as (a).

The desired conclusion is equality of \(S_2[\sigma](R\cdot f_1,R\cdot f_2)\) and \(S_2[\sigma](f_1,f_2)\) for every \(R\in O(4)\) and real compactly supported \(C^1\) tests with disjoint supports. The text expressly restricts this implication to two points and says that (b) enters only qualitatively. It says the proof is in an unnamed theorem and is not reproduced there. \(W_4\) invariance transports (d) to the other eleven diagonal mirrors; this transport does not itself generate continuous rotations.

Source: [raw III lines 79931–79989](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/theorem_0_complete_account_raw_III.tex#L79931-L79989).

### 2.1 Clause (iii-b)

For each \(n\ge2,R>0,d>0\), there is a finite constant \(C_n^\infty(d;R)\), independent of cutoff, bare coupling, volume, and positions, such that

\[
|S^T_{n;K,m}(f_1,\ldots,f_n)|\le C_n^\infty(d;R)\prod_i\|f_i\|_\sharp,
\qquad
\|f\|_\sharp=\max(\|f\|_\infty,40M\operatorname{Lip}f).
\]

Each support must lie in a radius-\(R\) ball, with pairwise distances at least \(d\); the stated volume floor must also hold. The constant is nonincreasing in \(d\), but **no decay in \(d\)** is asserted. Thus this is local regularity for separated observations, uniform over their positions. It is not global boundedness of an unsmeared kernel, nor an (L^2\)-operator bound, nor a uniform bound as supports collide.

The limit clause grants distributions of locally finite order off coincident points, but expressly does not assert temperedness, field operators, coinciding-point extensions, or a full relativistic spectral cone.

Sources: [raw I lines 2610–2621](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/theorem_0_complete_account_raw_I.tex#L2610-L2621), [limit and exclusions, lines 2689–2713](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/theorem_0_complete_account_raw_I.tex#L2689-L2713).

### 2.2 Clause (iv), including its test class and quantifiers

For each fixed \(0<\vartheta\le1\), choose its coupling ceiling \(\gamma_W^{\mathbb T}(\vartheta)\). The class \(\mathfrak T(d;\vartheta)\) consists of pairs of nonzero nonnegative Lipschitz tests satisfying

\[
\begin{split}
&\operatorname{supp}f_i\subset B(a_i,d),\\
&\int f_i\ge\vartheta\|f_i\|_\infty d^4,\\
&\operatorname{Lip}f_i\le\|f_i\|_\infty/(\vartheta d),\\
&d\le\operatorname{dist}(\operatorname{supp}f_1,\operatorname{supp}f_2)\le6d.
\end{split}
\]

Let

\[
s(d)=\min\{s\ge0:C_W(s)L^{-s}\le d\},
\]

where \(C_W(s)\ge1\) is nondecreasing and polylogarithmic in \(g^{-2}+B_\sharp(s+1)\). There are three fixed depth floors, and one needs \(s(d)\) above them and \(K-s(d)\ge k_W\). For the stated coupling and volume ranges the two witness inequalities are

\[
\frac{(2/9)b_0c_{\mathcal K}\|f_1\|_\infty\|f_2\|_\infty}
{[g^{-2}+B_\sharp(s(d)+1)]^2}
\le S^T_{2;K,m}(f_1,f_2)
\le
\frac{(8/3)b_0C_{\mathcal K}\|f_1\|_\infty\|f_2\|_\infty}
{[g^{-2}+\lambda_\sharp s(d)-c_5]^2}.
\]

At fixed \(d\), these pass to any stated infinite-volume continuum subsequence after the cutoff becomes large enough. Only then is \(d\to0\) taken. The claim is not that a fixed cutoff permits arbitrarily small \(d\).

Sources: [constants and scale, raw I lines 2720–2746](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/theorem_0_complete_account_raw_I.tex#L2720-L2746), [test class and full bound, lines 2758–2789](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/theorem_0_complete_account_raw_I.tex#L2758-L2789).

### 2.3 Standing Theorem 0 prerequisites

These are not free hypotheses for an arbitrary kernel. Theorem 0's setting is the four-dimensional periodic Wilson \(\mathrm{SU}(N)\) model, with clauses (ii)–(vi) stated at \(N=2\); an odd sufficiently large blocking factor \(L\); the specified ordered auxiliary-parameter choices; small reference coupling; its volume floor; small bare coupling and first-passage cutoff; and the additional source-radius-dependent coupling ceiling. Clause (iv) has its \(\vartheta\)-dependent ceiling and auxiliary lower bounds. The extra far-sphere flux hypothesis belongs to clause (vi), not to the scalar remark's displayed (a)–(d).

Sources: [H1–H7, raw I lines 1126–1205](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/theorem_0_complete_account_raw_I.tex#L1126-L1205), [Theorem 0 prefix, lines 2512–2532](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/theorem_0_complete_account_raw_I.tex#L2512-L2532).

## 3. The actual analytic proofs located

### 3.1 Simplified theorem, valid in dimension (d\ge3\)

[Pinned *Rotation invariance from lattice symmetry and reflection positivity*](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/QED3_slop/YM_Rotation_Invariance_simplified.pdf), pp. 1–2, Theorem A, assumes:

1. A Borel probability law \(\mu\) on tempered distributional real **two-forms**.
2. The ordinary closedness equation \(dF=0\), almost surely.
3. The **global** estimate \(\mathbb E_\mu e^{F(\chi)}\le e^{C\|\chi\|_2^2}\), for every real Schwartz two-form test \(\chi\).
4. Translation and signed-permutation invariance, with the tensor pullback on forms.
5. Reflection positivity of the **full characteristic functional** across both \(t=0\) and \(t+x=0\), for all finite families of same-side tests.

It concludes invariance of the full law under Euclidean isometries, every-order moment covariance for arbitrary (L^2\) two-form tests, and RP at every affine plane. It does not assume or invoke the YM4 scalar two-point logarithmic bound.

The proof is substantive:

- pp. 4–6, §3: constructs coordinate and diagonal reflection Hilbert spaces; compares two spectral representations of the same correlation; obtains \(H\ge|P|\). The spaces need not be identified and the second spectral measure may be complex, with controlled total variation.
- p. 6: explicit Laplace probes \(e^{-j}z^{1-4i\varepsilon j/\pi}(1+z)^{-3}\) exclude \(|p|>\omega\). I visually checked the page: the integrated tests are \(h(a)\overline{h(c)}\), so the apparent missing conjugation in text extraction is not an error.
- pp. 6–10, §4: analytic continuation and an angular-frequency bound of order \(2N\).
- pp. 10–12, §5: positivity and a tilted-frame sign comparison eliminate remaining frequencies, using all moment orders.
- pp. 13–16, Appendix A: Gaussian domination yields the time-slab source estimate and bounded insertion operators, which supply analytic-kernel estimates.
- pp. 17–18, Appendix B: closedness removes possible planar-contact defects.

This audit establishes the exact proof route and its hypotheses; it is not a line-by-line certification of the entire theorem.

### 3.2 QED3 precursor

[Pinned *OS axioms for the field strength tensor in three-dimensional electrodynamics*](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/QED3_slop/qed3_manuscript.pdf): Theorem 1.2, p. 4; Proposition 18.1, pp. 104–106; Theorems 18.20 and 18.21, pp. 122–123. These supply a closely related argument in three dimensions, again for a Gaussian-dominated, closed field-strength law. The simplified paper cites a supplied manuscript named `qed3_manuscript(2).pdf`; the repository file has the same title and matching §18 numbering/content, but the filename is not identical. I therefore record it as the matching public precursor, not a byte-certified copy of the separately named supplied file.

The other pinned PDFs, `qed3.pdf` and `qed3-consequences.pdf`, were also downloaded and searched. They do not supply the exact missing scalar YM4 two-point theorem under the remark's (a)–(d) in the passages located by this audit.

## 4. A precise direct-substitution obstruction

### Proposition (conditional on the Theorem 0(iv) lower witness)

Fix admissible parameters and \(g\le\gamma_W^{\mathbb T}(1/2)\). Suppose an infinite-volume two-point functional satisfies Theorem 0(iv)'s lower witness after the prescribed continuum passage. It cannot be the covariance of a scalar random distribution (X\) satisfying

\[
\mathbb E e^{X(f)}\le e^{C\|f\|_{L^2(\mathbb R^4)}^2}
\]

for all real tests, with finite (C\) independent of the tests. The same conclusion holds if (X\) is the centred action density.

**Proof.** Apply the exponential bound to \(tf\), for both signs of real \(t\). Expansion at zero gives mean zero and

\[
\mathbb E|X(f)|^2\le2C\|f\|_2^2.
\]

Cauchy–Schwarz therefore gives

\[
|S_2(f_1,f_2)|\le2C\|f_1\|_2\|f_2\|_2. \tag{G}
\]

Choose the explicit (C^1_c(\mathbb R^4)\) bump

\[
\varphi(x)=(1-|x|^2)_+^2,\qquad
f_{1,d}(x)=\varphi(x/d),\qquad
f_{2,d}(x)=\varphi((x-4de_0)/d).
\]

Direct calculation gives

\[
\|f_{i,d}\|_\infty=1,\quad
\int f_{i,d}=\frac{\pi^2}{12}d^4,\quad
\|f_{i,d}\|_2^2=\frac{\pi^2}{30}d^4,\quad
\operatorname{Lip}f_{i,d}=\frac8{3\sqrt3}\,d^{-1}<2d^{-1}.
\]

Their supports are radius-(d\) balls with distance exactly (2d\). Since \(\pi^2/12>1/2\), this pair belongs to **exactly the stated class** \(\mathfrak T(d;1/2)\). At small (d\) it embeds into the stated tori without wrapping. It also belongs to the limit's (C^1\) test class. If one starts Gaussian domination on Schwartz tests only, the resulting (L^2\) bound extends it to these (C^1\) tests by approximation; this is also part of Theorem A's conclusion.

By (G),

\[
|S_2(f_{1,d},f_{2,d})|\le \frac{C\pi^2}{15}d^4. \tag{1}
\]

By the witness lower bound, first fixing (d\) and passing (K,m\to\infty\) along the stated subsequence,

\[
S_2(f_{1,d},f_{2,d})\ge
\frac{(2/9)b_0c_{\mathcal K}}{[g^{-2}+B_\sharp(s(d)+1)]^2}. \tag{2}
\]

Here (s(d)\to\infty\), so all fixed lower depth floors eventually hold. The polylogarithmic growth of (C_W\) gives

\[
s(d)=O(1+\log(1/d)).
\]

For completeness, with (u=\log_L(1/d)\), take (s=\lceil2u\rceil\). For small (d\), the polylogarithm (C_W(s)\) is at most (d^{-1}\), while (L^{-s}\le d^2\), so this (s\) qualifies in the minimum defining (s(d)\). Thus (2) is at least (c_g/(1+\log(1/d))^2\) for some (c_g>0\). Since

\[
d^4(1+\log(1/d))^2\longrightarrow0,
\]

(1) and (2) contradict one another. ∎

**Scope.** The lower half of (iv) is used here only to exclude identifying the actual Theorem 0 scalar witness with a globally Gaussian-dominated (L^2\) field. The scalar remark itself assumes only the upper half. This calculation does **not** refute its conditional implication, or any alternative proof using the upper half in a different way. No authorial use of the unavailable shortcut is asserted.

## 5. The missing applicability bridge

The available Theorem A cannot be invoked simply by citing clauses (iii-b), (iv), and one-field diagonal RP:

- its variables are a closed two-form with tensor pullback; Theorem 0's variables are scalar action-density insertions;
- its global (L^2\) exponential estimate is different from separated-support (C^1\) bounds and a small-scale positive-bump estimate; the direct scalar substitution is excluded above if the lower witness is retained;
- it has a full probability law and all-order characteristic-functional RP; the extra diagonal assumption in the scalar remark concerns only one-field vectors;
- its analytic insertion estimates use precisely that global Gaussian bound; its contact-removal argument uses precisely closedness; neither step is supplied by the displayed scalar assumptions as an instance of this theorem.

What remains needed is a **separate scalar two-point analytic result**, with its hypotheses explicitly matching (a)–(d), or a fully written reduction of those scalar hypotheses to an applicable theorem. A possible proof might adapt the spectral comparison and use the logarithmic short-distance improvement differently, but that is an additional theorem to establish, not an implication certified by this audit.

Also, the bounded-kernel assertion at the end of the remark does not automatically apply to the action-density kernel. A globally bounded kernel would itself give (O(d^8)\) for these fixed-height bumps, again incompatible with the lower witness. Global boundedness and position-uniform separated-support estimates must remain distinct.

## 6. Source-search scope and reproducibility

- The exact upstream tree was retrieved at the pinned SHA, with `truncated=false`; it contains the three raw parts, raw master, YM4 draft PDF, README files, and four QED3-folder PDFs. `UPSTREAM_TREE.json` preserves that inventory.
- `SOURCE_MANIFEST.json` records byte sizes, SHA-256, computed Git blob hashes, exact paths, and immutable URLs for the seven principal files audited here. Raw-file hashes match the earlier pinned manifest. Downloaded PDF Git blob hashes match the pinned tree.
- `RAW_SEARCH_HITS.json` records literal searches for the two theorem references and nearby terminology across all three raw parts. Their matches occur only in the remark. Additional searches inspected rotation, spectral, positivity, and analytic-growth passages, plus the related public PDFs. This is not a formal proof of textual absence under arbitrary wording.
- `PINNED_EXTRACTS.txt` preserves numbered source ranges for the definitions, prerequisites, theorem clauses, remark, and the later threshold-countermodel statement.
- `audit_sources.py` is newly written, local, read-only analysis code; it verifies source hashes and exact radial integrals, and creates the audit metadata. No upstream repository code was executed. `CHECKS.json` records the test-function calculations.
- `theoremA-page2.png` and `spectral-page6.png` were rendered and visually checked to verify the theorem assumptions and the conjugation/probe formulas.

No remote repository was modified, no research PR was merged, no release was published, and no third party was contacted.
