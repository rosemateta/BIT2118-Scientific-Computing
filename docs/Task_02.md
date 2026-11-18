# Task 2: NumPy Arrays and Numerical Computation

**Application:** IoT sensor readings

## 1. Original program (`code/Task_02_numpy_arrays.py`)

### Inputs and mathematical operation

**Inputs:** 24 hourly temperatures in °C stored in one NumPy array.

**Operations:** mean (add all values, divide by 24), minimum, maximum, and the vectorized conversion F = 1.8C + 32 applied to the whole array at once.

### Output

```
Daily mean temperature: 23.12 C
Minimum temperature: 17.50 C
Maximum temperature: 29.40 C
First six Fahrenheit readings: [65.3  64.4  64.04 63.5  64.22 66.2 ]
```

### Meaning of the output

The daily mean of 23.12 °C is the typical temperature of the day. The minimum (17.50 °C) happens in the early morning and the maximum (29.40 °C) in the early afternoon. The Fahrenheit values (65.3, 64.4, ...) are the same readings in another unit.

## 2. Changing a parameter (`code/Task_02_numpy_arrays_extended.py`, Part A)

I changed the 13:00 reading from 29.4 °C to 40 °C (a heat spike). The mean rose from 23.12 °C to 23.56 °C and the maximum rose from 29.40 °C to 40.00 °C. One value changes the mean only slightly (it is shared among 24 values) but it fully controls the maximum.

## 3. New real-world case: Weekly rainfall at a farm (Part B of the same file)

### Assumptions and input data

A rain gauge gives one reading per day for 7 days (mm). Values: 0, 12.5, 3.2, 0, 25.4, 8.1, 0. Millimetres are converted to inches by dividing by 25.4.

### Output

```
PART A: original vs heat spike
Original: mean=23.12 C, max=29.40 C
Changed : mean=23.56 C, max=40.00 C

PART B: weekly rainfall
Total rainfall   : 49.2 mm (1.94 in)
Average per day  : 7.03 mm
Wettest day      : day 5 with 25.4 mm
Days with rain   : 4
```

### Interpretation

The farm got 49.2 mm (1.94 in) in the week, an average of 7.03 mm per day. Day 5 was the wettest (25.4 mm) and it rained on 4 of 7 days, so rain was uneven: most of the water came in a few days.
