#!/usr/bin/env python3
"""Exact finite arithmetic checks supplementing RESULT.md; stdlib only."""
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path
import json


def matmul(a, b):
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(len(b))), F(0))
                       for j in range(len(b[0]))) for i in range(len(a)))


def eye(d):
    return tuple(tuple(F(i == j) for j in range(d)) for i in range(d))


def transpose(a):
    return tuple(zip(*a))


def reflection(v):
    d = len(v)
    vv = sum(x*x for x in v)
    return tuple(tuple(F(i == j) - F(2)*v[i]*v[j]/vv
                       for j in range(d)) for i in range(d))


def signed_permutations(d):
    for perm in permutations(range(d)):
        for signs in product((-1, 1), repeat=d):
            yield tuple(tuple(F(signs[j] if i == perm[j] else 0)
                              for j in range(d)) for i in range(d))


def stringify(a):
    return [[str(x) for x in row] for row in a]


def check(condition, message):
    if not condition:
        raise AssertionError(message)


r = reflection((F(1), F(2)))
s = reflection((F(0), F(1)))
u = matmul(r, s)
check(r == ((F(3,5), F(-4,5)), (F(-4,5), F(-3,5))), 'extra mirror')
check(u == ((F(3,5), F(4,5)), (F(-4,5), F(3,5))), 'plane rotation')
check(matmul(r,r) == eye(2), 'reflection involution')
check(matmul(u,transpose(u)) == eye(2), 'rotation orthogonality')
check(u[0][0]*u[1][1] - u[0][1]*u[1][0] == 1, 'rotation determinant')
check(F(2)*u[0][0] == F(6,5), 'rational noninteger trace')

counts = []
for d in (2,3,4):
    group = set(signed_permutations(d))
    mirrors = {g for g in group if transpose(g) == g and
               matmul(g,g) == eye(d) and sum(g[i][i] for i in range(d)) == d-2}
    normals = []
    for i in range(d):
        n = [F(0)]*d
        n[i] = F(1)
        normals.append(tuple(n))
        for j in range(i+1,d):
            for sign in (-1,1):
                n = [F(0)]*d
                n[i], n[j] = F(1), F(sign)
                normals.append(tuple(n))
    expected = {reflection(n) for n in normals}
    check(mirrors == expected, f'exhaustive mirror classification d={d}')
    check(len(mirrors) == d*d, f'mirror count d={d}')
    counts.append({'dimension':d, 'group_size':len(group), 'mirror_count':len(mirrors)})

# Joint law p_{L,R}. For real half-tests (a,b), Q=2a^2/5+3ab/10+3b^2/10.
p00,p01,p10,p11 = F(2,5),F(1,5),F(1,10),F(3,10)
check(p00+p01+p10+p11 == 1, 'probability normalization')
off = (p01+p10)/2
det = p00*p11-off*off
check(p00 > 0 and det > 0, 'all real tests have positive quadratic form')
check(p10+p11 != p01+p11, 'unequal reflected marginals')
q_real, q_imag = p00+p11, p01-p10
check((q_real,q_imag) == (F(7,10),F(1,10)), 'complex reflected form exposes failure')

out = {
    'status':'passed',
    'arithmetic':'exact fractions, Python standard library',
    'extra_reflection':stringify(r),
    'product_rotation':stringify(u),
    'twice_rotation_cosine':'6/5',
    'hyperoctahedral_counts':counts,
    'real_only_counterexample':{
        'joint_weights':[['2/5','1/5'],['1/10','3/10']],
        'symmetric_quadratic_determinant':str(det),
        'left_mean':str(p10+p11),'right_mean':str(p01+p11),
        'complex_form':{'real':str(q_real),'imaginary':str(q_imag)}
    },
    'limitations':'Finite arithmetic only. Infinite-order, closure, RP and continuum statements are proved in RESULT.md, not by this check.'
}
path = Path(__file__).with_name('checks.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
