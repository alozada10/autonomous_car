import numpy as np


def wiener_value(previous_wiener: float = None,
                 delta_t: float = None,
                 tau: float = None):
    eta_i = np.random.normal(0, 1, 1)
    w_i = previous_wiener * np.e ** (-delta_t / tau) + eta_i * (2 * delta_t / tau) ** 0.5
    return w_i


def estimate_distance(real_distance: float = None,
                      vs: float = 0.1,
                      wiener: float = None):
    estimated_distance = real_distance + np.e ** (vs * wiener)
    return estimated_distance


def estimate_velocity(real_velocity: np.array,
                      real_distance: float = None,
                      wiener: float = None,
                      sigma_r: float = 0.01):
    estimated_velocity = real_velocity - real_distance * sigma_r * wiener
    return estimated_velocity
