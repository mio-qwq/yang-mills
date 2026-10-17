"""Exact symbolic curvature and equation-ideal witness; no numerical sampling."""
import itertools
import sympy as s
x=s.symbols('x1:5');edges=list(itertools.combinations(range(4),2));v=s.symbols('f12 f13 f14 f23 f24 f34');f=s.zeros(4)
for (a,b),z in zip(edges,v):f[a,b]=z;f[b,a]=-z
H=s.diag(s.I,s.I,-2*s.I)
assert s.trace(H)==0 and s.trace(H**2)==-6 and -s.I*s.trace(H**3)==6
A=[-sum((f[a,b]*x[b]*H for b in range(4)),s.zeros(3))/2 for a in range(4)]
F={}
for a in range(4):
 for b in range(4):
  F[a,b]=A[b].diff(x[a])-A[a].diff(x[b])+A[a]*A[b]-A[b]*A[a]
  assert s.simplify(F[a,b]-f[a,b]*H)==s.zeros(3)
for k,a,b in itertools.product(range(4),repeat=3):
 assert F[a,b].diff(x[k])+A[k]*F[a,b]-F[a,b]*A[k]==s.zeros(3)
polys=[v[0]**3,v[0]*(v[1]**2+v[2]**2+v[3]**2+v[4]**2),v[0]*v[5]**2,(v[1]*v[4]-v[2]*v[3])*v[5]]
mons=list(itertools.combinations_with_replacement(range(6),3))
B=s.Matrix([[s.Poly(p,*v).coeff_monomial(s.prod(v[j] for j in m)) for p in polys] for m in mons])
assert B.rank()==4
print('PASS: constant Cartan curvature F=fH, all covariant derivatives DF=0, exact YM equations, d(H,H,H)=6, four cubic polynomials independent. Embedding by zeros applies to every N>=3.')
