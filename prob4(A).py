import numpy as np
p = np.poly1d([1, 3, 5, 9, 8, 6, 4])
print(p)
rootsp = p.r
print("\nRoots of Polynomials is :", rootsp)
print("\nEvaluating polynomial at x=2:)", p(2))
print("\nCo-efficient of polynomial:", p.c)
