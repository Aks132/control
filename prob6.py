from numpy.linalg import eig
import numpy as np
a=np.array([[4,-1,5],[2,1,3],[6,-7,9]])
values , vectors = eig(a)
print("Eigen Values:",values)
print("Eigen Vectors",vectors)
