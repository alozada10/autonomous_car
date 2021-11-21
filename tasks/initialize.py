import numpy as np
import matplotlib.pyplot as plt

def initialize(sizeOfPlane,
               axis,
               roadPrecentage):
    initialPosition = []
    for velocity in axis:
        if velocity == 'x':
            position = [np.random.rand()*sizeOfPlane,(sizeOfPlane+(2*np.random.rand()-1)*np.random.rand()*sizeOfPlane*roadPrecentage)/2]
            initialPosition.append(position)
        elif velocity == 'y':
            position = [(sizeOfPlane+(2*np.random.rand()-1)*np.random.rand()*sizeOfPlane*roadPrecentage)/2,np.random.rand() * sizeOfPlane]
            initialPosition.append(position)
    return np.asarray(initialPosition)

'''
#Test
procent = 0.2 # how wide the width of the road is
road = 200 #plane size with a height
v0 = ['x','y','x']
x0 = initialize(road,v0,procent)

plt.scatter(x0[:,0],x0[:,1])
plt.xlim(0, 200)
plt.ylim(0, 200)
x1, y1 = [(road-procent*road)/2, (road-procent*road)/2], [0, 200]
x2, y2 = [(road+procent*road)/2, (road+procent*road)/2], [0, 200]
x3, y3 = [0, 200], [(road-procent*road)/2, (road-procent*road)/2]
x4, y4 = [0, 200], [(road+procent*road)/2, (road+procent*road)/2]
plt.plot(x1, y1, 'g')
plt.plot(x2,y2,'g')
plt.plot(x3, y3, 'g')
plt.plot( x4, y4, 'g')
plt.show()
'''