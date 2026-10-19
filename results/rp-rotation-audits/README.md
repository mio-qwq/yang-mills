# Reflection positivity and the rotational bridge

19 October 2026. Source-only research bundle. Includes
scoped proofs, independent AI-assisted audits, exact certificates and immutable
source receipts. This is not a Yang–Mills construction or a mass-gap solution.

## Proven, under explicit hypotheses

1. [RP-to-invariance bridge](reflection-rotation-bridge-20261019/RESULT.md): full
   complex unital reflection positivity implies the stated reflection symmetry.
   Translation placement or a suitable generating half-algebra extends it.
   On one continuum state, the extra (1,2,0,0) mirror plus W4 invariance and
   continuity suffice for O(4) invariance. Those inputs are not supplied here.
2. [Fixed-lattice obstruction](lattice-normal-obstruction-20261019/RESULT.md):
   the unchanged nearest-neighbor hypercubic stencil admits exactly the
   coordinate and signed-diagonal normal lines. In four dimensions these are
   16 mirrors generating the finite 384-element signed-permutation group.
   The specified tilted quotient has four separating mirrors and a 64-element
   stabilizer. Period changes alone do not create the missing oblique mirror.
3. [Bounded scalar rigidity](bounded-rp-kernel-test-20261019/RESULT.md): a
   continuous Hermitian scalar covariance away from zero, locally bounded near
   zero, with genuine complex RP at four coordinate mirrors and two specified
   diagonal mirrors is constant. The argument is analytic, using finite spectral
   mass, not density of a reflection group. The
   [independent audit](bounded-rp-kernel-independent-20261019/AUDIT.md) checks the
   precise final proof and its representation assumptions.

4. [Unbounded Gaussian sharpness example](unbounded-gaussian-rp-countermodel-20261019/RESULT.md):
   an explicit linear derivative of the massless Gaussian free field is
   translation- and W4-invariant and has full Gaussian RP at all sixteen
   mirrors, but its off-diagonal covariance is not rotationally invariant.
   Its ultraviolet singularity fails the separate logarithmic bound. This is
   a sharpness example for missing analytic hypotheses, not a counterexample
   to the bounded scalar theorem or a Wilson Yang–Mills construction.

## Source audit and limits

The [analytic applicability audit](analytic-rotation-audit-20261019/RESULT.md)
is pinned to upstream commit 785a68fdeef78a1da854c4807fe1f17b597d05e7.
Its search did not locate the separately named scalar theorem in the stated
raw files and PDFs; this is a bounded search report, not a nonexistence claim.
An available theorem for Gaussian-dominated closed distributional two-forms
has different hypotheses. Assuming the stated scalar lower witness bound,
its direct substitution would contradict the required Gaussian bound.

The new scalar theorem does not verify its applicability to a Wilson continuum
state or the separate logarithmically improved UV theorem. Contact terms,
tensor index action, complex versus real-only positivity, and same-state
identification remain distinct issues. The real-only alternating example is
not ordinary positive type. No continuum existence, mass gap, global literature
novelty, human peer review or formal proof-assistant verification is claimed.

## Reproduce

With Python 3.10 or later, from this directory:

    python -B verify.py
    python -B -O verify.py

No third-party Python packages are required. The aggregate checks hashes,
provenance and regenerated exact certificate bytes in temporary copies. The
lattice, bounded-kernel and Gaussian original checkers use assert statements: they
require normal Python. The aggregate deliberately launches those scripts
without -O in both modes and reports their actual optimization level. Running
those original scripts directly with -O is not a valid mathematical check.
The other original bridge checker and portable bump checker use explicit
exceptions and are tested in the requested mode. Deliberate package and
mathematical corruptions must be rejected.

The exact portable bump check reproduces the radial integral and Lipschitz
bounds without upstream files. audit_sources.py is retained as original
source-search code but is not run by the offline verifier because its external
PDF/TeX inputs are intentionally absent. Saved source-search findings remain
historical evidence. UPSTREAM_SOURCES.json contains immutable URLs, bytes,
SHA-256 and Git blob SHA-1 receipts. If those source files are obtained
separately, their bytes can be checked offline using:

    python -B verify.py --upstream-dir /path/to/upstream/files

This optional step validates bytes; it does not repeat the mathematical audit
or establish correctness of upstream assertions. No automatic downloads occur.

## Provenance and dependency map

All selected original proofs and checkers are byte-preserved. The copied author
checker and its output from the independent-audit folder are exact duplicates;
only their canonical author copies are included. Independent mathematics and
independent symbolic checks remain separate. PROVENANCE.json records this
mapping and all omissions. DEPENDENCIES.json locates historical Wilson/scaling
reports, included once as background to the scope audit; their old checkers
are not claimed rerun by this aggregate.

The complete inventory is manifest.json plus SHA256SUMS. SOURCE_* inventories
and original audit local paths are historical provenance. No upstream PDFs,
large extracted texts, raw TeX, screenshots, executables or caches are included.
This bundle adds results/rp-rotation-audits/ and replaces no prior result.
