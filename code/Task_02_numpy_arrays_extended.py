"""Task 2 extended: (A) parameter change, (B) new real-world case."""
import numpy as np

# ---------- PART A: change one input ----------
temps = np.array([18.5, 18.0, 17.8, 17.5, 17.9, 19.0, 21.5, 23.8, 25.6, 27.1, 28.3, 29.0,
                  29.4, 29.1, 28.5, 27.6, 26.2, 24.8, 23.4, 22.1, 21.0, 20.2, 19.6, 19.0])
print("PART A: original vs heat spike")
print(f"Original: mean={temps.mean():.2f} C, max={temps.max():.2f} C")
changed = temps.copy()
changed[12] = 40.0            # CHANGE: the 13:00 reading becomes 40 C (sensor spike)
print(f"Changed : mean={changed.mean():.2f} C, max={changed.max():.2f} C")

# ---------- PART B: new case - weekly rainfall at a farm in Nakuru ----------
# Assumptions: one rain gauge, one reading per day, values in millimetres.
rain_mm = np.array([0.0, 12.5, 3.2, 0.0, 25.4, 8.1, 0.0])
rain_inches = rain_mm / 25.4            # 1 inch = 25.4 mm (whole array at once)
print("\nPART B: weekly rainfall")
print(f"Total rainfall   : {rain_mm.sum():.1f} mm ({rain_inches.sum():.2f} in)")
print(f"Average per day  : {rain_mm.mean():.2f} mm")
print(f"Wettest day      : day {rain_mm.argmax()+1} with {rain_mm.max():.1f} mm")
print(f"Days with rain   : {(rain_mm > 0).sum()}")
