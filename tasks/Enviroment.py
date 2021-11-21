import numpy as np


move_list = {"up":(0,1),"right":(1,0), }



def initialize_position(sizeOfPlane, initialVelocity, roadPrecentage):
    initialPosition = []
    for velocity in initialVelocity:
        if velocity[0] != 0:
            position = [np.random.rand() * sizeOfPlane, (sizeOfPlane + (
                    2 * np.random.rand() - 1) * np.random.rand() * sizeOfPlane * roadPrecentage) / 2]
            initialPosition.append(position)
        elif velocity[1] != 0:
            position = [
                (sizeOfPlane + (2 * np.random.rand() - 1) * np.random.rand() * sizeOfPlane * roadPrecentage) / 2,
                np.random.rand() * sizeOfPlane]
            initialPosition.append(position)
    return np.asarray(initialPosition)
