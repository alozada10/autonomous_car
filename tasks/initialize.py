# car: [position x, position y, magnitude velocity, direction, autonomous/regular]
# axis: x (0), y (1)
# cars: regular (0), autonomous (1)
import numpy as np


def initialize(size: float = None,
               axis: list = None,
               velocities: np.array = None,
               autonomous_precentage: float = None,
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

    regular_cars = []
    autonomous_cars = []

    number_regular_cars = len(axis) - round(len(axis) * autonomous_precentage)
    number_autonomous_cars = round(len(axis) * autonomous_precentage)

    for i in range(number_regular_cars):
        eta_0 = np.random.normal(0, 1, 1)[0]
        if axis[i] == 'x':
            car_x = np.random.choice(pos_x, 1)[0]
            position = [car_x, r_x, velocities[i], 0, 0, eta_0]
            index_r = np.argwhere(pos_x == car_x)[0][0]
            pos_x = np.delete(pos_x, index_r)
            regular_cars.append(position)
        elif axis[i] == 'y':
            car_y = np.random.choice(pos_y, 1)[0]
            position = [r_y, car_y, velocities[i], 1, 0, eta_0]
            index_r = np.argwhere(pos_y == car_y)[0][0]
            pos_y = np.delete(pos_y, index_r)
            regular_cars.append(position)

    for j in range(number_regular_cars, number_regular_cars + number_autonomous_cars):
        eta_0 = np.random.normal(0, 1, 1)[0]
        if axis[j] == 'x':
            car_x = np.random.choice(pos_x, 1)[0]
            position = [car_x, r_x, velocities[j], 0, 1, eta_0]
            index_r = np.argwhere(pos_x == car_x)[0][0]
            pos_x = np.delete(pos_x, index_r)
            autonomous_cars.append(position)
        elif axis[j] == 'y':
            car_y = np.random.choice(pos_y, 1)[0]
            position = [r_y, car_y, velocities[j], 1, 1, eta_0]
            index_r = np.argwhere(pos_y == car_y)[0][0]
            pos_y = np.delete(pos_y, index_r)
            autonomous_cars.append(position)
    if len(autonomous_cars) == 0:
        autonomous_cars = np.array(autonomous_cars).reshape(0, 6)
    else:
        autonomous_cars = np.array(autonomous_cars)
    if len(regular_cars) == 0:
        regular_cars = np.array(regular_cars).reshape(0, 6)
    else:
        regular_cars = np.array(regular_cars)
    cars = np.vstack([regular_cars, autonomous_cars])
    return np.asarray(cars), np.array([r_y, r_x])
