#Improved Euler's Method
import numpy as np
import matplotlib.pyplot as plt
import math

t0 = 1
y0 = 1
t_spacing = 0.003125
n = 640
t_sol = []
y_sol = []

def model(t, y):
    dydt = (t*t-y)/(y-2*t)
    return dydt

def methd(t,y):
    m1 = model(t,y)
    m2 = model(t+t_spacing,y+t_spacing*m1)
    #print(m1)
    y += t_spacing*(m1+m2)/2
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

    #print("t,Y",result)
    i += 1

x = 0
while x < 8:
    i = 0
    y = y0
    t = t0
    y_max = y0
    y_min = y0
    t_spacing = 1/(5*pow(2,x))
    n = 10*pow(2,x)
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

        i += 1
    print(result[1])
    print(type(result[1]))
    x+=1

#print(t_sol, y_sol)
fig = plt.figure(figsize=(8, 8))
plt.scatter( t_sol,y_sol)
plt.plot(t_sol, y_sol)
#plt.xlim(t0 - 5, t0+t_spacing*n + 5)
#plt.ylim(y_min - 5, y_max + 5)
plt.xlabel('t')
plt.ylabel('y')
#plt.show()