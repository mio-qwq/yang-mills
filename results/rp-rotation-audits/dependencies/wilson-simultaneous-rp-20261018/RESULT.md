# Simultaneous coordinate and diagonal Wilson reflection positivity

18 October 2026. Fixed lattice spacing, SU(2), finite nonnegative Wilson coupling. This is a bounded construction and literature audit, not a continuum or mass-gap result.

## Result

**No simultaneous all-affine-plane construction was established.** The existing tilted construction gives one translation-invariant Wilson DLR state with diagonal RP, but the attempted reflection-group, finite-intersection, and averaging arguments do not supply the missing coordinate RP and full hypercubic symmetry.

There are three concrete results:

1. One Wilson DLR state can be chosen hypercubic invariant and RP simultaneously for every coordinate and signed-diagonal reflection **through one common lattice center**. This follows directly from centered free cubes. Translation invariance and other parallel planes do not follow from that construction.
2. Even a state that is already translation invariant and fully diagonally RP can lose diagonal RP after hypercubic averaging. An exact spin-measure example below has reflected form −2/9. This closes that proposed algebraic shortcut; it is not a Wilson Gibbs counterexample.
3. The primary general RP theorem is explicitly a **single-reflection theorem with RP boundary data**. Its authors discuss incompatible finite-volume reflection families and use boundary-limit independence or a uniqueness contradiction, rather than giving a general simultaneous-state theorem. A later authoritative account explicitly corrects an erroneous simultaneous direct/diagonal finite-torus argument.

The desired Wilson state's existence remains unresolved by this audit. Nothing here proves that the relevant Gibbs/RP intersection is empty.

## 1. Exact local Wilson input and what centered cubes give

Write the Wilson weight as

    exp[S],   S=(b/2) Σ_p Re Tr(U_p),   b≥0,

with product normalized Haar on oriented links and U_(y,x)=U_(x,y)^−1. For the diagonal reflection

    θ_a(x0,x1,z)=(x1+a,x0−a,z),

use positive-side links whose endpoints satisfy x0−x1≥a. The fixed-plane links in directions j≥2 are shared variables and must be conditioned on, not counted twice as independent variables.

On a reflection-invariant free induced subcomplex, the only plaquettes meeting both strict half-spaces are the (0,1) squares based at x0−x1=a. Their opposite vertices x and y=x+e0+e1 are fixed. The two half-paths are

    P+=U_(x,x+e0) U_(x+e0,y),
    P−=U_(x,x+e1) U_(x+e1,y)=P+∘θ_a.

The crossing term is

    Re Tr(P+ P−*)
      = Σ_ij [Re(P+)_ij Re(P−)_ij + Im(P+)_ij Im(P−)_ij].

Consequently exp[(b/2)Re Tr(P+P−*)] is a uniformly convergent positive sum of products (Θf)f. After splitting the remaining action into reflected half-actions and a fixed-plane part, conditioning on the plane variables turns every term in the RP integral into a nonnegative weight times an absolute square. This proves RP for the full continuous cylinder algebra on the closed half-space. The same factorization works for any signed diagonal after an orientation-preserving or orientation-reversing lattice symmetry; Re Tr is unchanged under inversion.

For the coordinate **site** reflection Ri,0 through xi=0, an elementary plaquette has normal-coordinate span at most one and cannot meet both strict sides. Conditional on the fixed-plane links, the action and Haar measure split into reflected independent halves. This yields coordinate site RP without the diagonal crossing factors.

Now take free induced cubes V_L={−L,…,L}^d. The same finite measure is RP for all Ri,0 and all reflections in xi±xj=0, and invariant under the full signed-permutation group W_d. All these statements survive a local weak subsequential limit. Every finite link set and its plaquette interaction neighborhood eventually lies inside V_L, so the finite DLR identities pass to the limit. Gauge invariance also passes. Hence:

**Common-center conclusion.** At every finite b≥0 there is a gauge-invariant Wilson DLR state invariant under W_d and simultaneously RP for all coordinate and signed-diagonal site planes through the origin.

This conclusion has no translation-invariance assertion. Cubes centered at (1/2,…,1/2) instead give the associated coordinate bond-plane family and diagonal planes through that common center; they do not automatically select the same infinite-volume state. Standard Wilson link-plane RP can also be used, with its usual crossing-link/gauge-projection treatment, but changing the center remains the unresolved selection step.

## 2. The affine group exposes the missing step

Let ri,c reflect xi in c, where 2c is an integer. Then

    ri,1/2 ri,0 = T_ei,
    θ_0 r0,c θ_0 = r1,c,
    T_z θ_a T_−z = θ_(a+z0−z1).

