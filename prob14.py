import control
import matplotlib.pyplot as plt
import scipy

num = [1]
denum = [1, 10, 100]
GH = control.tf(num, denum)
print(GH)
rlist, klist = control.rlocus(GH)
plt.show()
