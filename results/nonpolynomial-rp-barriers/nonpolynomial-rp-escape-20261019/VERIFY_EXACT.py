"""Exact symbolic checks only; no floating point eigenvalue tests."""
import sympy as S

def require(condition, description):
    if not condition:
        raise RuntimeError("Exact verification failed: " + description)

u=S.symbols('u', real=True)
a,w,omega=S.symbols('a w omega', positive=True)
beta=S.symbols('beta', real=True)
D=a*((u+beta)**2+omega**2)
upper=-beta+S.I*omega
residue=S.simplify(w/S.diff(D,u).subs(u,upper))
require(residue == -S.I*w/(2*a*omega), 'residue == -S.I*w/(2*a*omega)')
print('Upper-pole residue:', residue)

# W4 orbit of A=diag(2,1,1,1), m=1, along the specified diagonal.
Ds=[S.Rational(3,2)*u**2+u+S.Rational(5,2),
    S.Rational(3,2)*u**2-u+S.Rational(5,2),u**2+2,u**2+2]
for shift,Dj in zip([-S.Rational(1,3),S.Rational(1,3)],Ds[:2]):
    z=shift+S.I*S.sqrt(14)/3
    require(S.simplify(Dj.subs(u,z)) == 0, 'S.simplify(Dj.subs(u,z)) == 0')
    require(S.simplify(1/S.diff(Dj,u).subs(u,z)) == -S.I/S.sqrt(14), 'S.simplify(1/S.diff(Dj,u).subs(u,z)) == -S.I/S.sqrt(14)')
print('Explicit orbit off-axis poles:', '-1/3+i sqrt(14)/3, +1/3+i sqrt(14)/3')
s,t,B,B0=S.symbols('s t B B0', positive=True)
v=S.Matrix([-s**2,1])
Mosc=2*B*S.Matrix([[-t**2,t**4],[t**4,-t**6]])
Mrad=B0*S.Matrix([[s**2,s**4],[s**4,s**6]])
require(S.simplify((v.T*Mrad*v)[0]) == 0, 'S.simplify((v.T*Mrad*v)[0]) == 0')
qosc=S.factor((v.T*Mosc*v)[0])
require(S.simplify(qosc+2*B*t**2*(s**2+t**2)**2) == 0, 'S.simplify(qosc+2*B*t**2*(s**2+t**2)**2) == 0')
print('Explicit orbit two-time negative form:',qosc)

# Exact reflected geometry for the universal separable witness.
L=S.symbols('L',positive=True)
points=[S.Matrix([L/2,L/2,0,0]),S.Matrix([3*L/2,-L/2,0,0]),S.Matrix([5*L/2,-3*L/2,0,0])]
def reflect(x): return S.Matrix([-x[1],-x[0],x[2],x[3]])
h=S.symbols('h0:4',positive=True)
M=S.zeros(3)
for i,x in enumerate(points):
    for j,y in enumerate(points):
        d=reflect(x)-y
        M[i,j]=S.prod(h[int(S.simplify(S.Abs(v)/L))] for v in d)
expected=h[0]**2*S.Matrix([[h[1]**2,h[0]*h[2],h[1]*h[3]],
                         [h[0]*h[2],h[1]**2,h[0]*h[2]],
                         [h[1]*h[3],h[0]*h[2],h[1]**2]])
require(M == expected, 'M == expected')
v=S.Matrix([1,-2,1])
q=S.expand((v.T*M*v)[0])
require(S.expand(q-h[0]**2*(6*h[1]**2-8*h[0]*h[2]+2*h[1]*h[3])) == 0, 'S.expand(q-h[0]**2*(6*h[1]**2-8*h[0]*h[2]+2*h[1]*h[3])) == 0')
print('Universal product witness:',S.factor(q))
c,z=S.symbols('c z',positive=True)
q_exp=S.factor(q.subs({h[i]:c*z**i for i in range(4)}))
require(q_exp==2*c**4*z**2*(z-1)*(z+1), 'q_exp==2*c**4*z**2*(z-1)*(z+1)')
print('Single exponential:',q_exp,'< 0 for 0 < z < 1')
print('All exact checks passed.')
