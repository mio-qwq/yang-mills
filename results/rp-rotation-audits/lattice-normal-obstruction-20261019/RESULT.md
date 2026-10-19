# Exact reflection normals of the unchanged Wilson lattice

19 October 2026. Independent route-obstruction audit. This is a statement about the geometry and scope of the supplied fixed-cutoff proofs, not a no-go theorem for emergent rotational invariance.

## Main conclusions

1. The Euclidean hyperplane reflections acting on the original nearest-neighbor hypercubic Wilson lattice have exactly the unoriented normal lines
   \[
   \mathcal N_d=\{\mathbb R e_i\}\cup\{\mathbb R(e_i+e_j),\mathbb R(e_i-e_j):i<j\}.
   \]
   There are \(d^2\) of them, hence 16 in dimension four. They generate the signed-permutation group \(W_d\), of order \(2^d d!\), hence 384 in dimension four. This group is finite and closed, not dense in \(O(4)\).
2. Changing only the period subgroup never enlarges this list. A rational reflection preserving a chosen continuum period lattice need not act on its discrete sites, nearest-neighbor edges, or elementary plaquettes. The distinction is decisive here.
3. On the specific tilted family
   \[
   \Gamma_N=\langle N(e_0+e_1),N(e_0-e_1),Ne_2,Ne_3\rangle,
   \]
   the standard two-separating-fixed-cut argument applies to exactly four normal lines: \(e_0-e_1,e_0+e_1,e_2,e_3\). Taking even \(N\) makes all four site-cut proofs immediate. These four reflections generate an order-16 group. The entire period stabilizer within \(W_4\) has order 64, and its reflection automorphisms comprise eight mirrors, only four of which separate in the requisite way.
4. Conjugating the tilted construction by \(W_4\) supplies the other signed-diagonal directions in potentially different states. It does not place every RP inequality in one selected translation-invariant state, nor identify any such state with the reference cubic continuum family.
5. A useful nontrivial missing input can be stated with one normal, rather than a dense list: same-state continuum RP at \(n=(1,2,0,0)\), together with a valid RP-to-invariance bridge, existing \(W_4\) invariance, and continuity of the rotation action, suffices for \(O(4)\). This exact finite-cutoff reflection is forbidden by the unchanged stencil: \(r_n e_0=(3/5,-4/5,0,0)\).

The last point is a sufficient target for the **group-generation route**. A separate analytic rigidity theorem might use finitely many mirror positivity inequalities and additional growth/UV information to prove more than group generation. The finite-group result does not refute such a theorem.

## 1. Exact meaning of an unchanged action

Fix the embedded sites \(a(\mathbb Z^d+c)\), with independent compact-group variables on the nearest-neighbor oriented edges of displacement \(\pm a e_i\), inverses on reversed edges, and the uniform Wilson action on the elementary coordinate squares. A geometric reflection acts by pullback on those oriented edges. This is the action used in the inherited factorization proof; no interpolation, path replacement, or new edge variables are present.

A period change takes a subgroup \(\Lambda\subset a\mathbb Z^d\) and quotients this same local cell complex. It changes the boundary gluing, not its local edge or plaquette directions. A geometric reflection on the quotient must still map its discrete site set and specified cell complex to themselves.

The assertions below concern these geometric reflection maps. They do not classify unrelated transformations of gauge variables or abstract automorphisms of a degenerate finite graph, and do not assert that continuum RP must arise from an exact microscopic geometric reflection.

## 2. Classification theorem and proof

Let \(r_n=I-2nn^T/(n^Tn)\) be a hyperplane reflection, with \(n\ne0\). The following conditions are equivalent:

- \(r_n\) preserves \(\mathbb Z^d\);
- \(r_n\) preserves the coordinate nearest-neighbor edge stencil;
- \(r_n\) is a signed-permutation matrix;
- the normal line is in \(\mathcal N_d\).

An integer orthogonal matrix has an integer vector of Euclidean length one in each column, hence each column is a signed coordinate vector. Orthogonality makes their coordinate positions distinct. Thus the first three conditions are equivalent. Such a matrix also permutes the elementary coordinate plaquettes; orientations can reverse, but \(\operatorname{Re}\operatorname{Tr}U_p\) is unchanged under inversion, and product Haar is preserved.

