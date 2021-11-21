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



class AutonomousCar(Car):

    def __str__(self):
        """
        stringify card attributes
        :return: type of the car
        """
        return "AutonomousCar"