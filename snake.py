import pygame, random
from pygame.locals import *

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake Game')

snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255))

food = pygame.Surface((10, 10))
food.fill((255, 0, 0))
food_position = (random.randint(0,590), random.randint(0,590))


snake_direction = LEFT


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    screen.fill((0, 0, 0))
    screen.blit(food, food_position)
    for position in snake:
        screen.blit(snake_skin, position)

    
    pygame.display.update()



