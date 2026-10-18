# Raw-companion audit: tilted period lattice versus stated volume theorems

Audit date: 2026-10-18. Pinned repository: ethanwsussman/Yang--Mills-LLM-experiment, commit `785a68fdeef78a1da854c4807fe1f17b597d05e7`.

Local files `raw_I.tex`, `raw_II.tex`, `raw_III.tex` are the root repository files `theorem_0_complete_account_raw_I.tex`, `theorem_0_complete_account_raw_II.tex`, `theorem_0_complete_account_raw_III.tex`. All line references below are to those files at this commit.

## Bottom line

There is an explicit **axis-aligned rectangular-torus extension** in the raw account. There is **no located Yang--Mills theorem quantifying over arbitrary period lattices or finite covers**, and no located theorem including

\[
\Lambda_N=\langle N(e_0+e_1),N(e_0-e_1),Ne_2,Ne_3\rangle
\]

with the original coordinate nearest-neighbour bonds and plaquettes. That extension still requires a new result, or a new proof that the needed hypotheses hold on this quotient. The rectangular result is a bounded short-distance comparison for two- and three-point functions, not equality of local states or shape independence of the thermodynamic limit.

The raw account expressly identifies box-shape independence and the additional diagonal reflection positivity needed for the proposed rotation argument as unproved. Its only explicit arbitrary-lattice shape theorem found is for **quasi-free Gaussian models**, not interacting Wilson Yang--Mills.

## 1. Base construction, correlation theorem, and local consistency remain cubic

