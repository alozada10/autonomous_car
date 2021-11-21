import numpy as np


def update_position(current_position: np.array = None,
                    axis: str = None,
                    delta_t: float = None,
                    new_velocity: np.array = None):
    new_position = current_position.copy()
    if len(new_velocity) != 1:
        raise ValueError("New velocity must be 1D!")
    if axis == 'x':
        axis_inter = 0
    elif axis == 'y':
        axis_inter = 1
    else:
        raise ValueError("Axis must be x or y!")
    new_position[axis_inter] = current_position[axis_inter] + new_velocity * delta_t

    return new_position
