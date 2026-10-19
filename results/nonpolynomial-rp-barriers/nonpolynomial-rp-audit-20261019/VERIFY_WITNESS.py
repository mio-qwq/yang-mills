import sympy as s

def require(condition, message):
    if not condition:
        raise RuntimeError(message)

L=s.symbols('L', positive=True)
x=[s.Matrix([L/s.Integer(2)+j*L,L/s.Integer(2)-j*L,0,0]) for j in range(3)]
n=s.Matrix([1,1,0,0])/s.sqrt(2)
R=s.eye(4)-2*n*n.T
h0,h1,h2,h3=s.symbols('h0 h1 h2 h3', positive=True)
h={0:h0,1:h1,2:h2,3:h3}
K=s.zeros(3)
for i in range(3):
  require(s.simplify(n.dot(x[i])-L/s.sqrt(2))==0, "VERIFY_WITNESS.py: exact check 1")
  for j in range(3):
    delta=x[i]-R*x[j]
    exponents=[s.simplify(abs(v)/L) for v in delta]
    K[i,j]=s.prod(h[int(v)] for v in exponents)
c=s.Matrix([1,-2,1])
Q=s.factor((c.T*K*c)[0])
require(s.expand(Q-2*h0**2*(3*h1**2-4*h0*h2+h1*h3))==0, "VERIFY_WITNESS.py: exact check 2")
z,r=s.symbols('z r', positive=True)
Qa=s.factor(Q.subs({h0:z,h1:z*r,h2:z*r**2,h3:z*r**3}))
require(s.expand(Qa-2*z**4*r**2*(r-1)*(r+1))==0, "VERIFY_WITNESS.py: exact check 3")
print('reflection=',R)
print('matrix=',K)
print('Q=',Q)
print('single_atom_Q=',Qa)
print('PASS: all positions, reflected differences, Gram entries, quadratic and atomic identities exact')
