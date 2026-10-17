import itertools
from fractions import Fraction as Q

def compose(g,h):
 p,s=g;q,t=h
 return tuple(p[q[i]] for i in range(4)),tuple(t[i]*s[q[i]] for i in range(4))
def tr(g):
 p,s=g;return sum(s[i] for i in range(4) if p[i]==i)
def chars(g):
 g2=compose(g,g);g3=compose(g2,g);g4=compose(g3,g)
 v=tr(g);v2=tr(g2);v3=tr(g3);v4=tr(g4)
 l2=(v*v-v2)//2;l3=(v**3-3*v*v2+2*v3)//6;l4=(v**4-6*v*v*v2+3*v2*v2+8*v*v3-6*v4)//24
 s2=(v*v+v2)//2;j1=v*l2-l3;j2=s2*l2-v*l3+l4
 return v,l2,l3,l4,s2,j1,j2
sums={}
for p in itertools.permutations(range(4)):
 for s in itertools.product([-1,1],repeat=4):
  g=p,s;g2=compose(g,g);g3=compose(g2,g)
  v,l,l3,l4,sym,j1,j2=chars(g);_,l_2,_,_,_,j1_2,_=chars(g2);_,l_3,*_=chars(g3)
  v4=(l*l+l_2)//2;v5=l*j1;v6=l*j2+(j1*j1+j1_2)//2+(l**3-3*l*l_2+2*l_3)//6
  j1on=j1-v;j1on2=j1_2-tr(g2);j2on=j2-v*v+1
  v5on=l*j1on;v6on=l*j2on+(j1on*j1on+j1on2)//2+(l**3-3*l*l_2+2*l_3)//6
  vals={'Cubic':(l**3-3*l*l_2+2*l_3)//6,'V6':v6,'VxV5':v*v5,'L2xV4':l*v4,'V6on':v6on,'VxV5on':v*v5on}
  for a,c in [('scalar',1),('antisym',l),('symtensor',sym)]:
   for name,d in vals.items():sums[a,name]=sums.get((a,name),0)+c*d
print({k:Q(n,384) for k,n in sums.items()})
print('identity chars',chars((tuple(range(4)),(1,1,1,1))))
