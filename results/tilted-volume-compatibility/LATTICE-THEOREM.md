# Simultaneous coordinate and diagonal separating cuts are impossible on one flat torus

Derivation dated 2026-10-18 UTC; the companion `independent-verification.md` supplies an independent proof audit. This is an obstruction to a geometric proof method, not a theorem that a Wilson measure cannot satisfy both reflection-positive inequalities by another argument.

Let Λ⊂R^d be a full-rank lattice, d≥2. Suppose Λ is invariant under R0, the sign flip of coordinate0, and θ, the swap of coordinates0 and1. Then the fixed loci (each taken as the union of ALL its components) of the induced R0 and θ cannot BOTH disconnect R^d/Λ. The same statement holds for normal-shift affine versions of these reflections.

Lemma. For any lattice-preserving linear reflection R with one-dimensional negative eigenspace V− and positive eigenspace V+, write Λ±=Λ∩V±. Then D=Λ+⊕Λ− has index1or2 inΛ. The fixed locus of R on the torus separates exactly when the index is1.

Proof. Since λ±Rλ belongs to Λ± for every λ∈Λ and these vectors span V±, the two eigenspace lattices have ranks d−1 and1. The map Λ/D→(½Λ−)/Λ− induced by π−=(I−R)/2 is injective. Indeed π−λ∈½Λ− because λ−Rλ∈Λ−. If π−λ∈Λ− then λ−π−λ∈Λ+, so λ∈D. Since Λ− has rank1, the target group has order2.

If the index is1, the torus is (V−/Λ−)×(V+/Λ+), and R negates only the circle coordinate. Its fixed locus is the UNION of the two tangent tori over the two fixed circle points. Its complement has two components. Each tangent torus separately is nonseparating; their union is the relevant cut.

If the index is2, choose a generator t ofΛ− and a representative λ0=(t/2,s) in the product coordinates, with s∉Λ+ and2s∈Λ+. The full torus is the quotient of the product torus by the free involution h:(x,y)↦(x+t/2,y+s). The reflection commutes with this deck action. A quotient point fixed byR lifts either to Rz=z orRz=h(z). The latter would require y=y+s moduloΛ+, impossible. Thus only the two fixed subtori of the product reflection occur; h exchanges them, so the quotient fixed locus is connected. Removing the two upstairs components leaves two connected cylinders, and h exchanges these as well. The downstairs complement is connected. This proves the lemma.

Now suppose both R0 andθ have separating fixed loci. By the lemma R0 splitsΛ and its axis projectionP0 preservesΛ. Sinceθ preservesΛ, P1=θP0θ also preservesΛ. Thus the remaining projection I−P0−P1 preservesΛ, and

    Λ = a Z e0 ⊕ b Z e1 ⊕ Λ_rest

for positive a,b. Swap invariance impliesa=b. But the θ eigensublattice is

    a Z(e0+e1) ⊕ a Z(e0−e1) ⊕ Λ_rest,

which has index2 inΛ. By the lemma the θ fixed locus is nonseparating, contradiction.

For an affine reflection t_v R with v in the negative eigenspace, conjugation by translation v/2 transformsR into t_vR. Translation on a flat torus is a homeomorphism regardless of whether v/2 is a lattice vertex. Therefore the fixed-locus separation property is unchanged. This covers shifted coordinate-face and diagonal planes, not arbitrary glide reflections with tangent displacement.

Examples in two dimensions: Λ=NZ² splits the coordinate reflection but not coordinate swap; Λ=N span_Z{e0+e1,e0−e1} splits coordinate swap but not coordinate reflection. Both lattices are invariant under both reflections. Extra independent periods in other coordinates preserve the contrast.

Consequence for the research route: replacing straight tori by tilted tori supplies the diagonal separating geometry but cannot simultaneously preserve the coordinate separating geometry by choosing a third lattice invariant under these same reflections. This alone neither disproves a needed chessboard inequality nor proves periodic-state inequivalence: an alternative analytic proof might exist. It identifies why carrying all standard finite-volume RP factorizations across the replacement is not automatic.
