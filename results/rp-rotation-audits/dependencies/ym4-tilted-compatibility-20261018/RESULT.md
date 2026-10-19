# Tilted Wilson volumes versus the pinned YM4 construction

18 October 2026. This is a compatibility audit, not an audit of the full Yang–Mills construction or a mass-gap claim.

## Result

The new tilted-volume reflection-positivity construction is valid at fixed cutoff, but it is **not already covered by the quantifiers of the reference YM4 theorem**. The main manuscript fixes straight cubic tori. The raw companion account additionally states an axis-rectangular extension, under even coordinate chessboard-cell counts. Neither source quantifies over arbitrary period lattices or arbitrary finite covers in the way needed for the tilted quotient.

This is more than an omitted word in a theorem statement: the tilted geometry loses the separating coordinate-reflection cuts in directions 0 and 1 that drive the manuscript's chessboard estimates and untwisted trace-power comparison. It also loses finite-volume invariance under coordinate permutations exchanging the distinguished pair {0,1} with {2,3}. Its local weak limits might regain these properties, but that is a further result, not a consequence of translation invariance or pressure equality.

A useful exact comparison is available: the tilted partition function is a **twisted transfer trace**, Tr(T^N J), where J is a spatial half-period translation. This gives a one-sided real partition-function comparison, but not equality of local Wilson states and not the complex-source comparison used in the manuscript.

## 1. Sources and what they actually quantify over

Pinned repository: `ethanwsussman/Yang--Mills-LLM-experiment`, commit `785a68fdeef78a1da854c4807fe1f17b597d05e7`.

Main manuscript:
https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/ym4_manuscript_zeroth_draft.pdf

The PDF is dated 6 October 2026 and has 153 pages. Printed page numbers equal PDF page numbers. Relevant exact locations:

