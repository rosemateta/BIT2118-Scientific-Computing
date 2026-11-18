"""Task 12 extended: (A) change the radius, (B) new case: locating a phone by two towers."""
import numpy as np
from scipy.optimize import root

# ---------- PART A: circle radius 2 -> 3 ----------
print("PART A: circle radius 3, parabola y = x^2 - 1")
def eqs(z, r=3.0):
    x, y = z
    return [x**2 + y**2 - r**2, y - (x**2 - 1)]
for guess in ([1., 1.], [-1., 1.], [0., -3.]):
    s = root(eqs, guess)
    print(f"guess={guess}: solution={np.round(s.x, 4)}, residual norm={np.linalg.norm(eqs(s.x)):.1e}, ok={s.success}")

# ---------- PART B: new case ----------
# Assumptions: tower 1 at (0,0) km and tower 2 at (6,0) km. A phone is measured
# 5 km from tower 1 and 4 km from tower 2. Find (x, y) - two circle equations.
def towers(z):
    x, y = z
    return [x**2 + y**2 - 5**2, (x-6)**2 + y**2 - 4**2]
print("\nPART B: phone position from two towers")
for guess in ([3., 3.], [3., -3.]):
    s = root(towers, guess)
    print(f"guess={guess}: position=({s.x[0]:.4f}, {s.x[1]:.4f}) km, residual norm={np.linalg.norm(towers(s.x)):.1e}")
print("Two answers are mirror images; a third tower would pick the correct one.")
