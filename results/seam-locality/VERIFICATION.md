# Portable exact verification

Executed locally on 2026-10-17 with Python 3 standard library. Fresh runs; every exit status is checked. Numerical samples support but do not replace the symbolic proof.

## check_quartic.py

Working directory: `results/seam-locality`

Command: `python3 check_quartic.py`

Script SHA-256: `7eb3610a6e5788de5fc3cb59a2e5888da2103210af391645d4749a4179864127`

Exit status: 0

```text
n= 8 nonseam cubes containing strict +/- faces: 0 seam +/- pairs: 2048
original reflected cube matrix: [0, 1, 1, 0]
n= 9 nonseam cubes containing strict +/- faces: 0 seam +/- pairs: 3078
original reflected cube matrix: [0, 1, 1, 0]
```

## check_geometry.py

Working directory: `results/seam-locality`

Command: `python3 check_geometry.py`

Script SHA-256: `8415c6649841c048dcd6764d134f57dcc8b17ed14c23bd989aa3f5cbc0d074aa`

Exit status: 0

```text
{"cubes": 16384, "cylinder_crossing_faces": 448, "cylinder_interface_faces": 512, "faces": 24576, "interior_opposite_pairs": 0, "minimum_action_path_by_endpoint_depth": {"0": 1, "1": 2, "2": 3, "3": 4}, "n": 8, "nonseam_opposite_pairs": 0, "original_matrix": [[0, 1], [1, 0]], "seam_faces": 3008, "seam_opposite_pairs": 2048}
{"cubes": 26244, "cylinder_crossing_faces": 648, "cylinder_interface_faces": 729, "faces": 39366, "interior_opposite_pairs": 0, "minimum_action_path_by_endpoint_depth": {"0": 1, "1": 2, "2": 3, "3": 4, "4": 5}, "n": 9, "nonseam_opposite_pairs": 0, "original_matrix": [[0, 1], [1, 0]], "seam_faces": 4293, "seam_opposite_pairs": 3078}
{"cubes": 40000, "cylinder_crossing_faces": 900, "cylinder_interface_faces": 1000, "faces": 60000, "interior_opposite_pairs": 0, "minimum_action_path_by_endpoint_depth": {"0": 1, "1": 2, "2": 3, "3": 4, "4": 5}, "n": 10, "nonseam_opposite_pairs": 0, "original_matrix": [[0, 1], [1, 0]], "seam_faces": 5900, "seam_opposite_pairs": 4400}
```
