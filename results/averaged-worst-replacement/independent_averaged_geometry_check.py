#!/usr/bin/env python3
"""Independent exact checks; analytic inequalities are proved in the audit."""
from itertools import product
from fractions import Fraction as F
from collections import Counter
import hashlib
from pathlib import Path
root = Path(__file__).with_name('AVERAGED_WORST_REPLACEMENT.md')
assert hashlib.sha256(root.read_bytes()).hexdigest() == '41c3698b820a3905bd7fbbc444d44421c8b89a4078b472e86881999ee6d33586'

def shift(x, d, s, L):
    y=list(x); y[d]=(y[d]+s)%L; return tuple(y)

def walk(x, steps, L):
    links=[]
    for d,s in steps:
        y=shift(x,d,s,L)
        links.append(((x if s==1 else y,d),s))
        x=y
    return x,links

for L in (4,5,6):
    count=0
    for x in product(range(L),repeat=4):
        for mu in range(4):
            e=(x,mu); endpoint=shift(x,mu,1,L)
            staples=[]
            for nu in range(4):
                if nu==mu: continue
                for sign in (-1,1):
                    end, links=walk(endpoint,[(nu,sign),(mu,-1),(nu,-sign)],L)
                    assert end==x
                    assert e not in [k for k,s in links]
                    staples.append(links)
            counts=Counter(k for path in staples for k,s in path)
            assert len(counts)==18 and all(v==1 for v in counts.values())
            # Independently enumerate all plaquettes which could contain e.
            incident=set()
            for a in range(4):
                for b in range(a+1,4):
                    if mu not in (a,b): continue
                    other=b if a==mu else a
                    for base in (x,shift(x,other,-1,L)):
                        end,p=walk(base,[(a,1),(b,1),(a,-1),(b,-1)],L)
                        assert end==base
                        keys=frozenset(k for k,s in p)
                        if e in keys: incident.add(keys)
            assert len(incident)==6
            assert incident=={frozenset([e]+[k for k,s in p]) for p in staples}
            count+=1
    print(f'L={L}: all {count} target links have six distinct incident plaquettes and 18 private staple-path links.')

# Rational quaternion multiplication: tests the exact one-factor inverse construction.
def qmul(q,r):
    a,b,c,d=q; e,f,g,h=r
    return (a*e-b*f-c*g-d*h,a*f+b*e+c*h-d*g,a*g-b*h+c*e+d*f,a*h+b*g-c*f+d*e)
def conj(q): return (q[0],-q[1],-q[2],-q[3])
Q=[tuple(map(F,q)) for q in ((1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(F(3,5),F(4,5),0,0),(0,F(3,5),0,F(4,5)))]
for A,B,w in product(Q,repeat=3):
    middle=qmul(qmul(conj(A),w),conj(B))
    assert sum(t*t for t in middle)==1
    for sign in (-1,1):
        g=middle if sign==1 else conj(middle)
        assert qmul(qmul(A,g if sign==1 else conj(g)),B)==w
r=F(1,12)
assert 24/r**3 == 41472
assert F(3,8)*3*r*r == F(1,128)
assert F(9,10)/F(51,10)==F(3,17)
assert 298*71**2-1224**2==4042>0
assert 200*6==1200
assert F(5995,1000)-2>3
print('Exact rational attainability and all integer/rational constant checks PASS.')
