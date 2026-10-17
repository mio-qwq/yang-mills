"""Exact rational-quaternion geometry/attainability and separation check."""
from itertools import product
from fractions import Fraction as Q

I=(Q(1),Q(0),Q(0),Q(0)); J=(Q(0),Q(1),Q(0),Q(0))
def mul(a,b):
 a0,x,y,z=a;b0,u,v,w=b
 return (a0*b0-x*u-y*v-z*w,a0*u+x*b0+y*w-z*v,a0*v-x*w+y*b0+z*u,a0*w+x*v-y*u+z*b0)
def inv(a):return (a[0],-a[1],-a[2],-a[3])
def norm2(a):return sum(x*x for x in a)
def stereo(t):
 z=sum(x*x for x in t);return ((1-z)/(1+z),*(2*x/(1+z) for x in t))
def prod(xs):
 out=I
 for x in xs:out=mul(out,x)
 return out

def check(n):
 def shift(x,k):
  y=list(x);y[k]=(y[k]+1)%n;return tuple(y)
 e=((0,0,0,0),0);paths=[]
 for x in product(range(n),repeat=4):
  for mu in range(4):
   for nu in range(mu+1,4):
    p=[((x,mu),1),((shift(x,mu),nu),1),((shift(x,nu),mu),-1),((x,nu),-1)]
    if not any(f==e for f,s in p):continue
    if next(s for f,s in p if f==e)<0:p=[(f,-s) for f,s in p[::-1]]
    k=next(k for k,(f,s) in enumerate(p) if f==e)
    p=p[k:]+p[:k];assert p[0]==(e,1)
    paths.append(p[1:])
 neighbors=sorted({f for p in paths for f,s in p});assert len(neighbors)==18
 U={f:stereo((Q((k%3)+1,1000),Q((k%5)-2,1000),Q((k%7)-3,1000))) for k,f in enumerate(neighbors)}
 def val(f,s,assign):return assign[f] if s>0 else inv(assign[f])
 def solve(path,f,w,assign):
  j=next(j for j,(g,s) in enumerate(path) if g==f);sign=path[j][1]
  left=prod(val(g,s,assign) for g,s in path[:j]);right=prod(val(g,s,assign) for g,s in path[j+1:])
  answer=mul(mul(inv(left),w),inv(right))
  return answer if sign>0 else inv(answer)
 small=[stereo((Q(1,1000),Q(2,1000),Q(0))),stereo((Q(0),Q(1,1000),Q(3,1000))),stereo((Q(2,1000),Q(0),Q(1,1000)))]
 desired=[v for q in small for v in (q,inv(q))]
 for path,w in zip(paths,desired):
  parallel=next(f for f,s in path if f[1]==0)
  U[parallel]=solve(path,parallel,w,U)
 def staples(assign):return [prod(val(f,s,assign) for f,s in p) for p in paths]
 V=staples(U);assert V==desired
 S=tuple(sum(q[k] for q in V) for k in range(4));a=S[0]
 assert S[1:]==(0,0,0) and a>=Q(1199,200)
 assert all(norm2(q)==1 for q in U.values())
 assert any(mul(U[neighbors[0]],U[f])!=mul(U[f],U[neighbors[0]]) for f in neighbors[1:])
 for f in neighbors:
  i=next(i for i,p in enumerate(paths) if any(g==f for g,s in p))
  U2=dict(U);U2[f]=solve(paths[i],f,J,U)
  assert norm2(U2[f])==1
  V2=staples(U2);assert V2[i]==J
  assert all(V2[j]==V[j] for j in range(6) if j!=i)
  S2=tuple(sum(q[k] for q in V2) for k in range(4));a2=norm2(S2)
  alpha=S2[0];perp2=sum(x*x for x in S2[1:])
  assert a2>9 and 0<alpha<=Q(51,10) and perp2>=Q(81,100)
  # 2-2 alpha/sqrt(a2)>1/36, checked without square roots.
  assert 5184*alpha*alpha<5041*a2
 print(f'PASS n={n}: all 18 noncommuting replacements and center-separation inequalities, exact Fraction arithmetic.')

if __name__=='__main__':
 for n in (4,5):check(n)
