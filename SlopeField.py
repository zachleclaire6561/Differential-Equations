import numpy as np
import matplotlib.pyplot as plt
import math

t_min = -5
t_max = 5
y_min = -5
y_max = 5
t_freq = 30
y_freq = 30
t,y = np.meshgrid(np.linspace(t_min,t_max,t_freq), np.linspace(t_min,t_max,y_freq))

u = -t+y
v = -y


fig = plt.figure(figsize=(8, 8))
plt.xlim(t_min,t_max)
plt.ylim(t_min, t_max)
plt.xlabel('t')
plt.ylabel('y')
plt.quiver(t, y, u, v)
plt.show()