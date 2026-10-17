from itertools import permutations,product
from fractions import Fraction as Q
from collections import Counter

def compose(g,h):
 p,s=g;q,t=h
 return tuple(p[q[i]] for i in range(4)),tuple(t[i]*s[q[i]] for i in range(4))
def tr(g):return sum(g[1][i] for i in range(4) if g[0][i]==i)
def powers(g):
 a=(tuple(range(4)),(1,)*4);out=[]
 for k in range(1,13):a=compose(g,a);out.append(tr(a))
 return out
def sym(p,n):
 h=[Q(1)]
 for k in range(1,n+1):h.append(sum(p[j-1]*h[k-j] for j in range(1,k+1))/k)
 return h[n]
def vals(g):
 p=powers(g);v=p[0];s2=sym(p,2);j0=v*v-s2;j1=v*s2-sym(p,3);j2=v*sym(p,3)-sym(p,4)
 return Q(v),Q(j0),Q(j1),Q(j2)
out=Counter()
for p in permutations(range(4)):
 for s in product((-1,1),repeat=4):
  g=(p,s);g2=compose(g,g);g3=compose(g2,g)
  v,a,b,c=vals(g);v2,a2,b2,c2=vals(g2);v3,a3,b3,c3=vals(g3)
  V4=(a*a+a2)/2;V5=a*b;cube=(a**3-3*a*a2+2*a3)/6
  V6=a*c+(b*b+b2)/2+cube
  bon=b-v;bon2=b2-v2;con=c-v*v+1
  Von6=a*con+(bon*bon+bon2)/2+cube
  for name,value in [('A6',a*V6),('current5',a*v*V5),('curl4',a*a*V4),('A6_on',a*Von6),('current5_on',a*v*a*bon),('scalar6',V6),('sym6',(v*v+v2)/2*V6),('cubicA',a*cube)]:out[name]+=value
assert all((x/384).denominator==1 for x in out.values())
result={k:int(v/384) for k,v in out.items()}
assert result=={'A6':11,'current5':16,'curl4':7,'A6_on':6,'current5_on':12,'scalar6':6,'sym6':37,'cubicA':0},result
print(result)
