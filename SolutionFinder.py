import numpy as np
import scipy.integrate as odeint
import matplotlib.pyplot as plt

def model(y, t): 
    return y

#Graph bounds
t_min, t_max = -10, 10
y_min, y_max = -10, 10
y = []
t0 = [1, 0, 0, 0]
y0 = [3, 0, 0, 0]
#t0 = [0]
#y0 = [3]

i = 0
while i < len(y0) :
    y.append(odeint.odeint(model, y0[i], np.linspace(t0[i], t_max)))
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