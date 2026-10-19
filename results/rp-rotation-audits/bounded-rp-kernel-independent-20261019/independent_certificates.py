"""Independent exact algebraic checks. No floating point and no source-file changes."""
from itertools import permutations, product
from fractions import Fraction as F
from pathlib import Path
import json

D=4
zero=(0,)*D

def mul(a,b):
    out={}
    for u,c in a.items():
        for v,d in b.items():
            w=tuple(x+y for x,y in zip(u,v))
            out[w]=out.get(w,0)+c*d
    return {w:c for w,c in out.items() if c}

P={(1,1,1,1):1}
for i in range(D):
    for j in range(i+1,D):
        u=[0]*D; u[i]=2
        v=[0]*D; v[j]=2
        P=mul(P,{tuple(u):1,tuple(v):-1})
assert len(P)==24 and {sum(e) for e in P}=={16}

def perm_sign(p):
    return (-1)**sum(p[i]>p[j] for i in range(D) for j in range(i+1,D))

def subst(poly,perm,signs):
    out={}
    for powers,coef in poly.items():
        new=[0]*D
        for i,e in enumerate(powers):
            new[perm[i]]+=e
            coef*=signs[i]**e
        key=tuple(new)
        out[key]=out.get(key,0)+coef
    return {w:c for w,c in out.items() if c}

count=0
for perm in permutations(range(D)):
    for signs in product((-1,1),repeat=D):
        determinant=perm_sign(perm)
        for s in signs: determinant*=s
        assert subst(P,perm,signs)=={e:determinant*c for e,c in P.items()}
        count+=1
assert count==384

normals=[]
for i in range(D):
    n=[0]*D; n[i]=1; normals.append(n)
for i in range(D):
    for j in range(i+1,D):
        for s in (-1,1):
            n=[0]*D; n[i]=1; n[j]=s; normals.append(n)

def reflection(n):
    N=sum(a*a for a in n)
    return [[F(i==j)-F(2*n[i]*n[j],N) for j in range(D)] for i in range(D)]

def mv(A,v):
    return [sum(a*x for a,x in zip(row,v)) for row in A]

for n in normals:
    R=reflection(n)
    perm=[]; signs=[]
    for row in R:
        nonzero=[(j,c) for j,c in enumerate(row) if c]
        assert len(nonzero)==1 and abs(nonzero[0][1])==1
        j,c=nonzero[0]; perm.append(j); signs.append(int(c))
    det=perm_sign(perm)
    for s in signs:det*=s
    assert det==-1
    assert subst(P,perm,signs)=={e:-c for e,c in P.items()}

w=(1,2,3,4)
Pw=1
for x in w: Pw*=x
for i in range(D):
    for j in range(i+1,D):Pw*=w[i]**2-w[j]**2
assert Pw>0

X=[(F(1+2*j,4),F(1-2*j,4),F(0),F(0)) for j in range(3)]
R=reflection((1,1,0,0))
E=[[sum(abs(x-y) for x,y in zip(a,mv(R,b))) for b in X] for a in X]

assert E==[[1,1,2],[1,1,1],[2,1,1]]
v=(1,-2,1)
coef={}
for i in range(3):
    for j in range(3):
        k=int(E[i][j]); coef[k]=coef.get(k,0)+v[i]*v[j]
assert coef=={1:-2,2:2}
assert all(x[0]+x[1]>0 for x in X)
result={
    "polynomial_degree":16,
    "expanded_monomials":len(P),
    "signed_permutation_symbolic_identities":count,
    "reflection_polynomial_identities":len(normals),
    "P_at_1_2_3_4":Pw,
    "non_positive_type_witness":"C(1,2,3,4)=1+P(1,2,3,4)*exp(-30)>C(0)=1",
    "OU_distance_matrix":[[int(a) for a in row] for row in E],
    "OU_quadratic_coefficients":coef,
    "status":"all exact checks passed",
    "scope":"The analytic measure argument is independently reviewed, not machine verified."
}
Path(__file__).with_name("independent_checks.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
