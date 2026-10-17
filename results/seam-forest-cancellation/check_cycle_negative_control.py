"""Exact SU(2) Haar polynomial negative control for a four-seam capped disk.
Q8 cubature is exact here: each independent quaternion appears at degree two,
and Q8 and Haar S^3 have identical first and second coordinate moments.
"""
from itertools import product
from fractions import Fraction
from pathlib import Path
import hashlib, runpy
source=Path(__file__).with_name('PROOF.md')
assert hashlib.sha256(source.read_bytes()).hexdigest()=='a1e96b1b33c396a4317ecf0f0e2c546b3c35df70e6c7c3df42344bb947eb8f0f'
runpy.run_path(str(Path(__file__).with_name('check_seam_forest_geometry.py')),run_name='__main__')
I=(1,0,0,0); minusI=(-1,0,0,0); qi=(0,1,0,0)
Q8=[tuple(sign*int(i==j) for i in range(4)) for j in range(4) for sign in (-1,1)]
def mul(a,b):
    w,x,y,z=a; v,p,q,r=b
    return (w*v-x*p-y*q-z*r,w*p+x*v+y*r-z*q,w*q-x*r+y*v+z*p,w*r+x*q-y*p+z*v)
def conj(a): return (a[0],-a[1],-a[2],-a[3])
def loop(xs):
    ans=I
    for x in xs: ans=mul(ans,x)
    return ans

def capped_disk(us):
    total=0
    for vs in product(Q8,repeat=4):
        integrand=loop(vs)[0]
        for u,v in zip(us,vs): integrand*=mul(u,conj(v))[0]
        total+=integrand
    return Fraction(total,8**4)
for us in ([I]*4,[minusI,I,I,I],[qi,I,I,I],[qi,qi,qi,qi]):
    result=capped_disk(us)
    expected=Fraction(loop(us)[0],256)
    assert result==expected,(us,result,expected)
    print('PASS exact SU(2) capped four-seam polynomial:',us,'integral =',result)
assert capped_disk([I]*4)!=capped_disk([minusI,I,I,I])
print('PASS negative control: a four-cycle can retain internal holonomy; forest condition cannot be dropped.')
