from __future__ import print_function

import numpy as np
from scipy.integrate import simps
from numpy import trapz

f=open('ard.log',"r")
lines=f.read().splitlines() 
tid=[]
wh1=[]
wh2=[]
interval = 0.1
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

dist_trapz1 = trapz(tid, wh1)
dist_trapz2 = trapz(tid, wh2)
print("distance trapz integral wh1 =", dist_trapz1)
print("distance trapz integral wh2 =", dist_trapz2)

dist_simps1 = simps(tid, wh1)
dist_simps2 = simps(tid, wh2)
print("distance simps integral wh1 =", dist_simps1)
print("distance simps integral wh2 =", dist_simps2)
