"""Independent reconstruction, modular determinants, and corruption tests."""
import json,itertools,copy
from pathlib import Path
PAIRS=list(itertools.combinations(range(4),2))
def wave(m,p,i):
 if 's' in m:
  s,t=m['s'],m['t'];k=[1-s*s-t*t,i*(1+s*s+t*t),2*s,2*t];u=m['polarization_seed'][:];j=m['solve_index'];u[j]=-sum(k[h]*u[h] for h in range(4) if h!=j)*pow(k[j],-1,p)%p
  assert sum(x*x for x in k)%p==0
  assert sum(x*y for x,y in zip(k,u))%p==0
 else:k=m['momentum'];u=m['polarization']
 return [x%p for x in k],[(k[a]*u[b]-k[b]*u[a])%p for a,b in PAIRS]
def det(M,p):
 # Bareiss integer elimination, followed by residue, independently of modular row rank.
 M=copy.deepcopy(M);den=1;sgn=1;n=len(M)
 for k in range(n-1):
  if M[k][k]==0:
   r=next(r for r in range(k+1,n) if M[r][k]);M[r],M[k]=M[k],M[r];sgn=-sgn
  pivot=M[k][k]
  for r in range(k+1,n):
   for c in range(k+1,n):
    z=M[r][c]*pivot-M[r][k]*M[k][c];assert z%den==0;M[r][c]=z//den
  for r in range(k+1,n):M[r][k]=0
  den=pivot
 return sgn*M[-1][-1]%p

def matrices(d):
 p=d['prime'];js=d['current_candidates'];ks=d['curl_candidates'];J=[];D=[];K=[]
 for s in d['samples']:
  momentum,F=wave(s['p_parameters'],p,d['i']);q,G=wave(s['q_parameters'],p,d['i'])
  assert momentum==s['p'] and q==s['q'] and F==s['F'] and G==s['G']
  f=dict(zip(PAIRS,F));g=dict(zip(PAIRS,G));r=[(a+b)%p for a,b in zip(momentum,q)]
  jj=[[0 for _ in js] for _ in range(4)]
  for col,candidate in enumerate(js):
   for (a,b,c,h,e,v),coefficient in candidate:
    jj[a][col]+=coefficient*(f[b,c]*q[h]*g[e,v]+g[b,c]*momentum[h]*f[e,v])
  kk=[[0 for _ in ks] for _ in range(4)]
  for col,candidate in enumerate(ks):
   for (a,b,c,h,e,v),coefficient in candidate:
    value=coefficient*(f[c,h]*g[e,v]+g[c,h]*f[e,v]);kk[a][col]+=r[b]*value;kk[b][col]-=r[a]*value
  # Exact modular negative/control identity: every constructed curl has zero divergence.
  assert all(sum(r[a]*kk[a][col] for a in range(4))%p==0 for col in range(len(ks)))
  J.extend([[x%p for x in row] for row in jj]);K.extend([[x%p for x in row] for row in kk]);D.append([sum(r[a]*jj[a][col] for a in range(4))%p for col in range(len(js))])
 return {'current':J,'divergence':D,'curl':K}
def check(d):
 mats=matrices(d);out={}
 for name,M in mats.items():
  cert=d[name];minor=[[M[r][c] for c in cert['columns']] for r in cert['rows']]
  assert minor==cert['minor'],name+' minor does not match independently reconstructed entries'
  z=det(minor,d['prime']);assert z and z==cert['determinant_mod_prime'];out[name]=z
 return out
for fn in sorted(Path(__file__).parent.glob('certificate_*.json')):
 d=json.loads(fn.read_text());print(fn.name,check(d))
 bad=copy.deepcopy(d);bad['divergence']['minor'][0][0]=(bad['divergence']['minor'][0][0]+1)%d['prime']
 try:check(bad)
 except AssertionError:pass
 else:raise AssertionError('Corrupted matrix was accepted')
 bad=copy.deepcopy(d);bad['divergence']['determinant_mod_prime']=0
 try:check(bad)
 except AssertionError:pass
 else:raise AssertionError('Zero determinant was accepted')
 print('  Reconstruction, curl identity, and two corruption tests passed.')
