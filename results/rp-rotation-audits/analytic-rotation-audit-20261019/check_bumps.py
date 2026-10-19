#!/usr/bin/env python3
"""Portable exact bump calculations; no external source files needed."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json

def require(c,m):
    if not c: raise ValueError(m)

def radial(k):
    return sum((F((-1)**j*comb(k,j),4+2*j) for j in range(k+1)),F())
require(2*radial(2)==F(1,12),'L1 radial integral')
require(2*radial(4)==F(1,30),'L2 radial integral')
# pi>3 gives pi^2/12>3/4>1/2, and (8/(3sqrt(3)))^2=64/27<4.
require(F(9,12)>F(1,2),'mass-fraction admissibility')
require(F(64,27)<4,'Lipschitz admissibility')
checks={'phi':'(1-|x|^2)_+^2','regularity':'C^1_c(R^4)','theta':0.5,'sup_norm':1,'L1_over_d4':'pi^2/12','L2_squared_over_d4':'pi^2/30','Lip_times_d':'8/(3 sqrt(3))','separation_over_d':'2','Gaussian_covariance_upper':'(C pi^2/15) d^4','exact_radial_checks_passed':True}
checks['separation_over_d']=2
Path(__file__).with_name('CHECKS.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2))
