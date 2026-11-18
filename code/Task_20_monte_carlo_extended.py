"""Task 20 extended: (A) change N and the spread, (B) new case: finishing a project on time."""
import numpy as np

# ---------- PART A: change N and standard deviation ----------
print("PART A: overload probability (exact value for std=120 is about 10.57%)")
for N, std in ((1_000, 120.0), (100_000, 120.0), (100_000, 200.0)):
    rng = np.random.default_rng(42)
    d = rng.normal(850.0, std, N)
    print(f"N={N:>7,}, std={std:>5.0f}: P(overload)={np.mean(d > 1000.0):.3%}")

# ---------- PART B: new case ----------
# Assumptions: a software project has three tasks done one after another.
# Durations (days) are normal: design 10 +/- 2, coding 15 +/- 4, testing 7 +/- 2.
# The client deadline is 35 days. Estimate the probability of missing it.
rng = np.random.default_rng(7)
N = 200_000
total = rng.normal(10, 2, N) + rng.normal(15, 4, N) + rng.normal(7, 2, N)
late = total > 35
print("\nPART B: project deadline risk")
print(f"Average total duration: {total.mean():.2f} days")
print(f"P(finish after 35 days) = {late.mean():.2%}")
print(f"90% of simulations finish within {np.percentile(total, 90):.1f} days")
