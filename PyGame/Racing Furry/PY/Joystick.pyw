"""import pygame
import random
import math

# Variables
points_counter = 0  # keep track of points
loop = True  # to manage the game loop
game_over = False  # Flag to track the game state

# Loading Images
car_img = pygame.image.load("utilities/images/car.png")
barrier_img = pygame.image.load("utilities/images/barrier.png")
background_image = pygame.image.load("utilities/images/bg.png")
icon = pygame.image.load("utilities/images/icon.png")

# Defining attributes

# barrier
barrier_x_pos = [300, 440, 365]
barrier_x = random.choice(barrier_x_pos)
barrier_y = 10
barrier_y_change = 1.4
# lane
lane_marks_list = []
lane_marks_x = []
lane_marks_y = []
lane_marks_y_change = []
no_of_lane_marks = 5
# car
car_x = 400
car_y = 400
car_x_change = 0
for i in range(no_of_lane_marks):
    lane_marks_list.append(pygame.image.load("utilities/images/lanemarks.png"))
    lane_marks_x.append(320)
    lane_marks_x.append(450)
    lane_marks_y.append(100)
    lane_marks_y_change.append(2)

# initialize window
pygame.init()
font = pygame.font.Font("utilities/font/the_font_namco.ttf", 13)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Racing Fury | By Maaz")
pygame.display.set_icon(icon)

# background music
pygame.mixer.music.load("utilities/sounds/bg.mp3")
pygame.mixer.music.play(-1)

# Initialize joystick
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()

if joystick_count > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()


# Draw Functions
def draw_lanes(x, y, i):
    screen.blit(lane_marks_list[i], (x, y))


def draw_car(x, y):
    screen.blit(car_img, (x, y))


def draw_barrier(x, y):
    screen.blit(barrier_img, (x, y))


# Collision Detection
def collision(x1, x2, y1, y2):
    distance = math.sqrt((math.pow(x2 - x1, 2)) + (math.pow(y2 - y1, 2)))
    if distance < 50:
        return True
    else:
        return False


def show_points():
    points_label = font.render(str(points_counter), True, (0, 255, 0))
    screen.blit(points_label, (10, 10))


def play_again():
    pygame.mixer.music.load("utilities/sounds/bg.mp3")
    pygame.mixer.music.play(-1)
    global car_x, car_y, points_counter, barrier_y, barrier_x, barrier_y_change, barrier_x_pos, coll_check
    car_x = 400
    car_y = 400
    points_counter = 0
    barrier_x = random.choice(barrier_x_pos)
    barrier_y = 10
    barrier_y_change = 1.4


# The game loop
while loop:
    screen.fill((0, 0, 0))
    screen.blit(background_image, (0, 0))

    # Handle Keyboard Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                car_x_change = 1
            if event.key == pygame.K_LEFT:
                car_x_change = -1
            if event.key == pygame.K_SPACE and game_over:
                play_again()  # Restart the game
                game_over = False
        if event.type == pygame.KEYUP:
            car_x_change = 0

        # Handle joystick events
        if joystick_count > 0:
            if event.type == pygame.JOYAXISMOTION:
                if event.axis == 0:  # X-axis
                    car_x_change = event.value
            if event.type == pygame.JOYBUTTONDOWN and game_over:
                if event.button == 5:  # R1 button index may vary, adjust accordingly
                    play_again()
                    game_over = False

    if not game_over:  # Only update game logic if the game is not over
        # Increase points
        coll_check = collision(car_x, barrier_x, car_y, barrier_y)
        if not coll_check:
            points_counter += 1

        for n in range(no_of_lane_marks):
            lane_marks_y[n] += lane_marks_y_change[n]
            draw_lanes(lane_marks_x[n], lane_marks_y[n], n)
            if lane_marks_y[n] > 600:
                lane_marks_y[n] = 10

        # Change Barrier Pos
        barrier_y += barrier_y_change
        if barrier_y > 620:
            barrier_y = -20
            barrier_x = random.choice(barrier_x_pos)

        # Change Car Pos
        car_x += car_x_change
        if car_x < 260:
            car_x = 260
        if car_x > 480:
            car_x = 480

        # Check for the Collision
        if coll_check:
            game_over = True
            pygame.mixer.music.stop()
            pygame.mixer.Sound("utilities/sounds/explosion.wav").play()
            car_x_change = 0
            barrier_y_change = 0

    draw_barrier(barrier_x, barrier_y)
    draw_car(car_x, car_y)
    show_points()

    # Handle Game Over
    if game_over:
        game_over_label = font.render("game over!", True, (255, 0, 0))
        restart_label = font.render("press space bar!", True, (255, 0, 0))
        screen.blit(game_over_label, (320, 25))
        screen.blit(restart_label, (280, 60))

    pygame.display.update()
"""

