"""Task 6 extended: (A) change totals, (B) new case: electrical circuit currents."""
import numpy as np

# ---------- PART A: change the observed usage ----------
A = np.array([[4., 2.], [8., 12.]])
print("PART A: different observed totals")
for b in ([20., 72.], [26., 96.]):               # CHANGE: second case has higher usage
    x = np.linalg.solve(A, np.array(b))
    print(f"Totals {b} -> Type A={x[0]:.3f}, Type B={x[1]:.3f}")
print("Singular example (second row = 2 x first row):")
try:
    print(np.linalg.solve(np.array([[4., 2.], [8., 4.]]), np.array([20., 40.])))
except np.linalg.LinAlgError as e:
    print("Error:", e)

# ---------- PART B: new case ----------
# Assumptions: two-loop DC circuit. Loop 1 has a 12 V battery, R1=6, shared R2=4.
# Loop 2 has a 6 V battery (opposing), R3=5 and the shared R2=4. Resistances in ohms.
# Kirchhoff voltage law:
#   (6+4) I1 - 4 I2 = 12
#   -4 I1 + (5+4) I2 = -6
R_matrix = np.array([[10., -4.], [-4., 9.]])
volts = np.array([12., -6.])
I = np.linalg.solve(R_matrix, volts)
print("\nPART B: circuit loop currents")
print(f"I1 = {I[0]:.4f} A, I2 = {I[1]:.4f} A")
print(f"Current through shared resistor = {I[0]-I[1]:.4f} A")
print("Residual:", volts - R_matrix @ I)
