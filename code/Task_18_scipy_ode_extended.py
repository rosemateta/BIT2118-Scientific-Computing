"""Task 18 extended: (A) change R, (B) new case: SIR epidemic model."""
import numpy as np
from scipy.integrate import solve_ivp

# ---------- PART A: change resistance R = 1000 -> 2000 ohms ----------
Vs, C = 5.0, 0.001
for R in (1000.0, 2000.0):
    s = solve_ivp(lambda t, V: [(Vs - V[0])/(R*C)], (0, 10), [0.0], t_eval=np.linspace(0, 10, 201), rtol=1e-9, atol=1e-11)
    tau = R*C
    v_tau = float(np.interp(tau, s.t, s.y[0]))
    print(f"PART A: R={R:.0f} ohm, time constant={tau:.0f} s, V at tau={v_tau:.3f} V (63.2% of 5 V = 3.161), V at 10 s={s.y[0,-1]:.3f} V")

# ---------- PART B: new case ----------
# Assumptions: a school of 1000 students; 1 infected at start. Each infected student
# infects others at rate beta=0.35/day and recovers at rate gamma=0.1/day.
beta, gamma, N = 0.35, 0.10, 1000.0
def sir(t, y):
    S, I, R_ = y
    return [-beta*S*I/N, beta*S*I/N - gamma*I, gamma*I]
sol = solve_ivp(sir, (0, 120), [999., 1., 0.], t_eval=np.linspace(0, 120, 121), rtol=1e-8, atol=1e-10)
I = sol.y[1]
print("\nPART B: SIR epidemic in a school")
print(f"R0 = beta/gamma = {beta/gamma:.1f}")
print(f"Peak infections: {I.max():.0f} students on day {sol.t[I.argmax()]:.0f}")
print(f"Total ever infected by day 120: {N - sol.y[0, -1]:.0f}")
print("Check S+I+R at the end =", round(float(sol.y[:, -1].sum()), 4))
