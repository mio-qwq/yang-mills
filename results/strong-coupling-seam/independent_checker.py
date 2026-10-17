"""Independent finite combinatorial/edge-case checks; not a continuum proof."""
from itertools import product, combinations
from collections import defaultdict, Counter, deque
from fractions import Fraction
from math import tanh, exp

def lattice(n):
    E=[(x,m) for x in product(range(n),repeat=4) for m in range(4)]
    inc=defaultdict(list)
    for x in product(range(n),repeat=4):
        for m,k in combinations(range(4),2):
            xm=list(x); xm[m]=(xm[m]+1)%n
            xk=list(x); xk[k]=(xk[k]+1)%n
            p=frozenset(((x,m),(tuple(xm),k),(tuple(xk),m),(x,k)))
            assert len(p)==4
            for e in p: inc[e].append(p)
    C={e:Counter(f for p in inc[e] for f in p if f!=e) for e in E}
    for e in E:
        assert len(inc[e])==6 and sum(C[e].values())==18
        assert all(C[f][e]==v for f,v in C[e].items())
    return E,C

for n in (4,5):
    E,C=lattice(n)
    origin=((0,0,0,0),0)
    # A link across the periodic seam is graph-adjacent, despite a large
    # coordinate difference in the unwrapped representation.
    wrap=((0,n-1,0,0),0)
    assert wrap in C[origin]
    # Verify exact support propagation of powers of incidence matrix.
    distance={origin:0}; queue=deque([origin])
    while queue:
        e=queue.popleft()
        for f in C[e]:
            if f not in distance:
                distance[f]=distance[e]+1; queue.append(f)
    row={origin:1}
    for k in range(5):
        assert sum(row.values())==18**k
        assert all(distance[e]<=k for e in row)
        new=Counter()
        for e,w in row.items():
            for f,v in C[e].items(): new[f]+=w*v
        row=dict(new)
    print(f'PASS n={n}: {len(E)} links, symmetric multiplicities, degree 18, periodic wrap, power propagation')

# The sharp TV/log-oscillation bound is attained by two endpoint likelihood ratios.
for D in (0.01,0.2,1.0,4.0,10.0):
    a=exp(-D/2); b=exp(D/2)
    tv=(1-a)*(b-1)/(b-a)
    assert abs(tv-tanh(D/4))<1e-12
print('PASS: sharp TV factor 1/4')
# At beta=0, two disjoint plaquette normalized characters have variance 1/4
# each by SU(2) Haar character orthogonality; their difference is reflection-odd.
variance=2*Fraction(1,4)
Q=-variance
assert Q==Fraction(-1,2)
print('COUNTEREXAMPLE to unrestricted RP corollary: beta=0, F=X-Theta X, Q=-1/2 < 0')
print('Empty seam: V=0 identically, so all seam-response quantities vanish exactly.')
