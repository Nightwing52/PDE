import math
import time
import matplotlib.pyplot as plt
import numpy as np

#basic relaxation method
def liebmann(n, u_0, u_l, err=.01):
    u_avg=(u_l+u_0)/2
    u=[u_0]+(n-2)*[u_avg]+[u_l] #initial guess
    
    while True: #relaxation
        s=0.0
        for i in range(1, n-1):
            u_old=u[i]
            u[i]=.5*(u[i+1]+u[i-1])
            s+=math.fabs((u[i]-u_old)/u_old)
        if s < err:
            break
        
    return u

#simple plot method; used to plot solutions
def graph(x, y, xlabel, ylabel):
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.plot(x, y)

n=100
t0=time.clock()
u=liebmann(n, 0.0, 1.0)
print(time.clock()-t0)
s=[x for x in range(n)]
graph(s, u, "s", "u")
plt.show()