import pygame
import random
import math

# Variables
points_counter = 0  # keep track of points
loop = True  # to manage the game loop
game_over = False  # Flag to track the game state

# Loading Images
car_img = pygame.image.load("utilities/images/car.png")
barrier_img = pygame.image.load("utilities/images/barrier.png")
background_image = pygame.image.load("utilities/images/bg.png")
icon = pygame.image.load("utilities/images/icon.png")

# Defining attributes

# barrier
barrier_x_pos = [300, 440, 365]
barrier_x = random.choice(barrier_x_pos)
barrier_y = 10
barrier_y_change = 10
# lane
lane_marks_list = []
lane_marks_x = []
lane_marks_y = []
lane_marks_y_change = []
no_of_lane_marks = 2
# car
car_x = 400
car_y = 400
car_x_change = 0
for i in range(no_of_lane_marks):
    lane_marks_list.append(pygame.image.load("utilities/images/lanemarks.png"))
    lane_marks_x.append(320)
    lane_marks_x.append(450)
    lane_marks_y.append(100)
    lane_marks_y_change.append(20)

# initialize window
pygame.init()
font = pygame.font.Font("utilities/font/the_font_namco.ttf", 13)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Racing Fury | By Maaz")
pygame.display.set_icon(icon)

# background music
pygame.mixer.music.load("utilities/sounds/bg.mp3")
pygame.mixer.music.play(-1)

# Initialize joystick
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()

if joystick_count > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()


# Draw Functions
def draw_lanes(x, y, i):
    screen.blit(lane_marks_list[i], (x, y))


def draw_car(x, y):
    screen.blit(car_img, (x, y))


def draw_barrier(x, y):
    screen.blit(barrier_img, (x, y))


# Collision Detection
def collision(x1, x2, y1, y2):
    distance = math.sqrt((math.pow(x2 - x1, 2)) + (math.pow(y2 - y1, 2)))
    if distance < 50:
        return True
    else:
        return False


def show_points():
    points_label = font.render(str(points_counter), True, (0, 255, 0))
    screen.blit(points_label, (10, 10))


def play_again():
    pygame.mixer.music.load("utilities/sounds/bg.mp3")
    pygame.mixer.music.play(-1)
    global car_x, car_y, points_counter, barrier_y, barrier_x, barrier_y_change, barrier_x_pos, coll_check
    car_x = 400
    car_y = 400
    points_counter = 0
    barrier_x = random.choice(barrier_x_pos)
    barrier_y = 10
    barrier_y_change = 10


clock = pygame.time.Clock()

# The game loop
while loop:
    clock.tick(65)
    screen.fill((0, 0, 0))
    screen.blit(background_image, (0, 0))

    # Handle Keyboard Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                car_x_change = 10
            if event.key == pygame.K_LEFT:
                car_x_change = -10
            if event.key == pygame.K_SPACE and game_over:
                play_again()  # Restart the game
                game_over = False
        if event.type == pygame.KEYUP:
            car_x_change = 0

        # Handle joystick events
        if joystick_count > 0:
            if event.type == pygame.JOYAXISMOTION:
                if event.axis == 0:  # X-axis
                    car_x_change = event.value * 9
            if event.type == pygame.JOYBUTTONDOWN and game_over:
                if event.button == 5:  # R1 button index may vary, adjust accordingly
                    play_again()
                    game_over = False

    if not game_over:  # Only update game logic if the game is not over
        # Increase points
        coll_check = collision(car_x, barrier_x, car_y, barrier_y)
        if not coll_check:
            points_counter += 1

        for n in range(no_of_lane_marks):
            lane_marks_y[n] += lane_marks_y_change[n]
            draw_lanes(lane_marks_x[n], lane_marks_y[n], n)
            if lane_marks_y[n] > 600:
                lane_marks_y[n] = 10

        # Change Barrier Pos
        barrier_y += barrier_y_change
        if barrier_y > 620:
            barrier_y = -20
            barrier_x = random.choice(barrier_x_pos)

        # Change Car Pos
        car_x += car_x_change
        if car_x < 260:
            car_x = 260
        if car_x > 480:
            car_x = 480

        # Check for the Collision
        if coll_check:
            game_over = True
            pygame.mixer.music.stop()
            pygame.mixer.Sound("utilities/sounds/explosion.wav").play()
            car_x_change = 0
            barrier_y_change = 0

    draw_barrier(barrier_x, barrier_y)
    draw_car(car_x, car_y)
    show_points()

    # Handle Game Over
    if game_over:
        game_over_label = font.render("game over!", True, (255, 0, 0))
        restart_label = font.render("press space bar!", True, (255, 0, 0))
        screen.blit(game_over_label, (320, 25))
        screen.blit(restart_label, (280, 60))

    pygame.display.update()