For a direct classification of the normal, integer diagonal entries imply
\[
\frac{2n_i^2}{\|n\|^2}\in\{0,1,2\},\qquad
\sum_i\frac{2n_i^2}{\|n\|^2}=2.
\]
Every nonzero coordinate therefore contributes either 1 or 2. Either just one coordinate is nonzero, or exactly two are nonzero and have equal absolute value. These are precisely the listed axes and signed pair diagonals. Conversely those normals give a coordinate sign flip or a signed interchange of two coordinates.

This proof does not assume the normal is rational: it classifies all real normals.

For the affine plane \(n\cdot x=b\), the translation part is \(2bn/\|n\|^2\). On the unshifted unit lattice, coordinate mirrors require \(2b\in\mathbb Z\) when \(n=e_i\); signed-diagonal mirrors require \(b\in\mathbb Z\) when \(n=e_i\pm e_j\). A shifted lattice changes the allowable offsets, not the normal list. The inherited diagonal proof treats the latter integer planes. Coordinate site RP and coordinate bond RP use their respective standard algebras; the elementary fixed-plane conditioning proof alone is the site version.

### The generated group

The reflections in \(e_i^\perp\) give the independent sign changes. The reflections in \((e_i-e_j)^\perp\) give coordinate transpositions. Together they generate every signed permutation, and all generators already belong to that group. Thus the generated group is exactly \(W_d\), with \(2^d d!\) elements. Affine offsets can add translations, but the linear/orthogonal parts remain in \(W_d\). An infinite affine reflection group is not evidence of a dense orthogonal subgroup.

## 3. Why periods cannot repair a forbidden normal

Let \(V=(\mathbb Z^d+c)/\Lambda\), where \(\Lambda\subset\mathbb Z^d\), and suppose an affine Euclidean isometry \(x\mapsto Rx+t\) takes \(V\) to itself. The images of the two sites represented by \(c\) and \(c+e_i\) differ, modulo \(\Lambda\), by \(Re_i\). Two images in \(V\) differ by an integer vector modulo \(\Lambda\), so
\[
Re_i\in\mathbb Z^d+\Lambda=\mathbb Z^d.
\]
Thus \(R\) is integer orthogonal. For a reflection, the classification above applies. Neither an affine shift nor a different finite-index period subgroup evades the obstruction. The same proof after division by \(a\) applies at every lattice spacing.

This also explains the insufficiency of merely checking \(R\Lambda=\Lambda\). That condition makes \(R\) an isometry of the **continuum torus** \(\mathbb R^d/\Lambda\); it does not say that its sampled Wilson vertices form an invariant set.

### A one-edge exact certificate

For \(n=(1,2,0,0)\),
\[
r_n=\begin{pmatrix}
3/5&-4/5&0&0\\
-4/5&-3/5&0&0\\
0&0&1&0\\
0&0&0&1
\end{pmatrix},\qquad
r_ne_0=(3/5,-4/5,0,0).
\]
The edge from 0 to \(e_0\) has an endpoint whose image is not any original lattice vertex, even modulo any integer period subgroup. This finite exact obstruction applies at every volume and cutoff. In particular the inherited pullback \(U_{(x,y)}\mapsto U_{(r_nx,r_ny)}\) is not defined on the original link-variable space.

There nevertheless is a reflection-invariant integer **period** lattice:
\[
L=\langle(1,2,0,0),(2,-1,0,0),e_2,e_3\rangle.
\]
Its two displayed planar generators are the normal and tangent eigenvectors, so \(r_nL=L\). This gives a concrete example where continuum period compatibility is satisfied and discrete-site compatibility fails. Multiplying \(L\) by any integer does not cure that failure.

Clearing denominators, refining the lattice, or replacing an edge by a multi-edge path changes the situation as follows:

- Passing to \((1/q)\mathbb Z^d\) with its own nearest-neighbor edges leaves exactly the same normal classification after rescaling.
- The additive lattice \(\mathbb Z^d+r_n\mathbb Z^d\) can be invariant under this one reflection, but its vertices and/or edge stencil are different from the original Wilson model.
- Adding the reflected directions changes the local interaction. If the original elementary squares are retained alone, their reflected images are absent; adding the reflected plaquettes changes the action.
- An abstract Smith-normal-form identification of the finite vertex group with a rectangular product does not preserve its designated edge generators. It therefore does not identify the Wilson cell complex with the rectangular one in the reference theorem.

