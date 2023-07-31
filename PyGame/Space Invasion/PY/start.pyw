import pygame
import random
import math
import os

points = 0

pygame.init()
os.system('cls')
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invasion")

# Initialize joystick
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()
if joystick_count > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

# PLay Music
pygame.mixer.music.load("utilities/sounds/background.wav")
pygame.mixer.music.play(-1)

# Background Image
background = pygame.image.load("utilities/images/background.png")

# Player Settings
player_img = pygame.image.load("utilities/images/spaceship.png")
player_x = 370
player_y = 530
player_x_pos_change = 0
# player_y_pos_change = 0

# Enemy Settings
enemy_img = pygame.image.load("utilities/images/ufo.png")
enemy_x = random.randint(0, 735)
enemy_y = random.randint(50, 100)
enemy_x_pos_change = 9
enemy_y_pos_change = 80

# Bullet
bullet_img = pygame.image.load("utilities/images/bullet.png")
bullet_x = 0
bullet_y = 530
bullet_condition = "Ready"
bullet_x_pos_change = 0
bullet_y_pos_change = 15

font = pygame.font.Font("utilities/font/the_font_namco.ttf", 16)
result_label_font = pygame.font.Font("utilities/font/the_font_namco.ttf", 18)
result_label = result_label_font.render("game over!", True, (255, 0, 0))


# show the points
def show_points():
    points_label = font.render("points * " + str(points), True, (0, 200, 0))
    screen.blit(points_label, (320, 25))


# Fire
def bullet(x, y):
    global bullet_condition
    bullet_condition = "Fire"
    screen.blit(bullet_img, (x + 10, y))


# Player Draw
def player(x, y):
    screen.blit(player_img, (x, y))


# Draw Enemy
def enemy(x, y):
    screen.blit(enemy_img, (x, y))


# Collision Detection
def collision(x1, x2, y1, y2):
    distance = math.sqrt((math.pow(x2 - x1, 2)) + (math.pow(y2 - y1, 2)))
    if distance < 40:
        return True
    else:
        return False


# game Loop
loop = True
while loop:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_UP:
            #     player_y_pos_change = -0.5
            # if event.key == pygame.K_DOWN:
            #     player_y_pos_change = 0.5
            if event.key == pygame.K_RIGHT:
                player_x_pos_change = 4.36
            if event.key == pygame.K_LEFT:
                player_x_pos_change = -4.36
            if event.key == pygame.K_SPACE:
                bullet_x = player_x
                bullet(bullet_x, bullet_y)
                pygame.mixer.Sound("utilities/sounds/laser.wav").play()
        if event.type == pygame.KEYUP:
            player_x_pos_change = 0
        # Handle joystick events
        if joystick_count > 0:
            if event.type == pygame.JOYAXISMOTION:
                if event.axis == 0:  # X-axis
                    player_x_pos_change = event.value * 7
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 7:  # R1 button index may vary, adjust accordingly
                    bullet_x = player_x
                    bullet(bullet_x, bullet_y)
                    pygame.mixer.Sound("utilities/sounds/laser.wav").play()

    # Update Player pos Val
    player_x += player_x_pos_change

    # Restrict Player x position
    if player_x < 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    # Update enemy pos val
    enemy_x += enemy_x_pos_change

    # Restrict enemy x Movements
    if enemy_x < 0:
        enemy_x_pos_change = 9
        # enemy_y += enemy_y_pos_change
    elif enemy_x >= 736:
        enemy_x_pos_change = -9
        enemy_y += enemy_y_pos_change
    elif enemy_y > 460:
        enemy_x_pos_change = 0
        enemy_y_pos_change = 0
        enemy_y = 10
        pygame.mixer.music.stop()
        pygame.mixer.Sound("utilities/sounds/gameover.wav").play()
        screen.blit(result_label, (280, 300))

    # Control Bullet
    if bullet_y < 20:
        bullet_y = 530
        bullet_condition = "ready"

    if bullet_condition == "Fire":
        bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_pos_change

    # Detect Bullet hit
    coll_check = collision(bullet_x, enemy_x, bullet_y, enemy_y)
    if coll_check:
        pygame.mixer.Sound("utilities/sounds/explosion.wav").play()
        bullet_y = 530
        bullet_condition = "Ready"
        # enemy_x_pos_change = 0
        # enemy_y_pos_change = 0
        points += 1
        enemy_x = random.randint(0, 735)
        enemy_y = random.randint(50, 100)
    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    show_points()
    pygame.display.update()
