# Task 19: Numerical Optimization

**Application:** Cost reduction, resource allocation

## 1. Original program (`code/Task_19_optimization.py`)

### Inputs and mathematical operation

**Inputs:** costs 12 (Type A) and 18 (Type B), capacities 100 and 170, required capacity at least 1000.

**Operation:** `minimize` (SLSQP) minimizes 12x + 18y with the capacity constraint and x, y ≥ 0. Then whole-server combinations are tested.

### Output

```
Optimization success: True
Type A allocation: 0.000
Type B allocation: 5.882
Total capacity: 1000.00
Minimum planning cost: 105.88
Best nearby integer solution: (108, 0, 6, 1020)
```

### Meaning of the output

The cheapest plan uses 0 Type A and 5.882 Type B, with exactly 1000 capacity, and costs 105.88. With whole servers the best is 6 Type B servers (capacity 1020, cost 108).

## 2. Changing a parameter (`code/Task_19_optimization_extended.py`, Part A)

I changed the cost of Type B from 18 to 25. The best choice switched from all Type B (5.88 units, cost 105.88) to all Type A (10 units, cost 120). Type B was cheaper per capacity at 18 (0.106 per unit) but not at 25 (0.147 per unit, against 0.12 for A).

## 3. New real-world case: Cheapest chicken feed mix (Part B of the same file)

### Assumptions and input data

100 kg of mix from Feed A (KES 40/kg, 20% protein, 3000 kcal/kg) and Feed B (KES 55/kg, 35% protein, 2800 kcal/kg), at least 25 kg protein and 290,000 kcal.

### Output

```
PART A: cost B=18: A=0.000, B=5.882, cost=105.88, success=True
PART A: cost B=25: A=10.000, B=0.000, cost=120.00, success=True

PART B: cheapest feed mix
Success=True: Feed A=66.67 kg, Feed B=33.33 kg, cost=KES 4500.00
Protein=25.00 kg, energy=293,333 kcal
```

### Interpretation

Use 66.67 kg of A and 33.33 kg of B for the lowest cost, KES 4,500. Protein is exactly 25 kg (the limit) so that constraint is active; energy is 293,333 kcal, so it has some room.
