"""Exact normalized SU(2) cube-face product via degree-two Q8 cubature."""
from itertools import product,combinations
from fractions import Fraction
I=(1,0,0,0)
Q=[tuple(s if i==j else 0 for i in range(4)) for j in range(4) for s in (-1,1)]
def mul(a,b):
 w,x,y,z=a; W,X,Y,Z=b
 return(w*W-x*X-y*Y-z*Z,w*X+x*W+y*Z-z*Y,w*Y-x*Z+y*W+z*X,w*Z+x*Y-y*X+z*W)
def inv(a):return(a[0],-a[1],-a[2],-a[3])
verts=list(product((0,1),repeat=3)); edges=[]
for x in verts:
 for j in range(3):
  if x[j]==0:
   y=list(x);y[j]=1;edges.append((x,tuple(y)))
faces=[]
for j,k in combinations(range(3),2):
 other=next(i for i in range(3) if i not in (j,k))
 for v in (0,1):
  a=[0]*3;a[other]=v;b=a.copy();b[j]=1;c=b.copy();c[k]=1;d=a.copy();d[k]=1
  vs=list(map(tuple,[a,b,c,d,a])); faces.append(list(zip(vs,vs[1:])))
parent={x:x for x in verts}
def root(x):
 while parent[x]!=x:x=parent[x]
 return x
tree=[];free=[]
for e in edges:
 a,b=map(root,e)
 if a!=b: parent[a]=b;tree.append(e)
 else:free.append(e)
assert len(tree)==7 and len(free)==5
# Gauge fixing a spanning tree leaves independent Haar on five residual edges.
# Each occurs in exactly two faces, so integrand has degree <=2 in each SU2 quaternion.
assert all(sum(e in f or (e[1],e[0]) in f for f in faces)==2 for e in free)
# Q8's first and second coordinate moments exactly match normalized Haar on S3.
assert all(sum(q[i] for q in Q)==0 for i in range(4))
assert all(Fraction(sum(q[i]*q[j] for q in Q),8)==(Fraction(1,4) if i==j else 0) for i in range(4) for j in range(4))
s=0
for qs in product(Q,repeat=5):
 values={e:I for e in tree};values.update(zip(free,qs));p=1
 for face in faces:
  h=I
  for a,b in face: h=mul(h, values[(a,b)] if (a,b) in values else inv(values[(b,a)]))
  p*=h[0]
 s+=p
result=Fraction(s,8**5)
assert result==Fraction(1,1024)
print('SU2 normalized cube-face Haar product:',result,'samples',8**5)
