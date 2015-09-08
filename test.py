from mpl_toolkits.mplot3d import Axes3D
from random import randint
import numpy as np
import matplotlib.pyplot as plt
import math

#generate n dimensional random number array
def genRand(n):
    result=[] 
    for i in range(0,n):
  	r = randint(1,100)
        result.append(r)
 	print "random number ",i,": ",r
    return result

#p, q are coordinate array, n is the number of dimension 
def euclideanDistance(p,q,n):
    innerSum = 0
    for i in range(0,n):
        innerSum = innerSum + (p[i] - q[i])*(p[i] - q[i])
    return math.sqrt(innerSum)

genRand(5)
fig = plt.figure()
ax = fig.gca(projection='3d')

colors = ('r', 'g', 'b', 'k')
for c in colors:
    #x = np.random.sample(20)
    #y = np.random.sample(20)
    x = 200
    y = 200
    z = 200
    #print "X:",x,",Y:",y 
    #ax.scatter(x, y, 0, zdir='y', c=c)
    ax.scatter(x, y, z, zdir='y', c=c)
ax.legend()
ax.set_xlim3d(0, 1000)
ax.set_ylim3d(0, 1000)
ax.set_zlim3d(0, 1000)

plt.show()
