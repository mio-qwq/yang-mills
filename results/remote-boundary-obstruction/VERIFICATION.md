# Portable exact verification

Executed locally on 2026-10-17 with Python 3 standard library. Fresh runs; every exit status is checked. Numerical samples support but do not replace the symbolic proof.

## check_geometry_threshold.py

Working directory: `results/remote-boundary-obstruction`

Command: `python3 check_geometry_threshold.py`

Script SHA-256: `b9022a5c73e2a9ac04bac7e5508c3a78c590819880fac8bb30b112aa910de064`

Exit status: 0

```text
PASS L= 0 h= 4 negative coefficient denominator exponent= 9
PASS L= 1 h= 12 negative coefficient denominator exponent= 25
PASS L= 2 h= 20 negative coefficient denominator exponent= 41
PASS L= 3 h= 28 negative coefficient denominator exponent= 57
PASS L= 4 h= 36 negative coefficient denominator exponent= 73
PASS L= 5 h= 44 negative coefficient denominator exponent= 89
PASS L= 6 h= 52 negative coefficient denominator exponent= 105
PASS exact coefficients, geometry, threshold inequalities
```

## check_controls.py

Working directory: `results/remote-boundary-obstruction`

Command: `python3 check_controls.py`

Script SHA-256: `8a3db82ff12c84a3d0d40c0a8f8987a0c86debedf9ed0d65630d0ae7fd82727c`

Exit status: 0

```text
PASS: 612 admissible (L,n,k) geometries for 0<=L<=12, first nine admissible n.
PASS: exact rational coefficients and beta-star bounds for all tested (L,n).
PASS: n=8 has 12 four-cycles through origin, all elementary.
PASS: n=11 has 12 four-cycles through origin, all elementary.
Endpoint L=0,n=8: k=2,3,4,5; D=1; h=4; c=1/512.
Endpoint exact r=1/98304; beta_star=1/225614572159760555100365389824.
PASS: strict Cauchy remainder < (c/2) beta_star^h at the endpoint.

```

## check_representation.py

Working directory: `results/remote-boundary-obstruction`

Command: `python3 check_representation.py`

Script SHA-256: `7112502897568681e87b4eb5a65112bc629f4b715234a5c43755304ada97fd80`

Exit status: 0

```text
j=0/2: [(0, '1')]
j=1/2: [(1, '1/4'), (3, '-1/96'), (5, '1/1536'), (7, '-1/23040')]
j=2/2: [(2, '1/24'), (4, '-1/384'), (6, '1/5760'), (8, '-13/1105920')]
j=3/2: [(3, '1/192'), (5, '-1/2560'), (7, '1/36864')]
j=4/2: [(4, '1/1920'), (6, '-1/23040'), (8, '1/322560')]
D=3 covariance coefficient = 1/67108864
Reflected F coefficient = -1/33554432
PASS: reconstructed exact character series match the historical output byte-for-byte.
```
