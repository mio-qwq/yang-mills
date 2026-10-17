"""Orientation-aware global link assignments for all 18 target neighbors."""
import numpy as np
from itertools import product,combinations
from math import pi,sqrt,exp
I=np.eye(2,dtype=complex)
W=np.diag([np.exp(2j*pi/3),np.exp(-2j*pi/3)])
zero_staples=[I,I,-I,W,W@W]
assert np.max(abs(sum(zero_staples)))<1e-14

def shift(x,mu,n):
    y=list(x); y[mu]=(y[mu]+1)%n; return tuple(y)

def plaquettes(n,e):
    ps=[]
    for x in product(range(n),repeat=4):
        for m,k in combinations(range(4),2):
            p=(((x,m),1),((shift(x,m,n),k),1),((shift(x,k,n),m),-1),((x,k),-1))
            if any(f==e for f,s in p): ps.append(p)
    return ps

def trace_p(p,U):
    z=I.copy()
    for f,s in p:
        a=U.get(f,I); z=z@(a if s==1 else a.conj().T)
    return np.trace(z).real/2

# Off-diagonal probes exercise orientation, beyond the commuting boundary values.
rng=np.random.default_rng(207)
probes=[]
for _ in range(15):
    q=rng.normal(size=4); q/=np.linalg.norm(q)
    a,b,c,d=q
    probes.append(np.array([[a+1j*b,c+1j*d],[-c+1j*d,a-1j*b]]))
for n in (4,5):
    e=((0,0,0,0),0); ps=plaquettes(n,e)
    ns={f for p in ps for f,s in p if f!=e}
    assert len(ps)==6 and len(ns)==18
    assert all(sum(f in [g for g,s in p] for p in ps)==1 for f in ns)
    for target in ns:
        target_p=next(p for p in ps if target in [f for f,s in p])
        U={}
        for p,B in zip((p for p in ps if p!=target_p),zero_staples):
            # Other links are I. For signs s_e,s_f, the real trace term
            # equals ReTr(U_e B)/2 when U_f=B^(s_e*s_f).
            se=next(s for f,s in p if f==e)
            f,sf=next((f,s) for f,s in p if f!=e and f[1]==0)
            U[f]=B if se*sf==1 else B.conj().T
        for sign in (-1,1):
            U[target]=sign*I
            for ue in probes:
                U[e]=ue
                observed=sum(trace_p(p,U) for p in ps)
                expected=sign*np.trace(ue).real/2
                assert abs(observed-expected)<1e-12,(n,target,observed,expected)
    print(f'PASS n={n}: all 18 neighbors, both signs, 15 noncommuting target-link probes, globally assigned links')
p=1/3-sqrt(3)/(4*pi)
assert p>1/6
v=1-6*exp(-2)
assert 18*v>1 and 6*v>1
print(f'PASS cap p={p:.12f}>1/6; beta=4 TV lower={v:.12f}; row lower={18*v:.12f}')
