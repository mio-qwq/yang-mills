from itertools import product, combinations
from collections import Counter
N=8; D=4
origin=(0,)*D

def move(x,i,s=1):
 y=list(x); y[i]=(y[i]+s)%N; return tuple(y)
def edges(face):
 x,i,j=face
 return frozenset(((x,i),(x,j),(move(x,i),j),(move(x,j),i)))
def incident(edge):
 x,i=edge
 return frozenset((y,*sorted((i,j))) for j in range(D) if j!=i for y in (x,move(x,j,-1)))
def cube(base,dirs):
 return frozenset((move(base,k,s),i,j) for i,j in combinations(dirs,2) for k in dirs if k not in (i,j) for s in (0,1))
checks=[]
for i,j in combinations(range(D),2):
 root=(origin,i,j)
 other=[incident(e)-{root} for e in edges(root)]
 seen=set()
 for selected in product(*other):
  s=frozenset((root,*selected))
  assert len(s)==5
  counts=Counter(e for p in s for e in edges(p))
  boundary=[e for e,c in counts.items() if c==1]
  if not boundary:
   seen.add(s);continue
  candidates=set(incident(boundary[0]))-s
  for e in boundary[1:]: candidates.intersection_update(incident(e))
  for p in candidates:
   t=s|{p}; counts=Counter(e for q in t for e in edges(q))
   if min(counts.values())>=2:seen.add(t)
 expected={cube(move(origin,k,s),tuple(sorted((i,j,k)))) for k in range(D) if k not in (i,j) for s in (0,-1)}
 assert seen==expected
 checks.append({'orientation':(i,j),'tuples':len(list(product(*other))),'cores':len(seen)})
print('EXHAUSTIVE TORUS SUPPORT CHECK',checks)
p=((N-1,2,0,0),2,3);q=((2,0,0,0),2,3)
def theta(face):
 x,i,j=face
 return ((x[1],x[0],x[2],x[3]),i,j)
def cubes_through(face):
 x,i,j=face
 return {cube(move(x,k,s),tuple(sorted((i,j,k)))) for k in range(D) if k not in (i,j) for s in (0,-1)}
M=[[len(cubes_through(theta(a))&cubes_through(b)) for b in (p,q)] for a in (p,q)]
assert M==[[0,1],[1,0]],M
print('CUBE COVARIANCE MATRIX',M)
print('QUADRATIC COEFFICIENT',(M[0][0]-M[0][1]-M[1][0]+M[1][1])/1024)
