import pygame
import random
import numpy

pygame.init()

window_x = 1400
window_y = 800

start_pos_x = 650
start_pos_y = 200

static_pos_x1 = window_x / 2
static_pos_y1 = (window_y / 2)

fixed_pos = (static_pos_x1, static_pos_y1)

move_pos_x = (start_pos_x, start_pos_y)

time = 0

count = 0

count_2 = 0

count_3 = 0

white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)

radius = 10

WIN = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption("single pendulum")

distance_1 = random.randint(200, 250)
distance_2 = random.randint(100, 150)
distance_3 = random.randint(40, 60)

rotation_1 = random.randint(1, 2)
rotation_2 = random.randint(5, 10)
rotation_3 = random.randint(20, 50)

run = True
while run:

    FILL = True

    pygame.time.delay(0)

    time = time + 0.001

    move_pos_1 = (static_pos_x1 + distance_1 * (numpy.cos(rotation_1 * time)), static_pos_y1 + distance_1 *
                  numpy.sin(rotation_1 * time))

    move_pos_2 = (
        static_pos_x1 + distance_1 * (numpy.cos(rotation_1 * time)) - distance_2 * (numpy.cos(rotation_2 * time))
        , static_pos_y1 + distance_1 * numpy.sin(rotation_1 * time) + distance_2 * numpy.sin(rotation_2 * time))

    move_pos_3 = (static_pos_x1 + distance_1 * (numpy.cos(rotation_1 * time)) - distance_2 * (
                  numpy.cos(rotation_2 * time)) + distance_3 * numpy.sin(rotation_3 * time),
                  static_pos_y1 + distance_1 * numpy.sin(rotation_1 * time) + distance_2 * numpy.sin(
                  rotation_2 * time) + distance_3 * numpy.cos(rotation_3 * time))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        count = count + 1

    if count == 1:
        WIN.fill((0, 0, 0))
        count = count + 1

    if count > 0:
        pygame.draw.circle(WIN, yellow, move_pos_3, radius - 8)
        FILL = False

    if keys[pygame.K_UP]:
        count_2 = count_2 + 1

    if count_2 == 1:
        WIN.fill((0, 0, 0))
        count_2 = count_2 + 1

    if count_2 > 0:
        pygame.draw.circle(WIN, green, move_pos_2, radius - 8)
        FILL = False

    if keys[pygame.K_DOWN]:
        count_3 = count_3 + 1

    if count_3 == 1:
        WIN.fill((0, 0, 0))
        count_3 = count_3 + 1

    if count_3 > 0:
        pygame.draw.circle(WIN, red, move_pos_1, radius - 8)
        FILL = False

    if keys[pygame.K_LSHIFT]:
        FILL = True
        count = 0
        count_2 = 0
        count_3 = 0

    if FILL:
        WIN.fill((0, 0, 0))
        pygame.draw.line(WIN, white, move_pos_1, fixed_pos, 3)
        pygame.draw.line(WIN, white, move_pos_1, move_pos_2, 3)
        pygame.draw.line(WIN, white, move_pos_2, move_pos_3, 3)
        pygame.draw.circle(WIN, blue, fixed_pos, radius + 20)
        pygame.draw.circle(WIN, red, move_pos_1, radius + 10)
        pygame.draw.circle(WIN, green, move_pos_2, radius + 5)
        pygame.draw.circle(WIN, yellow, move_pos_3, radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
