"""Task 7 extended: (A) new measurement vector, (B) new case: spring-mass chain."""
import numpy as np, timeit
from scipy.linalg import lu_factor, lu_solve

# ---------- PART A: a new b vector with the same A ----------
A = np.array([[4., -1., 0.], [-1., 4., -1.], [0., -1., 3.]])
lu, piv = lu_factor(A)
b_new = np.array([20., 5., 0.])                     # CHANGE
x = lu_solve((lu, piv), b_new)
print("PART A: new measurement vector", b_new)
print("Solution:", np.round(x, 4), " residual norm:", np.linalg.norm(b_new - A @ x))

# ---------- PART B: new case ----------
# Assumptions: a chain of n masses held by springs (stiffness k=100 N/m each).
# The stiffness matrix K is fixed; every second a different set of forces (N) acts.
# Solve K u = f for the displacements u (m). First a small 4-mass chain, then a
# 400-mass chain to show why reusing the LU factors saves time.
def chain(n, k=100.0):
    return k * (2*np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1))

rng = np.random.default_rng(1)
K4 = chain(4); lu4, piv4 = lu_factor(K4)
f0 = rng.uniform(0, 10, 4)
print("\nPART B: spring-mass chain")
print("Forces on 4 masses:", np.round(f0, 3))
print("Displacements     :", np.round(lu_solve((lu4, piv4), f0), 5), "m")

n = 400
K = chain(n); forces = [rng.uniform(0, 10, n) for _ in range(300)]
t_direct = timeit.timeit(lambda: [np.linalg.solve(K, f) for f in forces], number=1)
t_lu = timeit.timeit(lambda: (lambda F: [lu_solve(F, f) for f in forces])(lu_factor(K)), number=1)
print(f"{len(forces)} force sets, n={n}: np.linalg.solve each time={t_direct:.3f}s, LU factor once + reuse={t_lu:.3f}s")
print(f"Speed-up from reusing LU: {t_direct/t_lu:.1f}x")