### A stronger finite-stencil obstruction

Let \(S\subset\mathbb R^4\) be any finite spanning displacement set. Its orthogonal symmetry group injects into the finite permutation group of \(S\): an orthogonal map fixing all of \(S\) fixes its span pointwise. Hence this symmetry group is finite. Consequently no finite spanning stencil can be exactly invariant under both \(W_4\) and \(r_{(1,2,0,0)}\), because Section 5 proves that these generate a dense subgroup of \(O(4)\).

Thus even broadening to a finite local stencil cannot make the proposed dense group an exact microscopic symmetry while retaining all its generators. Emergent or approximate continuum symmetry remains possible and is a different theorem.

## 4. Exact scope of the current tilted family

Write
\[
\Gamma_N=N\{z\in\mathbb Z^4:z_0\equiv z_1\pmod2\}.
\]
A signed permutation preserves this subgroup exactly when its underlying permutation preserves the distinguished pair \(\{0,1\}\). Signs do not affect parity. Its stabilizer therefore has order
\[
2^4\cdot2!\cdot2!=64.
\]
The reflection automorphisms among the 16 allowed lattice mirrors are:

- the four coordinate mirrors;
- the two mirrors with normals \(e_0\pm e_1\);
- the two mirrors with normals \(e_2\pm e_3\).

The eight cross-pair mirrors do not preserve \(\Gamma_N\) at all.

### Separating-cut criterion

For a reflection-invariant full-rank period lattice \(\Lambda\), let
\(\Lambda_\pm=\Lambda\cap V_\pm\), where \(V_-\) is the one-dimensional normal eigenspace. With \(P_-=(I-r)/2\),
\[
\Lambda_-\subset P_-\Lambda\subset\tfrac12\Lambda_-.
\]
Moreover
\[
\Lambda/(\Lambda_+\oplus\Lambda_-)\cong P_-\Lambda/\Lambda_-.
\]
The index is one or two. Index one gives a product of a normal circle and a tangent torus, with two fixed hypersurfaces and two exchanged complementary components. Index two identifies the two fixed hypersurfaces by a tangent-twisted half-normal period; only one remains and its complement is connected. This is the general separating-cut criterion proved in the inherited compatibility audit. Equivalently, the split occurs exactly when \(P_-\Lambda\subset\Lambda\).

Applying it to the generators of \(\Gamma_N\) gives:

- \(e_0-e_1\), \(e_0+e_1\): index one. The normal/tangent diagonal periods are separate generators. These are the two successful diagonal directions.
- \(e_2\), \(e_3\): index one. These are ordinary direct-product coordinate circles.
- \(e_0\), \(e_1\): index two. For example, \(P_{e_0}N(e_0+e_1)=Ne_0\notin\Gamma_N\).
- \(e_2-e_3\), \(e_2+e_3\): index two. For example, \(P_{e_2-e_3}Ne_2=(N/2)(e_2-e_3)\notin\Gamma_N\).

Thus exactly the four normal lines claimed in the summary have the standard separating geometry. They are mutually orthogonal; their reflections commute and independently reverse four orthogonal coordinates, generating \((\mathbb Z/2)^4\) of order 16.

### What is simultaneously available in a local limit

The original written tilted proof explicitly treats \(e_0-e_1\). Its extension to \(e_0+e_1\) is immediate by changing the sign of coordinate 1, which preserves both the period subgroup and the finite Wilson law. For even \(N\ge4\), the transverse coordinate site cuts \(x_j=0,N/2\), \(j=2,3\), have fixed-plane links and no plaquette meeting both strict sides. The same conditioning argument proves their RP as well. Each finite law therefore has all four RP inequalities simultaneously. A common local weak subsequence preserves them; exact lattice translation invariance conjugates them to all integer translates. This modest strengthening of the written one-normal result introduces no new analytic estimate.

