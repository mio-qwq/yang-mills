#!/usr/bin/env python3
"""Exact quotient-cell checks for the proposed tilted periodic geometry."""
from itertools import product, combinations
from pathlib import Path
import json

def check(d,N):
    verts={x for x in product(range(2*N),range(2*N),*[range(N)]*(d-2)) if x[0]%2==x[1]%2}
    def add(x,j):
        y=list(x)
        if j==0: y[0]=(y[0]+1)%(2*N); y[1]=(y[1]+1)%(2*N)
        elif j==1: y[0]=(y[0]-1)%(2*N); y[1]=(y[1]+1)%(2*N)
        else: y[j]=(y[j]+1)%N
        return tuple(y)
    def th(x): return ((-x[0])%(2*N),*x[1:])
    def side(x): return 0 if x[0] in (0,N) else (1 if x[0]<N else -1)
    def sw(j): return 1-j if j<2 else j
    assert len(verts)==2*N**d
    assert {th(x) for x in verts}==verts
    assert {x for x in verts if th(x)==x}=={x for x in verts if side(x)==0}
    edges={(x,j) for x in verts for j in range(d)}
    for x,j in edges:
        assert add(x,j) in verts
        assert th(add(x,j))==add(th(x),sw(j))
        assert {side(x),side(add(x,j))}!={-1,1}
        if th(x)==x and th(add(x,j))==add(x,j): assert j>=2
    crosses=0
    for x in verts:
        for i,j in combinations(range(d),2):
            vs=(x,add(x,i),add(x,j),add(add(x,i),j))
            assert len(set(vs))==4
            sides={side(y) for y in vs}
            crossing=1 in sides and -1 in sides
            assert crossing==(i==0 and j==1 and x[0] in (0,N))
            if crossing:
                crosses+=1
                pdir=0 if x[0]==0 else 1
                ndir=1-pdir
                assert side(add(x,pdir))==1
                assert side(add(x,ndir))==-1
                assert th(add(x,pdir))==add(x,ndir)
                assert th(x)==x and th(add(add(x,pdir),ndir))==add(add(x,pdir),ndir)
    return dict(d=d,N=N,vertices=len(verts),oriented_edges=len(edges),plaquettes=len(verts)*d*(d-1)//2,crossing_plaquettes=crosses)

rows=[check(d,N) for d in (2,3,4) for N in range(3,9)]
out={'status':'PASS','cases':len(rows),'checks':['quotient size 2 N^d and parity','two fixed planes u=0,N','all direction maps respected','no strict-side crossing links','only 01 squares at either fixed plane cross','positive and negative two-edge paths reflect with fixed endpoints'],'cases_detail':rows}
Path(__file__).with_name('tilted_torus_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ('status','cases','checks')},indent=2))
