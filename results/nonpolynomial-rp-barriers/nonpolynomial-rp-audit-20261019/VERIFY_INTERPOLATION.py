import sympy as s

def require(condition, message):
    if not condition:
        raise RuntimeError(message)

# Nodes correspond to rates log(2) +/- i*pi/2 and log(3), with r=t0=1.
z=s.symbols('z')
nodes=[-s.I/2,s.I/2,s.Rational(1,3)]
weights=[s.Integer(1),s.Integer(1),s.Integer(5)]
P=(72*z**2-8)/13
require(all(s.simplify(P.subs(z,n)-v)==0 for n,v in zip(nodes,[-2,-2,0])), "VERIFY_INTERPOLATION.py: exact check 1")
# exp(-t0*lambda_j)*P(exp(-r*lambda_j)) must be i,-i,0.
values=[s.simplify(n*P.subs(z,n)) for n in nodes]
require(values==[s.I,-s.I,0], "VERIFY_INTERPOLATION.py: exact check 2")
q=s.Matrix([-s.Rational(8,13),0,s.Rational(72,13)])
times=[1,2,3]
K=s.Matrix([[s.simplify(sum(B*n**(a+b) for n,B in zip(nodes,weights))) for b in times] for a in times])
Q=s.simplify((q.T*K*q)[0])
require(Q==-2, "VERIFY_INTERPOLATION.py: exact check 3")
print('P=',P)
print('Laplace values=',values)
print('Hankel matrix=',K)
print('coefficients=',list(q))
print('Q=',Q)
print('PASS: exact real interpolation polynomial isolates conjugate rates with Q=-2')