The origin reflections generate only the finite signed-permutation group. Adding r0,1/2 to r0,0 and θ_0 generates translations in both e0 and e1. Thus the first mixed affine obstruction already arises for this small triple. No nonempty finite induced lattice domain can be invariant under that triple. This explains why arbitrary finite lists of affine cuts cannot simply be put into one centered free box.

The previous cylinder proof succeeds for one parallel family because its reflection group only forces one longitudinal translation direction, leaving a finite transverse alphabet and a strictly positive one-dimensional transfer kernel. The mixed triple forces two unbounded directions. At fixed remaining transverse width that gives a genuinely two-dimensional effective system, to which the one-dimensional all-DLR uniqueness estimate does not apply. This is a scope obstruction to that proof, not a nonexistence theorem for another cylinder construction.

Coordinate and diagonal reflections also belong to distinct conjugacy classes under W_d: a signed permutation sends a coordinate normal to a coordinate normal and a two-coordinate diagonal normal to another two-coordinate diagonal normal. Full W_d invariance would extend an established diagonal inequality to its diagonal orbit, but would not turn it into a coordinate inequality.

## 3. A translation-invariant diagonally RP measure whose rotation average fails RP

This is an exact counterexample to an averaging operation, on scalar spins on Z². It is **not** a Wilson state or a finite-temperature Gibbs counterexample.

Let a be three-periodic, with

    a(0)=1,   a(1)=a(2)=−1.

Define

    μ_v=(1/3)Σ_(r=0)^2 δ_[σ_x=a(x0+x1+r)],
    μ_u=(1/3)Σ_(r=0)^2 δ_[σ_x=a(x0−x1+r)].

Both measures are invariant under every lattice translation. Every configuration in μ_v is fixed pointwise by θ_0(x0,x1)=(x1,x0). Therefore, for any positive-side function G,

    μ_v((Θ_0 G)G)=μ_v(|G|²)≥0.

So μ_v has full uncentered diagonal RP, not merely a selected covariance inequality. Signed coordinate permutations send μ_v to either μ_v or μ_u. There are four of each among the eight elements of W₂; sign reversal gives the same phase-averaged measure. Its full hypercubic average is consequently

    μ̄=(μ_v+μ_u)/2.

Use the strictly positive-side detector

    Q=1{σ_(1,0)=σ_(2,1)=σ_(3,2)},
    F=Q[σ_(1,0)+1/3].

All three support sites satisfy x0−x1=1. In μ_v their tangent coordinates are 1,3,5, covering all three residues, so Q=0. In μ_u they have equal normal coordinate, so Q=1, and also Θ_0Q=1. The three values of (Θ_0F)F in μ_u are

    4/9, −8/9, −8/9.

Thus

    μ_v((Θ_0F)F)=0,
    μ_u((Θ_0F)F)=−4/9,
    μ̄((Θ_0F)F)=−2/9.

Moreover μ_v(F)=μ_u(F)=0, so this is also a negative connected reflected covariance. Translation invariance, reflection invariance, and full W₂ invariance of the final average do not repair RP.

The exact rational calculation is reproduced in `check_orientation_average.py` and `orientation_average_check.json`. The detector, orbit weights, and −2/9 form were also independently checked algebraically.

## 4. Why compactness and Gibbs-preserving symmetry averaging are insufficient

For a fixed reflection r and its positive algebra, let C_r be the set of reflection-invariant probability measures satisfying all continuous-cylinder RP inequalities. C_r is closed and convex: each inequality is a continuous linear inequality in the measure, and invariance is a closed linear condition. The Wilson DLR set G_b is likewise compact and convex because the variables are compact and the interaction is continuous and finite range.

The target is an intersection such as

    G_b ∩ TI ∩ W_d-invariant ∩ (intersection of C_r over required affine r).

Compactness proves that this intersection is nonempty **if** every finite subcollection already has a common member. It does not prove that finite-intersection premise. Individual nonemptiness, common-center finite families, and separately constructed orientation-dependent states are insufficient.

For a lattice symmetry g,

    g_* C_r = C_(g r g^−1),

with the corresponding transported half-algebra. A group can permute a family of closed convex sets without giving them a common point. Amenable averaging or a fixed-point theorem applies only after a nonempty, group-stable convex set has been supplied. The one-plane cone and the one-center intersection are not stable under all translations; the already translation-invariant diagonal cone is not stable under W_d, as Section 3 demonstrates.

An optional layered-Ising illustration, conditional on the standard low-temperature plus/minus layer-state facts, is recorded separately in `origin-rp-gibbs-averaging-counterexample.md`. It is not needed for the exact six-atom obstruction above and makes no claim about free Wilson limits.

