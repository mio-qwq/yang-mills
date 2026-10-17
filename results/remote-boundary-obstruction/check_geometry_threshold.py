"""Independent arithmetic checks of theorem geometry/threshold, not an operator proof."""
from fractions import Fraction
for L in range(7):
    for n in range(max(8,6*L+5),max(8,6*L+5)+5):
        D=2*L+1; h=4*D; c=Fraction(1,2**(16*L+9)); M=6*n**4; r=Fraction(1,4*M)
        beta=c*r**(h+1)/48
        assert beta/r < Fraction(1,2)
        assert 24*beta/r**(h+1)==c/2
        for k in range(3*L+2,n-3*L-2):
            p=(n-1-L,k); q=(k,L)
            assert all(L<=x<=n-1-L for x in p+q)
            assert p[0]>p[1] and q[0]>q[1]
            assert (q[1]-p[0])%n==D and n-D>D
            sp=n-1-L-k; sq=k-L
            assert min(sp,n-sp,sq,n-sq)>=D+1
    print('PASS L=',L,'h=',8*L+4,'negative coefficient denominator exponent=',16*L+9)
assert Fraction(2,2**(8*3+2))==Fraction(1,2**25)
assert Fraction(2,2**(8*1+2))==Fraction(1,512)
print('PASS exact coefficients, geometry, threshold inequalities')
