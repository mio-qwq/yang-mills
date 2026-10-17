import itertools,random,json
from pathlib import Path
from collections import defaultdict
P=1009; I=next(x for x in range(P) if x*x%P==P-1)
rng=random.Random(682341)
pairs=list(itertools.combinations(range(4),2))
H=[((0,1,2,3),1),((1,0,2,3),-1),((0,1,3,2),1),((1,0,3,2),-1)]
def parity(t):return [t.count(i)%2 for i in range(4)]==[1,1,0,0]
def canonpair(a,b):return ((a,b),1) if a<b else ((b,a),-1)
def project(t,kind):
 out=defaultdict(int)
 for perm,sg in H:
  z=[perm[x] for x in t]
  if kind=='j':
   a,b,c,d,e,f=z;(bc,s)=canonpair(b,c);(ef,v)=canonpair(e,f);z=(a,*bc,d,*ef);sg*=s*v
  else:
   a,b,c,d,e,f=z;(ab,s)=canonpair(a,b);(cd,u)=canonpair(c,d);(ef,v)=canonpair(e,f)
   if ef<cd:cd,ef=ef,cd
   z=(*ab,*cd,*ef);sg*=s*u*v
  out[z]+=sg
 return tuple(sorted((z,c) for z,c in out.items() if c))
Js=set();Ks=set()
for a in range(4):
 for bc in pairs:
  for d in range(4):
   for ef in pairs:
    z=(a,*bc,d,*ef)
    if parity(z):
     t=project(z,'j')
     if t:Js.add(t)
for ab in pairs:
 for cd in pairs:
  for ef in pairs:
   z=(*ab,*cd,*ef)
   if parity(z):
    t=project(z,'k')
    if t:Ks.add(t)
Js=sorted(Js);Ks=sorted(Ks)
def wave(on):
 if on:
  u,v=[rng.randrange(P) for _ in range(2)];meta={'s':u,'t':v};p=[1-u*u-v*v,I*(1+u*u+v*v),2*u,2*v];p=[x%P for x in p]
  a=[rng.randrange(P) for _ in range(4)];meta['polarization_seed']=a[:];j=next(j for j in range(4) if p[j]);meta['solve_index']=j;a[j]=-sum(p[k]*a[k] for k in range(4) if k!=j)*pow(p[j],-1,P)%P
 else:
  p=[rng.randrange(P) for _ in range(4)];a=[rng.randrange(P) for _ in range(4)];meta={'momentum':p[:],'polarization':a[:]}
 f={(b,c):(p[b]*a[c]-p[c]*a[b])%P for b,c in pairs}
 return p,f,meta
def determinant(a):
 a=[r[:] for r in a];det=1
 for j in range(len(a)):
  k=next((k for k in range(j,len(a)) if a[k][j]%P),None)
  if k is None:return 0
  if j!=k:a[k],a[j]=a[j],a[k];det=-det
  x=a[j][j]%P;det=det*x%P
  for k in range(j+1,len(a)):
   z=a[k][j]*pow(x,-1,P)%P
   for l in range(j,len(a)):a[k][l]=(a[k][l]-z*a[j][l])%P
 return det%P
def certificate(rows):
 basis={}; selected=[]
 for rowidx,row in enumerate(rows):
  row=[x%P for x in row]
  for j,b in sorted(basis.items()):
   v=row[j]
   if v:row=[(x-v*y)%P for x,y in zip(row,b)]
  nz=next((j for j,x in enumerate(row) if x),None)
  if nz is not None:
   v=pow(row[nz],-1,P);basis[nz]=[x*v%P for x in row];selected.append(rowidx)
 cols=sorted(basis)
 minor=[[rows[i][j]%P for j in cols] for i in selected]
 return {"rank":len(basis),"rows":selected,"columns":cols,"minor":minor,"determinant_mod_prime":determinant(minor)}
def rank(rows):return certificate(rows)["rank"]
for on in (False,True):
 jrows=[];drows=[];krows=[];samples=[]
 for _ in range(100):
  p,F,pm=wave(on);q,G,qm=wave(on);samples.append({"p_parameters":pm,"q_parameters":qm,"p":p,"q":q,"F":[F[x] for x in pairs],"G":[G[x] for x in pairs]});r=[(x+y)%P for x,y in zip(p,q)]
  vals=[]
  for t in Js:
   out=[0]*4
   for (a,b,c,d,e,f),coef in t:out[a]+=coef*(F[b,c]*q[d]*G[e,f]+G[b,c]*p[d]*F[e,f])
   vals.append([x%P for x in out])
  jrows.extend([[v[a] for v in vals] for a in range(4)]);drows.append([sum(r[a]*v[a] for a in range(4))%P for v in vals])
  kvals=[]
  for t in Ks:
   out=[0]*4
   for (a,b,c,d,e,f),coef in t:
    z=coef*(F[c,d]*G[e,f]+G[c,d]*F[e,f]);out[a]+=r[b]*z;out[b]-=r[a]*z
   kvals.append([x%P for x in out])
  krows.extend([[v[a] for v in kvals] for a in range(4)])
 Path(__file__).with_name('certificate_'+('on' if on else 'off')+'.json').write_text(json.dumps({'prime':P,'i':I,'current_candidates':Js,'curl_candidates':Ks,'samples':samples,'current':certificate(jrows),'divergence':certificate(drows),'curl':certificate(krows)},indent=2)+"\n")
 print({'on_shell':on,'projected_current_candidates':len(Js),'projected_K_candidates':len(Ks),'rank_currents':rank(jrows),'rank_divergences':rank(drows),'rank_curls':rank(krows),'prime':P,'sqrt_minus_one':I})

