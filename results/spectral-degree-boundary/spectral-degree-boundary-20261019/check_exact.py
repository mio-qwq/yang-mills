"""Exact finite algebra checks. These do not certify the analytic proof."""
import json
from pathlib import Path

import sympy as sp


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


p = sp.symbols("p0:4")
q = sum(x*x for x in p)
Q4 = sum(x**4 for x in p)
Q6 = sum(x**6 for x in p)
I = sp.I
r2 = sp.sqrt(2)

tests = {
    "degree4_coordinate": (Q4, (I, 1, 0, 0), 2),
    "degree4_diagonal_difference": (Q4, ((I+1)/r2, (I-1)/r2, 0, 0), -2),
    "degree6_coordinate": (Q6, (I*r2, 1, 1, 0), -6),
    "degree6_diagonal_transverse": (Q6, (I/r2, I/r2, 1, 0), sp.Rational(3, 4)),
}
out = {"algebra": {}, "contact_family": {}, "growth_family": {}}
for name, (poly, point, expected) in tests.items():
    got = sp.simplify(poly.subs(dict(zip(p, point))))
    require(got == expected, f"{name}: expected {expected}, got {got}")
    out["algebra"][name] = str(got)

for j in range(1, 5):
    H = Q4**j / sp.Integer(4)**j
    P = 1 + (q+j*j)*H
    norm = sum(abs(c) for c in sp.Poly(P, *p).coeffs())
    require(norm == j*j+5, f"contact coefficient norm failed at j={j}")
    require(sp.total_degree(P) == 4*j+2, f"contact degree failed at j={j}")
    quotient, remainder = sp.div(P, q+j*j, *p)
    require(sp.expand(quotient-H) == 0 and remainder == 1, f"contact division failed at j={j}")
    out["contact_family"][str(j)] = {"coefficient_norm": str(norm), "degree": 4*j+2, "quotient_remainder": 1}

    G = Q4**(2*j) / sp.Integer(16)**j
    norm = sum(abs(c) for c in sp.Poly(G, *p).coeffs())
    require(norm == 1, f"growth coefficient norm failed at j={j}")
    require(sp.total_degree(G) == 8*j, f"growth degree failed at j={j}")
    # Nonzero restriction to q=0 proves q does not divide the top part.
    top_residue = sp.simplify(G.subs(dict(zip(p, (I, 1, 0, 0)))))
    require(top_residue == sp.Rational(1, 4)**j, f"null-cone check failed at j={j}")
    out["growth_family"][str(j)] = {"coefficient_norm": str(norm), "degree": 8*j, "nonzero_null_cone_value": str(top_residue)}

out["status"] = "all exact algebra checks passed; analytic arguments require mathematical review"
target = Path(__file__).with_name("CHECKS.json")
target.write_text(json.dumps(out, indent=2)+"\n")
print(target.read_text())
