#!/usr/bin/env python3
"""Exact finite checks for RESULT.md; Python standard library only.

The script verifies polynomial algebra, not Gaussian functional analysis.
Optimized Python is rejected because the exact checks use assert statements.
"""
import sys

if not __debug__:
    sys.stderr.write("ERROR: optimized Python (-O/-OO) is unsupported; exact checks require assertions.\n")
    raise SystemExit(2)

from fractions import Fraction as F
from itertools import combinations
from math import comb
from pathlib import Path
import json


def clean(p):
    return {a: F(c) for a, c in p.items() if c}


def const(c, n=3):
    return {(0,) * n: F(c)} if c else {}


def var(i, n=3):
    a = [0] * n
    a[i] = 1
    return {tuple(a): F(1)}


def add(*polys):
    out = {}
    for p in polys:
        for a, c in p.items():
            out[a] = out.get(a, F(0)) + c
    return clean(out)


def scale(p, c):
    return clean({a: c * v for a, v in p.items()})


def mul(p, q):
    out = {}
    for a, c in p.items():
        for b, d in q.items():
            ab = tuple(x + y for x, y in zip(a, b))
            out[ab] = out.get(ab, F(0)) + c * d
    return clean(out)


def power(p, k):
    n = len(next(iter(p)))
    out = const(1, n)
    for _ in range(k):
        out = mul(out, p)
    return out


def evaluate(p, xs):
    return sum(c * product(F(x) ** k for x, k in zip(xs, a))
               for a, c in p.items())


def product(xs):
    out = F(1)
    for x in xs:
        out *= x
    return out


def same(p, q):
    assert clean(p) == clean(q), (p, q)


def diagonal_residue_q_even(m):
    # ((u+v)^(2m)+(u-v)^(2m))/2^m + w^(2m)+z^(2m),
    # followed by u^2=-(A+B+C), v^2=A, w^2=B, z^2=C.
    A, B, C = (var(i) for i in range(3))
    T = add(A, B, C)
    terms = [scale(mul(power(T, j), power(A, m-j)),
                   F(2, 2 ** m) * comb(2*m, 2*j) * (-1) ** j)
             for j in range(m+1)]
    return add(*terms, power(B, m), power(C, m))


def as_terms(p):
    return [{"powers": list(a), "coefficient": str(c)}
            for a, c in sorted(p.items(), reverse=True)]


