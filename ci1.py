"""
**Importing Libraries**
"""

import numpy as np

"""Performing fuzzy operations on fuzzy sets"""

def union(A, B):
  return np.maximum(A, B)

def intersection(A, B):
  return np.minimum(A, B)

def complement(A):
  return 1 - A

def difference(A, B):
  return np.maximum(A - B, 0)

"""Defining fuzzy sets"""

A = np.array([0.2, 0.4, 0.6, 0,8])
B = np.array([0.3, 0.5, 0,7, 0.9])

print("Union of A and B:", union(A, B))
print("Intersection of A and B:", intersection(A, B))
print("Difference of A and B:", difference(A, B))
print("Complement of A:", complement(A))

"""Creating fuzzy relations"""

def cartesian_product(A, B):
  return np.outer(A, B)

"""Performing min-max composition on fuzzy relations"""

def max_min_composition(R1, R2):
  return np.maximum(np.minimum(R1, R2),0)

R1 = cartesian_product(A, B)
R2 = cartesian_product(B, A)
result = max_min_composition(R1, R2)

print(f"Cartesian product of A and B:\n{R1}")
print(f"Cartesian product of B and A:\n{R2}")
print(f"Min-max composition of R1 and R2:\n{result}")
