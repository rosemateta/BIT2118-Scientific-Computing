# Task 3: Mathematical Functions and Vectorization

**Application:** Large datasets, simulations, signal processing

## 1. Original program (`code/Task_03_vectorization.py`)

### Inputs and mathematical operation

**Inputs:** 1,000,000 random latency values between 5 and 250 ms.

**Operations:** divide by 1000 (ms to s) and square. Done two ways: a Python `for` loop, and one NumPy expression. `timeit` measures the time of each.

### Output

```
First five squared latency values: [0.03787665 0.01266192 0.04637842 0.03092504 0.00078812]
Loop time: 0.3169 s
Vectorized time: 0.0053 s
Approximate speed-up: 59.3x
```

### Meaning of the output

The first values (for example 0.0379) are latency in seconds, squared. The timing lines show the main lesson: vectorized code gives the same answer as the loop but much faster, so it is the right choice for millions of values.

## 2. Changing a parameter (`code/Task_03_vectorization_extended.py`, Part A)

I changed the data size N from 1,000 to 100,000 to 1,000,000. The vectorized code was 19x, 13x and 70x faster than the loop. The speed-up is large for every size, because NumPy does the loop in fast compiled code. (Exact times differ from computer to computer.)

## 3. New real-world case: VAT and currency conversion on shop sales (Part B of the same file)

### Assumptions and input data

1,000,000 sales between KES 50 and KES 20,000. VAT is 16% and 1 USD = 129 KES (assumed fixed). Formula: total = price × 1.16, USD = total / 129.

### Output

```
PART A: speed-up for different sizes
N=    1,000: loop=0.00014s vectorized=0.000007s speed-up=19.3x
N=  100,000: loop=0.01406s vectorized=0.001085s speed-up=13.0x
N=1,000,000: loop=0.14752s vectorized=0.002112s speed-up=69.8x

PART B: VAT and currency conversion
First three prices (KES)     : [ 7553.79 12911.95 17123.32]
First three totals with VAT  : [ 8762.39 14977.87 19863.05]
First three totals (USD)     : [ 67.93 116.11 153.98]
Total sales incl. VAT        : KES 11,629,201,400
VAT collected                : KES 1,604,027,779
```

### Interpretation

All 1,000,000 totals were computed in a fraction of a second with three array lines. VAT collected is about KES 1.6 billion on sales of about KES 11.6 billion, which is exactly 16/116 of the VAT-inclusive total, as expected.
