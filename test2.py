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

#hamming distance, p, q are coordinate array, d is the number of dimension 
def hammingDistance(p,q,d):
    innerSum = 0
    for i in range(0,d):
	innerSum= abs(p[i]-q[i]) 
    return innerSum
#euclidean Distance, p, q are coordinate array, d is the number of dimension 
def euclideanDistance(p,q,d):
    innerSum = 0
    for i in range(0,d):
        innerSum = innerSum + (p[i] - q[i])*(p[i] - q[i])
    #print "eu distance: ",math.sqrt(innerSum)
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
    if minv==0:
	#print "minv is zero"
        return 9999999
    tmp = (maxv-minv)/minv 
    #print "max:",maxv,"minv:",minv,"tmp: ",tmp
    return math.log(tmp,2)

#main function start here: 
fig = plt.figure()
ax = fig.gca(projection='3d')
for d in range (1,101): 
    for n in range (100,1001):
	distance=[]
	for i in range (0,n):
    	    point1 = genRand(d)
            #print "point1, x: ",point1[0]
            point2 = genRand(d)
            #print "point2, x: ",point2[0]
            distance.append(hammingDistance(point1,point2,d))
        variance = gema(maxInArray(distance),minInArray(distance))
        x = d 
        y = n  
        z = variance 
        ax.scatter(x, y, z, zdir='y', c='b')
        print "d:",d,"n:",n
ax.legend()
ax.set_xlim3d(0, 100)
ax.set_ylim3d(0, 1000)
ax.set_zlim3d(0, 900)
plt.show()
