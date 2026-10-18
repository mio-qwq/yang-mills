"""Finite combinatorial checks for the independently audited tilted torus."""
from itertools import product, combinations
import json

def check(N,d):
    mod=2*N
    V=[(u,v)+z for u in range(mod) for v in range(mod) if (u-v)%2==0 for z in product(range(N), repeat=d-2)]
    def add(x,i):
        y=list(x)
        if i==0: y[0]=(y[0]+1)%mod; y[1]=(y[1]+1)%mod
        elif i==1: y[0]=(y[0]-1)%mod; y[1]=(y[1]+1)%mod
        else: y[i]=(y[i]+1)%N
        return tuple(y)
    def theta(x): return ((-x[0])%mod,)+x[1:]
    def sigma(i): return 1-i if i<2 else i
    def side(x): return 0 if x[0] in (0,N) else (1 if x[0]<N else -1)
    E={(x,i) for x in V for i in range(d)}
    undirected={}
    fixed=0
    for x,i in E:
        y=add(x,i)
        assert x!=y
        key=frozenset((x,y))
        assert key not in undirected, ('duplicate/reversed edge',N,d,x,i)
        undirected[key]=(x,i)
        assert add(theta(x),sigma(i))==theta(y)
        assert not {side(x),side(y)}=={-1,1}
        refl=(theta(x),sigma(i))
        if refl==(x,i):
            assert i>=2 and side(x)==side(y)==0
            fixed+=1
        if side(x)==side(y)==0:
            assert refl==(x,i)
    cuts={0:0,N:0}
    plane=0
    for x in V:
        for i,j in combinations(range(d),2):
            xi,xj=add(x,i),add(x,j)
            xij=add(xi,j)
            assert xij==add(xj,i)
            ps=(x,xi,xij,xj)
            assert len(set(ps))==4
            sides={side(y) for y in ps}
            if -1 in sides and 1 in sides:
                assert (i,j)==(0,1) and x[0] in (0,N)
                assert theta(x)==x and theta(xij)==xij
                assert theta(xi)==xj
                assert side(xi)==-side(xj)!=0
                cuts[x[0]]+=1
            if sides=={0}:
                assert i>=2 and j>=2
                plane+=1
    return dict(N=N,d=d,vertices=len(V),edges=len(E),fixed_plane_edges=fixed,crossing_plaquettes=cuts,plane_plaquettes=plane)

results=[check(N,d) for N in range(3,8) for d in range(2,5)]
print(json.dumps(results,indent=2))
