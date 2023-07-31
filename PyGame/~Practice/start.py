"""import pygame
import random
import math

# loading images
background_image = pygame.image.load("utilities/images/bg.png")
bg_ground_img = pygame.image.load("utilities/images/ground.png")
up_pipe_img = pygame.image.load("utilities/images/pipe.png")
down_pipe_img = pygame.transform.flip(up_pipe_img, False, True)
pipe_list = [up_pipe_img, down_pipe_img]

# Attributes
up_pipe_x = 1300
up_pipe_y = 300
pipe_x_change = -20

down_pipe_x = 1300
down_pipe_y = -300


# down_x_change = -6


# functions
def up_draw_pipe(x, y):
    up_pipe = up_pipe_img
    screen.blit(up_pipe, (x, y))


def down_draw_pipe(x, y):
    down_pipe = down_pipe_img
    screen.blit(down_pipe, (x, y))


# Variables
loop = True
ground_scroll = 0
scroll_speed = 6

# Initializing the game
pygame.init()
screen = pygame.display.set_mode((1300, 681))
clock = pygame.time.Clock()

# The game loop
clock.tick(60)
while loop:
    screen.blit(background_image, (0, 0))

    # Handle Keyboard Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    up_pipe_x += pipe_x_change
    if down_pipe_x < -10:
        down_pipe_x = 1300
    if up_pipe_x < -10:
        up_pipe_x = 1300
    up_draw_pipe(up_pipe_x, up_pipe_y)
    if up_pipe_x < 1250:
        down_draw_pipe(down_pipe_x, down_pipe_y)
        down_pipe_x += pipe_x_change

    # Ground Scroller
    screen.blit(bg_ground_img, (ground_scroll, 541))
    ground_scroll -= scroll_speed
    if abs(ground_scroll) > 35:
        ground_scroll = 0

    pygame.display.update()
"""

import pygame
import random
import math

# loading images
background_image = pygame.image.load("utilities/images/bg.png")
bg_ground_img = pygame.image.load("utilities/images/ground.png")
up_pipe_img = pygame.image.load("utilities/images/pipe.png")
down_pipe_img = pygame.transform.flip(up_pipe_img, False, True)
pipe_list = [up_pipe_img, down_pipe_img]

# Attributes
up_pipe_x = 1300
up_pipe_y = 300
pipe_x_speed = 20

down_pipe_x = 1300
down_pipe_y = -300


# functions
def up_draw_pipe(x, y):
    up_pipe = up_pipe_img
    screen.blit(up_pipe, (x, y))


def down_draw_pipe(x, y):
    down_pipe = down_pipe_img
    screen.blit(down_pipe, (x, y))


# Initializing the game
pygame.init()
screen = pygame.display.set_mode((1300, 681))
clock = pygame.time.Clock()

# Variables
loop = True
ground_scroll = 0
scroll_speed = 6

# The game loop
while loop:
    clock.tick(60)  # Limit the frame rate to 60 FPS

    # Handle Keyboard Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    # Update pipe positions
    elapsed_time = clock.get_time()  # Get the elapsed time since the last frame
    up_pipe_x -= pipe_x_speed * (elapsed_time / 1000)  # Convert elapsed_time to seconds
    if up_pipe_x < -10:
        up_pipe_x = 1300

    if up_pipe_x < 1250:
        down_draw_pipe(down_pipe_x, down_pipe_y)
        down_pipe_x -= pipe_x_speed * (elapsed_time / 1000)  # Convert elapsed_time to seconds
        if down_pipe_x < -10:
            down_pipe_x = 1300

    # Render the scene
    screen.blit(background_image, (0, 0))
    up_draw_pipe(up_pipe_x, up_pipe_y)
    screen.blit(bg_ground_img, (ground_scroll, 541))
    pygame.display.update()

# Exit the game
pygame.quit()
