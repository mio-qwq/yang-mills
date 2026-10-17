"""Independent full-group character and stabilizer linear-system check."""
import itertools as it
import sympy as s
from fractions import Fraction
E=list(it.combinations(range(4),2)); ei={e:i for i,e in enumerate(E)}
M=list(it.combinations_with_replacement(range(6),3)); mi={m:i for i,m in enumerate(M)}
def edge_action(p,sign):
 out=[]
 for a,b in E:
  x,y=p[a],p[b]; out.append((ei[tuple(sorted((x,y)))],sign[a]*sign[b]*(1 if x<y else -1)))
 return out
def tracepower(act,n):
 ans=0
 for a in range(6):
  b=a; z=1
  for _ in range(n):b,w=act[b];z*=w
  if b==a:ans+=z
 return ans
total=Fraction(0); count=0
for p in it.permutations(range(4)):
 for sig in it.product((-1,1),repeat=4):
  a=edge_action(p,sig); t1,t2,t3=[tracepower(a,j) for j in (1,2,3)]
  total+=t1*Fraction(t1**3+3*t1*t2+2*t3,6); count+=1
assert count==384 and total/count==4
# Solve full 56-dimensional component equations, with all sign flips and both stabilizer swaps.
gens=[]
for k in range(4):
 sig=[1]*4;sig[k]=-1;gens.append((tuple(range(4)),sig,-1 if k<2 else 1))
gens += [((1,0,2,3),(1,)*4,-1),((0,1,3,2),(1,)*4,1)]
blocks=[]
for p,sig,target in gens:
 a=edge_action(p,sig); T=s.zeros(56)
 for j,m in enumerate(M):
  images=[a[e] for e in m]; out=tuple(sorted(v[0] for v in images));z=1
  for _,q in images:z*=q
  T[mi[out],j]=z
 blocks.append(T-target*s.eye(56))
C=s.Matrix.vstack(*blocks); assert C.rank()==52
# Explicit proposed four polynomials, built independently by their index pairs.
def vec(terms):
 v=s.zeros(56,1)
 for coefficient,edges in terms:
  key=tuple(sorted(ei[e] for e in edges));v[mi[key]]+=coefficient
 return v
B=s.Matrix.hstack(vec([(1,[(0,1)]*3)]),vec([(1,[(0,1),e,e]) for e in [(0,2),(0,3),(1,2),(1,3)]]),vec([(1,[(0,1),(2,3),(2,3)])]),vec([(1,[(0,2),(1,3),(2,3)]),(-1,[(0,3),(1,2),(2,3)])]))
assert C*B==s.zeros(C.rows,4) and B.rank()==4
bad=B.copy();bad[mi[tuple(sorted([ei[(0,3)],ei[(1,2)],ei[(2,3)]]))],3]=1
assert C*bad!=s.zeros(C.rows,4)
# H=diag(i,i,-2i,0,...) has trace H=0, trace H^3=6i and trace H^2=-6.
assert sum([1,1,-2])==0 and sum(v**3 for v in [1,1,-2])==-6
print('PASS: 384-group character multiplicity=4; 56-column stabilizer kernel=4; proposed basis rank=4; wrong-sign negative test rejected; Cartan cubic nonzero.')
