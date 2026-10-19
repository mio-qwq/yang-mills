#!/usr/bin/env python3
"""Original, standard-library-only exact checks for the accompanying proof.

This does not execute any inherited repository source. Run without -O.
The general classification is proved in RESULT.md; this finite check supplements it.
"""
from fractions import Fraction as F
from itertools import permutations, product, combinations
from collections import deque
import json
from pathlib import Path

D = 4
I = tuple(tuple(F(i == j) for j in range(D)) for i in range(D))
E = tuple(tuple(F(i == j) for i in range(D)) for j in range(D))


def matvec(a, x):
    return tuple(sum(a[i][j] * x[j] for j in range(D)) for i in range(D))


def matmul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(D))
                       for j in range(D)) for i in range(D))


def refl(n):
    q = sum(x * x for x in n)
    return tuple(tuple(F(i == j) - F(2 * n[i] * n[j], q)
                       for j in range(D)) for i in range(D))


def in_gamma(x):
    return all(t.denominator == 1 for t in x) and (x[0] - x[1]) % 2 == 0


def perm_group(gens, size):
    ident = tuple(range(size))
    seen, todo = {ident}, deque([ident])
    while todo:
        p = todo.popleft()
        for g in gens:
            q = tuple(g[p[i]] for i in range(size))
            if q not in seen:
                seen.add(q)
                todo.append(q)
    return seen


def action(a, points):
    lookup = {x: i for i, x in enumerate(points)}
    return tuple(lookup[matvec(a, x)] for x in points)


normals = [tuple(int(i == j) for i in range(D)) for j in range(D)]
for i, j in combinations(range(D), 2):
    for sign in (-1, 1):
        normals.append(tuple((1 if k == i else sign if k == j else 0)
                             for k in range(D)))
reflections = {refl(n) for n in normals}
assert len(reflections) == 16

signed = set()
for p in permutations(range(D)):
    for signs in product((-1, 1), repeat=D):
        signed.add(tuple(tuple(F(signs[j] if i == p[j] else 0)
                               for j in range(D)) for i in range(D)))
assert len(signed) == 384
signed_mirrors = {a for a in signed
                  if matmul(a, a) == I and sum(a[i][i] for i in range(D)) == 2}
assert signed_mirrors == reflections
coordinate_stencil = tuple(E) + tuple(tuple(-x for x in e) for e in E)
full_group = perm_group([action(r, coordinate_stencil) for r in reflections], 8)
assert len(full_group) == 384

# Gamma_1 = <e0+e1, e0-e1, e2, e3>. Scaling by N changes none of these tests.
B = ((F(1), F(1), F(0), F(0)), (F(1), F(-1), F(0), F(0)), E[2], E[3])
stabilizer = {a for a in signed if all(in_gamma(matvec(a, b)) for b in B)}
assert len(stabilizer) == 64
mirror_rows = []
split_matrices = []
for n in normals:
    r = refl(n)
    preserves = r in stabilizer
    # Splitting iff the normal projection (I-R)/2 preserves Gamma.
    projector = tuple(tuple((I[i][j] - r[i][j]) / 2 for j in range(D))
                      for i in range(D))
    splits = preserves and all(in_gamma(matvec(projector, b)) for b in B)
    if splits:
        split_matrices.append(r)
    mirror_rows.append({"normal": n, "preserves_tilted_periods": preserves,
                        "two_separating_fixed_cuts": splits})
assert len(split_matrices) == 4
assert sum(x["preserves_tilted_periods"] for x in mirror_rows) == 8
split_group = perm_group([action(r, coordinate_stencil) for r in split_matrices], 8)
assert len(split_group) == 16

r12 = refl((1, 2, 0, 0))
assert matvec(r12, E[0]) == (F(3, 5), F(-4, 5), F(0), F(0))
rotation = matmul(r12, refl((0, 1, 0, 0)))
assert rotation[:2] == ((F(3, 5), F(4, 5), F(0), F(0)),
                       (F(-4, 5), F(3, 5), F(0), F(0)))

# A rational outside-W4 mirror need not generate a dense group.
# W4 and r_(1,1,1,1) both preserve the 24 short roots of F4.
roots24 = coordinate_stencil + tuple(tuple(F(s, 2) for s in ss)
                                    for ss in product((-1, 1), repeat=D))
assert len(set(roots24)) == 24
r1111 = refl((1, 1, 1, 1))
assert r1111 not in signed
generators = [refl(n) for n in normals[:4]]
generators += [refl(tuple(1 if k == i else -1 if k == i + 1 else 0
                          for k in range(D))) for i in range(3)]
generators += [r1111]
extra_finite_group = perm_group([action(a, roots24) for a in generators], 24)
assert len(extra_finite_group) == 1152

out = {
    "dimension": D,
    "allowed_unoriented_nearest_neighbor_mirrors": 16,
    "signed_permutation_group_order": len(full_group),
    "tilted_period_stabilizer_within_local_action_group_order": len(stabilizer),
    "tilted_period_reflection_automorphisms": 8,
    "tilted_separating_cut_mirrors": 4,
    "tilted_separating_mirror_generated_group_order": len(split_group),
    "mirrors": mirror_rows,
    "rational_obstruction_normal": [1, 2, 0, 0],
    "reflected_unit_edge": [str(x) for x in matvec(r12, E[0])],
    "added_reflection_rotation_cosine": "3/5",
    "added_reflection_rotation_infinite_order_certificate":
        "2 cos(theta) = 6/5 is rational and not an integer; a finite-order rotation would make it an algebraic integer.",
    "body_diagonal_extension_group_order": len(extra_finite_group),
    "all_assertions_passed": True,
}
path = Path(__file__).with_name("exact_results.json")
path.write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
