# Task 5: Matrix Algebra and Matrix Operations

**Application:** Computer graphics

## 1. Original program (`code/Task_05_matrix_algebra.py`)

### Inputs and mathematical operation

**Inputs:** the 4 corners of a unit square, a 45° rotation matrix and a scaling matrix (x × 2, y × 1.5).

**Operations:** matrix product `rotation @ scale`, then every point is multiplied by the combined matrix, and the determinant is calculated.

### Output

```
Original points:
 [[0. 0.]
 [1. 0.]
 [1. 1.]
 [0. 1.]]
Transformation matrix:
 [[ 1.41421356 -1.06066017]
 [ 1.41421356  1.06066017]]
Transformed points:
 [[ 0.          0.        ]
 [ 1.41421356  1.41421356]
 [ 0.35355339  2.47487373]
 [-1.06066017  1.06066017]]
Determinant: 2.9999999999999996
```

### Meaning of the output

The transformed corners show the square turned into a stretched, tilted parallelogram. The determinant 3.0 is the factor by which area grows (2 × 1.5 = 3). A non-zero determinant means the transformation can be reversed.

## 2. Changing a parameter (`code/Task_05_matrix_algebra_extended.py`, Part A)

I changed the angle from 45° to 90° and the scale from (2, 1.5) to (3, 1). The square is now turned a quarter-turn and stretched to 3 units. The determinant became 3.0 (rotation does not change area, scaling by 3×1 multiplies it by 3).

## 3. New real-world case: Shrinking, rotating and moving a triangle logo (Part B of the same file)

### Assumptions and input data

Triangle corners in pixels (0,0), (40,0), (20,60). Shrink to 50%, rotate 30°, then move 100 px right and 50 px up. A move needs homogeneous coordinates (a 3×3 matrix).

### Output

```
PART A: 90-degree rotation with scale (3, 1)
Transformation:
 [[ 0. -1.]
 [ 3.  0.]]
Transformed square:
 [[ 0.  0.]
 [ 0.  3.]
 [-1.  3.]
 [-1.  0.]]
Determinant (area factor): 3.0

PART B: logo transformation
Original corners:
 [[ 0.  0.]
 [40.  0.]
 [20. 60.]]
New corners:
 [[100.    50.  ]
 [117.32  60.  ]
 [ 93.66  80.98]]
Area before: 1200.0  Area after: 300.0
```

### Interpretation

The new corners are (100, 50), (117.32, 60) and (93.66, 80.98). Area goes from 1200 to 300 px² (0.5 × 0.5 = 0.25 of the original), which matches the determinant of the 2×2 part. One combined matrix transformed all points consistently.
