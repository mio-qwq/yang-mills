# Independent verification of the reflection-lattice obstruction

The claimed obstruction is correct. Here, “the fixed locus separates” means that the complement of the entire fixed-point set is disconnected. In the split case, its two components jointly separate; neither component individually separates.

## Lemma: a lattice-preserving hyperplane reflection

Let V = V+ ⊕ V− be the orthogonal eigenspace decomposition of a linear reflection R on R^d, with dim V− = 1. Let Λ be a full-rank R-invariant lattice, put Λ± = Λ ∩ V±, and H = Λ+ ⊕ Λ−.

The projections π± = (I ± R)/2 satisfy 2π±Λ ⊂ Λ±. Their images span V±, so Λ± have full rank in their respective eigenspaces and H has finite index in Λ. The map

    Λ/H → (½Λ−)/Λ−,  [λ] ↦ [π−λ]

is well-defined and injective: if π−λ ∈ Λ−, then π+λ = λ − π−λ ∈ Λ+. Since Λ− has rank one, the group on the right has order two. Therefore [Λ:H] is 1 or 2.

Write Λ− = Zt with t a nonzero vector in V−, and K = V+/Λ+.

### Index one

The torus is (V−/Zt) × K, and R acts by (x,y) ↦ (−x,y). Its fixed locus consists of the two disjoint subtori

    {0} × K and {t/2} × K.

The complement has exactly two connected components, the two open normal semicircles times K. Each individual fixed subtorus has connected complement.

### Index two

Choose h ∈ Λ representing the nonzero coset of Λ/H. After subtracting an element of Λ−, write h = t/2 + s with s ∈ V+. Then 2s ∈ Λ+ and s ∉ Λ+: otherwise t/2 = h − s would belong to Λ−, contradicting its primitive generator t.

The product torus T0 = V/H double-covers T = V/Λ. Its nontrivial deck transformation is

    τ(x,y) = (x + t/2, y + s).

R commutes with τ on T0. A point of T is fixed precisely when one of its lifts z satisfies Rz = z or Rz = τz in T0. The latter equality is impossible, because its tangent-coordinate equation would require s = 0 in K. Thus no additional affine fixed components appear in the quotient.

The two fixed subtori in T0 are exchanged by τ. Their images form one connected embedded fixed subtorus in T. The two components of T0 minus its fixed locus are likewise exchanged by τ; hence T minus its fixed locus is connected.

Consequently:

    Fix(R on V/Λ) separates ⇔ Λ = Λ+ ⊕ Λ−.

## The coordinate reflection and coordinate swap cannot both separate

Let R0 change the sign of coordinate 0, and let θ interchange coordinates 0 and 1. Assume Λ is invariant under both. Suppose Fix(R0) separates. By the lemma, the coordinate projection P0 onto Re0 preserves Λ.

The coordinate projection P1 = θ P0 θ onto Re1 therefore also preserves Λ. Hence I − P0 − P1 preserves Λ, and, writing W = span(e2,…,e(d−1)),

    Λ = (Λ ∩ Re0) ⊕ (Λ ∩ Re1) ⊕ (Λ ∩ W).

The full-rank condition makes the first two summands aZe0 and bZe1 for positive a,b. Invariance under θ implies a = b. Thus

    Λ = aZe0 ⊕ aZe1 ⊕ ΛW.

For θ, its plus and minus eigensublattices are

    Λθ+ = aZ(e0 + e1) ⊕ ΛW,
    Λθ− = aZ(e0 − e1).

Their sum has index two in Λ: in the first two coordinates, its coefficient pairs are precisely the integer pairs of equal parity. The lemma shows that Fix(θ) is connected and nonseparating. This proves the claimed incompatibility.

## Two-dimensional examples

1. Square lattice Λ = aZ². R0 fixes x = 0 and x = a/2 modulo a, and their union separates. The swap θ fixes the single diagonal x = y modulo a; its complement is connected.

2. Diagonal lattice Λ = Z(a,a) ⊕ Z(a,−a). Both symmetries preserve Λ. In product coordinates x = a(u+v), y = a(u−v), with u,v modulo one, θ acts as (u,v) ↦ (u,−v). Its fixed circles v = 0 and v = 1/2 jointly separate. R0 acts as (u,v) ↦ (−v,−u), with the single fixed circle u+v = 0 modulo one, which is nonseparating. Equivalently, the two θ-fixed lifts are x−y = 0 and x−y = a modulo 2a, whereas the R0-fixed lifts x ∈ aZ all descend to one circle.

## Face-plane shifts and scope

A normal-shift affine reflection f(x) = Rx + c, with c ∈ V−, satisfies f = T(c/2) R T(−c/2). Translation is well-defined on every torus, so f is conjugate to R and has the same fixed-locus component and separation classification. In particular, replacing a site plane by a face plane, such as x0 ↦ 1 − x0, cannot avoid this obstruction. This argument does not require a claim about general affine glide reflections.

The theorem concerns only the geometric construction requiring both reflection fixed loci to separate the torus. It does not rule out reflection positivity of a Wilson measure proved by a different mechanism.

## Final exact-file review

The 2026-10-18 independent review verified the prepublication version of `LATTICE-THEOREM.md` at SHA-256:

    62efa6e4812a5887dcdfabd95a812d928ff2b06e163e09aac0349145d3e8b1e9

This exact version contains both clarifications: the spanning argument establishing the eigensublattice ranks, and the correct deck-map equation `Rz = h(z)`. The proof, its topological separation convention, its normal-shift affine extension, and its restricted geometric-method conclusion are correct. No substantive gap remains. The review is tied to those prepublication bytes. `../PROVENANCE_2026-10-18.json` records the publication-only introductory wording change and the published hash; the mathematical proof is unchanged.
