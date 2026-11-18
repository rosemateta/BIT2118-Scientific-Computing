"""Task 13 extended: (A) change data/query, (B) new case: missing soil-moisture reading."""
import numpy as np
from scipy.interpolate import interp1d, CubicSpline

# ---------- PART A: change the 12:00 reading from 25.0 to 30.0 ----------
hours = np.array([8, 9, 10, 11, 12, 13, 14], float)
for name, temp in (("original", [18, 20, 22.5, 24, 25, 25.5, 25]),
                   ("changed ", [18, 20, 22.5, 24, 30, 25.5, 25])):
    lin = interp1d(hours, temp)(11.5); cub = CubicSpline(hours, temp)(11.5)
    print(f"PART A {name}: at 11:30 linear={float(lin):.2f} C, cubic={float(cub):.2f} C")

# ---------- PART B: new case ----------
# Assumptions: soil moisture (%) is recorded daily on a farm; the day-4 reading is
# missing because the sensor failed. Estimate it from the other days.
days = np.array([1, 2, 3, 5, 6, 7], float)
moisture = np.array([34.0, 32.5, 30.8, 27.0, 25.1, 23.9])
lin = interp1d(days, moisture)
cub = CubicSpline(days, moisture)
print("\nPART B: missing soil moisture on day 4")
print(f"Linear estimate: {float(lin(4)):.2f} %")
print(f"Cubic spline   : {float(cub(4)):.2f} %")