A nonlinear operation that reflects and glues a half-space marginal would require a new compatibility proof for all Wilson DLR kernels, including plaquettes across every other cut. Finite-volume conditional independence is not a proof of the requisite infinite-half-space Markov property. Likewise, symmetry of a stochastic Gibbs sampler does not establish preservation of an RP cone.

## 5. What the primary sources actually prove

### Fröhlich–Israel–Lieb–Simon (1978)

J. Fröhlich, R. Israel, E. H. Lieb, B. Simon, *Phase Transitions and Reflection Positivity. I. General Theory and Long Range Lattice Models*, CMP 62, 1–34. [Author-hosted published PDF](https://math.caltech.edu/SimonPapers/93.pdf).

Section 3 is explicitly about a single plane. Theorem 3.5, pp.14–15, characterizes reflection-negative interactions by RP of finite-volume Gibbs laws on reflection-symmetric regions **with RP boundary data**. Its first remark preserves RP under limits through those regions. This is not a theorem guaranteeing common boundary data or common limits for an arbitrary affine reflection group.

Most relevant is the discussion on p.28: some lattices have reflection planes incompatible with any one finite cutoff. The authors obtain the necessary infinite-volume inequalities from correlation inequalities and sequence-independent boundary limits when available; otherwise they use a uniqueness assumption within a contradiction proof of phase coexistence. They do not replace these inputs by a general simultaneous-state existence theorem.

### Biskup (2009)

M. Biskup, *Reflection Positivity and Phase Transitions in Lattice Spin Models*, LNM 1970, 1–86. [Author-hosted PDF](https://www.math.ucla.edu/~biskup/PDFs/private/2008-2010/Biskup-LNM08.pdf).

Sections 5.4–5.5, especially Lemma 5.10 on pp.56–57 and the caution on p.58, distinguish the diagonal torus from the direct torus. The caution explicitly corrects the simultaneous direct/diagonal finite-volume use in Biskup–Kotecký (2007), equation (4.39). Its thermodynamic repair uses boundary-independence of the **restricted partition function per site**. That repair does not identify local Gibbs states or establish joint RP of one such state.

This agrees with the period-lattice obstruction in the inherited geometry audit. The fact that both reflections are torus automorphisms is weaker than the required separating, pointwise-fixed reflection cuts.

### Evertz–Jansen–Kastrup–Fredenhagen–Marcu (1987)

*Proof of universal perimeter law behaviour of the Wegner-Wilson loop in nonabelian lattice gauge theories with Higgs fields*, Phys. Lett. B 194, 277–282. [Author-hosted primary PDF](https://itp.tugraz.at/~evertz/Pubs/1987_PLB_194_277_Proof_of_Perimeter_Law_in_Nonabelian_Higgs.pdf).

Equations (7)–(13), pp.278–279, prove the oblique cut-plaquette cone factorization with free reflection-symmetric volumes. Immediately afterward, the text first discusses one-plane RP limits and then **assumes** an infinite-volume Gibbs state RP for all coordinate half-integer planes and diagonal integer planes before its lemmas. Its observation that such a state is automatically TI is consistent with the group relations above; it does not itself construct that common state.

### A stochastic shortcut is not automatic

A. Jaffe, *Stochastic Quantization, Reflection Positivity, and Quantum Fields*, [primary arXiv PDF](https://arxiv.org/pdf/1411.2964), Theorem III.1, provides a useful scope warning: even the usual stochastic quantization of a free scalar field can fail RP at every finite stochastic time in dimension at least two. This is not a Wilson result, but rules out treating symmetry and local Gibbs dynamics as an abstract RP-preservation argument without further proof.

## 6. Status and precise remaining construction target

The successful common-center construction and the existing all-parallel diagonal construction establish different nonempty subsets of the Wilson Gibbs simplex. Their intersection with full translation invariance and both affine reflection families is not established by the audited arguments.

A genuinely new construction would need, for example, a proved family of Wilson-compatible operations preserving the joint RP cone with a common Gibbs fixed point, or joint approximate RP for every finite list of affine cuts and cylinder tests while the local DLR defects tend to zero. Those are explicit missing conclusions, not estimates supplied by compactness, vanishing boundary density, or group symmetry.

This audit stops here. It does not repeat the source-differentiability or susceptibility bridge, does not infer equality with the prescribed straight-periodic cluster set, and does not assert a general impossibility result.

## Verification and provenance

Only public primary literature and the three supplied local reports were read. Original exact arithmetic code was written and run locally. No repository or downloaded code was executed; no external content was changed. The published FILS PDF, Biskup PDF, Jaffe preprint, extracted text, exact counterexample arithmetic, and hashes are retained with this report. No simultaneous all-affine-plane Wilson existence theorem is claimed.
