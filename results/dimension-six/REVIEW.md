# Independent assistant review: dimension-six SU(2) certificate

Reviewed 2026-10-17 UTC. Target: frozen results/dimension-six packet in /tmp/ym-publish-20261017. PROOF.md SHA-256: 67564576831882cc8f06cb6e22cc9ffc0fa68eebae39fa611a5fd5c2a9b407dd.

## Outcome

No blocking mathematical or computational flaw identified in the bounded local-algebra statement: antisymmetric W4 multiplicity modulo gauge-invariant total derivatives is 2 off shell and 1 modulo the Yang-Mills differential ideal. This is a separate AI-assisted review, not human peer review or proof-assistant formal verification. It does not validate any global/quantum Yang-Mills claim.

## Reproduced checks

Ran characters2.py, independent_characters.py, check_certificate.py, and validate_equivariance.py successfully. The character multiplicities reproduce 11/16/7 off shell and 6/12/7 on shell. Independently reconstructed minor determinants are (current, divergence, curl)=(586,990,585) off shell and (579,149,336) on shell modulo 1009. Corruption tests pass. Regenerated JSON files using a copy of divergence.py in a separate directory; both compare byte-for-byte with the frozen files.

## Mathematical review

1. The parity condition and (12)-odd/(34)-even stabilizer condition characterize the component of an equivariant map from Lambda^2 V. The candidate projector has the appropriate signs, including its action on the vector/current and antisymmetric potential indices. Extending by signed-permutation transport is consistent with the full stabilizer. All candidate monomials are valid gauge-invariant currents after replacing the displayed linear derivative by a covariant derivative inside the color pairing.

2. At weights 4,5,6, SU(2) color invariants are exhausted by the rank-two pairing and rank-three alternating tensor. The indicated Sym^2, tensor-product, and Lambda^3 modules are appropriate. The elementary edge-graph argument correctly excludes Lambda^2 V from the cubic-color term; its two stabilizer actions coincide, whereas the desired target characters differ.

3. The nonlinear jet argument is sound at the claimed orders: radial/normal gauge supplies triangular polynomial coordinates with top Young modules (k+1,1). The Yang-Mills equations and their first derivatives are affine in their highest jets. The displayed polynomial potentials prove surjectivity of their principal maps onto V and trace-free V tensor V. The identity D_mu J_mu=0 supplies the scalar compatibility, so no extra top-order equation has been silently subtracted. These facts justify the stated on-shell character upper bounds. For a fully expanded exposition, spell out the radial-gauge coordinate bijection and explain exactness of taking invariants under compact SU(2) and finite W4.

4. The on-shell lower bounds can be justified more directly than the prose currently emphasizes. A sum of two complex null plane waves in one fixed color direction is an exact solution of the nonlinear SU(2) equations, since all commutators vanish. Therefore every element of the full Yang-Mills differential ideal vanishes on these tests. A nonzero evaluated minor proves independence modulo that full ideal, not only a linearized ideal. Complex solutions are legitimate tests for polynomial identities over the reals.

5. The modular lifting argument is valid: 1009 is prime, 469^2=-1 modulo 1009, and each selected polarization denominator is invertible. The formulas define rational functions over Q(i); an identically zero characteristic-zero determinant could not have the recorded nonzero residue. No density of the chosen sample family is needed for a lower bound.

6. Curl images are genuine gauge-invariant curls and their divergence vanishes identically. Seven independent curl images and current dimensions 16/12 give upper divergence ranks 9/5. The matching modular lower ranks prove equality. This avoids any general covariant Poincare lemma. Because the possible nonlinear discrepancy at weight six is cubic in F and its target isotypic component is zero, the quadratic testing determines this full nonabelian channel.

## Presentation limitations

The dimension claims were already proposed in the reference manuscript. Describe this packet as an explicit finite certificate/proof of that local classification, not a new discovery of the dimensions. It provides quotient dimensions and current/curl certificates, not an independently displayed preferred basis of quotient representatives. No historical-priority conclusion follows from this review. No statement about existence, continuum rotation symmetry, clustering, or the mass gap follows.

Publication serialization note: the GitHub web editor adds a terminal newline to JSON. The publication copy normalizes both certificates to that convention and changes only the generator serialization to emit it. Parsed certificate data and all mathematical calculations are unchanged. The lead assistant reran regeneration and checks after this normalization.