Odd \(N\) is harmless for the two diagonal directions, as the original parity proof established. No odd-period transverse bond-plane argument is needed for the above conclusion because even \(N\to\infty\) is cofinal.

This is an exact statement of what the inherited **geometric factorization method** supplies. Failure of separating geometry is not, by itself, a proof that every conceivable algebraic RP argument fails for the other reflections or that these inequalities cannot reappear in a limit.

Running the same construction with another distinguished coordinate pair supplies its two signed diagonals and transverse coordinate cuts in another state. The union over these choices exhausts \(\mathcal N_4\), but does not prove simultaneous RP of one state. Centered free cubes separately give all 16 origin mirrors and \(W_4\) invariance in a Gibbs limit, with translation invariance unproved. These are distinct existence statements, as the simultaneous-RP audit emphasizes.

## 5. A precise sufficient extra normal for the group route

Let \(s_1=r_{e_1}\). Then
\[
r_{(1,2,0,0)}s_1=
\begin{pmatrix}3/5&4/5\\-4/5&3/5\end{pmatrix}\oplus I_2.
\]
Its planar rotation angle \(\theta\) satisfies \(\cos\theta=3/5\). If it had finite order, its eigenvalue \(\zeta=e^{i\theta}\) would be a root of unity. Hence \(\zeta+\zeta^{-1}=6/5\) would be an algebraic integer. A rational algebraic integer is an integer, a contradiction. Thus \(\theta/(2\pi)\) is irrational, and its powers are dense in the coordinate-plane circle subgroup \(SO(2)_{01}\).

If a continuous Euclidean correlation structure is invariant under \(W_4\) and this one extra reflection, its closed stabilizer contains that circle. Coordinate permutations conjugate this circle to all six coordinate-plane rotation circles. Those generate \(SO(4)\); a coordinate reflection then gives \(O(4)\). This is also a special explicit case of the source's proved generation theorem, raw III lines 104376–104455.

The inference is conditional on invariance of **one and the same** limiting object under the two groups, with continuity sufficient to close its stabilizer. A family of individually RP states indexed by normals is not enough. If the available RP-to-invariance bridge is only for two-point kernels, the conclusion is only two-point rotational invariance, not invariance of every Schwinger function or of the full field law.

### Not every new rational normal is enough

For \(m=(1,1,1,1)\), \(r_m=I-\tfrac12\mathbf1\mathbf1^T\) is outside \(W_4\), but \(W_4\) and \(r_m\) preserve the finite set
\[
\mathcal S=\{\pm e_i\}\cup\{\tfrac12(\pm1,\pm1,\pm1,\pm1)\},
\]
which has 24 elements and spans \(\mathbb R^4\). They therefore generate a finite group, in fact order 1152 (the usual \(F_4\) symmetry group).

Here is an elementary exact count, without invoking classification of finite reflection groups. A symmetry of \(\mathcal S\) is determined by the images of an ordered orthonormal coordinate basis. There are 24 choices for its first vector, 6 perpendicular choices for the second, 4 for the third, and 2 for the fourth, so at most 1152 maps. The generated group's orbit of \(e_0\) contains all eight axes under \(W_4\) and all sixteen half-sign vectors after applying \(r_m\) and \(W_4\). Its stabilizer of \(e_0\) contains the 48 sign/permutation symmetries of the other coordinates. The group therefore has at least \(24\cdot48=1152\) elements, giving equality. The perpendicular counts for half-sign first vectors follow from the already proved transitive action. This also shows why an arbitrary 'one additional reflection' is not a sufficient replacement for the explicit infinite-order check.

## 6. The genuine missing inputs, separated by route

### Group-generation route

The finite-cutoff construction cannot acquire a dense set of exact geometric normals merely by tilting its periods. A concrete useful target is therefore an **asymptotic** inequality at \(n=(1,2,0,0)\) for the same continuum state already carrying the reference symmetries and estimates. For example, for appropriate approximants to each fixed positive-side test vector, a reflected quadratic form lower bound \(Q_{a,n}\ge-\varepsilon_a\), with \(\varepsilon_a\to0\), plus convergence to the claimed continuum reflected form, would supply the extra RP. The inherited exact cone proof supplies no such estimate for this normal.

