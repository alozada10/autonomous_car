class RegularCar:
    def __init__(self,position,velocity,area,safe_distance,horse_power):
        self.position = position
        self.velocity = velocity
        self.area = area
        self.safe_distance = safe_distance
        self.horse_power = horse_power

    def __str__(self):
        """
        stringify card attributes
        :return: type of the car
        """
        return "RegularCar"


    def update_postion_velocity(self):
        pass



class AutonomousCar:
    def __init__(self,position,velocity,area,safe_distance,horse_power):
        self.position = position
        self.velocity = velocity
        self.area = area
        self.safe_distance = safe_distance
        self.horse_power = horse_power

    def __str__(self):
        """
        stringify card attributes
        :return: type of the car
        """
        return "AutonomousCar"

    def update_postion_velocity(self):
        pass
