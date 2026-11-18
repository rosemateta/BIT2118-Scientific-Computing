# Task 12: Polynomial and Nonlinear Equation Solving

**Application:** Geometry, control systems

## 1. Original program (`code/Task_12_nonlinear_equations.py`)

### Inputs and mathematical operation

**Inputs:** the circle x² + y² = 4, the parabola y = x² − 1, and two starting guesses.

**Operation:** `scipy.optimize.root` changes x and y until both residuals are about zero.

### Output

```
Initial guess: [1.0, 1.0]
Intersection: [1.51748991 1.30277564]
Residuals: [np.float64(-2.4780177909633494e-13), np.float64(-2.4158453015843406e-13)]
Converged: True

Initial guess: [-1.0, 1.0]
Intersection: [-1.51748991  1.30277564]
Residuals: [np.float64(-2.4780177909633494e-13), np.float64(-2.4158453015843406e-13)]
Converged: True
```

### Meaning of the output

The curves meet at (1.5175, 1.3028) and (−1.5175, 1.3028). Residuals are about 1e-13 and `Converged: True`, so the answers satisfy both equations. The two answers are mirror images because both curves are symmetric about the y-axis.

## 2. Changing a parameter (`code/Task_12_nonlinear_equations_extended.py`, Part A)

I changed the circle radius to 3. The intersections moved to (±1.8364, 2.3723). I also tried a bad start [0, −3]; the solver failed (success = False, residual 2.0) so the starting guess matters.

## 3. New real-world case: Locating a phone from two towers (Part B of the same file)

### Assumptions and input data

Tower 1 at (0,0) km, tower 2 at (6,0) km. The phone is 5 km from tower 1 and 4 km from tower 2: x²+y²=25 and (x−6)²+y²=16.

### Output

```
PART A: circle radius 3, parabola y = x^2 - 1
guess=[1.0, 1.0]: solution=[1.8364 2.3723], residual norm=2.0e-12, ok=True
guess=[-1.0, 1.0]: solution=[-1.8364  2.3723], residual norm=2.0e-12, ok=True
guess=[0.0, -3.0]: solution=[ 0. -3.], residual norm=2.0e+00, ok=False

PART B: phone position from two towers
guess=[3.0, 3.0]: position=(3.7500, 3.3072) km, residual norm=0.0e+00
guess=[3.0, -3.0]: position=(3.7500, -3.3072) km, residual norm=0.0e+00
Two answers are mirror images; a third tower would pick the correct one.
```

### Interpretation

Two possible positions: (3.75, 3.31) and (3.75, −3.31) km, mirror images across the line joining towers. A third tower is needed to choose the right one, which is why GPS uses several satellites.
