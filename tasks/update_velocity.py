# inputs
# a: the maximum vehicle acceleration
# b: comfortable braking deceleration, b>0
# v_current: current velocity of the vehicle. 1D array
# v_current_neighbor: current velocity of the vehicle in front of the current vehicle. 1D array
# v_0: the velocity the vehicle would drive at in free traffic.
# t_char: the minimum possible time to the vehicle in front
# s_0: the minimum distance between cars.
# s_current: current net distance between neighboring cars (including size)
# delta_t: time step
# delta: free parameter. Usually 4

# output
# new_velocity: updated velocity. 1D array

import numpy as np


def update_velocity(a: float = None,
                    b: float = None,
                    v_current: np.array = None,
                    v_current_neighbor: np.array = None,
                    v_0: float = None,
                    t_char: float = None,
                    s_current: float = None,
                    s_0: float = None,
                    delta_t: float = None,
                    delta: float = 4):
    if len(v_current) != 1 or len(v_current_neighbor) != 1:
        raise ValueError("Current and neighbor velocity must be 1D!")
    if v_current <= 5:
        a = 20 * a
    v_delta = v_current - v_current_neighbor
    v_free_road = a * (1 - (v_current / v_0) ** delta)
    v_interaction = -a * (
            (s_0 + v_current * t_char) / s_current + v_current * v_delta / (2 * s_current * (a * b) ** 0.5)) ** 2
    delta_v = (v_free_road + v_interaction) * delta_t
    new_velocity = v_current + delta_v

    return new_velocity
