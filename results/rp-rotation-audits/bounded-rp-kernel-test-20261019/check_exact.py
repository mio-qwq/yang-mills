"""Exact finite certificates accompanying RESULT.md; standard library only."""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import json

D=4
normals=[]
for i in range(D):
    n=[0]*D; n[i]=1; normals.append(n)
for i,j in combinations(range(D),2):
    for sign in [-1,1]:
        n=[0]*D; n[i]=1; n[j]=sign; normals.append(n)
def reflection(n):
    norm=sum(a*a for a in n)
    return [[Q(int(i==j))-Q(2*n[i]*n[j],norm) for j in range(D)] for i in range(D)]
def mv(M,x): return [sum(a*b for a,b in zip(row,x)) for row in M]
def discriminant(x):
    v=Q(1)
    for a in x: v*=a
    for i,j in combinations(range(D),2): v*=x[i]*x[i]-x[j]*x[j]
    return v
samples=[[Q(i+1) for i in range(D)], [Q(2),Q(-3),Q(5),Q(7)], [Q(1,2),Q(2,3),Q(3,4),Q(4,5)]]
for n in normals:
    R=reflection(n)
    for x in samples:
        rx=mv(R,x)
        assert sum(t*t for t in rx)==sum(t*t for t in x)
        assert discriminant(rx)==-discriminant(x)
        assert discriminant([-t for t in rx])==-discriminant(x)
points=[[Q(1+2*j,4),Q(1-2*j,4),Q(0),Q(0)] for j in range(3)]
R=reflection([1,1,0,0])
distances=[[sum(abs(x[k]-mv(R,y)[k]) for k in range(D)) for y in points] for x in points]
assert distances==[[1,1,2],[1,1,1],[2,1,1]]
v=[1,-2,1]
coeff={}
for i in range(3):
    for j in range(3):
        exponent=int(distances[i][j]); coeff[exponent]=coeff.get(exponent,0)+v[i]*v[j]
assert coeff=={1:-2,2:2}
result={"normals_checked":len(normals),"exact_samples_per_normal":len(samples),"alternating_discriminant_checks_passed":True,"OU_reflected_L1_distances":[[int(x) for x in row] for row in distances],"OU_test_vector":v,"OU_quadratic_polynomial":{"a":-2,"a^2":2},"OU_sign":"2a(a-1)<0 for a=exp(-1) in (0,1)","analytic_proof":"Not machine checked; see RESULT.md"}
Path(__file__).with_name("checks.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
