"""Task 14 extended: (A) change the model, (B) new case: exponential growth of users."""
import numpy as np
from scipy.optimize import curve_fit

# ---------- PART A: fit a straight line instead of a quadratic ----------
users = np.array([50, 100, 150, 200, 250, 300, 350], float)
resp = np.array([82, 95, 115, 145, 185, 238, 305], float)
lin = lambda x, a, b: a*x + b
quad = lambda x, a, b, c: a*x**2 + b*x + c
for name, f in (("linear", lin), ("quadratic", quad)):
    p, _ = curve_fit(f, users, resp)
    rmse = np.sqrt(np.mean((resp - f(users, *p))**2))
    print(f"PART A {name:9s}: RMSE={rmse:.2f} ms, prediction at 400 users={f(400, *p):.1f} ms")

# ---------- PART B: new case ----------
# Assumptions: monthly active users (thousands) of a campus app over 8 months.
# Growth is assumed exponential: y = a * exp(b * x).
month = np.arange(1, 9, dtype=float)
active = np.array([2.1, 2.6, 3.4, 4.3, 5.4, 7.0, 8.8, 11.3])
model = lambda x, a, b: a*np.exp(b*x)
p, _ = curve_fit(model, month, active, p0=(2, 0.2))
rmse = np.sqrt(np.mean((active - model(month, *p))**2))
print("\nPART B: user growth")
print(f"Fitted: y = {p[0]:.3f} * exp({p[1]:.4f} x)")
print(f"RMSE = {rmse:.3f} thousand users; monthly growth = {np.exp(p[1])-1:.1%}")
print(f"Forecast month 10: {model(10, *p):.1f} thousand users")
