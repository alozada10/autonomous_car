import numpy as np
from autonomous_car.tasks import get_neighbors, update_velocity, update_position, human_driver


def update_cars(cars: np.array = None,
                box_size: int = None,
                light_status: int = None,
                light_prob: float = None,
                center: np.array = None,
                size: int = None,
                a: float = None,
                b: float = None,
                v_0: float = None,
                t_char: float = None,
                s_0: float = None,
                delta_t: float = None,
                delta: float = 4,
                vs: float = 0.1):
    temp_cars = []
    temp_v = []
    for car in cars:

        # autonomous cars
        if car[4] == 1:
            n_distance, neighbor = get_neighbors.get_neighbor_distance(r=car,
                                                                       arena=cars,
                                                                       arena_side=size)
            car_current_v = np.array([car[2]])
            car_neighbor_v = np.array([neighbor[2]])

            new_v = update_velocity.update_velocity(a=a,
                                                    b=b,
                                                    v_current=car_current_v,
                                                    v_current_neighbor=car_neighbor_v,
                                                    v_0=v_0,
                                                    t_char=t_char,
                                                    s_current=n_distance,
                                                    s_0=s_0,
                                                    delta_t=delta_t,
                                                    delta=delta)

            if new_v < 0:
                new_v = np.array([0.5])

            new_car = update_position.update_position(car=car,
                                                      all_cars=cars,
                                                      light_status=light_status,
                                                      light_prob=light_prob,
                                                      box_size=box_size,
                                                      center=center,
                                                      axis=car[3],
                                                      delta_t=delta_t,
                                                      size=size,
                                                      new_velocity=new_v)
            temp_cars.append(new_car)
            temp_v.append(new_v)

        # regular cars
        elif car[4] == 0:

            n_real_distance, neighbor = get_neighbors.get_neighbor_distance(r=car,
                                                                            arena=cars,
                                                                            arena_side=size)
            w = human_driver.wiener_value(previous_wiener=car[5],
                                          delta_t=delta_t,
                                          tau=t_char)
            n_distance = human_driver.estimate_distance(real_distance=n_real_distance,
                                                        vs=vs,
                                                        wiener=w)

            car_current_v = np.array([car[2]])
            car_neighbor_real_v = np.array([neighbor[2]])

            car_neighbor_v = human_driver.estimate_velocity(real_velocity=car_neighbor_real_v,
                                                            real_distance=n_real_distance,
                                                            wiener=w,
                                                            sigma_r=0.01)

            new_v = update_velocity.update_velocity(a=a,
                                                    b=b,
                                                    v_current=car_current_v,
                                                    v_current_neighbor=car_neighbor_v,
                                                    v_0=v_0,
                                                    t_char=t_char,
                                                    s_current=n_distance,
                                                    s_0=s_0,
                                                    delta_t=delta_t,
                                                    delta=delta)

            if new_v < 0:
                new_v = np.array([0.5])

            new_car = update_position.update_position(car=car,
                                                      all_cars=cars,
                                                      light_status=light_status,
                                                      light_prob=light_prob,
                                                      box_size=box_size,
                                                      center=center,
                                                      axis=car[3],
                                                      delta_t=delta_t,
                                                      size=size,
                                                      new_velocity=new_v)
            new_car[5] = w
            temp_cars.append(new_car)
            temp_v.append(new_v)
    new_cars = np.array(temp_cars)

    return new_cars, np.mean(temp_v)
