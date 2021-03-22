import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def model(R,F):
    dF = 2*R -1.2 * R * F
    dR = -F + 0.9 * R * F
    return [dR, dF]

#Graph bounds
t_min, t_max = -10, 10
y_min, y_max = -10, 10
sols = []
y = []
t0 = [0, 0, 0, 0]
R0 = [0.5, 0, 0, 0]
F0 = [0.5, 0, 0, 0]
#t0 = [0]
#y0 = [3]

i = 0
while i < len(F0):
    y.append((solve_ivp(model, [t0[i], t_max], [R0[i], F0[i]])).sol(np.linspace(t0[i], t_min)))
    i+=1

fig = plt.figure(figsize=(8, 8))
plt.xlim(t_min,t_max)
plt.ylim(y_min, y_max)
plt.xlabel('t')
plt.ylabel('y')

i = 0
while i < len(y0) :
    plt.plot(np.linspace(t0[i],t_max), y[i])
    i += 1
#for y_sol in y: 
#    plt.plot(np.linspace(t0,t_max), y_sol)
plt.show()