#Finding TF
import control
import matplotlib.pyplot as plt
import scipy

z = [-1,-5]
p = [0,-3,-4,-7]
k = [5]

[num,den]= scipy.signal.zpk2tf(z,p,k)
#Creating a transfer function G = num/den
G =control.tf(num,den)
print(G)

