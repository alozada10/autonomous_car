# inputs
# r: current vehicle. 4D array.
# arena: all vehicles. N*3 array, where N is all the cars in the simulation
# warning: ignoring other cars not in lane

from autonomous_car.tasks import utils as ut
import numpy as np


def get_neighbor_distance(r,
                          arena,
                          arena_side):
    if len(arena) < 2:
        raise ValueError("You need at least 2 cars!")

    axis = int(r[3])
    virtual_env = ut.create_virtual_env(arena,
                                        arena_side)
    lane_neighbors = virtual_env[virtual_env[:, 3] == axis]
    min_distance = 1 * 10 ** 8
    neighbor = None
    for i in range(len(lane_neighbors)):
        i_n = lane_neighbors[i]
        i_distance = i_n[axis] - r[axis]
        if 0 < i_distance < min_distance:
            min_distance = i_distance

            neighbor = np.concatenate([ut.correct_displacement(i_n[0:2], [arena_side, arena_side]), i_n[2:]])
    return min_distance, neighbor

