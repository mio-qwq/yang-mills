"""Independent standard-library edge-incidence audit, not imported from target."""
from collections import defaultdict, deque
from itertools import combinations, product
import json

def step(x,a,n):
    y=list(x); y[a]=(y[a]+1)%n; return tuple(y)
def vertices(x,axes,n):
    out={x}
    for a in axes: out |= {step(v,a,n) for v in list(out)}
    return out

def run(n):
    points=list(product(range(n), repeat=4))
    faces=[(x,ab) for x in points for ab in combinations(range(4),2)]
    lookup={f:i for i,f in enumerate(faces)}
    incidence=defaultdict(list); edges=[]; fverts=[]; seam=set()
    crossing=0; interface=0
    for i,(x,(a,b)) in enumerate(faces):
        es=((x,a),(step(x,b,n),a),(x,b),(step(x,a,n),b))
        edges.append(es)
        vs=vertices(x,(a,b),n); fverts.append(vs)
        for e in es: incidence[e].append(i)
        if any(d<2 and y[d]==n-1 for y,d in es): seam.add(i)
        else:
            ds=[v[0]-v[1] for v in vs]
            if min(ds)<0<max(ds):
                assert (a,b)==(0,1) and x[0]==x[1]
                mirror=[v for v in vs if v[0]==v[1]]
                assert len(mirror)==2
                crossing+=1
            if min(ds)==max(ds)==0:
                assert (a,b)==(2,3)
                interface+=1
            for y,d in es:
                z=step(y,d,n)
                assert (y[0]-y[1])*(z[0]-z[1])>=0
    distance={p:0 for p in seam}; queue=deque(seam)
    while queue:
        p=queue.popleft()
        for e in edges[p]:
            for q in incidence[e]:
                if q not in distance:
                    distance[q]=distance[p]+1; queue.append(q)
    depth_min={}
    for (x,a), ps in incidence.items():
        y=step(x,a,n)
        if a<2 and x[a]==n-1: continue
        depth=min(x[0],x[1],y[0],y[1],n-1-x[0],n-1-x[1],n-1-y[0],n-1-y[1])
        k=1+min(distance[p] for p in ps)
        assert k>=depth+1,(n,x,a,depth,k)
        depth_min[depth]=min(depth_min.get(depth,10**9),k)
    bad_nonseam=bad_interior=seam_pairs=0
    cube_sets=[]
    for x in points:
        for abc in combinations(range(4),3):
            fs=[]
            for a in abc:
                ab=tuple(b for b in abc if b!=a)
                fs.extend((lookup[(x,ab)],lookup[(step(x,a,n),ab)]))
            cube_sets.append(set(fs))
            pos=[p for p in fs if all(v[0]>v[1] for v in fverts[p])]
            neg=[p for p in fs if all(v[0]<v[1] for v in fverts[p])]
            wrap=any(a<2 and x[a]==n-1 for a in abc)
            if pos and neg:
                if wrap: seam_pairs+=len(pos)*len(neg)
                else: bad_nonseam+=len(pos)*len(neg)
            if wrap:
                assert not any(all(1<=v[0]<=n-2 and 1<=v[1]<=n-2 for v in fverts[p]) for p in fs)
            for p in pos:
                if all(1<=v[0]<=n-2 and 1<=v[1]<=n-2 for v in fverts[p]):
                    bad_interior+=len(neg)
    assert bad_nonseam==bad_interior==0
    p=lookup[((n-1,2,0,0),(2,3))]; q=lookup[((2,0,0,0),(2,3))]
    def reflect(i):
        x,ab=faces[i]; return lookup[((x[1],x[0],x[2],x[3]),tuple(sorted(1-a if a<2 else a for a in ab))) ]
    matrix=[[sum(reflect(a) in c and b in c for c in cube_sets) for b in (p,q)] for a in (p,q)]
    assert matrix==[[0,1],[1,0]]
    return dict(n=n,faces=len(faces),seam_faces=len(seam),cubes=len(cube_sets),nonseam_opposite_pairs=bad_nonseam,interior_opposite_pairs=bad_interior,seam_opposite_pairs=seam_pairs,minimum_action_path_by_endpoint_depth=depth_min,cylinder_crossing_faces=crossing,cylinder_interface_faces=interface,original_matrix=matrix)
if __name__=='__main__':
    for n in (8,9,10): print(json.dumps(run(n),sort_keys=True),flush=True)
