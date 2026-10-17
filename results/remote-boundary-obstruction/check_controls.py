from fractions import Fraction as Q
from itertools import product
from pathlib import Path
cases=0
for L in range(13):
 for n in range(max(8,6*L+5),max(8,6*L+5)+9):
  D=2*L+1;h=4*D;c=Q(1,2**(16*L+9));M=6*n**4;r=Q(1,4*M);bs=c*r**(h+1)/48
  assert 2*Q(1,4)*Q(1,256)**D==c
  assert n-D>=4*L+4>D
  assert bs/r<Q(1,2)
  assert 24*bs/r**(h+1)==c/2
  assert 12*bs/(r**(h+1)*(1-bs/r))<c/2
  ks=range(3*L+2,n-3*L-2)
  assert len(ks)>0
  for k in ks:
   p=(n-1-L,k);q=(k,L);tp=p[::-1];tq=q[::-1]
   assert p[0]>p[1] and q[0]>q[1]
   assert all(L<=x<=n-1-L for x in p+q)
   assert min(*(x for x in p+q),*(n-1-x for x in p+q))==L
   assert tp[0]==q[0] and tq[1]==p[1]
   def dist(x,y):return min((x-y)%n,(y-x)%n)
   assert dist(tp[1],q[1])==D and dist(tq[0],p[0])==D
   sp=n-1-L-k;sq=k-L
   assert sp>=D+1 and sq>=D+1 and n-sp>=4*L+3 and n-sq>=4*L+3
   assert min(sp,n-sp,sq,n-sq)>=D+1
   cases+=1

def loops4(n):
 origin=(0,0,0);steps=[tuple(s if i==d else 0 for i in range(3)) for d in range(3) for s in (-1,1)]
 cycles=set()
 for ss in product(steps,repeat=4):
  vs=[origin]
  for st in ss:vs.append(tuple((x+y)%n for x,y in zip(vs[-1],st)))
  if vs[-1]!=origin or len(set(vs[:-1]))!=4:continue
  edges=frozenset(tuple(sorted((a,b))) for a,b in zip(vs,vs[1:]));cycles.add(edges)
 elementary=set()
 for a in range(3):
  for b in range(a+1,3):
   for sa,sb in product((-1,1),repeat=2):
    va=tuple((sa if d==a else 0)%n for d in range(3));vb=tuple((sb if d==b else 0)%n for d in range(3));vab=tuple((x+y)%n for x,y in zip(va,vb))
    vs=[origin,va,vab,vb,origin];elementary.add(frozenset(tuple(sorted((x,y))) for x,y in zip(vs,vs[1:])))
 assert cycles==elementary and len(cycles)==12
 return len(cycles)
lines=[f'PASS: {cases} admissible (L,n,k) geometries for 0<=L<=12, first nine admissible n.', 'PASS: exact rational coefficients and beta-star bounds for all tested (L,n).',f'PASS: n=8 has {loops4(8)} four-cycles through origin, all elementary.',f'PASS: n=11 has {loops4(11)} four-cycles through origin, all elementary.']
L=0;n=8;D=1;h=4;c=Q(1,512);r=Q(1,24*n**4);bs=c*r**5/48
lines+=['Endpoint L=0,n=8: k=2,3,4,5; D=1; h=4; c=1/512.',f'Endpoint exact r={r}; beta_star={bs}.', 'PASS: strict Cauchy remainder < (c/2) beta_star^h at the endpoint.']
text='\n'.join(lines)+'\n';print(text);Path(__file__).with_name('CONTROL_RESULTS.txt').write_text(text)
