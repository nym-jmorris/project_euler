'''
We create an array of points in a two dimensional plane using the following random number generator:

s0 = 290797
sn+1 = sn**2 mod 50515093

Let d(k) be the shortest distance of any two (distinct) points among P0...Pk-1.
E.g.
d(14) == 546446.466846479

Find d(2 000 000)
. Give your answer rounded to places after the decimal point.

solution is available here: 
https://www.ivl-projecteuler.com/overview-of-problems/5-difficulty/problem-816

Need an optimized function for computing min dist.  

'''

points = []
points.append(290797)

def makePoint(point):
    points.append(point**2 % 50515093)

# for i in range(1,4000000):
pcount = 28000
for i in range(1,pcount):
    makePoint(points[i-1])

# for i in range(0,len(points),2):
#     print('S_{}: {} '.format(i,points[i]))
#     print('S_{}: {} '.format(i+1,points[i+1]))
#     print('({},{})\n'.format(points[i],points[i+1]))

from math import sqrt

def distance(x1,y1,x2,y2):
    dist = sqrt((x2-x1)**2+(y2-y1)**2)
    return dist

# points.clear()
# points = [1,1,4,4]
mindist = []
for i in range (0,len(points),2):
    for j in range (i,len(points),2):
        dist = distance(points[i],points[i+1],points[j],points[j+1])
        
        if dist != 0: 
            mindist.append(dist)
            # print('x1: {}, y1: {}, x2: {}, y2: {}, d: {}'.format(points[i],points[i+1],points[j],points[j+1],dist))

print('Min distance inside a cloud of {} points is {}.'.format(int(pcount/2),min(mindist)))