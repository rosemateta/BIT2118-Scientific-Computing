# Task 20: Random Numbers and Monte Carlo Methods

**Application:** Risk analysis

## 1. Original program (`code/Task_20_monte_carlo.py`)

### Inputs and mathematical operation

**Inputs:** capacity 1000, demand normal with mean 850 and standard deviation 120, N = 100,000 simulations.

**Operation:** generate random demands and count the fraction above capacity.

### Output

```
Estimated overload probability: 10.6160%
Number of overload cases: 10616 out of 100000
```

### Meaning of the output

The estimated overload probability is 10.62% (10,616 overloads in 100,000). The graph starts noisy and then settles at about 10.6%, which shows that Monte Carlo converges as N grows.

![graph](../outputs/task_20_monte_carlo.png)

## 2. Changing a parameter (`code/Task_20_monte_carlo_extended.py`, Part A)

I changed N and the spread. With N = 1,000 the estimate was 10.10%; with N = 100,000 it was 10.62% (exact about 10.57%). With std = 200 the risk rose to 22.60%. More simulations give a steadier estimate, and more variability gives more risk.

## 3. New real-world case: Software project deadline risk (Part B of the same file)

### Assumptions and input data

Three tasks one after another with normal durations: design 10±2, coding 15±4, testing 7±2 days. The deadline is 35 days. 200,000 simulations.

### Output

```
PART A: overload probability (exact value for std=120 is about 10.57%)
N=  1,000, std=  120: P(overload)=10.100%
N=100,000, std=  120: P(overload)=10.616%
N=100,000, std=  200: P(overload)=22.602%

PART B: project deadline risk
Average total duration: 32.01 days
P(finish after 35 days) = 27.11%
90% of simulations finish within 38.3 days
```

### Interpretation

The average total is 32.0 days. The chance of finishing after 35 days is about 27.1%. In 90% of simulations the project is done within 38.3 days, so promising 35 days is risky; a safer promise would be about 38–39 days.
