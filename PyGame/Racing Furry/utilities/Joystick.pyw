import pygame
import random
import math
import settings as st

# Variables
fps = st.values[0]
points_counter = 0  # keep track of points
loop = True  # to manage the game loop
game_over = False  # Flag to track the game state
if st.values[1] == 30:
    current_mode_selected = "easy"
    mode_color = (0, 255, 0)
elif st.values[1] == 40:
    current_mode_selected = "medium"
    mode_color = (255, 255, 0)
elif st.values[1] == 60:
    current_mode_selected = "hard"
    mode_color = (255, 0, 0)

# Loading Images
car_img = pygame.image.load(st.values[3])
barrier_img = pygame.image.load("images/barrier.png")
background_image = pygame.image.load("images/bg.png")
icon = pygame.image.load("images/icon.png")

# Defining attributes

# barrier
barrier_x_pos = [400, 500, 600, 700, 800, 860]
barrier_x = random.choice(barrier_x_pos)
barrier_y = 10
barrier_y_change = st.values[1]
# lane
lane_marks_list = []
lane_marks_x = []
lane_marks_y = []
lane_marks_y_change = []
no_of_lane_marks = 2
# car
car_x = 682
car_y = 600
car_x_change = 0
for i in range(no_of_lane_marks):
    lane_marks_list.append(pygame.image.load("images/lanemarks.png"))
    lane_marks_x.append(843)
    lane_marks_x.append(530)
    lane_marks_y.append(100)
    lane_marks_y_change.append(st.values[2])

# initialize window
pygame.init()
font = pygame.font.Font("font/the_font_namco.ttf", 20)
screen = pygame.display.set_mode((1366, 768))
background_image = pygame.transform.scale(background_image, (1366, 768))
pygame.display.set_caption("Racing Fury | By Maaz")
pygame.display.set_icon(icon)

# background music
musics = ["sounds/bg1.mp3", "sounds/bg2.mp3", "sounds/bg3.mp3",
          "sounds/bg4.mp3"]
music_file = random.choice(musics)
pygame.mixer.music.load(music_file)
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
    points_label = font.render(str(int(points_counter)), True, (0, 255, 0))
    screen.blit(points_label, (10, 10))
    highest_score_label = font.render("highest score", True, (255, 255, 255))
    screen.blit(highest_score_label, (1050, 10))
    highest_score = font.render(str(int(st.values[4])), True, (0, 255, 0))
    screen.blit(highest_score, (1150, 50))
    current_mode_label = font.render("current mode", True, (255, 255, 255))
    screen.blit(current_mode_label, (1050, 250))
    current_mode = font.render(current_mode_selected, True, mode_color)
    screen.blit(current_mode, (1150, 290))


def play_again():
    global music_file, musics
    music_file = random.choice(musics)
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(-1)
    global car_x, car_y, points_counter, barrier_y, barrier_x, barrier_y_change, barrier_x_pos, coll_check
    car_x = 682
    car_y = 600
    points_counter = 0
    barrier_x = random.choice(barrier_x_pos)
    barrier_y = 10
    barrier_y_change = st.values[1]


def right_highest_score_to_file():
    st.values[4] = points_counter
    with open("settings.py", "w") as f:
        f.write("values = " + str(st.values) + "\n# setting fps, mode, lane_speed, car, highest_score\n")
        f.close()


clock = pygame.time.Clock()

# The game loop
while loop:
    clock.tick(fps)
    screen.fill((0, 0, 0))
    screen.blit(background_image, (0, 0))

    # Handle Keyboard Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                car_x_change = 30
            if event.key == pygame.K_LEFT:
                car_x_change = -30
            if event.key == pygame.K_SPACE and game_over:
                play_again()  # Restart the game
                game_over = False
        if event.type == pygame.KEYUP:
            car_x_change = 0

        # Handle joystick events
        if joystick_count > 0:
            if event.type == pygame.JOYAXISMOTION:
                if event.axis == 0:  # X-axis
                    car_x_change = event.value * 25
            if event.type == pygame.JOYBUTTONDOWN and game_over:
                if event.button == 5:  # R1 button index may vary, adjust accordingly
                    play_again()
                    game_over = False

    if not game_over:  # Only update game logic if the game is not over
        # Increase points
        coll_check = collision(car_x, barrier_x, car_y, barrier_y)
        if not coll_check:
            points_counter += 0.5
        if points_counter % 50 == 0:
            barrier_y_change += 1
            car_y -= 0.5
        if points_counter > st.values[4]:
            st.values[4] = points_counter

        for n in range(no_of_lane_marks):
            lane_marks_y[n] += lane_marks_y_change[n]
            draw_lanes(lane_marks_x[n], lane_marks_y[n], n)
            if lane_marks_y[n] > 766:
                lane_marks_y[n] = 10

        # Change Barrier Pos
        barrier_y += barrier_y_change
        if barrier_y > 766:
            barrier_y = -20
            barrier_x = random.choice(barrier_x_pos)

        # Change Car Pos
        car_x += car_x_change
        if car_x < 387:
            car_x = 387
        if car_x > 900:
            car_x = 900

        # Check for the Collision
        if coll_check:
            game_over = True
            pygame.mixer.music.stop()
            pygame.mixer.Sound("sounds/explosion.wav").play()
            car_x_change = 0
            barrier_y_change = 0
            if points_counter >= st.values[4]:
                right_highest_score_to_file()

    draw_barrier(barrier_x, barrier_y)
    draw_car(car_x, car_y)
    show_points()

    # Handle Game Over
    if game_over:
        game_over_label = font.render("game over!", True, (255, 0, 0))
        restart_label = font.render("press space bar!", True, (255, 0, 0))
        screen.blit(game_over_label, (550, 25))
        screen.blit(restart_label, (550, 60))

    pygame.display.update()
