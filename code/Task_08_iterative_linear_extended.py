"""Task 8 extended: (A) change boundary temperatures/tolerance, (B) new case: long metal rod."""
import numpy as np

def tri(n):
    return 2*np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)

def jacobi(A, b, tol=1e-8, max_iter=20000):
    D = np.diag(A); R = A - np.diagflat(D); x = np.zeros_like(b)
    for it in range(1, max_iter+1):
        xn = (b - R @ x) / D
        if np.linalg.norm(xn - x, np.inf) < tol: return xn, it
        x = xn
    return x, max_iter

def gauss_seidel(A, b, tol=1e-8, max_iter=20000):
    x = np.zeros_like(b)
    for it in range(1, max_iter+1):
        old = x.copy()
        for i in range(len(b)):
            x[i] = (b[i] - A[i, :i] @ x[:i] - A[i, i+1:] @ old[i+1:]) / A[i, i]
        if np.linalg.norm(x - old, np.inf) < tol: return x, it
    return x, max_iter

# ---------- PART A: change boundaries to 200 C / 50 C and tolerance ----------
A = tri(5)
print("PART A: boundaries 200/50, tolerances 1e-4 and 1e-10")
b = np.array([200., 0, 0, 0, 50.])
for tol in (1e-4, 1e-10):
    xj, ij = jacobi(A, b, tol); xg, ig = gauss_seidel(A, b, tol)
    print(f"tol={tol:g}: Jacobi {ij} iterations, Gauss-Seidel {ig} iterations")
print("Temperatures (Gauss-Seidel, tol 1e-10):", np.round(xg, 3))

# ---------- PART B: new case ----------
# Assumptions: metal rod with 20 interior points, ends held at 150 C and 30 C,
# no heat source along the rod. Steady state is a straight line between the ends.
n = 20
A = tri(n); b = np.zeros(n); b[0], b[-1] = 150., 30.
xe = np.linalg.solve(A, b)
xj, ij = jacobi(A, b); xg, ig = gauss_seidel(A, b)
print("\nPART B: rod with 20 points")
print(f"Jacobi iterations: {ij}, Gauss-Seidel iterations: {ig}")
print("Max difference from direct solution (Gauss-Seidel):", np.max(np.abs(xg - xe)))
print("Temperature at points 1, 10, 20:", np.round([xe[0], xe[9], xe[-1]], 2))
