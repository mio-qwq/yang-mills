"""Exact mixed-plaquette geometry for the actual free-cube seam."""
from itertools import product

def move(x,mu,delta,n):
 y=list(x); y[mu]=(y[mu]+delta)%n; return tuple(y)

def check(n):
 assert n%2==0 and n>=6
 d=4; N=n//2
 x=(n-1,N,N,N); target=(x,0)
 opposite=[(move(x,nu,sign,n),0) for nu in range(1,d) for sign in (-1,1)]
 selected=set(opposite+[target]); incidence={e:[] for e in selected}
 def internal(e):
  x,mu=e
  return all(x) and all(move(x,mu,1,n))
 for y in product(range(n),repeat=d):
  for mu in range(d):
   for nu in range(mu+1,d):
    p=((y,mu),(move(y,mu,1,n),nu),(move(y,nu,1,n),mu),(y,nu))
    statuses=[bool(internal(e)) for e in p]
    mixed=any(statuses) and not all(statuses)
    for e in set(p)&selected: incidence[e].append((p,mixed))
 for e in selected:
  assert len(incidence[e])==6
  assert all(mixed for p,mixed in incidence[e])
 assert len(set(opposite))==6
 union={tuple(p) for e in opposite for p,mixed in incidence[e]}
 assert len(union)==36
 # Each target staple contains exactly its own one of the six opposite links.
 for p,mixed in incidence[target]:
  assert len(set(p)&set(opposite))==1
  assert len(set(p)-{target})==3
 print(f'PASS n={n}: target and six opposite crossing links have only deleted/mixed plaquettes; six private staples; 36 incident seam plaquettes.')

if __name__=='__main__':
 for n in (6,8,10): check(n)
