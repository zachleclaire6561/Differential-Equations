'''
Solves for systems of differential equations
Refernce: https://apmonitor.com/pdc/index.php/Main/SolveDifferentialEquations
'''
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

def func(z, t):
    x = z[0]
    y = z[1]
    dxdt = 2
    dydt = y*y
    return [dxdt, dydt]

z0 = [100,-1]
# n = # points
n = 300
t = np.linspace(0, 15, n)
x = np.empty_like(t)
y = np.empty_like(t)

x[0] = z0[0]
y[0] = z0[1]

z = odeint(func, z0, t)
x = z[0]
y = z[1]
'''
for i in range(1,300):
    tspan = [t[i-1], t[i]]
    #solve
    #next init condition
    z0 = z
    print(z)

print(z)
'''
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Example Systems')
plt.show()
