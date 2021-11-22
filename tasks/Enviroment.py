from library2 import *
import pygame
import numpy as np
import time
import random


nr_cars = 2

#Starting with making some regular in random positions
list_of_cars  = []
for i in range(0,nr_cars):
    random_position_x = np.random.randint(0,100)
    random_position_y = np.random.randint(0,100)
    random_velocity = np.random.rand()*10
    random_v_0 = 2
    random_area = 4
    random_s_0=10
    random_max_acceleration = 1
    random_b_dec = 1
    axis = ["x","y"]
    random_axis = random.choice(axis)
    random_min_distance = 10
    list_of_cars.append(RegularCar(i,random_position_x,random_position_y,random_velocity,random_v_0,random_area,random_s_0,random_max_acceleration,random_b_dec
                                   ,random_axis,random_min_distance))

"""
dict_positions = {}
indexes = np.arange(0,len(list_of_cars))
trajectory = []
nr_timesteps = 10
for i in range (0,nr_timesteps):
    positions =[]
    for car in list_of_cars:
        car.update_position(1)
        car.check_position_velocity()
        car.update_velocity(0,0.5,5,1)
        positions.append(car.position_x)
"""