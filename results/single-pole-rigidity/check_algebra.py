"""Exact algebra checks for the single-pole rigidity proof.
Not a formal verification of distribution theory or Yang--Mills.
"""
import sympy as S
x, M, d = S.symbols('x M d', positive=True)
s6_negative = -(x+M)**3 + x**3/4
s6_positive = x**3 - (x+M)**3/4
s4_positive = (x+M)**2+x**2
s4_negative = (x**2-6*x*(x+M)+(x+M)**2)/2
assert S.Poly(s6_negative,x).LC() == -S.Rational(3,4)
assert S.Poly(s6_positive,x).LC() == S.Rational(3,4)
assert S.Poly(s4_positive,x).LC() == 2
assert S.Poly(s4_negative,x).LC() == -2
h_on_shell = S.expand(s4_positive-3*M**2/(d+2))
assert S.Poly(h_on_shell**2,x).LC() == 4
# Verify the general invariant basis reduction, using formal power sums.
s1,s2,s3=S.symbols('s1 s2 s3')
a=S.symbols('a0:7')
p=a[0]+a[1]*s1+a[2]*s1**2+a[3]*s2+a[4]*s1**3+a[5]*s1*s2+a[6]*s3
A=a[0]-M*a[1]+M**2*a[2]-M**3*a[4]
B=a[3]-M*a[5]
C=a[6]
assert S.expand(p.subs(s1,-M)-(A+B*s2+C*s3)) == 0
# Verify h_d is harmonic in d=3,4,5 as finite exact sanity checks.
for dim in (3,4,5):
    p=S.symbols('p:'+str(dim)); r2=sum(t*t for t in p)
    h=sum(t**4 for t in p)-S.Rational(3,dim+2)*r2**2
    assert S.expand(sum(S.diff(h,t,2) for t in p)) == 0
print('PASS: invariant reduction and four residue sign coefficients')
print('PASS: degree-eight square has nonconstant mass-shell residue, leading coefficient 4')
print('PASS: h_d harmonic in dimensions 3, 4, 5 (sanity checks; theorem has general proof)')

# Negative controls: either sign of a forbidden leading coefficient gives a negative residue.
assert s6_negative.subs({x:100,M:1}) < 0
assert -s6_positive.subs({x:100,M:1}) < 0
assert s4_negative.subs({x:100,M:1}) < 0
assert -s4_positive.subs({x:100,M:1}) < 0
print("PASS: four forbidden-coefficient negative controls")
