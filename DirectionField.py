import numpy as np
import matplotlib.pyplot as plt
import math

t_min = -10
t_max = 10
y_min = -10
y_max = 10
t_freq = 20
y_freq = 10
t,y = np.meshgrid(np.linspace(t_min,t_max,t_freq), np.linspace(t_min,t_max,y_freq))

u = -t+y
v = -y
N = np.sqrt((u)**2 + v**2)
u = u/N 
v = v/N

fig = plt.figure(figsize=(8, 8))
plt.xlim(t_min,t_max)
plt.ylim(t_min, t_max)
plt.xlabel('y')
plt.ylabel('v')
plt.quiver(t, y, u, v)
plt.show()