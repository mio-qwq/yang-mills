from itertools import product,combinations
from collections import Counter
D=4
zero=(0,)*D
def add(v,i,k=1):
 u=list(v);u[i]+=k;return tuple(u)
def edges(p):
 x,i,j=p
 return frozenset([(x,i),(x,j),(add(x,i),j),(add(x,j),i)])
def incident(e):
 x,i=e
 return {(y,min(i,j),max(i,j)) for j in range(D) if j!=i for y in (x,add(x,j,-1))}
root=(zero,0,1)
E=edges(root)
choices=[incident(e)-{root} for e in sorted(E)]
cores=set();five=0
for ns in product(*choices):
 S=frozenset([root,*ns])
 assert len(S)==5
 counts=Counter(e for p in S for e in edges(p))
 boundary={e for e,k in counts.items() if k==1}
 if not boundary:
  five+=1;cores.add(S);continue
 candidates=set.intersection(*(incident(e) for e in boundary))-set(S)
 for q in candidates:
  T=S|{q}; c=Counter(e for p in T for e in edges(p))
  if min(c.values())>=2: cores.add(T)
expected=set()
# cubes containing root, in either side of any perpendicular axis
for k in range(D):
 if k in (0,1):continue
 for shift in (0,-1):
  base=add(zero,k,shift)
  C=set()
  for i,j in combinations((0,1,k),2):
   rem=next(a for a in (0,1,k) if a not in (i,j))
   for side in (0,1):C.add((add(base,rem,side),min(i,j),max(i,j)))
  expected.add(frozenset(C))
assert cores==expected,(cores,expected)
print('Dimension',D,'root-neighbor choices',5**4,'five-face cores',five,'six-face cores',len(cores))
print('Every <=6-face non-peelable connected plaquette set containing root is an elementary cube boundary.')
