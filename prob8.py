import numpy as np
import sympy as sym
import control as ct
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

Gp = ct.tf(10,[1,7,10])
ts = 1
Gz =ct.sample_system(Gp, ts)
sym.pprint(Gz)


t = np.linspace(0,14*ts,num=15)

#remove comment in which you want to display
T, yout = ct.impulse_response(Gz, t) 
#R, yout = ct.step_response(Gz, t)

yout=yout.flatten()

fig, ax = plt.subplots()
ax.step(T, yout)
#ax.step(R, yout)
ax.yaxis.set_minor_locator(MultipleLocator(0.05))
ax.yaxis.set_major_locator(MultipleLocator(0.1))
plt.margins(0.1, 0.1)
plt.title('Impulse Response c.1)')
plt.xlabel('Time [sec]')
plt.ylabel('Amplitude')
plt.grid(True) 
plt.show()
