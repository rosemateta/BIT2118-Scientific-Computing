# Task 11: Root Finding: Newton-Raphson and Secant Methods

**Application:** Interest rates, finance

## 1. Original program (`code/Task_11_newton_secant.py`)

### Inputs and mathematical operation

**Inputs:** cash flows [−10000, 3000, 3500, 4000, 2500] and starting guesses.

**Operation:** find the rate r where NPV(r) = 0 (the Internal Rate of Return). Newton uses the derivative of NPV; secant uses two guesses and no derivative.

### Output

```
IRR using Newton-Raphson: 11.542461%
IRR using Secant method: 11.542461%
NPV at Newton solution: 0.000000
Newton iterations: 4, Secant iterations: 7
```

### Meaning of the output

The project earns an annual return of 11.54%. Both methods agree and NPV at that rate is 0. If the required return is below 11.54% the project is worth doing.

## 2. Changing a parameter (`code/Task_11_newton_secant_extended.py`, Part A)

I raised the initial investment from 10,000 to 12,000. The IRR fell from 11.54% to 3.33%. A higher cost with the same income gives a smaller return. Newton used 4–5 steps and secant 7, showing Newton converges faster when the derivative is available.

## 3. New real-world case: Interest rate of a loan (Part B of the same file)

### Assumptions and input data

A customer borrows KES 100,000 and repays KES 9,000 monthly for 12 months.

### Output

```
PART A: IRR when investment rises
Investment 10000: IRR Newton=11.5425% (4 its), Secant=11.5425% (7 its)
Investment 12000: IRR Newton=3.3298% (5 its), Secant=3.3298% (7 its)

PART B: loan interest rate
Monthly rate Newton=1.2043%, Secant=1.2043%
Nominal annual rate = 14.45%, effective annual = 15.45%
Total repaid = KES 108,000, interest paid = KES 8,000
```

### Interpretation

The monthly rate is 1.2043%, which is 14.45% nominal per year or 15.45% effective. The customer pays KES 8,000 interest in total. This reveals the real cost of the loan.
