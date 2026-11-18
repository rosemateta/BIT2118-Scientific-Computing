# Task 4: Floating-Point Arithmetic and Numerical Errors

**Application:** Banking, GPS, simulations

## 1. Original program (`code/Task_04_numerical_errors.py`)

### Inputs and mathematical operation

**Inputs:** the numbers 0.1, 0.2, 0.3, √2 and its approximation 1.414, and small values x = 1e-4, 1e-8, 1e-12.

**Operations:** exact comparison versus `np.isclose`, absolute error |true − approx|, relative error = absolute / |true|, and two formulas for (√(1+x) − 1)/x.

### Output

```
0.1 + 0.2 = 0.30000000000000004
Exact comparison: False
Tolerance-based comparison: True
Absolute error: 0.00021356
Relative error: 0.01510114%
x=1e-04: direct=0.499987500624, stable=0.499987500625
x=1e-08: direct=0.499999996961, stable=0.499999998750
x=1e-12: direct=0.500044450291, stable=0.500000000000
```

### Meaning of the output

0.1 + 0.2 gives 0.30000000000000004, so `==` says False but `np.isclose` says True: computers store 0.1 and 0.2 in binary with tiny rounding. In the last loop the direct formula loses accuracy as x gets smaller (at x=1e-12 it gives 0.50004445 instead of 0.5) because two nearly equal numbers are subtracted. The rewritten stable formula stays correct (0.500000000000).

## 2. Changing a parameter (`code/Task_04_numerical_errors_extended.py`, Part A)

I changed the approximation of √2 from 1.414 to 1.4 and to 1.41421356. Relative error was 1.005%, 0.0151% and about 0.0000002%. More correct digits give a smaller error.

## 3. New real-world case: Adding shop sales of KES 0.10, 1000 times (Part B of the same file)

### Assumptions and input data

A shop records 1,000 sales of KES 0.10 and the total should be KES 100.

### Output

```
PART A: error for different approximations of sqrt(2)
approx=1.4       : absolute error=0.0142135624, relative error=1.005051%
approx=1.414     : absolute error=0.0002135624, relative error=0.015101%
approx=1.41421356: absolute error=0.0000000024, relative error=0.000000%

PART B: adding 0.10 one thousand times
Float sum          : 99.9999999999986
Equal to 100?      : False
np.isclose to 100? : True
Absolute error     : 1.4068746168049984e-12
math.fsum          : 100.0
Decimal sum        : 100.00
```

### Interpretation

The simple float sum gives 99.9999999999986, so `== 100` is False (error about 1.4e-12). `np.isclose`, `math.fsum` and `Decimal` all give 100. Lesson: for money use `Decimal` (or whole cents), and never compare floats with `==`.
