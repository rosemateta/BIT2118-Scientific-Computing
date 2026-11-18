"""Task 9 extended: (A) add a link, (B) new case: friendship network of 5 students."""
import numpy as np

def centrality(A, names):
    w, v = np.linalg.eigh(A)               # symmetric matrix -> eigh is safe
    vec = np.abs(v[:, -1]); vec = vec / vec.sum()
    print(f"Dominant eigenvalue: {w[-1]:.4f}")
    for n, s in zip(names, vec): print(f"  {n}: {s:.4f}")

# ---------- PART A: add the link A-D to the original network ----------
A = np.array([[0,1,1,0],[1,0,1,1],[1,1,0,1],[0,1,1,0]], float)
print("PART A: original network"); centrality(A, "ABCD")
A2 = A.copy(); A2[0, 3] = A2[3, 0] = 1          # CHANGE
print("After adding link A-D (all nodes now equal):"); centrality(A2, "ABCD")

# ---------- PART B: new case ----------
# Assumptions: friendships among 5 students (1 = friends). Ann knows everyone,
# Brian and Cate are friends, Dan and Eve are friends, nobody else is linked.
names = ["Ann", "Brian", "Cate", "Dan", "Eve"]
F = np.array([[0,1,1,1,1],
              [1,0,1,0,0],
              [1,1,0,0,0],
              [1,0,0,0,1],
              [1,0,0,1,0]], float)
print("\nPART B: friendship network")
centrality(F, names)
