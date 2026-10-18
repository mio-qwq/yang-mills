from itertools import product, combinations
import json

def check(N,d):
 verts=[(u,v)+z for u in range(2*N) for v in range(2*N) if (u-v)%2==0 for z in product(range(N),repeat=d-2)]
 V=set(verts)
 def step(x,j):
  y=list(x)
  if j==0:y[0]=(y[0]+1)%(2*N);y[1]=(y[1]+1)%(2*N)
  elif j==1:y[0]=(y[0]-1)%(2*N);y[1]=(y[1]+1)%(2*N)
  else:y[j]=(y[j]+1)%N
  return tuple(y)
 def theta(x):return ((-x[0])%(2*N),)+x[1:]
 def sign(x):return 0 if x[0] in (0,N) else 1 if x[0]<N else -1
 assert len(V)==2*N**d
 assert sum(theta(x)==x for x in V)==2*N**(d-1)
 cross=0
 for x in verts:
  assert theta(theta(x))==x
  for j in range(d):
   y=step(x,j);assert y in V and sign(x)*sign(y)!=-1
   jj=1-j if j<2 else j
   assert theta(y)==step(theta(x),jj)
  for i,j in combinations(range(d),2):
   a=step(x,i);b=step(x,j);c=step(a,j)
   assert c==step(b,i)
   P={x,a,b,c};assert len(P)==4
   if {sign(z) for z in P}>={-1,1}:
    cross+=1;assert (i,j)==(0,1) and x[0] in (0,N)
    assert {theta(z) for z in P}==P
    fixed=[z for z in P if theta(z)==z];assert len(fixed)==2
    assert x in fixed and c in fixed and theta(a)==b
 assert cross==2*N**(d-1)
 return {'N':N,'dimension':d,'vertices':len(V),'crossing_plaquettes':cross,'status':'PASS'}
print(json.dumps([check(N,d) for N in (3,4,5) for d in (2,3,4)],indent=2))
