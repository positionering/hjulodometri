from __future__ import print_function

import numpy as np
from scipy.integrate import simps
from scipy.integrate import cumtrapz
from numpy import trapz
import matplotlib.pyplot as plt

f=open('ard.log',"r")
lines=f.read().splitlines() 
tid=[]
wh1=[]
wh2=[]
interval = 0
d = 0.00
for x in lines:
    n = float(x.split(' ')[0])
    w1 = float(x.split(' ')[1])
    w2 = float(x.split(' ')[2])
    if n - d > interval:
        tid.append(n)
        wh1.append(w1)
        wh2.append(w2)
    d = n
f.close()

#numpys trapz
dist_trapz1 = trapz(wh1,tid)
dist_trapz2 = trapz(wh2,tid)
print("distance trapz integral wh1 =", dist_trapz1)
print("distance trapz integral wh2 =", dist_trapz2)

#scipys trapz
dist_cumtrapz1 = cumtrapz(wh1, tid, initial=0)
dist_cumtrapz2 = cumtrapz(wh2, tid, initial=0)
print("distance cumtrapz integral wh1 =", dist_cumtrapz1)
print("distance cumtrapz integral wh2 =", dist_cumtrapz2)

#scipys simps
dist_simps1 = simps(wh1, tid)
dist_simps2 = simps(wh2, tid)
print("distance simps integral wh1 =", dist_simps1)
print("distance simps integral wh2 =", dist_simps2)

plt.plot(tid, dist_cumtrapz1, 'r-', tid, dist_cumtrapz2, 'b-', tid, wh1, 'g-', tid, wh2, 'w-')
plt.show()
