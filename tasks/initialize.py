import numpy as np
import matplotlib.pyplot as plt


def initialize(sizeOfPlane,
               axis,
               velocities,
               roadPrecentage):
    if len(axis) != len(velocities):
        raise ValueError("Directions a velocities need the same number of elements!")
    initialPosition = []
    r_x = (sizeOfPlane + (2 * np.random.rand() - 1) * np.random.rand() * sizeOfPlane * roadPrecentage) / 2
    r_y = (sizeOfPlane + (2 * np.random.rand() - 1) * np.random.rand() * sizeOfPlane * roadPrecentage) / 2
    outside_box1 = np.random.rand() * 1/2 * (sizeOfPlane-roadPrecentage*sizeOfPlane)
    outside_box2 = sizeOfPlane/2 + outside_box1
    for i in range(len(axis)):
        if axis[i] == 'x':
            position = [np.random.choice([outside_box1,outside_box2]), r_x, velocities[i], 0]
            initialPosition.append(position)
        elif axis[i] == 'y':
            position = [r_y, np.random.choice([outside_box1,outside_box2]), velocities[i], 1]
            initialPosition.append(position)
    return np.asarray(initialPosition), np.array([r_x, r_y])


'''
# Test
procent = 0.2  # how wide the width of the road is
road = 200  # plane size with a height
axis = ['x', 'y', 'x', 'x']
v0 = np.array([10, 10, 1, 0])
x0 = initialize(road, axis, v0, procent)

plt.scatter(x0[:, 0], x0[:, 1])
plt.xlim(0, 200)
plt.ylim(0, 200)
x1, y1 = [(road - procent * road) / 2, (road - procent * road) / 2], [0, 200]
x2, y2 = [(road + procent * road) / 2, (road + procent * road) / 2], [0, 200]
x3, y3 = [0, 200], [(road - procent * road) / 2, (road - procent * road) / 2]
x4, y4 = [0, 200], [(road + procent * road) / 2, (road + procent * road) / 2]
plt.plot(x1, y1, 'g')
plt.plot(x2, y2, 'g')
plt.plot(x3, y3, 'g')
plt.plot(x4, y4, 'g')
plt.show()
'''
