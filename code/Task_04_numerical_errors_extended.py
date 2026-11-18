"""Task 4 extended: (A) change the approximation, (B) new case: adding money."""
import math
from decimal import Decimal
import numpy as np

# ---------- PART A: change the approximation of sqrt(2) ----------
print("PART A: error for different approximations of sqrt(2)")
true_value = np.sqrt(2)
for approx in (1.4, 1.414, 1.41421356):          # CHANGE: more digits
    ae = abs(true_value - approx)
    print(f"approx={approx:<10}: absolute error={ae:.10f}, relative error={ae/true_value:.6%}")

# ---------- PART B: new case ----------
# Assumption: a shop records 1,000 sales of KES 0.10 each. Total should be KES 100.
total = 0.0
for _ in range(1000):
    total += 0.1
print("\nPART B: adding 0.10 one thousand times")
print("Float sum          :", repr(total))
print("Equal to 100?      :", total == 100.0)
print("np.isclose to 100? :", np.isclose(total, 100.0))
print("Absolute error     :", abs(total - 100.0))
print("math.fsum          :", math.fsum([0.1]*1000))
print("Decimal sum        :", sum([Decimal('0.10')]*1000))
