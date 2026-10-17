"""Independent centered-coordinate geometry and analytic-constant checks."""
from itertools import product,combinations
from math import pi,sqrt,log

def move(x,j,k,N):
 y=list(x); y[j]=(y[j]+k+N)%(2*N)-N; return tuple(y)
def check(N):
 vertices=list(product(range(-N,N),repeat=4))
 inside=lambda x: all(-N+1<=z<=N-1 for z in x)
 def interior(e): return inside(e[0]) and inside(move(e[0],e[1],1,N))
 ps=[]
 for x in vertices:
  for mu,nu in combinations(range(4),2):
   ps.append(frozenset(((x,mu),(move(x,mu,1,N),nu),(move(x,nu,1,N),mu),(x,nu))))
 for mu in range(4):
  for face in (-N,N-1):
   x=tuple(face if j==mu else 0 for j in range(4)); e=(x,mu)
   B={(move(x,j,k,N),mu) for j in range(4) if j!=mu for k in (-1,1)}
   relevant={f:[p for p in ps if f in p] for f in B|{e}}
   for f,fp in relevant.items():
    assert len(fp)==6
    assert all(0<sum(interior(g) for g in p)<4 for p in fp)
   assert len(set().union(*(set(relevant[f]) for f in B)))==36
   paths=[p-{e} for p in relevant[e]]
   assert len(set().union(*paths))==18
   assert all(len(path&B)==1 for path in paths)
 print(f'PASS side {2*N}: all 8 faces, 36 mixed incident plaquettes, 18 disjoint staple links')
for N in (3,4): check(N)
c=(sqrt(2)/(81*pi))**3
assert 1.7e-7<c<1.8e-7
# Exact identity for the product-ball optimization, checked at varied beta.
haar_c=8/(3*pi**3)
for beta in (1,4,10,100,10000):
 delta=(8*beta)**-.5
 direct=8*delta**2+2/(3*beta)*log(1/(haar_c*delta**3))
 simplified=(1+log(8*beta)+(2/3)*log(3*pi**3/8))/beta
 assert abs(direct-simplified)<1e-12
print('PASS small-h constant and periodic entropy prefactor algebra')
