import numpy as np
p = np.poly1d([1, 15, -23, 105])
print(p)
rootsp = p.r
print("\nRoots of Polynomials is :", rootsp)
print("\nEvaluating polynomial at x=2:)", p(2))
print("\nCo-efficient of polynomial:", p.c)
