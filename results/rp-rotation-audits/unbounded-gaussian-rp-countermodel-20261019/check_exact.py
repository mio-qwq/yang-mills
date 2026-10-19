#!/usr/bin/env python3
"""Exact, standard-library-only algebra checks for the linear Gaussian model.

This certifies the finite polynomial calculations, not the analytic Gaussian/RP
arguments in RESULT.md. It executes no repository or downloaded code.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import permutations, product
from pathlib import Path
import json

if not __debug__:
    raise RuntimeError("Run without -O/-OO: exact checks use Python assertions.")

DIM = 4
ZERO = (0,) * DIM


def clean(p):
    return {a: c for a, c in p.items() if c}


def add(*ps):
    out = {}
    for p in ps:
        for a, c in p.items():
            out[a] = out.get(a, 0) + c
    return clean(out)


def scale(p, c):
    return clean({a: c * v for a, v in p.items()})


def multiply(p, q):
    out = {}
    for a, c in p.items():
        for b, d in q.items():
            ab = tuple(a[i] + b[i] for i in range(DIM))
            out[ab] = out.get(ab, 0) + c * d
    return clean(out)


def differentiate(p, j):
    out = {}
    for a, c in p.items():
        if a[j]:
            b = list(a)
            b[j] -= 1
            out[tuple(b)] = c * a[j]
    return clean(out)


def evaluate(p, values):
    total = F(0)
    for a, c in p.items():
        term = F(c)
        for z, n in zip(values, a):
            term *= z ** n
        total += term
    return total


def monomial(j, n):
    a = [0] * DIM
    a[j] = n
    return {tuple(a): 1}


X = [monomial(j, 1) for j in range(DIM)]
R2 = add(*(monomial(j, 2) for j in range(DIM)))
Q = add(*(monomial(j, 4) for j in range(DIM)))


@lru_cache(None)
def derivative_numerator(alpha):
    """D^alpha |x|^-2 = N_alpha(x) / (|x|^2)^(|alpha|+1).

    Recursion follows exactly from the product and chain rules, away from 0.
    """
    if alpha == ZERO:
        return {ZERO: 1}
    j = next(j for j, n in enumerate(alpha) if n)
    beta = list(alpha)
    beta[j] -= 1
    beta = tuple(beta)
    n = sum(beta)
    prev = derivative_numerator(beta)
    return add(multiply(R2, differentiate(prev, j)),
               scale(multiply(X[j], prev), -2 * (n + 1)))


def signed_permutation(p, perm, signs):
    """Substitute x_i -> signs[i] * x_perm[i]."""
    out = {}
    for a, c in p.items():
        b = [0] * DIM
        for i in range(DIM):
            b[perm[i]] += a[i]
            c *= signs[i] ** a[i]
        out[tuple(b)] = out.get(tuple(b), 0) + c
    return clean(out)


N8 = {}
for i in range(DIM):
    for j in range(DIM):
        alpha = [0] * DIM
        alpha[i] += 4
        alpha[j] += 4
        N8 = add(N8, derivative_numerator(tuple(alpha)))

assert all(sum(a) == 8 for a in N8)
assert add(*(differentiate(differentiate(N8, j), j)
             for j in range(DIM))) == {}

expected_by_partition = {
    (8, 0, 0, 0): 18432 * 51,
    (6, 2, 0, 0): -18432 * 476,
    (4, 4, 0, 0): 18432 * 1186,
    (4, 2, 2, 0): 18432 * 12,
    (2, 2, 2, 2): -18432 * 216,
}
expected = {}
for partition, coefficient in expected_by_partition.items():
    for alpha in set(permutations(partition)):
        expected[alpha] = coefficient
assert N8 == expected

group_count = 0
for perm in permutations(range(DIM)):
    for signs in product((-1, 1), repeat=DIM):
        assert signed_permutation(Q, perm, signs) == Q
        assert signed_permutation(N8, perm, signs) == N8
        group_count += 1
assert group_count == 384

mirrors = []
for i in range(DIM):
    perm, signs = list(range(DIM)), [1] * DIM
    signs[i] = -1
    mirrors.append((perm, signs))
for i in range(DIM):
    for j in range(i + 1, DIM):
        for sign in (-1, 1):
            perm, signs = list(range(DIM)), [1] * DIM
            perm[i], perm[j] = j, i
            signs[i] = signs[j] = sign
            mirrors.append((perm, signs))
assert len(mirrors) == 16
for perm, signs in mirrors:
    assert signed_permutation(Q, perm, signs) == Q
    assert sum(signs[i] if perm[i] == i else 0 for i in range(DIM)) == 2
    for i in range(DIM):
        assert perm[perm[i]] == i
        assert signs[i] * signs[perm[i]] == 1

u = (F(1), F(0), F(0), F(0))
v = (F(3, 5), F(4, 5), F(0), F(0))
assert sum(z * z for z in u) == sum(z * z for z in v) == 1
axis, rotated = evaluate(N8, u), evaluate(N8, v)
assert axis == 940032
assert rotated == F(19060586496, 78125)
real_difference = axis - rotated
assert real_difference == F(54379413504, 78125)

# The SO(2) block used in either the real-space or null-vector certificate.
R = ((F(3, 5), F(-4, 5)), (F(4, 5), F(3, 5)))
assert R[0][0] * R[1][1] - R[0][1] * R[1][0] == 1
assert all(sum(R[k][i] * R[k][j] for k in range(2)) == int(i == j)
           for i in range(2) for j in range(2))

# p = (i,1,0,0), Rp = (i,3/5,4/5,0); only even powers occur.
p_squared = (F(-1), F(1), F(0), F(0))
rp_squared = (F(-1), F(9, 25), F(16, 25), F(0))
assert sum(p_squared) == sum(rp_squared) == 0
q_p = sum(z * z for z in p_squared)
q_rp = sum(z * z for z in rp_squared)
null_difference = q_p ** 2 - q_rp ** 2
assert q_p == 2 and q_rp == F(962, 625)
assert null_difference == F(637056, 390625)

# An explicit bound: |N8(x)| <= coefficient_l1 * |x|^8.
coefficient_l1 = sum(abs(c) for c in N8.values())
assert coefficient_l1 == 246841344

# Smooth admissible bump constructed by mollifying (1-|x|^2/a^2)_+^2.
# Only rational inequalities are checked here; integration and mollification
# arguments are written out in RESULT.md.
a, eps = F(19, 20), F(1, 100)
lower_sup = (1 - (eps / a) ** 2) ** 2
assert lower_sup == F(9024, 9025) ** 2
assert a + eps == F(24, 25) < 1
assert F(3, 4) * a ** 4 > F(1, 2)  # pi^2 > 9
lip_bound_squared = F(64, 27) / a ** 2
assert lip_bound_squared < 4 * lower_sup ** 2
assert 4 - 2 * (a + eps) == F(52, 25)

out = {
    "status": "all exact checks passed",
    "scope": "finite algebra only; analytic proof is in RESULT.md",
    "python_dependencies": "standard library only",
    "W4_elements_checked": group_count,
    "W4_mirrors_checked": len(mirrors),
    "N8_degree": 8,
    "N8_monomials": len(N8),
    "N8_harmonic": True,
    "N8_axis": str(axis),
    "N8_rational_rotated_axis": str(rotated),
    "N8_real_point_difference": str(real_difference),
    "N8_coefficient_l1_bound": coefficient_l1,
    "null_Q_before": str(q_p),
    "null_Q_after": str(q_rp),
    "null_Q_squared_difference": str(null_difference),
    "UV_fixed_height_pair_scaling_exponent": -2,
    "UV_test_theta": "1/2",
    "UV_bump_support_radius_at_scale_one": str(a + eps),
    "UV_pair_support_separation_at_scale_one": str(4 - 2 * (a + eps)),
    "N8_coefficients": [{"powers": list(alpha), "coefficient": c}
                        for alpha, c in sorted(N8.items(), reverse=True)],
}
base = Path(__file__).resolve().parent
(base / "CHECKS.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps({k: v for k, v in out.items() if k != "N8_coefficients"}, indent=2))
