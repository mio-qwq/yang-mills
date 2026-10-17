"""Independent geometry checker, written for this audit; standard library only."""
from itertools import product, combinations

def add(x,a,n):
 y=list(x); y[a]=(y[a]+1)%n; return tuple(y)
def verts(x,axes,n):
 return {tuple((x[i]+sum(b for a,b in zip(axes,bits) if a==i))%n for i in range(4)) for bits in product((0,1),repeat=len(axes))}
def face(x,axes):return (x,tuple(sorted(axes)))
def theta(p):
 x,axes=p; return ((x[1],x[0],x[2],x[3]),tuple(sorted(1-a if a<2 else a for a in axes)))
def run(n):
 forbidden=0; seam_pairs=0
 for x in product(range(n),repeat=4):
  for axes in combinations(range(4),3):
   fs=[]
   for a in axes:
    other=tuple(b for b in axes if b!=a)
    fs.extend((face(x,other),face(add(x,a,n),other)))
   pos=[p for p in fs if all(v[0]>v[1] for v in verts(p[0],p[1],n))]
   neg=[p for p in fs if all(v[0]<v[1] for v in verts(p[0],p[1],n))]
   wrap=any(a<2 and x[a]==n-1 for a in axes)
   if pos and neg:
    if wrap:seam_pairs+=len(pos)*len(neg)
    else:forbidden+=len(pos)*len(neg)
 assert forbidden==0,(n,forbidden)
 print('n=',n,'nonseam cubes containing strict +/- faces:',forbidden,'seam +/- pairs:',seam_pairs)
 # The original four pairs, computed without relying on prior code.
 p=face((n-1,2,0,0),(2,3));q=face((2,0,0,0),(2,3))
 def together(a,b):
  return sum(a in fs and b in fs for fs in cubes)
 cubes=[]
 for x in product(range(n),repeat=4):
  for axes in combinations(range(4),3):
   fs=set()
   for a in axes:
    other=tuple(b for b in axes if b!=a)
    fs|={face(x,other),face(add(x,a,n),other)}
   cubes.append(fs)
 counts=[together(theta(a),b) for a,b in ((p,p),(p,q),(q,p),(q,q))]
 assert counts==[0,1,1,0],counts
 print('original reflected cube matrix:',counts)
if __name__=='__main__':
 for n in (8,9):run(n)
