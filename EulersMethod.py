#Euler's Method For Systems Of Diff Eqs
import numpy as np
import matplotlib.pyplot as plt
import math

t0 = 0
x0 = 1
y0 = 1
t_spacing = 0.5
n = 15
x_sol = []
y_sol = []

def model(t, x, y):
    dxdt = -y
    dydt = x
    return [dxdt, dydt]

def methd(t,y,x):
    sys_model = model(t,x,y)
    print(sys_model)
    x += t_spacing*sys_model[0]
    y += t_spacing*sys_model[1]
    t += t_spacing
    return [t,x,y]

i = 0
x = x0
y = y0
t = t0
x_max, y_max = x0, y0
x_min, y_min = x0, y0
while i < n :
    #init values
    result = methd(t,y,x)
    t = result[0]
    x = result[1]
    y = result[2]
    x_sol.append(x)
    y_sol.append(y)

    if(x > x_max):
        x_max = x
    if(x < x_min):
        x_min = x
    if(y > y_max):
        y_max = y
    if(y < y_max):
        y_max = y

    print("X,Y",result)
    i += 1

print(x_sol, y_sol)
fig = plt.figure(figsize=(8, 8))
plt.plot(x_sol, y_sol)
plt.xlim(x_min - 5, x_max + 5)
plt.ylim(y_min - 5, y_max + 5)
plt.xlabel('t')
plt.ylabel('y')
plt.show()