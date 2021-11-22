import numpy as np


class Car:
    def __init__(self,environment,position,velocity,area,safe_distance,horse_power):
            self.position = position
            self.velocity = velocity
            self.area = area
            self.safe_distance = safe_distance
            self.horse_power = horse_power
            self.environment = environment

    def update_postion_velocity(self):
        pass

class RegularCar(Car):
    
    def __str__(self):
        """
        stringify card attributes
        :return: type of the car
        """
        return "RegularCar"

    def update_velocity(self,a: float = None,
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
        v_delta = v_current - v_current_neighbor
        v_free_road = a * (1 - (v_current / v_0) ** delta)
        v_interaction = -a * (
                (s_0 + v_current * t_char) / s_current + v_current * v_delta / (2 * s_current * (a * b) ** 0.5)) ** 2
        delta_v = (v_free_road + v_interaction) * delta_t
        new_velocity = v_current + delta_v

        return new_velocity

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





class AutonomousCar(Car):

    def __str__(self):
        """
        stringify card attributes
        :return: type of the car
        """
        return "AutonomousCar"