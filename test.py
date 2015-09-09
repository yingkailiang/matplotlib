from mpl_toolkits.mplot3d import Axes3D
from random import randint
import numpy as np
import matplotlib.pyplot as plt
import math

#generate d dimensional random number array
def genRand(d):
    result=[] 
    for i in range(0,d):
  	r = randint(1,100)
        result.append(r)
 	#print "random number ",i,": ",r
    return result

#p, q are coordinate array, d is the number of dimension 
def euclideanDistance(p,q,d):
    innerSum = 0
    for i in range(0,d):
        innerSum = innerSum + (p[i] - q[i])*(p[i] - q[i])
    return math.sqrt(innerSum)

#max from array
def maxInArray(a):
    result = a[0] 
    for ai in a:
	if result < ai:
	    result = ai	
    return result

#max from array
def minInArray(a):
    result = a[0] 
    for ai in a:
	if result > ai:
	    result = ai	
    return result

#compute the variance
def gema(maxv,minv):
    tmp = (maxv-minv)/minv 
    return math.log(tmp,2)

#main function start here: 
d = 100
n = 100
distance=[]
for i in range (0,n):
    point1 = genRand(d)
    point2 = genRand(d)
    distance.append(euclideanDistance(point1,point2,d))
variance = gema(maxInArray(distance),minInArray(distance))

fig = plt.figure()
ax = fig.gca(projection='3d')
colors = ('r', 'g', 'b', 'k')
for c in colors:
    #x = np.random.sample(20)
    #y = np.random.sample(20)
    x = d 
    y = n  
    z = variance 
    #print "X:",x,",Y:",y 
    #ax.scatter(x, y, 0, zdir='y', c=c)
    ax.scatter(x, y, z, zdir='y', c=c)
ax.legend()
ax.set_xlim3d(0, 1000)
ax.set_ylim3d(0, 1000)
ax.set_zlim3d(0, 1000)

plt.show()
