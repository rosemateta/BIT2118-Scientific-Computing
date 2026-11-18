# Task 6: Solution of Systems of Linear Equations

**Application:** Resource allocation, circuits

## 1. Original program (`code/Task_06_linear_systems.py`)

### Inputs and mathematical operation

**Inputs:** coefficient matrix A = [[4,2],[8,12]] (CPU and memory per server type) and totals b = [20, 72].

**Operation:** `np.linalg.solve(A, b)` finds x so that Ax = b. The residual b − Ax checks the answer.

### Output

```
Type A servers: 3
Type B servers: 4
Verification A @ solution: [20. 72.]
Residual: [0. 0.]
Residual norm: 0.0
```

### Meaning of the output

The solution (3 Type A and 4 Type B servers) means these numbers of machines produce exactly 20 CPU units and 72 GB. The residual 0 proves A·x reproduces b.

## 2. Changing a parameter (`code/Task_06_linear_systems_extended.py`, Part A)

I changed the totals to [26, 96]. The answer changed from 3 and 4 servers to 3.75 and 5.5, which are not whole servers, so those totals could not come from whole machines. I also showed that a matrix with a row that is a multiple of another is singular and NumPy raises an error (no unique solution).

## 3. New real-world case: Currents in a two-loop electrical circuit (Part B of the same file)

### Assumptions and input data

Loop 1: 12 V battery, R1 = 6 Ω, shared R2 = 4 Ω. Loop 2: 6 V battery opposing, R3 = 5 Ω, shared R2 = 4 Ω. Kirchhoff equations: 10·I1 − 4·I2 = 12 and −4·I1 + 9·I2 = −6.

### Output

```
PART A: different observed totals
Totals [20.0, 72.0] -> Type A=3.000, Type B=4.000
Totals [26.0, 96.0] -> Type A=3.750, Type B=5.500
Singular example (second row = 2 x first row):
Error: Singular matrix

PART B: circuit loop currents
I1 = 1.1351 A, I2 = -0.1622 A
Current through shared resistor = 1.2973 A
Residual: [ 0.0000000e+00 -8.8817842e-16]
```

### Interpretation

I1 = 1.1351 A and I2 = −0.1622 A. The minus sign means loop 2's current actually flows opposite to the direction we assumed. Current in the shared resistor is I1 − I2 = 1.2973 A. The residual is about zero so the solution is correct.
