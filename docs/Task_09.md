# Task 9: Eigenvalues and Eigenvectors

**Application:** PageRank, network centrality

## 1. Original program (`code/Task_09_eigenvalues.py`)

### Inputs and mathematical operation

**Input:** the 4×4 adjacency matrix of a network (1 = link).

**Operations:** `np.linalg.eig` finds all eigenvalues and eigenvectors; the largest eigenvalue's eigenvector, made positive and scaled to sum to 1, is the importance score. Av = λv is checked.

### Output

```
All eigenvalues: [ 2.5616 -0.     -1.5616 -1.    ]
Dominant eigenvalue: 2.561552812808829
Eigenvector-based importance:
A: 0.2192
B: 0.2808
C: 0.2808
D: 0.2192
Verification error: 1.5059797815742444e-15
```

### Meaning of the output

The largest eigenvalue is 2.5616. B and C score 0.2808 each (most important, 3 links each) and A and D score 0.2192 (2 links each). The verification error is about 1e-15, so Av = λv holds.

## 2. Changing a parameter (`code/Task_09_eigenvalues_extended.py`, Part A)

I added the missing link A–D. The dominant eigenvalue rose from 2.5616 to 3.0 and all four nodes became equal (0.25 each), because every node now links to the other three. More connections increase the dominant eigenvalue.

## 3. New real-world case: Friendship network of 5 students (Part B of the same file)

### Assumptions and input data

Ann is friends with everyone, Brian–Cate are friends, Dan–Eve are friends (symmetric 5×5 matrix).

### Output

```
PART A: original network
Dominant eigenvalue: 2.5616
  A: 0.2192
  B: 0.2808
  C: 0.2808
  D: 0.2192
After adding link A-D (all nodes now equal):
Dominant eigenvalue: 3.0000
  A: 0.2500
  B: 0.2500
  C: 0.2500
  D: 0.2500

PART B: friendship network
Dominant eigenvalue: 2.5616
  Ann: 0.2808
  Brian: 0.1798
  Cate: 0.1798
  Dan: 0.1798
  Eve: 0.1798
```

### Interpretation

Ann scores 0.2808 and the others 0.1798 each, so Ann is the most influential student, as she is the connection between the two pairs.
