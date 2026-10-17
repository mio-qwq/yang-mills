"""Exact incidence check for the explicit 4D Wilson Dobrushin bound."""
from itertools import product
from collections import Counter
from fractions import Fraction

def shift(x, mu, n):
    y=list(x); y[mu]=(y[mu]+1)%n; return tuple(y)

def check(n=5,d=4):
    links=[(x,mu) for x in product(range(n),repeat=d) for mu in range(d)]
    incidences={e:[] for e in links}
    for x in product(range(n),repeat=d):
        for mu in range(d):
            for nu in range(mu+1,d):
                p=((x,mu),(shift(x,mu,n),nu),(shift(x,nu,n),mu),(x,nu))
                assert len(set(p))==4
                for e in p: incidences[e].append(p)
    for e,ps in incidences.items():
        assert len(ps)==2*(d-1)
        multiplicity=Counter(f for p in ps for f in p if f!=e)
        assert sum(multiplicity.values())==6*(d-1)
    beta=Fraction(1,36)
    assert 6*(d-1)*beta==Fraction(1,2)
    print(f'PASS: {len(links)} links, each in {2*(d-1)} plaquettes; summed off-diagonal multiplicity {6*(d-1)}; beta=1/36 gives q=1/2.')

if __name__=='__main__': check()
