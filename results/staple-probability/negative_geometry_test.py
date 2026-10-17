"""Reject a torus too small for the required transverse margin."""
from independent_geometry_check import check
try:
    check(2)
except AssertionError:
    print("PASS rejected side4: required private-link seam geometry fails")
else:
    raise AssertionError("invalid side4 geometry was accepted")
