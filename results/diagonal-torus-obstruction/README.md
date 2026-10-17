# Finite-torus half-algebra obstruction

For the four-dimensional SU(2) Wilson torus of side n >= 8, with normalized plaquette trace X_p = Tr(U_p)/2 and density exp(beta sum_p X_p), the coordinate-swap reflection theta(x0,x1,x2,x3)=(x1,x0,x2,x3) and the representative half x0>x1 in coordinates 0,...,n-1 admit a local plaquette difference F=P-Q with

    E_beta[(Theta F) F] = -beta^4/512 + O_n(beta^5).

The form is strictly negative for 0 < beta <= 1/[128(6n^4)^5]. The two observable plaquettes have nonwrapping links strictly in this specified half, but approach the artificial periodic seam as volume grows.

## Scope

This obstructs this precise finite-torus half-algebra positivity shortcut. A conjugate reflection requires the conjugated half-algebra. It is not a counterexample for every centered fundamental domain, every torus half-algebra, or the specific fixed compact sources strictly inside C in the existing boundary-response bridge. It neither refutes continuum reflection positivity nor settles Yang–Mills existence or mass gap. No historical novelty claim is made.

PROOF.md also discusses the known free-box factorization and its literature context. The included independent audit specifically checks the finite-torus coefficient, geometry, and explicit small-beta range; it must not be read as a blanket transfer of free-box positivity to periodic geometry.

## Reproduce

Python 3, standard library only. From this directory:

    python check_small_cores.py
    python independent_audit.py
    python check_cube_haar.py

The first classifier uses integer-lattice local cores. The independent checker enumerates all six root orientations modulo 8 and checks the witness cube-count matrix. The independent exact Haar checker uses degree-two quaternion cubature on five gauge-fixed links (32,768 samples), yielding 1/1024. These finite checks support, rather than formally verify, the written all-n argument. See VERIFICATION.md and INDEPENDENT_AUDIT.md.
