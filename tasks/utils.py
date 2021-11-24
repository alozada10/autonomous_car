import numpy as np
import pandas as pd


def correct_displacement(index, shape):
    new_index = np.array([(i % s + s) % s for i, s in zip(index, shape)])
    return np.round(new_index, 4)


def create_virtual_env(all_positions, side_size):
    x = all_positions[:, 0].copy()
    y = all_positions[:, 1].copy()
    v = all_positions[:, 2].copy()

    up = np.array([np.array([i, j, k, 1]) for i, j, k in zip(x, y + side_size, v)])
    right = np.array([np.array([i, j, k, 0]) for i, j, k in zip(x + side_size, y, v)])

    return np.concatenate([all_positions, up, right])


def turn_time_series(data):
    df = None
    for i in range(len(data)):
        temp_df = pd.DataFrame({'x': data[i][:, 0], 'y': data[i][:, 1], 'generation': i})
        df = pd.concat([df, temp_df])
    return df
