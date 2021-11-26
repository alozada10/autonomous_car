import numpy as np
from autonomous_car.tasks import utils as ut


def update_position(car: np.array = None,
                    light_prob: float = None,
                    all_cars: np.array = None,
                    light_status: int = None,
                    box_size: int = None,
                    center: np.array = None,
                    axis: int = None,
                    delta_t: float = None,
                    size: int = None,
                    new_velocity: np.array = None):
    axis = int(axis)
    new_car = car.copy()
    new_car[2] = new_velocity
    if len(new_velocity) != 1:
        raise ValueError("New velocity must be 1D!")
    if axis not in [0, 1]:
        raise ValueError("Axis must be x or y!")
    new_pos = new_car[int(axis)] + new_velocity * delta_t
    current_pos = new_car[int(axis)]
    if axis == light_status:
        if (new_pos >= center[axis] - box_size / 2) and (new_pos <= center[axis]):
            r_inter = np.random.random()
            if r_inter <= light_prob:
                clear_intersection = ut.check_clear_intersection(cars=all_cars,
                                                                 axis=axis,
                                                                 center=center,
                                                                 box_size=box_size)
                if clear_intersection:
                    new_car[int(axis)] = new_car[int(axis)] + new_velocity * delta_t
                    new_car[0:2] = ut.correct_displacement(new_car[0:2], [size, size])
                else:
                    new_car[2] = 0
                    return new_car
            else:
                new_car[int(axis)] = new_car[int(axis)] + new_velocity * delta_t
                new_car[0:2] = ut.correct_displacement(new_car[0:2], [size, size])
        else:
            new_car[int(axis)] = new_car[int(axis)] + new_velocity * delta_t
            new_car[0:2] = ut.correct_displacement(new_car[0:2], [size, size])
    else:
        if (new_pos <= center[axis] - box_size / 2) or (new_pos >= center[axis]):
            new_car[int(axis)] = new_pos
            new_car[0:2] = ut.correct_displacement(new_car[0:2], [size, size])
        elif (current_pos >= center[axis] - box_size / 2) and (current_pos <= center[axis]):
            new_car[int(axis)] = new_pos
            new_car[0:2] = ut.correct_displacement(new_car[0:2], [size, size])
        else:
            new_car[2] = 0
            return new_car
    return new_car
