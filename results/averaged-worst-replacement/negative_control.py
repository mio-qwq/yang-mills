"""Reject an excluded small torus and an invalid separation constant."""
from check_generic_neighbor_replacement import check
try:
 check(2)
except AssertionError:
 print('PASS rejected side2: eighteen private neighbors do not exist')
else:
 raise AssertionError('excluded torus unexpectedly passed private-neighbor test')
assert not 297*71**2>1224**2
print('PASS rejected invalid 297 separation denominator')
