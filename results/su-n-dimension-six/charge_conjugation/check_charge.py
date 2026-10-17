"""Exact noncommuting matrix tests for the charge-conjugation identities."""
import sympy as s
I=s.I
X=s.Matrix([[I,1+I,2],[-1+I,2*I,I],[-2,I,-3*I]])
Y=s.Matrix([[0,2-I,I],[-2-I,I,3], [I,-3,-I]])
Z=s.Matrix([[2*I,I,1],[I,-I,2-I],[-1,-2-I,-I]])
def C(a):return -a.T
def bracket(a,b):return a*b-b*a
def pair(a,b):return s.expand(s.trace(a*b))
def f(a,b,c):return s.expand(s.trace(a*bracket(b,c)))
def d(a,b,c):return s.expand(-I*s.trace(a*(b*c+c*b)))
for a in (X,Y,Z):assert a.conjugate().T==-a and s.trace(a)==0 and C(C(a))==a
assert (C(bracket(X,Y))-bracket(C(X),C(Y))).applyfunc(s.expand)==s.zeros(3)
assert pair(C(X),C(Y))==pair(X,Y)
assert f(C(X),C(Y),C(Z))==f(X,Y,Z)
assert d(C(X),C(Y),C(Z))==-d(X,Y,Z)
assert f(X,Y,Z)!=0 and d(X,Y,Z)!=0
# A nonreal SU(3) plaquette trace; conjugation preserves its real part.
U=s.diag(I,I,-1);assert s.det(U)==1 and U.conjugate().T*U==s.eye(3)
assert s.re(s.trace(U.conjugate()))==s.re(s.trace(U))
assert s.im(s.trace(U))!=0
print('PASS: involution, Lie bracket, pairing even, f even, d odd, nonzero witnesses, Wilson real trace invariant.')
print('witness f,d=',f(X,Y,Z),d(X,Y,Z))
