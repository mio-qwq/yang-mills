"""Exact combinatorial check; no Monte Carlo or clustering assumptions."""
from itertools import product, combinations

def check(n):
    def shift(x,k):
        y=list(x); y[k]=(y[k]+1)%n; return tuple(y)
    def internal(e):
        x,k=e
        return all(x) and all(shift(x,k))
    adj={}; counts={}; seam_edges=set()
    for x in product(range(n),repeat=4):
        for mu in range(4):
            e=(x,mu)
            if internal(e):
                y=shift(x,mu)
                assert x!=y and abs(x[mu]-y[mu])==1
                adj.setdefault(x,set()).add(y)
                adj.setdefault(y,set()).add(x)
        for mu,nu in combinations(range(4),2):
            p=((x,mu),(shift(x,mu),nu),(shift(x,nu),mu),(x,nu))
            inside=[e for e in p if internal(e)]
            counts[len(inside)]=counts.get(len(inside),0)+1
            if len(inside)==1: seam_edges.add(inside[0])
    assert set(counts)<={0,1,4}
    for x,neighbors in adj.items():
        for y in neighbors:
            assert (sum(x)-sum(y))%2==1
            assert not (neighbors & adj[y]) # no triangles
    # Every four-cycle is a coordinate unit square; enumerate by common neighbors.
    squares=set()
    for x,neighbors in adj.items():
        for y,z in combinations(neighbors,2):
            for w in (adj[y]&adj[z])-{x}:
                vertices=frozenset((x,y,z,w))
                varying=[k for k in range(4) if len({v[k] for v in vertices})>1]
                assert len(varying)==2
                assert all(max(v[k] for v in vertices)-min(v[k] for v in vertices)==1 for k in varying)
                squares.add(vertices)
    print(f'PASS n={n}: plaquette counts={counts}; seam-edge count={len(seam_edges)}; '
          f'four-cycles={len(squares)}, all elementary; no cycles with <=3 distinct edges.')

if __name__=='__main__':
    for n in (4,5,6,8): check(n)
