import json,itertools
from collections import defaultdict
from pathlib import Path
base=Path(__file__).resolve().parent
P=1009
assert all(P%d for d in range(2,32))

def swap(t,perm,kind):
 z=[perm[i] for i in t];sgn=1
 slots=[(1,2),(4,5)] if kind=='current' else [(0,1),(2,3),(4,5)]
 for a,b in slots:
  if z[a]>z[b]:z[a],z[b]=z[b],z[a];sgn=-sgn
 if kind=='curl' and z[2:4]>z[4:6]:z[2:4],z[4:6]=z[4:6],z[2:4]
 return tuple(z),sgn
for name in ('off','on'):
 doc=json.loads((base/f'certificate_{name}.json').read_text())
 assert doc['prime']==P and doc['i']**2%P==P-1
 for kind in ('current','curl'):
  for candidate in doc[kind+'_candidates']:
   original=dict((tuple(t),c) for t,c in candidate)
   for t,c in original.items():
    assert [t.count(k)%2 for k in range(4)]==[1,1,0,0]
   for perm,sign in [((1,0,2,3),-1),((0,1,3,2),1)]:
    moved=defaultdict(int)
    for t,c in original.items():u,s=swap(t,perm,kind);moved[u]+=s*c
    moved={t:c for t,c in moved.items() if c}
    assert moved=={t:sign*c for t,c in original.items()}
 print(name, 'all candidate sign/parity and stabilizer equivariance verified')
