import numpy as np
import pandas as pd


def check_array(array: np.array = None,
                list_arrays: np.array = None):
    return next((True for elem in list_arrays if np.array_equal(elem, array)), False)


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


def check_clear_intersection(cars: np.array = None,
                             axis: int = None,
                             center: np.array = None,
                             box_size: int = None):
    cars_opposite_lane = cars[cars[:, 3] == abs(axis - 1)]
    cars_intersection_1 = cars_opposite_lane[
        (cars_opposite_lane[:, abs(axis - 1)] > center[abs(axis - 1)] - box_size / 2)]
    cars_intersection_2 = cars_opposite_lane[
        (cars_opposite_lane[:, abs(axis - 1)] < center[abs(axis - 1)] + box_size / 2)]
    cars_intersection = np.array([i for i in cars_intersection_1 if check_array(array=i,
                                                                                list_arrays=cars_intersection_2)])
    resp = True
    if len(cars_intersection > 0):
        resp = False
    return resp


def turn_time_series(data,
                     center,
                     boxsize,
                     lights):
    df = pd.DataFrame(
        {'x': [-1, -1, -1, -1],
         'y': [-1, -1, -1, -1],
         'type': ['green_light', 'red_light', 'regular', 'center'],
         'generation': [-1, -1, -1, -1]})
    light_labels_x = {0: 'green_light', 1: 'red_light'}
    light_labels_y = {0: 'red_light', 1: 'green_light'}

    for i in range(len(data)):
        temp_df = pd.DataFrame({'x': data[i][:, 0],
                                'y': data[i][:, 1],
                                'type': ['regular'] * len(data[i]),
                                'generation': i})
        lights_df = pd.DataFrame({'x': [center[0] - boxsize / 3,
                                        center[0] + boxsize / 3],
                                  'y': [center[1] + boxsize / 3,
                                        center[1] - boxsize / 3],
                                  'type': [light_labels_x[lights[i]],
                                           light_labels_y[lights[i]]],
                                  'generation': i})
        center_df = pd.DataFrame({'x': [center[0],
                                        center[0] - boxsize / 2,
                                        center[0] + boxsize / 2,
                                        center[0] - boxsize / 2,
                                        center[0] + boxsize / 2],
                                  'y': [center[1],
                                        center[1] + boxsize / 2,
                                        center[1] + boxsize / 2,
                                        center[1] - boxsize / 2,
                                        center[1] - boxsize / 2],
                                  'type': ['center'] * 5,
                                  'generation': i})
        temp_df = pd.concat([temp_df, center_df])
        temp_df = pd.concat([temp_df, lights_df])
        df = pd.concat([df, temp_df])
    return df
