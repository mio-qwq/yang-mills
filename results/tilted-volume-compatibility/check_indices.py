from fractions import Fraction
import json

def det(u,v):return u[0]*v[1]-u[1]*v[0]
def contains(basis,v):
 a,b=basis;D=det(a,b)
 return Fraction(det(v,b),D).denominator==1 and Fraction(det(a,v),D).denominator==1
out=[]
for N in range(1,33):
 straight=((N,0),(0,N));tilted=((N,N),(N,-N))
 coordinate=((2*N,0),(0,2*N))
 for B in (straight,tilted):
  assert all(contains(B,(-v[0],v[1])) and contains(B,(v[1],v[0])) for v in B)
 indices={'straight_coordinate':1,'straight_diagonal':abs(det(*tilted)//det(*straight)), 'tilted_coordinate':abs(det(*coordinate)//det(*tilted)),'tilted_diagonal':1}
 assert indices=={'straight_coordinate':1,'straight_diagonal':2,'tilted_coordinate':2,'tilted_diagonal':1}
 assert not contains(tilted,(N,0)) and contains(tilted,(2*N,0))
 out.append({'N':N,'indices':indices})
print(json.dumps({'status':'PASS','scope':'Exact lattice examples only; the general topology result is proved in the accompanying text.','cases':out},indent=2))
