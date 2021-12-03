import numpy as np
import matplotlib.pyplot as plt


def initialize(size: float = None,
               axis: list = None,
               velocities: np.array = None,
               lane_percentage: float = None,
               min_distance: float = None):
    if len(axis) != len(velocities):
        raise ValueError("Directions a velocities need the same number of elements!")
    r_x = (size + (2 * np.random.rand() - 1) * np.random.rand() * size * lane_percentage) / 2
    r_y = (size + (2 * np.random.rand() - 1) * np.random.rand() * size * lane_percentage) / 2
    pos_x = np.arange(0, size, min_distance)
    pos_y = np.arange(0, size, min_distance)
    pos_x_right = pos_x[(pos_x >= r_x + (size * lane_percentage) / 2)]
    pos_x_left = pos_x[(pos_x <= r_x - (size * lane_percentage) / 2)]
    pos_x = np.concatenate([pos_x_left, pos_x_right])
    pos_y_right = pos_y[(pos_y >= r_y + (size * lane_percentage) / 2)]
    pos_y_left = pos_y[(pos_y <= r_y - (size * lane_percentage) / 2)]
    pos_y = np.concatenate([pos_y_left, pos_y_right])
    if (len(axis) > len(pos_x)) or (len(axis) > len(pos_y)):
        raise ValueError("Too many cars for initial given minimum distance!")

    cars = []

    for i in range(len(axis)):
        if axis[i] == 'x':
            car_x = np.random.choice(pos_x, 1)[0]
            position = [car_x, r_x, velocities[i], 0]
            index_r = np.argwhere(pos_x == car_x)[0][0]
            pos_x = np.delete(pos_x, index_r)
            cars.append(position)
        elif axis[i] == 'y':
            car_y = np.random.choice(pos_y, 1)[0]
            position = [r_y, car_y, velocities[i], 1]
            index_r = np.argwhere(pos_y == car_y)[0][0]
            pos_y = np.delete(pos_y, index_r)
            cars.append(position)
    return np.asarray(cars), np.array([r_y, r_x])


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