- Section 1.2, p. 7: T_m = R^4/(2 L^m Z^4); bare sites are epsilon (Z+1/2)^4 modulo the same coordinate period lattice, epsilon=L^(-K).
- Hypothesis (H1), p. 10: Wilson SU(2) on that periodic torus T_m. Hypothesis (H5) is only a lower bound on the cubic exponent m, not a quantifier over shape.
- Theorem 0 inherits (H1)–(H7), including this volume family. At fixed cutoff the lattice side is 2 L^(K+m).
- Theorem 3.1, pp. 44–45, assumes (H1)–(H6) and quantifies over m and g_0. Its local sourced-vacuum decomposition and extensive complex-source bound are not stated on arbitrary covers. Remark 3.2's free integer n_T describes a larger family of **cubic** side-one discretizations, not an arbitrary period lattice.
- Lemma 6.4, pp. 95–96, genuinely treats rectangular T[n] = product_mu R/(n_mu ell Z), all n_mu even, and coordinatewise multiplication of one side. Remark 6.5(iii) specifies that the intermediate rectangular tori carry only the bare measure. Remark 6.6 also gives coordinatewise monotonicity without divisibility.
- Lemma 6.7, pp. 98–99, identifies nonwrapping localized terms across the cubic family. It explicitly defines lifts modulo s Z^4 and quantifies over m. It does not itself extend the construction to another quotient.
- Lemma 6.8, pp. 99–100, compares vacuum constants on two cubic tori using the q^4-sheeted coordinate cover for q=L^(m-m'). Its proof has an adaptable short-domain orbit-counting part, separated below from the unproved extension of its inputs.
- Theorem 6.13, pp. 102–105, compares local two-point functions on two members of the cubic family. Corollary 6.19, p. 107, improves the difference to a short-distance d^2 bound; it does not make it vanish as the volume increases at fixed positive d. Remark 6.28, pp. 111–112, explicitly declines uniqueness/convergence of the infinite-volume state.

The raw companion source has a genuine but limited extra shape statement:

- `theorem_0_complete_account_raw_III.tex`, label `9.98:thm-short-distance-uniqueness`, clause (f), lines 72174–72214: its short-distance conclusions also apply to **axis-rectangular tori** whose four side lengths are specified even multiples of the coordinate cell side and exceed the reference side. It says the RG is needed only on two reference cubic tori; all other rectangular volumes use coordinate link RP, chessboard, transfer, and convexity bounds. The proof is at lines 73847 ff. This is not a skew/tilted extension and not exact shape-independence.
- The same file, label `10.1:rem-diagonal-positivity`, lines 79931–79983, explicitly treats diagonal RP for the prescribed continuum limit as an additional hypothesis not proved or assumed by Theorem 0. Its discussion identifies box-shape independence as the missing type of input. We use this as a scope disclaimer, not as an independently proved equivalence between every possible form of scalar RP and full state independence.
- The raw sources' broad-looking chessboard and transfer statements still define product coordinate tori: raw II, `8.7:lem-chessboard-torus` at line 108696; `8.22:lem-trace-subadditivity` at lines 141001–141054, with its positive trace-power proof at 141190–141255.

See `RAW_PERIOD_AUDIT.md` for the companion-source audit and exact pinned source links.

## 2. Exact relationship between the tilted and straight lattices

Write

    Gamma_N = span_Z{N(e_0+e_1), N(e_0-e_1), N e_j : j>=2}
            = {N a : a in Z^d, a_0 congruent a_1 mod 2}.

Then Gamma_N is an index-two sublattice of N Z^d. Therefore Z^d/Gamma_N is a two-sheeted cover of the ordinary straight N torus. A rectangular cover is

    R_N = span_Z{2N e_0, 2N e_1, N e_j : j>=2},

which has index two in Gamma_N. Thus its quotient covers the tilted quotient with degree two. The straight 2N cube is another finite cover, of degree 2^(d-1).

If N is divisible by the block scales, the ordinary coordinate block partitions descend to the tilted quotient. Coarsening by L changes Gamma_N to Gamma_(N/L), preserving the quotient's form. This is a valid geometric compatibility check. It does not establish the RG estimates, its global normalization conventions, or equality of Wilson measures under the covering map.

In particular, independent link variables on different sheets are not constrained equal. There is no canonical pushdown of a generic covering configuration to one base configuration. Restricting to one selected lift of each base link does not restore the missing local interactions across a cut. Conditioning all deck-related variables to be equal is a different, zero-Haar-measure constraint at positive continuous coupling, not the original Wilson law.

There is also a Smith-normal-form trap. The finite site group is abstractly Z/N times Z/(2N) times (Z/N)^(d-2), but the unimodular change y_0=x_0, y_1=x_1-x_0 that makes the periods rectangular sends the designated steps e_0,e_1 to (1,-1),(0,1). The Wilson plaquettes become parallelograms in that coordinate description. Therefore the abstract rectangular group isomorphism does not identify the standard coordinate-nearest-neighbor Wilson action or restore the source's coordinate chessboard geometry.

For linear translation-invariant operators, the dual frequencies split exactly into two sectors:

    xi_i = 2 pi k_i / N for every i;

or

    xi_0 = 2 pi (k_0+1/2)/N,
    xi_1 = 2 pi (k_1+1/2)/N,
    xi_j = 2 pi k_j/N for j>=2.

Indeed the two diagonal periods require N(xi_0+xi_1) and N(xi_0-xi_1) to be multiples of 2 pi. Hence a translation-invariant free operator's spectrum is the union of the periodic and simultaneously half-shifted spectra. This is useful for checking free determinants or Green functions; it is not a factorization of the interacting Wilson measure.

## 3. Proven twisted-transfer identity

Take N>=3, finite b>=0, and the bare Wilson density exp[-b sum_p(1-Re tr U_p)], with normalized Haar measure. Let

    Sigma = (Z/2N) x (Z/N)^(d-2)

be the spatial cross-section in coordinates 1,...,d-1. The tilted quotient is the cylinder with time coordinate x_0=0,...,N-1 and this cross-section, with its final slice glued to the initial slice by the spatial translation

    s(x_1,x_2,...) = (x_1+N,x_2,...).

This follows from the period (N,N,0,...); its sign is immaterial because s=s^(-1).

Let H=L^2(SU(2)^(spatial bonds of Sigma), Haar). Let M be multiplication by the spatial Wilson weight on one layer, and let K be the kernel obtained by integrating the time-link variables between two layers. As in the proof of the manuscript's Lemma 6.4, K is positive self-adjoint: it is convolution by a positive-definite Wilson class function followed by the commuting gauge-invariance projection. Its continuous positive kernel makes it trace class. Set

    T = M^(1/2) K M^(1/2).

Then T is positive trace class. Let J be pullback by s on spatial gauge configurations. J is unitary and self-adjoint, J^2=I, and [J,T]=0 because the action and Haar measure are spatially translation invariant.

Expanding the trace as an integral of kernels gives

    Z_tilt(N,b) = Tr(T^N J).

Each interior factor integrates exactly the plaquettes between successive layers; the final factor joins the last spatial configuration to the spatially translated initial configuration, exactly as in the tilted quotient. The M^(1/2) factors pair into one spatial action factor per layer, including at the seam because M commutes with J. No gauge fixing or extra constraint has been introduced.

The untwisted rectangular torus with side lengths (N,2N,N,...,N) has

    Z_rect(N,2N,N,...) = Tr(T^N).

The rectangular two-sheeted cover with side lengths (2N,2N,N,...,N) has

    Z_cover = Tr(T^(2N)).

Decompose H=H_+ direct-sum H_- into the +/-1 eigenspaces of J. Commutation gives

    Z_tilt = Tr(T_+^N) - Tr(T_-^N),
    Z_rect = Tr(T_+^N) + Tr(T_-^N).

The original positive Boltzmann integral gives Z_tilt>0, so

    0 < Z_tilt <= Z_rect,
    Z_rect - Z_tilt = 2 Tr(T_-^N).

This proves a real zero-source partition-function inequality. It does not make T^N J positive, nor identify derivatives of log Z_tilt with those of log Z_rect. The source theorem needs uniform bounds on complex-source generating functions after one common holomorphic counterterm; that conclusion does not follow from the displayed real inequality. In the mirror-periodic complex-source setting the seam still inserts J into the trace, so the manuscript's positive-trace-power proof cannot just be copied.

## 4. Why the coordinate chessboard geometry is absent

For the coordinate reflection R_0(x)=(-x_0,x_1,...), a point of R^d/Gamma_N is fixed exactly when

    (-2x_0,0,...,0) belongs to Gamma_N,

which is equivalent to x_0 being a multiple of N. The apparent planes x_0=0 and x_0=N are identified by the tilted period (N,N). There is one fixed hypersurface, and its complement is connected: every point off it has a unique time coordinate in (0,N) with spatial point in Sigma. R_0 sends that connected cylinder to itself via

    (x_0,x_1,...) -> (N-x_0,x_1+N,...).

Consequently there are not two complementary components exchanged by R_0. The geometric hypotheses used in Lemmas 3.7–3.9 and 4.4 are absent. The same applies in direction 1. Directions j>=2 remain ordinary product directions and still have separating coordinate cuts.

The two diagonal normal directions e_0-e_1 and e_0+e_1 do have the needed cuts; this is precisely the new construction's advantage. The tilted quotient is also invariant under individual coordinate sign changes, interchange of 0 and 1, and permutations among j>=2. It is not invariant under all of W_4: interchanging 0 and 2 sends the period N e_2 to N e_0, which is not a period. Thus Lemma 4.1's full finite-volume hypercubic invariance also needs a new argument if one changes families.

These statements show failure of the manuscript's geometric proof hypotheses. They do not assert that every possible algebraic definition of coordinate RP must fail for all observables, or that the infinite-volume tilted limit cannot regain coordinate RP or full hypercubic symmetry.

### No period lattice supplies both standard separating cuts

There is a useful general obstruction, independently checked here. Let Lambda be a full-rank lattice invariant under a linear reflection R with one-dimensional normal eigenspace V_- and tangent eigenspace V_+. Put Lambda_+=Lambda intersect V_+, Lambda_-=Lambda intersect V_-.

Normal projection P_- identifies

    Lambda/(Lambda_+ direct-sum Lambda_-)
       with P_-Lambda/Lambda_-.

Since (I-R)Lambda is contained in Lambda_-, one has

    Lambda_- subset P_-Lambda subset (1/2)Lambda_-.

The index is therefore 1 or 2. Fixed hyperplanes of R on the quotient have normal coordinate in (1/2)Lambda_- modulo P_-Lambda. Index 1 gives two components and the product split; index 2 identifies them, leaving a single nonseparating component. In the latter case a fundamental normal open interval times the tangent torus parametrizes the complement, which is connected.

Suppose Lambda is invariant under R_0 and the coordinate interchange theta_01, and both reflections have the two-sided separating geometry. Splitting for R_0, and then for R_1=theta_01 R_0 theta_01, yields

    Lambda = a Z e_0 direct-sum b Z e_1 direct-sum Lambda_rest.

Theta_01 invariance forces a=b. But theta_01's eigensublattice is then

    a Z(e_0+e_1) direct-sum a Z(e_0-e_1) direct-sum Lambda_rest,

of index two in Lambda. Its diagonal fixed set is nonseparating, a contradiction. Thus simply searching for a translation-period torus possessing both standard two-sided cuts cannot repair this problem. This is a geometric factorization obstruction, not a theorem ruling out other RP arguments.

## 5. Exact list of extension obligations

There are different routes, and their obligations should not be conflated.

### Route A: prove that the new state belongs to the original straight-periodic cluster set

A state-selection or local-observable comparison theorem would retain all the original family estimates and symmetries. The new construction does not prove it. Neither the two-sheeted covering relation nor equal bulk pressures supplies it. The manuscript's Theorem 6.13 and Corollary 6.19 do not supply it either: they compare only the original family and yield a nonzero short-distance error, not a vanishing large-volume error.

### Route B: rebuild the source construction on tilted quotients

At minimum, the following exact statements need a tilted analogue or a sufficient substitute:

1. **Theorem 3.1(c),(d), pp.44–45**, and the zero-source stability inputs restated in **Proposition 6.1 (S),(F), pp.93–94**: define the same multiscale construction on the quotient and prove the required source analyticity, locality, exponential domain bounds and cutoff-uniform extensive bounds. Descending block partitions alone proves none of these analytical estimates.
2. **Lemma 6.7, pp.98–99**, if the argument compares vacuum constants across shapes: extend its actual local-term identification to the tilted construction. Then establish the corresponding **Lemma 6.8, pp.99–100**. Its orbit-counting step extends conditionally to a degree-two cover, as explained below, but the existence and estimates for the tilted local terms are additional input.
3. **Lemmas 3.7–3.9, pp.52–54**, **Theorem 3.10, pp.55–59**, and **Proposition 6.2, p.94**: replace the missing coordinate cuts by a proved alternative that still yields the per-ball, volume-independent complex-source bound. A diagonal-cell chessboard may be a promising different geometry, but its overlap/parity and trace estimates are not established by the present fixed-cutoff RP proof.
4. **Lemma 6.4 and Remark 6.6, pp.95–97**, and hence **Theorem 6.13, pp.102–105**: provide an appropriate tilted trace/pressure comparison. The exact twisted identity in Section 3 exposes the extra J sector that the existing positive-power proof does not handle. The raw axis-rectangular extension uses these same coordinate facts and does not bypass this obligation.
5. For the complete short-distance witness, either extend **Theorem 5.8, p.79**, directly, including its kernel and horizon estimates, or prove a valid new transfer theorem importing the cubic witness **Theorem 6.21** and yielding a tilted version of **Theorem 6.24, p.109**. The fixed-cutoff Gibbs existence/RP result supplies no such quantitative estimates.
6. **Theorem 4.10, p.66**, can be rerun once the required uniform correlation estimates are supplied, but the assertions of **Theorem 4.12, p.69**, use **Lemma 4.1** for full W_4 symmetry and **Lemma 4.4** for coordinate RP. Translation invariance and the new diagonal RP do not replace those missing hypotheses. The raw diagonal-RP implication specifically asks for coordinate RP and full W_4 invariance in addition to diagonal positivity.

### Route C: preserve RG on small cubic reference tori only

The manuscript's **Remark 6.17, pp.105–106**, and **Remark 6.30, p.112**, are useful: sufficiently large cubic/axis-rectangular volumes can be handled using bare-measure comparison, with RG used only on two cubic reference volumes. Thus a future tilted extension need not necessarily redo the full RG on every tilted torus. It would instead need a replacement for the large-volume chessboard/trace/pressure package, strong enough for the common-counterterm complex bound in equations (6.16)–(6.21). The new diagonal RP and twisted zero-source trace alone do not establish that package.

### Conditional extension of the vacuum-energy orbit count

Suppose a pair of compatible quotient lattices Lambda_fine subset Lambda_base of finite index q already has (i) the same local RG terms on all sufficiently short lifted domains, (ii) the same per-point exponential domain and remainder bounds, (iii) exact block-count normalization terms, and (iv) block partitions descending to both quotients. Then the short-domain part of Lemma 6.8 extends with q in place of q^4:

- each Lambda_base orbit of a short lifted pointed domain is exactly q Lambda_fine orbits;
- short local terms therefore cancel exactly in E_fine-q E_base;
- the remaining domains have tree length at least the injectivity scale divided by a constant multiple of the block size;
- their per-point exponential tails, summed over RG levels, give the same kind of convergent cutoff-independent series.

For Gamma_N subset N Z^d, q=2 and the minimum sup norm of a nonzero period is N, so the relevant injectivity scales match those of the base cube. The proof is literally the short-domain lift/orbit partition followed by the tail estimate used on pp.99–100. This conditional counting fact is genuine; it does not establish assumptions (i)–(iii) for a construction not yet defined and estimated on Gamma_N, and it does not repair the missing chessboard step.

## 6. Bottom line

The appropriate new conclusion is fixed-cutoff existence of a translation-invariant, diagonally reflection-positive Wilson Gibbs state along a different family. It cannot yet be inserted as the selected state in the pinned reference theorem. The source has some shape flexibility, specifically axis rectangles and adaptable local counting, but no theorem covering the tilted family with the needed bounds and symmetries. No equality of local states, continuum conclusion, or mass-gap claim is inferred here.

## Provenance

Only the pinned public source files were downloaded and read. All downloaded source bytes were checked against the Git blob SHAs in the pinned commit; `SOURCE_MANIFEST.json` records these checks. PDF text extraction and one page rendering were performed; no repository code or TeX was executed and no public writes were made.

SHA-256 of inspected files:

- ym4.pdf: 869ed86a1384dbc57277647e2bcd4096f545e533c74e45917c1caccb4868b24b
- raw_I.tex: 4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93
- raw_II.tex: 6a1f74b05f74ba44a2186c11fb08e139178d86b15c1494a95c434212944b2b8f
- raw_III.tex: 7e36523b85fb4f85aefdd45ab175420459f24e34fe56a4e83e53a6829c7a352d
