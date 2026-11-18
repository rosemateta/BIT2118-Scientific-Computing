"""Task 19 extended: (A) change cost/capacity, (B) new case: cheapest chicken feed mix."""
import numpy as np
from scipy.optimize import minimize

# ---------- PART A: Type B now costs 25 per unit instead of 18 ----------
def solve(cA, cB):
    r = minimize(lambda z: cA*z[0] + cB*z[1], x0=[5, 3], method="SLSQP",
                 bounds=[(0, None)]*2,
                 constraints={"type": "ineq", "fun": lambda z: 100*z[0] + 170*z[1] - 1000})
    return r
for cB in (18, 25):                                  # CHANGE
    r = solve(12, cB)
    print(f"PART A: cost B={cB}: A={r.x[0]:.3f}, B={r.x[1]:.3f}, cost={r.fun:.2f}, success={r.success}")

# ---------- PART B: new case ----------
# Assumptions: mix x kg of Feed A and y kg of Feed B to make 100 kg of chicken feed.
# Feed A: KES 40/kg, 20% protein, 3000 kcal/kg.   Feed B: KES 55/kg, 35% protein, 2800 kcal/kg.
# Mix must have at least 25 kg protein and at least 290,000 kcal in total.
cost = lambda z: 40*z[0] + 55*z[1]
cons = [
    {"type": "eq",   "fun": lambda z: z[0] + z[1] - 100},
    {"type": "ineq", "fun": lambda z: 0.20*z[0] + 0.35*z[1] - 25},
    {"type": "ineq", "fun": lambda z: 3000*z[0] + 2800*z[1] - 290000},
]
r = minimize(cost, x0=[60, 40], method="SLSQP", bounds=[(0, None)]*2, constraints=cons)
x, y = r.x
print("\nPART B: cheapest feed mix")
print(f"Success={r.success}: Feed A={x:.2f} kg, Feed B={y:.2f} kg, cost=KES {r.fun:.2f}")
print(f"Protein={0.20*x+0.35*y:.2f} kg, energy={3000*x+2800*y:,.0f} kcal")
