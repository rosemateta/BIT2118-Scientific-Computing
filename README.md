# BIT 2118 Scientific Computing: Group Work

Name: Rose  |  Course: BIT 2118 Scientific Computing  |  Mount Kenya University

This repository covers Tasks 2 to 20 of the group work. For each task it contains:

1. the original program from the brief (`code/Task_XX_*.py`),
2. an extended program (`code/Task_XX_*_extended.py`) with **Part A** (one input changed) and **Part B** (a new real-world case),
3. the saved program output (`outputs/`), and graphs where the task makes one,
4. a document (`docs/Task_XX.md`) covering: inputs and operation, meaning of the output, effect of the parameter change, and the new case with its assumptions, data, output and interpretation.

| Task | Topic | Documentation | Original code | Extended code |
|---|---|---|---|---|
| 2 | NumPy Arrays and Numerical Computation | [Doc](docs/Task_02.md) | `Task_02_numpy_arrays.py` | `Task_02_numpy_arrays_extended.py` |
| 3 | Mathematical Functions and Vectorization | [Doc](docs/Task_03.md) | `Task_03_vectorization.py` | `Task_03_vectorization_extended.py` |
| 4 | Floating-Point Arithmetic and Numerical Errors | [Doc](docs/Task_04.md) | `Task_04_numerical_errors.py` | `Task_04_numerical_errors_extended.py` |
| 5 | Matrix Algebra and Matrix Operations | [Doc](docs/Task_05.md) | `Task_05_matrix_algebra.py` | `Task_05_matrix_algebra_extended.py` |
| 6 | Solution of Systems of Linear Equations | [Doc](docs/Task_06.md) | `Task_06_linear_systems.py` | `Task_06_linear_systems_extended.py` |
| 7 | Gaussian Elimination and LU Decomposition | [Doc](docs/Task_07.md) | `Task_07_gaussian_lu.py` | `Task_07_gaussian_lu_extended.py` |
| 8 | Iterative Methods for Linear Systems | [Doc](docs/Task_08.md) | `Task_08_iterative_linear.py` | `Task_08_iterative_linear_extended.py` |
| 9 | Eigenvalues and Eigenvectors | [Doc](docs/Task_09.md) | `Task_09_eigenvalues.py` | `Task_09_eigenvalues_extended.py` |
| 10 | Root Finding: Bisection and Fixed-Point Methods | [Doc](docs/Task_10.md) | `Task_10_bisection_fixed_point.py` | `Task_10_bisection_fixed_point_extended.py` |
| 11 | Root Finding: Newton-Raphson and Secant Methods | [Doc](docs/Task_11.md) | `Task_11_newton_secant.py` | `Task_11_newton_secant_extended.py` |
| 12 | Polynomial and Nonlinear Equation Solving | [Doc](docs/Task_12.md) | `Task_12_nonlinear_equations.py` | `Task_12_nonlinear_equations_extended.py` |
| 13 | Interpolation | [Doc](docs/Task_13.md) | `Task_13_interpolation.py` | `Task_13_interpolation_extended.py` |
| 14 | Curve Fitting and Approximation | [Doc](docs/Task_14.md) | `Task_14_curve_fitting.py` | `Task_14_curve_fitting_extended.py` |
| 15 | Numerical Differentiation | [Doc](docs/Task_15.md) | `Task_15_numerical_differentiation.py` | `Task_15_numerical_differentiation_extended.py` |
| 16 | Numerical Integration | [Doc](docs/Task_16.md) | `Task_16_numerical_integration.py` | `Task_16_numerical_integration_extended.py` |
| 17 | Ordinary Differential Equations – Euler Method | [Doc](docs/Task_17.md) | `Task_17_euler_ode.py` | `Task_17_euler_ode_extended.py` |
| 18 | Numerical Solution of ODEs Using SciPy | [Doc](docs/Task_18.md) | `Task_18_scipy_ode.py` | `Task_18_scipy_ode_extended.py` |
| 19 | Numerical Optimization | [Doc](docs/Task_19.md) | `Task_19_optimization.py` | `Task_19_optimization_extended.py` |
| 20 | Random Numbers and Monte Carlo Methods | [Doc](docs/Task_20.md) | `Task_20_monte_carlo.py` | `Task_20_monte_carlo_extended.py` |

## How to run

```bash
pip install -r requirements.txt
cd code
python Task_02_numpy_arrays.py
python Task_02_numpy_arrays_extended.py
```

Scripts that draw graphs also save them in `outputs/` (run from inside the `code` folder). Timing results (Tasks 3 and 7) depend on the computer.

Notes: `np.trapezoid` needs NumPy 2.x, so Task 16 falls back to `np.trapz` on older NumPy. In Task 13 the 10-minute time list is trimmed so it never goes past the last measurement (14:00), which `interp1d` would reject.
