from __future__ import print_function

import numpy as np
from scipy.integrate import simps
from scipy.integrate import cumtrapz
from numpy import trapz
import matplotlib.pyplot as plt
nm  = ['testlogs/wodometry_test_first30',
        'testlogs/wodometry_test_second30',
        'testlogs/wodometry_test_third30slow',
        'testlogs/wodometry_test_fourth30slowfast',
        'testlogs/wodometry_test_fifth30fast',
        'testlogs/wodometry_test_sixth90normal']

f=open(nm[0],"r")
lines=f.read().splitlines() 
tid=[]
wh1=[]
wh2=[]
interval = 0
d = 0.00
for x in lines:
    n = float((x.split(' ')[4]).split(':')[1])
    w1 = float((x.split(' ')[0]).split(':')[1])
    w2 = float((x.split(' ')[1]).split(':')[1])
    if n - d > interval:
        tid.append(n*1e-3)
        wh1.append(w1/3.6)
        wh2.append(w2/3.6)
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
print("distance cumtrapz integral wh1 =", dist_cumtrapz1[-1])
print("distance cumtrapz integral wh2 =", dist_cumtrapz2[-1])

#scipys simps
dist_simps1 = simps(wh1, tid)
dist_simps2 = simps(wh2, tid)
print("distance simps integral wh1 =", dist_simps1)
print("distance simps integral wh2 =", dist_simps2)

plt.subplot(2,1,1)
plt.plot(tid, dist_cumtrapz1, 'r-', tid, dist_cumtrapz2, 'b-')
plt.grid()
plt.subplot(2,1,2)
plt.plot(tid, wh1, 'g--', tid, wh2, 'r--')
plt.grid()
plt.show()
