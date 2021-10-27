
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt 

a = np.array([[1, 1], [0, 0]])
b = np.array([[0], [1]])
c = np.array([[1, 0]])
d = np.array([[0]])


sys = signal.StateSpace(a, b, c, d)
print(sys)

t = np.linspace(0, 1.25, 500, endpoint=False)
u = 1 * t


tout, yout, xout = signal.lsim((a,b,c,d), U=u, T=t)

plt.plot(t, u, 'r', alpha=0.5, linewidth=1, label='input')
plt.plot(tout, yout, 'k', linewidth=1.5, label='output')
plt.legend(loc='best', shadow=True, framealpha=1)
plt.grid(alpha=0.3)
plt.xlabel('t')
plt.show()