- **Definition `1.1:def-lattice`**, raw I lines **403–447**, sets `T_m = R^4/(2L^m Z^4)` and the shifted coordinate lattice at spacing `L^{-K}`. The action is then defined on that lattice in `1.1:def-wilson-action`, lines **449–480**. [Source](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/theorem_0_complete_account_raw_I.tex#L403-L480)
- The correlation theorem does allow an additional arbitrary integer `N_T`, but this changes the common side count only. **Definition `5.1:def-torus-floor`**, raw II lines **679–686**, takes a torus of side 1, spacing `epsilon=L^{-K}N_T^{-1}`, and `N=N_T L^m` sites **per side** at the terminal lattice. **Theorem `5.1:thm-correlation-theorem`**, raw II **2791–2812, 2865–2874**, quantifies over every integer `N_T>=1` under this setting. It does not quantify over four independent periods, oblique periods, or a twist of the boundary gluing. [Setting](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/theorem_0_complete_account_raw_II.tex#L679-L686) · [Theorem](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/theorem_0_complete_account_raw_II.tex#L2791-L2874)
- **Definition `4.38:def-admissible-sites`**, raw I **57027–57092**, makes a site the pair `(m,K')` and its level-j torus `R^4/s_j Z^4`, with `s_j=2L^{m+K'-j}`. Thus “site-free,” “every torus,” and “cofinal exhaustion” in this section range over this family. [Source](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/theorem_0_complete_account_raw_I.tex#L57027-L57092)
- **Theorem `4.38:thm-torus-independence`**, raw I **58187–58285**, assumes the construction and its induction at every such site. Its clause (i) identifies non-wrapping *localized analytic terms* on common lifts. The proof in **`4.38:prf-proof-non-wrapping`**, **58416–58495**, explicitly uses intrinsic local walk ingredients. This is potentially reusable machinery, but it is neither a theorem constructing the expansion on a new quotient nor an equality of Gibbs marginals. **Volume-consistent families**, **60638–60661**, likewise use the already-defined cubic sites. [Statement/proof](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/theorem_0_complete_account_raw_I.tex#L58187-L58495) · [Families](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/theorem_0_complete_account_raw_I.tex#L60638-L60661)
- **Infinite-volume theorem `7.4:thm-infinite-volume`**, raw II **66412–66455**, takes sequences of cutoffs and the cubic exponents `m_j -> infinity`, with correlation/RP/per-ball bounds as assumptions. No general shape or boundary-condition family appears in this quantification. [Source](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/theorem_0_complete_account_raw_II.tex#L66412-L66455)

## 2. “Any torus” reflection/chessboard lemma means a coordinate product torus

**Lemma `8.7:lem-chessboard-torus`**, raw II **108696–108760**, has the title “Reflection positivity and the chessboard estimate on any torus,” but begins with

\[
\mathbb T=\prod_{\mu=1}^d\mathbb Z/n_\mu\mathbb Z.
\]

It allows arbitrary coordinate periods `n_mu>=3`, including odd periods. Its reflections are coordinate reflections with two fixed hyperplanes, and its tiles are products of coordinate intervals. The proof at **108763–108790** splits bonds/plaquettes between two closed coordinate arcs and the fixed planes; the all-directions step at **108920–108946** iterates the separate coordinate directions. Thus this is useful rectangular coverage, but does not itself cover a non-product period subgroup merely because it is finite index or invariant under a reflection. [Statement](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/theorem_0_complete_account_raw_II.tex#L108696-L108760) · [Proof geometry](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/theorem_0_complete_account_raw_II.tex#L108763-L108946)

The earlier **`6.1:lem-reflection-positivity`**, raw II **60440–60513**, is even more explicit about `R^4/NZ^4`, two antipodal link planes and two open components. A reflection preserving a quotient's period lattice is not by itself the separating-half geometry used in that proof. [Source](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/theorem_0_complete_account_raw_II.tex#L60440-L60513)

## 3. Trace/extensivity statements do not provide a finite-cover law transfer

**Lemma `8.22:lem-trace-subadditivity`**, raw II **140995–141054**, defines

\[
\mathbb T[\mathbf n]=\prod_{\mu=0}^3\mathbb R/(n_\mu\ell)\mathbb Z,
\qquad n_\mu\in2\mathbb N,
\]

and mirror-periodic complex source weights satisfying (M1) conjugate-reflection symmetry and (M2) vanishing on face-crossing plaquettes. It proves `0 <= Z_{n^(mu,k)}(W) <= Z_n(W)^k`, and iterates this for simultaneous coordinate multiplication.

The actual proof, **141179–141255**, closes the product with an ordinary trace, constructs a nonnegative trace-class `T=(AA*)^(n_0/2)`, and uses `Z_{n^(0,k)}=Tr(T^k)`, `Z_n=Tr(T)`. Its eigenvalue argument uses nonnegative eigenvalues. The scope remark **141259–141274** extends the gauge-group/plaquette-weight hypotheses, not the allowed gluing or covers. There is no assertion with a spatial translation inserted in the trace or with arbitrary deck transformations. A twisted closure is therefore an additional calculation/estimate, not an instance of the stated theorem. [Statement](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/theorem_0_complete_account_raw_II.tex#L140995-L141054) · [Proof and scope](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/theorem_0_complete_account_raw_II.tex#L141179-L141274)

**Lemma `8.22:lem-vacuum-energy-density`**, raw II **141276–141365**, compares the zero-source normalizing constants on two cubic tori, using exact extensivity of normalization counts and cancellation of matching non-wrapping localized terms. Its own scope remark, **141522–141538**, explicitly says this concerns the number `E_m`, says nothing about the bare measure or effective densities, and asserts no covariance for nonconstant sources. This blocks an inference from pressure/extensivity alone to local-state equality. [Source](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/theorem_0_complete_account_raw_II.tex#L141276-L141538)

**Theorem `8.22:thm-volume-transfer`**, raw II **141540–141583**, is explicitly conditional on RP, chessboard/placement/periodization/face/Schwarz–Cauchy inputs, correlation/stability, trace subadditivity, and vacuum-energy-density comparison. It concludes a uniform *bound* on the difference of two connected two-point functions on cubic tori at the same bare coupling and cutoff. The displayed bound does not tend to zero merely because the larger volume increases. [Source](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/theorem_0_complete_account_raw_II.tex#L141540-L141583)

## 4. Explicit rectangular extension: what is actually asserted

**Theorem `9.98:thm-short-distance-uniqueness`**, raw III **72033–72077**, lists its inherited correlation, volume-transfer and tuned-family/uniqueness assumptions, restricts `n` to **2 or 3**, and defines the short-distance error

\[
\tau_n=C^\star_{T,n}L^{-(4-n)\underline{s}'(g)}d^{4-n}\prod_i\|f_i\|_\infty.
\]

Clause **(f), Shapes**, **72174–72214**, explicitly replaces cubic tori by rectangular tori with each coordinate side `b` satisfying

\[
b\in 2\ell_n L^{\overline{s}'(g)}\mathbb N,
\qquad b\ge 2L^{m_\natural(g,n)}.
\]

The constants are enlarged to their convexity variants. The statement includes thermal boxes with three sides growing and the allowed fourth side fixed. It speaks of **cutoff-limit points** on the non-cubic rectangle, not convergence of the full cutoff sequence. [Theorem and assumptions](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/theorem_0_complete_account_raw_III.tex#L72033-L72214)

The proof is labeled **`9.98:prf-proof-rectangular-tori`**, **73847–74047**. Its printed heading says “Proof of (g)” although the current theorem labels Shapes as (f). Essential steps:

1. **73859–73893:** four side lengths give four separate even chessboard cell counts, dominating the reference cubic counts.
2. **73895–73920:** chessboard estimate and componentwise monotonicity of normalized rectangular partition functions. The text expressly says divisibility of the large counts by the small counts is unnecessary.
3. **73922–73975:** a cubic small-volume stability bound and a pressure sandwich between smaller/larger coordinate cubes, using a convexity lemma and a one-sided vacuum mismatch bound.
4. **73977–74037:** a bounded connected-function discrepancy through the reference cube; subsequential limits retain that bounded error.
5. **74031–74041:** thermal boxes and explicit denial of full cutoff convergence on a non-cubic rectangle.

It expressly says no Bałaban construction on the rectangle is used; the large rectangle needs the bare-measure RP, chessboard, monotonicity and convexity inputs (**73985–73989**). This is the best candidate blueprint for a new tilted-volume argument, but these inputs have not been established there for tilted gluing. [Proof](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/theorem_0_complete_account_raw_III.tex#L73847-L74047)

**Cross-reference and audit scope:** The raw rectangular proof appeals to a “convexity lemma” and a convexity variant of volume transfer without a named label at this passage. Searches confined to these three raw files found those references but not a separately stated pressure-convexity lemma with the constant `((2L-1)/(L-1))^4`; the explicit raw-II trace lemma itself states coordinate-multiple subadditivity. This is a cross-reference issue, not an unavailable prerequisite: **the main manuscript, Remark 6.6, page 97, explicitly establishes componentwise monotonicity of the normalized rectangular partition function using Schatten norms and the requisite convexity estimate, with exactly `c_L=((2L-1)/(L-1))^4`**. That manuscript passage has been checked in the companion main-manuscript audit. The rectangular route therefore has this identified supporting result. Neither that result nor the raw rectangular argument extends its quantification to tilted gluing. This report does not independently certify all other inherited inputs of the construction.

## 5. Direct disclaimers and the only general-shape theorem found

- **`9.98:rem-five-counter-states`**, raw III **75550–75578**, explicitly lists **independence of the shape of the torus** among properties not asserted. [Source](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/theorem_0_complete_account_raw_III.tex#L75550-L75578)
- **`10.1:rem-diagonal-positivity`**, **79931–79983**, treats diagonal RP as an additional hypothesis, neither assumed by Theorem 0 nor proved. It says that for the periodic family this would amount to box-shape independence, and explicitly says this is not proved. This is the raw account's most direct acknowledgment of the missing bridge. Its assertion that diagonal RP holds on `Z^4` and fails on straight tori is a source assertion here; this audit has not supplied a separate proof of that assertion. [Source](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/theorem_0_complete_account_raw_III.tex#L79931-L79983)
- The rotational-current discussion at **76766–76779** mentions the response to an infinitesimal/finite period-lattice tilt. Its proof at **76885–76888** expressly says the identification with an infinitesimal tilt response is **stated and not proved**. It cannot serve as the missing shape theorem. [Claim](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/theorem_0_complete_account_raw_III.tex#L76766-L76779) · [Proof disclaimer](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/theorem_0_complete_account_raw_III.tex#L76885-L76888)
- **`10.7:thm-quasi-free-boxes`**, **106138–106168**, does quantify over tori `R^4/(ell Lambda)` of **any lattice shape**, in clause (b). Its subject is centered Gaussian fields and local Wick polynomials. The other-shape proof is at **106250–106251**. This is not a Wilson-measure/correlation construction theorem. [Source](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/theorem_0_complete_account_raw_III.tex#L106138-L106251)

## 6. Consequence for the proposed Lambda_N route

Although the two diagonal period generators are orthogonal in Euclidean space, the rectangular theorem's sides and product graph are aligned with the **original coordinate bonds**. Rotating the period basis also rotates the coordinate lattice and plaquettes; it does not identify this Wilson graph with the axis-aligned rectangular graphs in the theorem. Likewise, an abstract isomorphism of finite site groups does not identify their designated nearest-neighbour generators and plaquettes.

The reusable pieces are local lifted geometry, admissible block partitions, compact-group positivity, and the rectangular transfer strategy. To turn those into the needed argument one must establish an appropriate tilted-boundary reflection/chessboard/trace or direct correlation theorem, including its normalization and source control. To identify the resulting limit with a pre-existing cubic limit, one additionally needs a local-observable/Schwinger-function comparison whose error actually vanishes in the relevant limiting procedure. Uniform pressure bounds, equality of pressure densities, index-two covering geometry, and vanishing density of a cut seam alone supply none of that identification.

Searches covered period lattices, oblique/tilted/skew/helical/twisted geometry, rectangular tori, finite covers, shape dependence, and boundary conditions, followed by inspection of the stated hypotheses and surrounding proofs. “Tilt”/“twist” elsewhere predominantly refers to source or configuration perturbations; “finite cover” hits concern covers by cubes/subcomplexes, not a global finite-cover theorem for Wilson measures. Local free/Dirichlet boundary conditions similarly concern localized operators, not the proposed periodic quotient.
