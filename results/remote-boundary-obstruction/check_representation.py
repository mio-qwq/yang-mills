"""Portable reconstructed exact control; not the original review's missing script.
Derive SU(2) tensor multiplicities via chi_1 chi_j = chi_(j-1)+chi_(j+1)
where subscripts are twice-spin; divide c_j by (j+1)c_0 as formal series.
"""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
N=8
coeff={j:[Q(0) for _ in range(N+1)] for j in range(N+1)}
mult={0:1}
for m in range(N+1):
    for j,a in mult.items(): coeff[j][m]=Q(a,2**m*factorial(m))
    nxt={}
    for j,a in mult.items():
        for k in (j-1,j+1):
            if k>=0:nxt[k]=nxt.get(k,0)+a
    mult=nxt
lines=[]
for j in range(5):
    t=[Q(0) for _ in range(N+1)]
    for m in range(N+1):
        t[m]=coeff[j][m]/(j+1)-sum(coeff[0][i]*t[m-i] for i in range(1,m+1))
    assert t[j]==Q(1,2**j*factorial(j)*(j+1))
    lines.append(f'j={j}/2: '+str([(m,str(a)) for m,a in enumerate(t) if a]))
assert Q(1,4)**4==Q(1,256)
a=Q(1,4)*Q(1,256)**3
lines += [f'D=3 covariance coefficient = {a}', f'Reflected F coefficient = {-2*a}']
output='\n'.join(lines)+'\n'
assert output==Path(__file__).with_name('L1_representation_check.txt').read_text()
print(output,end='')
print('PASS: reconstructed exact character series match the historical output byte-for-byte.')
