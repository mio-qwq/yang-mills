from fractions import Fraction as Q
from pathlib import Path
lam=[Q(1),Q(1,2),Q(1,3),Q(1,3)]
raw=[[Q(1,3),Q(1,5),Q(0),Q(1,9)],[Q(1,5),Q(-1,4),Q(1,7),Q(0)],[Q(0),Q(1,7),Q(1,6),Q(1,8)],[Q(1,9),Q(0),Q(1,8),Q(-1,5)]]
signs=[1,-1,1,-1]
cases=0
for n in range(8,45):
 z=sum(x**n for x in lam)
 mu=sum(raw[i][i]*lam[i]**n for i in range(4))/z
 b=[[raw[i][j]-(mu if i==j else 0) for j in range(4)] for i in range(4)]
 bx=[[signs[i]*b[i][j]*signs[j] for j in range(4)] for i in range(4)]
 assert sum(b[i][i]*lam[i]**n for i in range(4))==0
 def corr(a,c,s):return sum(a[i][j]*c[j][i]*lam[j]**s*lam[i]**(n-s) for i in range(4) for j in range(4))/z
 vals={s:corr(b,b,s) for s in range(1,n)}
 for s in vals:
  assert vals[s]==vals[n-s]>0
  assert abs(corr(b,bx,s))<=vals[s]
  assert corr(bx,bx,s)==vals[s]
 for s in range(1,n//2):assert vals[s]>vals[s+1]
 for L in range(7):
  if n<max(8,6*L+5):continue
  D=2*L+1
  for k in range(3*L+2,n-3*L-2):
   hp=n-1-L-k;hq=k-L
   assert min(hp,n-hp,hq,n-hq)>D
   assert vals[hp]+vals[hq]-2*vals[D]<0
   cases+=1
text=f'PASS: centered exact-rational spectral and translation controls for n=8,...,44.\nPASS: all spectral sums symmetric and strictly decreasing toward midpoint.\nPASS: translated autocorrelation identical and mixed correlation bounded by autocorrelation.\nPASS: strict negative geometric upper bound for {cases} admissible (L,n,k) combinations.\nThese finite-matrix controls test formulas, not the infinite-dimensional theorem.\n'
print(text);Path(__file__).with_name('CONTROL_RESULTS.txt').write_text(text)
