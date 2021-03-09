import numpy as np
import matplotlib.pyplot as plt
from random import random
from math import sqrt

# # evenly sampled time at 200ms intervals
# t = np.arange(0., 5., 0.2)


# # red dashes, blue squares and green triangles
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.show()

x = 0
y = 0

xcoords = [x]
ycoords = [y]

for i in range(0,100000):
    if random()-0.5 < 0:
        x +=1
    else: x -= 1
    if random()-0.5 <0:
        y += 1
    else: y -= 1
    xcoords.append(x)
    ycoords.append(y)

maxx = max(max(xcoords),abs(min(xcoords)))
maxy = max(max(ycoords),abs(min(ycoords)))

dist = sqrt(maxx**2 + maxy**2)
print(dist)

plt.plot(xcoords,ycoords,'c--')
plt.axis([-round(dist),round(dist), -round(dist),round(dist)])
plt.show()
