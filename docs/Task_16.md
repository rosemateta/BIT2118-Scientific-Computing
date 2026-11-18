# Task 16: Numerical Integration

**Application:** Energy, total flow

## 1. Original program (`code/Task_16_numerical_integration.py`)

### Inputs and mathematical operation

**Inputs:** power (kW) read every 2 hours for 12 hours.

**Operation:** area under the power curve with the trapezoidal rule (straight lines) and Simpson's rule (parabolas).

### Output

```
Energy using trapezoidal rule: 15.700 kWh
Energy using Simpson's rule: 15.800 kWh
Difference between estimates: 0.100 kWh
```

### Meaning of the output

The home used about 15.7 kWh (trapezoid) or 15.8 kWh (Simpson) in 12 hours. The 0.1 kWh difference is just the numerical method; the values agree closely.

## 2. Changing a parameter (`code/Task_16_numerical_integration_extended.py`, Part A)

I tested accuracy on sin(x) from 0 to π (exact 2) using 5, 9 and 33 points. Trapezoid error fell from 1.0e-1 to 1.6e-3 and Simpson error from 4.6e-3 to 1.0e-6. More points help both, and Simpson is much more accurate for smooth data.

## 3. New real-world case: Water pumped from a borehole (Part B of the same file)

### Assumptions and input data

Flow (L/s) every 10 minutes for 1 hour: 2.0, 2.4, 2.9, 3.0, 2.6, 2.1, 1.8.

### Output

```
PART A: accuracy against number of points (exact value 2)
n= 5: trapezoid error=1.04e-01, Simpson error=4.56e-03
n= 9: trapezoid error=2.58e-02, Simpson error=2.69e-04
n=33: trapezoid error=1.61e-03, Simpson error=1.03e-06

PART B: borehole water volume
Trapezoidal: 8,940 litres
Simpson    : 8,960 litres
Average flow = 2.483 L/s
```

### Interpretation

About 8,940–8,960 litres in the hour (average flow 2.48 L/s). The two rules agree within 0.2%, so the estimate is reliable.
