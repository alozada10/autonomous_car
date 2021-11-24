import numpy as np
from autonomous_car.tasks import utils as ut


def update_position(car: np.array = None,
                    light_status: int = None,
                    box_size: int = None,
                    center: np.array = None,
                    axis: int = None,
                    delta_t: float = None,
                    size: int = None,
                    new_velocity: np.array = None):
    axis = int(axis)
    new_car = car.copy()
    if len(new_velocity) != 1:
        raise ValueError("New velocity must be 1D!")
    if axis not in [0, 1]:
        raise ValueError("Axis must be x or y!")

    if axis == light_status:
        new_car[int(axis)] = new_car[int(axis)] + new_velocity * delta_t
        new_car[0:2] = ut.correct_displacement(new_car[0:2], [size, size])
    else:
        new_pos = new_car[int(axis)] + new_velocity * delta_t
        if (new_pos <= center[axis] - box_size) or (new_pos >= center[axis]):
            new_car[int(axis)] = new_pos
            new_car[0:2] = ut.correct_displacement(new_car[0:2], [size, size])
        else:
            return new_car

    return new_car
