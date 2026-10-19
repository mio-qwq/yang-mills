# Scalar general angular rigidity

Source-only research archive, 19 October 2026.

## Accepted result and limits

For tau>0 and b>0, let F_b(p) be the angular average of
1/[b+|p|^2+tau(p dot v)^2] on S3 against a normalized nonnegative L1 density rho.
If rho is antipodally even and W4-invariant, reflection positivity at the
coordinate mirror e1 and diagonal mirror (e1+e2)/sqrt(2) forces rho=1 almost
everywhere. Conversely the constant density is reflection positive at every
mirror. Without antipodal evenness, only the even part is identified: the odd
part is invisible to the covariance. The general formulation requires covariance
reflection invariance and reflection positivity at every coordinate and diagonal
mirror. These are full-spacetime/all-tangential-momenta hypotheses.

The result covers arbitrary L1 densities and has no finite-axis or finite-harmonic
restriction. Its proof includes compact spectral support, two-mirror continuation,
Jensen equality propagation, even harmonic identifiability, and transfer to finite
positive mass. A nonconstant even W4-invariant density has an existential compact
negative witness for at least one required mirror; no numerical witness is given.

This class of positive normalized angular-integral scalar Gaussian covariances is
classified under the stated hypotheses. Adding axes or smoother densities within
it does not evade the result. Interacting Yang-Mills and its mass gap are outside
scope. There is no formal proof-assistant certification, external peer review or
novelty claim. Exact symbolic checks verify algebra, not the analytic theorem.

## Reproduce

Check `sha256sum -c SHA256SUMS`, extract the original ZIP and run in its directory.
The recorded environment is Python 3.12.14 with SymPy 1.14.0 already installed:

    python -I -B tools/verify_package.py
    python -I -B tools/replay_checks.py
    python -I -B -O tools/replay_checks.py
    python -I -B tools/rebuild_archive.py ../rebuilt.zip

The primary checker runs 28 exact checks and three built-in corruption rejections
per mode; the independent checker runs five exact checks. Eight external mutation
variants must fail in both modes, giving 16 required rejections per replay.
Outputs match preserved reference bytes. No network access is needed. The
deterministic archive uses sorted paths, fixed metadata and ZIP_STORED.

Read proofs/GENERAL_ANGULAR_RIGIDITY.md and proofs/INDEPENDENT_AUDIT.md. The complete
bounded-Hankel analytic dependency is included as proofs/BOUNDED_HANKEL_FULL_SOURCE.md.
Original source bytes, original manifests, append-only historical reconciliation
and exact outputs are preserved; no changed current pin is silently rewritten.

## Archive verification

VERIFICATION.json records the frozen checkpoint and a fresh independent archival
clean extraction, complete replay in both Python modes, and byte-identical rebuild.
The checkpoint's local-only/external-action fields describe packaging before this
additive archival commit. This directory adds only the exact original ZIP, this
README, SHA256SUMS and VERIFICATION.json. No existing source or archive is replaced.
No PR, merge, tag or release is created by this source archival operation.
