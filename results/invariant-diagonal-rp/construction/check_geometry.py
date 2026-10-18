#!/usr/bin/env python3
"""Exact finite combinatorial checks. Original audit code, no third-party code."""
from itertools import product, combinations
import json
from pathlib import Path

def add(x,j):
    y=list(x); y[j]+=1; return tuple(y)
def u(x): return x[0]-x[1]
def v(x): return x[0]+x[1]
def theta(x,a): return (x[1]+a,x[0]-a,*x[2:])
def swap(j): return 1-j if j<2 else j

def check(d,W,a,T):
    # |u-a|<=T and |v|<=W imply |x0|,|x1| <= (|a|+T+W)/2.
    B=abs(a)+T+W+1
    verts={x for x in product(range(-B,B+1),range(-B,B+1),*[range(-W,W+1)]*(d-2))
           if abs(v(x))<=W and abs(u(x)-a)<=T}
    assert {theta(x,a) for x in verts}==verts
    edges={(x,j) for x in verts for j in range(d) if add(x,j) in verts}
    assert {(theta(x,a),swap(j)) for x,j in edges}==edges
    for x,j in edges:
        vals=[u(x),u(add(x,j))]
        assert min(vals)>=a or max(vals)<=a
        if vals==[a,a]: assert j>=2
    ps={(x,i,j) for x in verts for i,j in combinations(range(d),2)
        if add(x,i) in verts and add(x,j) in verts and add(add(x,i),j) in verts}
    refl={(theta(x,a),*sorted((swap(i),swap(j)))) for x,i,j in ps}
    assert refl==ps
    crosses=0
    for x,i,j in ps:
        vs=[x,add(x,i),add(x,j),add(add(x,i),j)]
        vals=[u(y) for y in vs]
        crossing=min(vals)<a<max(vals)
        assert crossing == (i==0 and j==1 and u(x)==a)
        if crossing:
            crosses+=1
            assert theta(x,a)==x
            assert theta(add(x,0),a)==add(x,1)
            assert theta(add(add(x,0),1),a)==add(add(x,0),1)
        # Positively oriented link tails of this plaquette.
        tails=[x,add(x,i),add(x,j),x]
        blocks={u(y)//2 for y in tails}
        assert max(blocks)-min(blocks)<=1
    return dict(d=d,width=W,center=a,length=T,vertices=len(verts),edges=len(edges),plaquettes=len(ps),crossing_plaquettes=crosses)

results=[check(d,W,a,T) for d in (2,3,4) for W in (1,2) for a in range(-2,3) for T in (1,3)]
out={'status':'PASS','cases':len(results),'checks':['reflection-invariant vertices, oriented links, plaquettes','no strict-side crossing link','fixed links have tangent directions','only 01 plaquettes based at u=a cross','crossing paths are reflections with fixed endpoints','each plaquette uses at most two adjacent disjoint two-level link blocks'],'cases_detail':results}
Path(__file__).with_name('geometry_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ('status','cases','checks')},indent=2))
