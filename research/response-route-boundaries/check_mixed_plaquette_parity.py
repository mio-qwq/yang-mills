from itertools import product

def check(n):
 def shift(x,k):
  y=list(x); y[k]=(y[k]+1)%n; return tuple(y)
 def inside(e):
  x,k=e; return bool(all(x) and all(shift(x,k)))
 counts={}
 for x in product(range(n),repeat=4):
  for mu in range(4):
   for nu in range(mu+1,4):
    p=((x,mu),(shift(x,mu),nu),(shift(x,nu),mu),(x,nu))
    k=sum(inside(e) for e in p)
    counts[k]=counts.get(k,0)+1
 assert set(counts)<= {0,1,4},counts
 print(f'PASS side {n}: counts {counts}; every mixed plaquette has three exterior factors.')

if __name__=='__main__':
 for n in (4,6,8): check(n)
