#Euler's Method
import numpy as np
import matplotlib.pyplot as plt
import math

t0 = 1
y0 = 1
t_spacing = 0.2
n = 10
t_sol = []
y_sol = []

def model(t, y):
    dydt = (t*t-y)/(y-2*t)
    return dydt

def methd(t,y):
    m1 = model(t,y)
    #print(m1)
    y += t_spacing*m1
    t += t_spacing
    return [t,y]

i = 0
y = y0
t = t0
y_max = y0
y_min = y0
while i < n :
    #init values
    result = methd(t,y)
    t = result[0]
    y = result[1]
    y_sol.append(y)
    t_sol.append(t)
    if(y > y_max):
        y_max = y
    if(y < y_max):
        y_max = y

    print("t,Y",result)
    i += 1

#print(t_sol, y_sol)
fig = plt.figure(figsize=(8, 8))
plt.scatter( t_sol,y_sol)
plt.plot(t_sol, y_sol)
#plt.xlim(t0 - 5, t0+t_spacing*n + 5)
#plt.ylim(y_min - 5, y_max + 5)
plt.xlabel('t')
plt.ylabel('y')
plt.show()