def main():
    A, B, C = (var(i) for i in range(3))
    S = add(B, C)
    T = add(A, B, C)
    q4d = diagonal_residue_q_even(2)
    q6d = diagonal_residue_q_even(3)
    expected4 = add(scale(power(A, 2), -2), scale(mul(A, S), -2),
                    scale(add(power(B, 2), power(C, 2)), F(3, 2)), mul(B, C))
    expected6 = scale(mul(S, add(power(A, 2), mul(A, S),
                                  scale(power(add(B, scale(C, -1)), 2), F(1, 4)))), 3)
    same(q4d, expected4)
    same(q6d, expected6)
    q4c = add(power(T, 2), power(A, 2), power(B, 2), power(C, 2))
    q6c = add(scale(power(T, 3), -1), power(A, 3), power(B, 3), power(C, 3))
    rays = {
        "coordinate_axis": ([1, 0, 0], q4c, q6c, [2, 0]),
        "diagonal_difference_axis": ([1, 0, 0], q4d, q6d, [-2, 0]),
        "coordinate_two_equal": ([1, 1, 0], q4c, q6c, [6, -6]),
        "diagonal_external_axis": ([0, 1, 0], q4d, q6d, [F(3, 2), F(3, 4)]),
    }
    ray_results = {}
    for name, (point, p, q, expected) in rays.items():
        actual = [evaluate(p, point), evaluate(q, point)]
        assert actual == list(map(F, expected))
        ray_results[name] = {"squared_coordinates": point,
                             "Q4": str(actual[0]), "Q6": str(actual[1])}

    # Newton identities in four x_i=p_i^2 variables.
    xs = [var(i, 4) for i in range(4)]
    es = {}
    for j in range(1, 5):
        terms = []
        for inds in combinations(range(4), j):
            term = const(1, 4)
            for i in inds:
                term = mul(term, xs[i])
            terms.append(term)
        es[j] = add(*terms)
    Q4 = add(*(power(x, 2) for x in xs))
    Q6 = add(*(power(x, 3) for x in xs))
    same(Q4, add(power(es[1], 2), scale(es[2], -2)))
    same(Q6, add(power(es[1], 3), scale(mul(es[1], es[2]), -3), scale(es[3], 3)))

    # Diagonal e4: ((u^2-v^2)^2 / 4) * w^2*z^2.
    e4d_direct = scale(mul(power(add(scale(T, -1), scale(A, -1)), 2), mul(B, C)), F(1, 4))
    e4d = scale(mul(power(add(scale(A, 2), B, C), 2), mul(B, C)), F(1, 4))
    same(e4d_direct, e4d)
    e4c = scale(mul(T, mul(A, mul(B, C))), -1)
    assert evaluate(e4c, [1, 1, 1]) == -3
    assert evaluate(q4c, [1, 1, 1]) ** 2 == 144
    assert evaluate(e4d, [1, 0, 0]) == 0
    assert evaluate(q4d, [1, 0, 0]) ** 2 == 4

    # Exact symbolic witness A=sqrt(3)-1, B=C=1 without floats:
    # reduce the univariate specialization modulo A^2+2A-2.
    def specialize_BC_one(p):
        out = {}
        for (a, b, c), coefficient in p.items():
            out[a] = out.get(a, F(0)) + coefficient
        return {k: v for k, v in out.items() if v}
    def reduce_root(p):
        out = specialize_BC_one(p)
        while out and max(out) >= 2:
            d = max(out)
            coef = out.pop(d)
            out[d-1] = out.get(d-1, F(0)) - 2*coef
            out[d-2] = out.get(d-2, F(0)) + 2*coef
            out = {k: v for k, v in out.items() if v}
        return out
    assert reduce_root(q4d) == {}
    assert reduce_root(e4d) == {0: F(3)}

    # Explicit nonnegative coordinate certificate.
    vars3 = [A, B, C]
    sos = {}
    for i, j in combinations(range(3), 2):
        k = next(v for v in range(3) if v not in (i, j))
        diff = add(vars3[i], scale(vars3[j], -1))
        sos = add(sos, scale(power(diff, 4), 2),
                  scale(mul(mul(vars3[k], add(vars3[i], vars3[j])), power(diff, 2)), 16))
    inequality_poly = add(power(q4c, 2), scale(mul(T, mul(A, mul(B, C))), -48))
    same(inequality_poly, sos)

    # Complex-null witness is rational in x_i=p_i^2.
    x = [F(-1), F(1), F(0), F(0)]
    rx = [F(-1), F(1, 2), F(1, 2), F(0)]
    assert sum(x) == sum(rx) == 0
    value = evaluate(Q4, x) ** 2
    rotated_value = evaluate(Q4, rx) ** 2
    assert (value, rotated_value, value-rotated_value) == (F(4), F(9, 4), F(7, 4))

    result = {
        "status": "PASS",
        "arithmetic": "fractions.Fraction; exact polynomial dictionaries; no floating point",
        "optimized_python": "Explicit startup rejection (exit 2) under -O and -OO; no PASS output is generated.",
        "diagonal_Q4": as_terms(q4d),
        "diagonal_Q6": as_terms(q6d),
        "diagonal_e4": as_terms(e4d),
        "forcing_rays": ray_results,
        "Newton_identities": "PASS",
        "degree_eight_cone_endpoint": {"coordinate_Q4_squared": "144", "coordinate_e4": "-3", "upper_gamma_over_alpha": "48"},
        "diagonal_zero_Q4_witness": {"A": "sqrt(3)-1", "B": "1", "C": "1", "Q4": "0", "e4": "3"},
        "coordinate_nonnegative_polynomial_identity": "PASS",
        "null_witness_P": str(value),
        "null_witness_rotated_P": str(rotated_value),
        "null_witness_difference": str(value-rotated_value),
        "limits": "Finite polynomial checks only; analytic Gaussian and RP proofs are in RESULT.md."
    }
    path = Path(__file__).with_name("CHECKS.json")
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "output": str(path), "checks": "all listed exact identities and witnesses"}, indent=2))


if __name__ == "__main__":
    main()
