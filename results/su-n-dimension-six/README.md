# SU(N≥3), dimension six: quotient dimensions 6/5 and four symmetric-cubic classes

A standalone finite local-operator result: antisymmetric hypercubic tensor densities have quotient dimensions 6 off shell and 5 on shell, with four additional symmetric-color cubic classes compared with SU(2). Read THEOREM.md for the exact conventions and proof. The four added classes are charge-conjugation odd: the C-even quotient remains **2/1** for every N>=2. They are excluded from symmetry-preserving C-even rotation counterterms; see the charge-conjugation refinement in the theorem.

## Contents

- THEOREM.md: statement, color-tensor proof, nonlinear equation justification, rank argument, four representatives and constant-Cartan witness
- check_symmetric_cubic.py: independent 384-element character sum, full 56-monomial stabilizer system, basis and wrong-sign negative test
- check_cartan_witness.py: exact symbolic curvature, covariant derivative and cubic-independence checks
- su2_certificate/: included dependencies for the unchanged quadratic-sector counts and exact divergence/curl rank certificates; PROOF.md explains those certificates
- AI_REVIEW.md: earlier independent AI review of the candidate, retained with its original context
- SOURCE_MANIFEST.json: exact input SHA-256 hashes and attribution
- actualrunlog.txt: actual commands, versions and outputs from this packet's checks

## Reproduce

Requires Python 3 and SymPy. From this directory run:

    python check_symmetric_cubic.py
    python check_cartan_witness.py
    python charge_conjugation/check_charge.py
    python su2_certificate/characters2.py
    python su2_certificate/check_certificate.py

The last checker reconstructs the stored matrices and verifies nonzero minors through integer Bareiss elimination; it also rejects deliberate matrix-entry and determinant corruption. The generator divergence.py is included for reproducibility but rerunning it overwrites its adjacent certificate JSON files. The verification commands above are read-only.

## Boundaries

These are constant-coefficient polynomial local densities in a pure gauge connection. Quotients use gauge-invariant polynomial divergence currents and, on shell, the full Yang–Mills differential ideal. The result does not apply unchanged to explicit-coordinate currents, arbitrary nonlocal operators, matter fields or unspecified gauge groups.

The supplied upstream SU(2) statement is credited; this extension was derived in the parent research task and checked by AI assistants. No human review, proof-assistant certification, historical priority, continuum construction or mass-gap result is claimed. The frozen v0.1 packet and upstream repository were not changed. Local polynomial Cartan connections are algebraic test fields, not assertions about finite-action global configurations.
