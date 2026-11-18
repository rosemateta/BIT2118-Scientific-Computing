"""Task 15 extended: (A) change the step size h, (B) new case: acceleration from speed."""
import numpy as np

# ---------- PART A: forward vs central difference of sin(x) at x = 1 ----------
exact = np.cos(1.0)
print("PART A: derivative of sin(x) at x=1 (exact = cos(1) = %.8f)" % exact)
for h in (0.1, 0.01, 0.001):                       # CHANGE: step size
    fwd = (np.sin(1+h) - np.sin(1)) / h
    cen = (np.sin(1+h) - np.sin(1-h)) / (2*h)
    print(f"h={h:<6}: forward error={abs(fwd-exact):.2e}, central error={abs(cen-exact):.2e}")

# ---------- PART B: new case ----------
# Assumptions: a matatu's speed (m/s) is logged every 2 s while it accelerates.
# Acceleration = rate of change of speed.
t = np.array([0, 2, 4, 6, 8, 10, 12], float)
v = np.array([0.0, 3.1, 6.4, 9.2, 11.0, 12.1, 12.5])
acc = np.gradient(v, t)                    # central inside, one-sided at the ends
print("\nPART B: acceleration from speed data")
for ti, vi, ai in zip(t, v, acc):
    print(f"t={ti:>4.0f}s speed={vi:>5.1f} m/s acceleration={ai:>5.2f} m/s^2")
print(f"Largest acceleration at t={t[acc.argmax()]:.0f}s: {acc.max():.2f} m/s^2")
