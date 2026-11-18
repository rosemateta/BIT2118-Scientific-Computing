# Task 7: Gaussian Elimination and LU Decomposition

**Application:** Engineering simulations

## 1. Original program (`code/Task_07_gaussian_lu.py`)

### Inputs and mathematical operation

**Inputs:** a fixed 3×3 matrix A and three measurement vectors b.

**Operations:** `lu_factor` splits A into L (lower) and U (upper) once; `lu_solve` then solves each b using forward and back substitution.

### Output

```
Measurement set 1
Solution: [5. 5. 5.]
Residual norm: 0.0

Measurement set 2
Solution: [5.31707317 5.26829268 4.75609756]
Residual norm: 1.7763568394002505e-15

Measurement set 3
Solution: [4.90243902 5.6097561  5.53658537]
Residual norm: 0.0

Direct solution for first set: [5. 5. 5.]
```

### Meaning of the output

Each solution is the vector of unknowns for one measurement set. The tiny residual norm (about 1e-15) means the answers are accurate to computer precision, and the LU result equals the direct `np.linalg.solve` result.

## 2. Changing a parameter (`code/Task_07_gaussian_lu_extended.py`, Part A)

I used a new measurement vector b = [20, 5, 0]. The same factors gave a new solution [5.73, 2.93, 0.98] with a residual of about 1e-15, with no need to factor again. A different b changes the answer but not the factorization.

## 3. New real-world case: Spring-mass chain under many force sets (Part B of the same file)

### Assumptions and input data

A chain of masses joined by springs of stiffness 100 N/m. The stiffness matrix K is fixed; 300 different random force sets (0–10 N) act on a 400-mass chain. Solve K·u = f for displacement u.

### Output

```
PART A: new measurement vector [20.  5.  0.]
Solution: [5.7317 2.9268 0.9756]  residual norm: 1.831026719408895e-15

PART B: spring-mass chain
Forces on 4 masses: [5.118 9.505 1.442 9.486]
Displacements     : [0.12271 0.19424 0.17073 0.1328 ] m
300 force sets, n=400: np.linalg.solve each time=0.702s, LU factor once + reuse=0.028s
Speed-up from reusing LU: 25.0x
```

### Interpretation

For 4 masses the displacements are 0.12–0.19 m. For the 400-mass chain, factoring once and reusing was about 25 times faster than solving from scratch each time (timings vary by computer). Reuse of LU is the right tool when A stays the same.
