"""Task 16 extended: (A) change number of points, (B) new case: water volume from flow."""
import numpy as np
from scipy.integrate import simpson

trap = getattr(np, "trapezoid", None) or np.trapz

# ---------- PART A: integral of sin(x) from 0 to pi (exact = 2) with more points ----------
print("PART A: accuracy against number of points (exact value 2)")
for n in (5, 9, 33):                               # CHANGE: number of samples
    x = np.linspace(0, np.pi, n); y = np.sin(x)
    print(f"n={n:>2}: trapezoid error={abs(trap(y, x)-2):.2e}, Simpson error={abs(simpson(y, x=x)-2):.2e}")

# ---------- PART B: new case ----------
# Assumptions: a flow meter records water flow (litres/second) every 10 minutes
# for 1 hour at a borehole. Total volume = area under the flow-versus-time curve.
t_min = np.array([0, 10, 20, 30, 40, 50, 60], float)
flow = np.array([2.0, 2.4, 2.9, 3.0, 2.6, 2.1, 1.8])        # L/s
t_s = t_min * 60
print("\nPART B: borehole water volume")
print(f"Trapezoidal: {trap(flow, t_s):,.0f} litres")
print(f"Simpson    : {simpson(flow, x=t_s):,.0f} litres")
print(f"Average flow = {trap(flow, t_s)/t_s[-1]:.3f} L/s")
