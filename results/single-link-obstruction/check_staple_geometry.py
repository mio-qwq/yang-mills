"""Exact geometry and realizable diagonal-SU(2) staple-sum checks."""
from itertools import product
from collections import Counter

def shift(x,mu,n):
 y=list(x); y[mu]=(y[mu]+1)%n; return tuple(y)

# diag(exp(i*pi*k/3),exp(-i*pi*k/3)); first entry in units (1/2,i*sqrt(3)/2).
ROOTS=((2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1))

def check(n):
 d=4;e=((0,)*d,0);paths=[]
 for x in product(range(n),repeat=d):
  for mu in range(d):
   for nu in range(mu+1,d):
    p=(((x,mu),1),((shift(x,mu,n),nu),1),((shift(x,nu,n),mu),-1),((x,nu),-1))
    if any(f==e for f,sign in p):
     target_sign=next(sign for f,sign in p if f==e)
     # Reverse the loop if target is negative, then remove target; diagonal matrices commute.
     paths.append({f:sign*target_sign for f,sign in p if f!=e})
 assert len(paths)==6 and all(len(p)==3 for p in paths)
 counts=Counter(f for p in paths for f in p)
 assert len(counts)==18 and set(counts.values())=={1}
 for path in paths: assert sum(mu==0 for x,mu in path)==1
 def staple_sum(assignment):
  result=[0,0]
  for path in paths:
   phase=sum(sign*assignment.get(f,0) for f,sign in path.items())%6
   for k in (0,1): result[k]+=ROOTS[phase][k]
  return tuple(result)
 for f in counts:
  selected=next(k for k,path in enumerate(paths) if f in path)
  phases=iter((0,0,3,2,4)); assignment={}
  for k,path in enumerate(paths):
   phase=0 if k==selected else next(phases)
   parallel=next(edge for edge in path if edge[1]==0)
   assignment[parallel]=(phase*path[parallel])%6
  assert staple_sum(assignment)==(2,0), (n,f,'before')
  assignment[f]=(assignment.get(f,0)+3)%6
  assert staple_sum(assignment)==(-2,0), (n,f,'after')
 print(f'PASS n={n}: six disjoint staples, 18 neighbors, all 18 one-link flips realize H=+I to H=-I exactly.')

if __name__=='__main__':
 for n in (4,5,6,8): check(n)
