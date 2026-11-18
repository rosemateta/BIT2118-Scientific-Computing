"""Task 5 extended: (A) change angle/scale, (B) new case: moving a triangle logo."""
import numpy as np

def rot(deg):
    a = np.deg2rad(deg)
    return np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])

square = np.array([[0., 0.], [1., 0.], [1., 1.], [0., 1.]])

# ---------- PART A: change angle to 90 degrees and scale to (3, 1) ----------
print("PART A: 90-degree rotation with scale (3, 1)")
T = rot(90) @ np.diag([3.0, 1.0])
print("Transformation:\n", np.round(T, 4))
print("Transformed square:\n", np.round(square @ T.T, 4))
print("Determinant (area factor):", round(np.linalg.det(T), 4))

# ---------- PART B: new case ----------
# Assumptions: a triangular app logo with corners given in pixels. We shrink it to
# 50 %, rotate it 30 degrees and then move it 100 px right and 50 px up.
# Moving (translation) needs homogeneous coordinates [x, y, 1].
logo = np.array([[0., 0.], [40., 0.], [20., 60.]])
homog = np.hstack([logo, np.ones((3, 1))])
S = np.diag([0.5, 0.5, 1.0])
R = np.eye(3); R[:2, :2] = rot(30)
M = np.eye(3); M[:2, 2] = [100, 50]
full = M @ R @ S                       # scale first, then rotate, then move
result = (homog @ full.T)[:, :2]
print("\nPART B: logo transformation")
print("Original corners:\n", logo)
print("New corners:\n", np.round(result, 2))
print("Area before:", 0.5 * 40 * 60, " Area after:", 0.5 * 40 * 60 * np.linalg.det(full[:2, :2]))
