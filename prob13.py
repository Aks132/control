import control
import matplotlib.pyplot as plt
import scipy

num = [1]
denum = [1,8,29,52,0]
GH = control.tf(num, denum)
print(GH)
rlist, klist = control.rlocus(GH)
plt.show()
