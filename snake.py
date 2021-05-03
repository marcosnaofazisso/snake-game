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


snake_direction = LEFT


def random_position_food():
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return (x // 10 * 10, y // 10 * 10)


food = pygame.Surface((10, 10))
food.fill((255, 0, 0))
food_position = random_position_food()


def collision(c1, c2):
    return (c1[0] == c2[0] and (c1[1] == c2[1]))



clock = pygame.time.Clock()



while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        
        if event.type == KEYDOWN:
            if event.key == K_UP:
                snake_direction = UP
            if event.key == K_DOWN:
                snake_direction = DOWN
            if event.key == K_RIGHT:
                snake_direction = RIGHT
            if event.key == K_LEFT:
                snake_direction = LEFT


    if collision(snake[0], food_position):
        food_position = random_position_food()
        snake.append((0, 0))

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])


    if snake_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if snake_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if snake_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if snake_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])



    screen.fill((0, 0, 0))
    screen.blit(food, food_position)
    for position in snake:
        screen.blit(snake_skin, position)



    clock.tick(20)
    
    pygame.display.update()