Alternatively one could construct an exactly RP Wilson model on a rotated lattice and prove a universality/state-identification theorem comparing its continuum correlation functions to the original family. Rotating the whole microscopic lattice transports the construction to a new embedding; it does not identify its limiting law with the old one. That identification is the substantive missing theorem, not a coordinate substitution.

Even before an extra nonlattice normal is considered, the supplied tilted state must be put in the same continuum family as the reference bounds, full \(W_4\) symmetry, and coordinate RP. The compatibility audit lists the missing local-state/source-control comparisons. Equal pressures and a finite-cover relationship do not supply them.

### Separate analytic two-point rigidity route

Raw III, lines 79931–79990, contains Remark `10.1:rem-diagonal-positivity`, claiming two-point \(O(4)\) invariance from:

1. coordinate one-field RP and \(\mathbb R^4\rtimes W_4\) invariance;
2. Theorem 0 clause (iii-b);
3. the logarithmic upper bound in clause (iv) at the indicated small reference coupling;
4. one signed-diagonal one-field RP inequality, equivalent under \(W_4\) to all twelve.

This claim is stronger than multiplying the finite reflection generators. It cannot be rejected just because their group is finite. It must be proved or audited as an analytic theorem using its extra assumptions. Exact-phrase searches across the three supplied raw files located this claim and its unlabeled reference to a theorem, but did not locate that theorem's actual statement/proof. This audit does not certify it or assert that no proof exists elsewhere.

The later source proposition `10.8:prop-threshold-sharpness`, raw III lines 109238–109346, claims a nonrotational free-field example with all sixteen RP mirrors, but is explicitly marked **Proof outstanding**. It is not being used here as a proved counterexample. Its UV scaling is also different, so it would not automatically contradict the earlier claimed theorem under its exact assumptions.

The coordinated bridge audit should therefore keep two questions separate: (i) what the validated elementary RP-to-invariance bridge plus group closure actually gives; (ii) whether the stronger analytic theorem stated in the source has a complete valid proof under assumptions genuinely available for the same Wilson limit.

## 7. Verification and provenance

`check_exact.py` is original standard-library code, written for this audit and run locally without `-O`. All assertions passed. `exact_results.json` records:

- enumeration of all 384 signed permutation matrices and exactly 16 reflection matrices;
- equality of those reflections with the proved normal list;
- order 384 of their generated group;
- order 64 of the selected tilted period stabilizer;
- its eight reflection automorphisms and exactly four split mirrors;
- order 16 of the split-mirror group;
- the exact rational one-edge obstruction and infinite-order rotation matrix;
- order 1152 of the body-diagonal finite extension.

These finite checks supplement, not replace, the general proofs above. No inherited or downloaded repository code was executed and no remote state was changed.

Primary supplied proof locations inspected:

- `wilson-invariant-diagonal-rp-20261018/construction/RESULT.md`, lines 13–28 (precise fixed-parallel-family theorem), 30–73 (local factorization), 75–123 (tilted quotient and local limit).
- `wilson-invariant-diagonal-rp-20261018/independent-audit/TILTED_TORUS_ADDENDUM.md`, Sections 1–5 (parity, separation, full-algebra factorization, local DLR qualification).
- `wilson-simultaneous-rp-20261018/RESULT.md`, Sections 1–4 (common-center construction, affine versus orthogonal group, averaging counterexample, missing common state).
- `ym4-tilted-compatibility-20261018/RESULT.md`, Sections 2, 4, 5 (periods versus cell complex, split-period obstruction, missing reference-family inputs).
- `ym4-tilted-compatibility-20261018/raw_III.tex`, lines 79931–79990, 104376–104455, 109238–109346 as specified above.

The pinned raw source is commit `785a68fdeef78a1da854c4807fe1f17b597d05e7` of `ethanwsussman/Yang--Mills-LLM-experiment`. Public line links:

- [Diagonal-positivity remark](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/theorem_0_complete_account_raw_III.tex#L79931-L79990)
- [Group-generation theorem](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/theorem_0_complete_account_raw_III.tex#L104376-L104455)
- [Proof-outstanding counter-model](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/785a68fdeef78a1da854c4807fe1f17b597d05e7/theorem_0_complete_account_raw_III.tex#L109238-L109346)
