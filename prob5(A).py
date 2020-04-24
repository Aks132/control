import numpy as np
p = np.poly1d([1, -2, 9])
print(p)
rootsp = p.r
print("\nEvaluating polynomial at s=5:)", p(5))
