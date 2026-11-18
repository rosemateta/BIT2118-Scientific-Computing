"""Task 17 extended: (A) change step size h, (B) new case: logistic population growth."""
import numpy as np

# ---------- PART A: cooling with different step sizes ----------
Ta, T0, k = 25.0, 90.0, 0.12
exact30 = Ta + (T0 - Ta)*np.exp(-k*30)
print("PART A: Euler error at 30 min for different h (exact = %.4f C)" % exact30)
for h in (5.0, 1.0, 0.1):                          # CHANGE
    n = int(round(30/h)); T = T0
    for _ in range(n):
        T += h * (-k*(T - Ta))
    print(f"h={h:<4}: Euler={T:.4f} C, error={abs(T-exact30):.4f} C")

# ---------- PART B: new case ----------
# Assumptions: a fish pond holds at most K = 1000 fish. Population P grows by
# dP/dt = r P (1 - P/K) with r = 0.4 per month, P(0) = 50, time in months.
r, K, P0, h = 0.4, 1000.0, 50.0, 0.5
t = np.arange(0, 24 + h, h); P = np.zeros_like(t); P[0] = P0
for i in range(len(t)-1):
    P[i+1] = P[i] + h * r*P[i]*(1 - P[i]/K)
exact = K / (1 + (K/P0 - 1)*np.exp(-r*t))
print("\nPART B: logistic growth in a fish pond")
for m in (6, 12, 18, 24):
    i = int(m/h)
    print(f"Month {m:>2}: Euler={P[i]:7.1f}, exact={exact[i]:7.1f}")
print(f"Month when Euler passes 500 fish: {t[np.argmax(P >= 500)]:.1f}")
