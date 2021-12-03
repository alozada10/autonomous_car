import plotly.express as px
import numpy as np
import autonomous_car.tasks.initialize as initialize
from autonomous_car.tasks import update_cars
from autonomous_car.tasks import utils as ut

iterations = 1
box_size = 100
size = 2000
number_cars = 2
time_step = 1
time_lights = 20
max_acc = 0.73
regular_decc = 1.67
freeway_velocity = 50
minimum_distance = 10
safe_time_headway = 1.5
light_prob = 1

initial_velocities = np.random.randint(10, 50, number_cars)
initial_directions = np.random.choice(['x', 'y'],
                                      number_cars)  # ['x','x','y','y']#np.random.choice(['x', 'y'], number_cars)
initial_cars, center = initialize.initialize(size=size,
                                             axis=initial_directions,
                                             velocities=initial_velocities,
                                             lane_percentage=0.3,
                                             min_distance=minimum_distance)
# initial_cars= np.array([[1,50,3,0],[30,50,2,0],[50,7,3,1],[50,1,4,1]])*1.0
# center = [50,50]

result = [initial_cars]
light_status = np.random.choice([0, 1], 1)[0]
ligths = [light_status]
result_velocities = [np.mean(initial_velocities)]
print(center)
for t in range(1, iterations):
    if t % time_lights == 0:
        light_status = abs(light_status - 1)
    ligths.append(light_status)
    new_cars, mean_v = update_cars.update_cars(cars=initial_cars,
                                               light_status=light_status,
                                               light_prob=light_prob,
                                               box_size=box_size,
                                               center=center,
                                               size=size,
                                               a=max_acc,
                                               b=regular_decc,
                                               v_0=freeway_velocity,
                                               t_char=safe_time_headway,
                                               s_0=minimum_distance,
                                               delta_t=time_step,
                                               delta=4)
    # print('new pop', new_cars)
    result.append(new_cars)
    result_velocities.append(mean_v)

    initial_cars = new_cars

result_plot = [i[:, 0:2] for i in result]

fig = px.scatter(ut.turn_time_series(data=result_plot,
                                     center=center,
                                     boxsize=box_size,
                                     lights=np.array(ligths)),
                 x='x',
                 y='y',
                 color='type',
                 animation_frame='generation',
                 width=500,
                 height=500)
fig.show()
result = np.array(result)
print(result.shape)
result_reshaped = result.reshape(result.shape[0], -1)
np.savetxt("result.txt", result_reshaped)
ligths = np.array(ligths)
np.savetxt("lights.txt", ligths)
velocities_final = np.array(result_velocities)
np.savetxt("vel.csv", velocities_final)
