import pygame
import numpy as np
import time

#Screen
screenSize = (400, 400)
screen = pygame.display.set_mode(screenSize)

#Background
background = pygame.image.load('images/123.png')

#Display caption
pygame.display.set_caption("Simulation")

tick = 0
car_positions = np.array([[[0,205],[10,205],[20,205],[30,205],[40,205]],
                          [[205,0],[205,10],[205,20],[205,30],[205,40]]])
car = pygame.image.load('images/carup.png')
car = pygame.transform.scale(car, (12, 25))
#car_positions[car_number, tick(timestep), 0 or 1(x or y)]
running = True


while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for pos in car_positions:
        x = pos[tick,0]
        y = pos[tick,1]
        screen.blit(car,(x,y))
    pygame.display.update()
    if tick < 4:
        tick = tick + 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    time.sleep(1)