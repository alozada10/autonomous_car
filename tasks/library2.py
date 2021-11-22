import numpy as np
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

class Car:
    def __init__(self,index,position_x,position_y, velocity,v_0, area, safe_distance, max_acc:float = None,b_dec: float = None, axis: str = None ,min_distance : float = None):
        """

        :param index: Identity of the car
        :param position_x: current x position of the car
        :param position_y: current y position of the car
        :param velocity: current velocity of the vehicle. 1D array
        :param v_0: the velocity the vehicle would drive at in free traffic.
        :param area: Area in the environment the car is occupying
        :param safe_distance: the minimum distance between cars.
        :param max_acc: the maximum vehicle acceleration
        :param b_dec: comfortable braking deceleration
        :param axis: the axis the car is driving at "x" or "y"
        :param min_distance: the minimum distance between cars

        """
        self.index = index
        self.position_x = position_x
        self.position_y = position_y
        self.velocity = velocity
        self.area = area
        self.safe_distance = safe_distance
        self.max_acc = max_acc
        self.axis = axis
        self.b_dec = b_dec
        self.min_distance = min_distance
        self.v_0 = v_0
        self.delta = 4



    def update_postion_velocity(self):
        pass


class RegularCar(Car):

    def __str__(self):
        """
        stringify card attributes
        :return: type of the car
        """
        return "RegularCar"

    def update_position(self,delta_t: float = None):
        #if len(self.velocity) != 1:
        #    raise ValueError("New velocity must be 1D!")
        if self.axis == 'x':
            self.position_x = self.position_x + self.velocity *delta_t

        elif self.axis == 'y':
            self.position_y = self.position_y + self.velocity *delta_t
        else:
            raise ValueError("Axis must be x or y!")

        return




    def update_velocity(self,v_current_neighbor: np.array = None,  #passing it for now
                        t_char: float = None,  #it comes in too
                        s_current: float = None,  #dont know this one
                        delta_t: float = None): #this one goes also in
        #if len(self.velocity) != 1 or len(v_current_neighbor) != 1:
        #    raise ValueError("Current and neighbor velocity must be 1D!")
        v_delta = self.velocity - v_current_neighbor
        print(v_delta)
        v_free_road = self.max_acc * (1 - (self.velocity / self.v_0) ** self.delta)
        print(v_free_road)
        v_interaction = - self.max_acc * (
                (self.min_distance + self.velocity * t_char) / s_current + self.velocity * v_delta / (2 * s_current * (self.max_acc * self.b_dec) ** 0.5)) ** 2
        print(v_interaction)
        delta_v = (v_free_road + v_interaction) * delta_t
        print(delta_v)
        new_velocity = self.velocity + delta_v

        self.velocity = new_velocity

    def get_distance_car(self,other):
        distance = np.sqrt((self.position_x- other.position_x)**2 + (self.position_y- other.position_y)**2)
        return distance

    def check_position_velocity(self):
        if self.position_x >100:
            self.position_x = 100
        if self.position_y > 100:
            self.position_y =100
        if abs(self.velocity) > 100:
            self.velocity =100






class AutonomousCar(Car):

    def __str__(self):
        """
        stringify card attributes
        :return: type of the car
        """
        return "AutonomousCar"