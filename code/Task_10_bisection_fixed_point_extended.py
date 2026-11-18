"""Task 10 extended: (A) change a parameter, (B) new case: break-even point."""
import numpy as np
from scipy.optimize import root_scalar

# ---------- PART A: change the heat-loss coefficient (10 -> 20) and the bracket ----------
def make(c):
    f = lambda T: T - 25 - c*np.exp(-T/20)
    g = lambda T: 25 + c*np.exp(-T/20)
    return f, g

print("PART A: effect of coefficient c")
for c in (10, 20):
    f, g = make(c)
    sol = root_scalar(f, bracket=[20, 60], method="bisect", xtol=1e-10)
    T = 30.0; n = 0
    while abs(g(T) - T) > 1e-10 and n < 200:
        T = g(T); n += 1
    print(f"c={c}: bisection={sol.root:.6f} C ({sol.iterations} its), fixed-point={T:.6f} C ({n} its)")

# ---------- PART B: new case ----------
# Assumptions: a bakery sells q loaves a day. Price falls as it sells more, so revenue
# R(q) = 120 q exp(-q/150). Daily cost C(q) = 2000 + 30 q (KES). Break-even: R(q) = C(q).
f = lambda q: 120*q*np.exp(-q/150) - (2000 + 30*q)
q = np.linspace(1, 600, 6000)
signs = np.where(np.diff(np.sign(f(q))) != 0)[0]
print("\nPART B: bakery break-even")
for i in signs:
    r = root_scalar(f, bracket=[q[i], q[i+1]], method="bisect", xtol=1e-9)
    print(f"Break-even at q = {r.root:.2f} loaves, revenue = KES {120*r.root*np.exp(-r.root/150):.2f}")
print(f"Maximum daily profit near q = {q[np.argmax(f(q))]:.0f} loaves: KES {f(q).max():.2f}")
