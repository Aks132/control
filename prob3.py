#simple poles and zeros
import control
import matplotlib.pyplot as plt

num = [ 6, 36, 48]
den = [1,8,15,0]

#Creating a transfer function G = num/den
G = control.tf(num,den) 

control.pzmap(G)
plt.grid(True)
plt.title('poles and zeros')
plt.xlabel('Y')
plt.ylabel('X')
plt.show()

