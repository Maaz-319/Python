import pygame
import math

# variables
jumping_p_1 = False
jumping_p_2 = False
jump_count_p_1 = 10  # Number of pixels to jump
jump_count_p_2 = 10  # Number of pixels to jump
game_over = False  # Flag to track the game state

# importing Assets
background_image = pygame.image.load("utilities/images/background.png")
icon = pygame.image.load("utilities/images/icon.png")
player_1_img = pygame.image.load("utilities/images/player_1.png")
player_2_img = pygame.image.load("utilities/images/player_2.png")
bullet_1_img = pygame.image.load("utilities/images/bullet_1.png")
bullet_2_img = pygame.image.load("utilities/images/bullet_2.png")

# Attributes
# Player_1
player_1_x = 20
player_1_y = 450
player_1_x_change = 0
player_1_y_change = 0
player_1_health = 100

# Player_2
player_2_x = 700
player_2_y = 450
player_2_x_change = 0
player_2_y_change = 0
player_2_health = 100

# Bullet_1
bullet_1_x = 0
bullet_1_y = 455
bullet_1_x_change = 40
bullet_1_state = "loaded"

# Bullet_2
bullet_2_x = 0
bullet_2_y = 455
bullet_2_x_change = 40
bullet_2_state = "loaded"

# Initialize Screen
pygame.init()
screen = pygame.display.set_mode((800, 600))
font = pygame.font.Font("utilities/font/the_font_namco.ttf", 20)
pygame.display.set_caption("Dual Bullet Blitz | By Maaz")
pygame.display.set_icon(icon)
pygame.mixer.music.load("utilities/sounds/bg.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

# Initialize joystick
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()

if joystick_count > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()


# Defining Functions
def draw_player_1(x, y):
    screen.blit(player_1_img, (x, y))


def draw_player_2(x, y):
    screen.blit(player_2_img, (x, y))


def draw_bullet_1(x, y):
    global bullet_1_state
    screen.blit(bullet_1_img, (x+16, y-1))
    bullet_1_state = "Fire"


def draw_bullet_2(x, y):
    global bullet_2_state
    screen.blit(bullet_2_img, (x+16, y-1))
    bullet_2_state = "Fire"


def track_bullet_1_collision(x1, x2, y1, y2):
    distance = math.sqrt((math.pow(x2 - x1, 2)) + (math.pow(y2 - y1, 2)))
    if distance < 20:
        return True
    else:
        return False


def track_bullet_2_collision(x1, x2, y1, y2):
    distance = math.sqrt((math.pow(x2 - x1, 2)) + (math.pow(y2 - y1, 2)))
    if distance < 20:
        return True
    else:
        return False


def show_player_1_health():
    player_1_health_label = font.render(str(player_1_health), True, (200, 0, 0))
    screen.blit(player_1_health_label, (150, 10))


def show_player_2_health():
    player_2_health_label = font.render(str(player_2_health), True, (200, 0, 0))
    screen.blit(player_2_health_label, (600, 10))


clock = pygame.time.Clock()

loop = True
while loop:
    clock.tick(60)  # restrict fps to 60
    screen.fill((0, 0, 0))
    screen.blit(background_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_over:
                player_1_x = 20
                player_2_x = 700
                game_over = False
                player_1_health = player_2_health = 100
                pygame.mixer.music.load("utilities/sounds/bg.mp3")
                pygame.mixer.music.set_volume(0.3)
                pygame.mixer.music.play(-1)

            if not game_over:
                if event.key == pygame.K_UP:
                    pygame.mixer.Sound("utilities/sounds/jump.wav").play()
                    if not jumping_p_1:
                        jumping_p_1 = True
                if event.key == pygame.K_KP8:
                    pygame.mixer.Sound("utilities/sounds/jump.wav").play()
                    if not jumping_p_2:
                        jumping_p_2 = True
                if event.key == pygame.K_SPACE:
                    pygame.mixer.Sound("utilities/sounds/gunshot.wav").play()
                    bullet_1_x = player_1_x
                    bullet_1_y = player_1_y
                    draw_bullet_1(bullet_1_x, bullet_1_y)
                if event.key == pygame.K_p:
                    pygame.mixer.Sound("utilities/sounds/gunshot.wav").play()
                    bullet_2_x = player_2_x
                    bullet_2_y = player_2_y
                    draw_bullet_2(bullet_2_x, bullet_2_y)
    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            player_1_x += 5
        elif keys[pygame.K_LEFT]:
            player_1_x -= 5
        if keys[pygame.K_KP6]:
            player_2_x += 5
        elif keys[pygame.K_KP4]:
            player_2_x -= 5
        # if keys[pygame.K_SPACE]:
        #     print("Space")
        #     bullet_1_x = player_1_x
        #     bullet_1_y = player_1_y
        #     draw_bullet_1(bullet_1_x, bullet_1_y)
        # if keys[pygame.K_p]:
        #     bullet_2_x = player_2_x
        #     bullet_2_y = player_2_y
        #     draw_bullet_2(bullet_2_x, bullet_2_y)

    # jumping_p_1 logic
    if jumping_p_1:
        if jump_count_p_1 >= -10:
            neg = 1
            if jump_count_p_1 < 0:
                neg = -1
            player_1_y -= (jump_count_p_1 ** 2) * 0.5 * neg
            jump_count_p_1 -= 1
        else:
            jumping_p_1 = False
            jump_count_p_1 = 10
    # jumping_p_2 logic
    if jumping_p_2:
        if jump_count_p_2 >= -10:
            neg = 1
            if jump_count_p_2 < 0:
                neg = -1
            player_2_y -= (jump_count_p_2 ** 2) * 0.5 * neg
            jump_count_p_2 -= 1
        else:
            jumping_p_2 = False
            jump_count_p_2 = 10

    # Update the position of player 1
    player_1_x += player_1_x_change
    player_1_y += player_1_y_change
    if player_1_y > 500:
        player_1_y = 450
    if player_1_x < 10:
        player_1_x = 10
    if player_1_x > 700:
        player_1_x = 700

    # Update Position of player 2
    player_2_x += player_2_x_change
    player_2_y += player_2_y_change
    if player_2_y > 500:
        player_2_y = 450
    if player_2_x < 10:
        player_2_x = 10
    if player_2_x > 700:
        player_2_x = 700

    # Update bullet_1 position
    if bullet_1_x > 800:
        bullet_1_x = player_1_x
        bullet_1_y = player_1_y
        bullet_1_state = "loaded"
    if bullet_1_state == "Fire":
        draw_bullet_1(bullet_1_x, bullet_1_y)
        bullet_1_x += bullet_1_x_change

    # Update bullet_2 position
    if bullet_2_x < 0:
        bullet_2_x = player_2_x
        bullet_2_y = player_2_y
        bullet_2_state = "loaded"
    if bullet_2_state == "Fire":
        draw_bullet_2(bullet_2_x, bullet_2_y)
        bullet_2_x -= bullet_2_x_change

    # Check bullet_1 collision
    collision_1 = track_bullet_1_collision(player_2_x, bullet_1_x, player_2_y, bullet_1_y)
    if collision_1 and not game_over:
        if bullet_1_state == "Fire":
            player_2_health -= 20
            bullet_1_x = player_1_x
            bullet_1_y = player_1_y
            bullet_1_state = "loaded"

    # Check bullet_2 collision
    collision_2 = track_bullet_2_collision(player_1_x, bullet_2_x, player_1_y, bullet_2_y)
    if collision_2 and not game_over:
        if bullet_2_state == "Fire":
            player_1_health -= 20
            bullet_2_x = player_2_x
            bullet_2_y = player_2_y
            bullet_2_state = "loaded"

    if player_1_health == 0:
        winner_label = font.render("player 2 wins", True, (0, 255, 0))
        screen.blit(winner_label, (270, 40))
        if not game_over:
            pygame.mixer.Sound("utilities/sounds/gameover.wav").play()
        game_over = True
        pygame.mixer.music.stop()
    elif player_2_health == 0:
        winner_label = font.render("player 1 wins", True, (0, 255, 0))
        screen.blit(winner_label, (270, 40))
        if not game_over:
            pygame.mixer.Sound("utilities/sounds/gameover.wav").play()
        game_over = True
        pygame.mixer.music.stop()

    draw_player_1(player_1_x, player_1_y)
    draw_player_2(player_2_x, player_2_y)
    show_player_1_health()
    show_player_2_health()
    pygame.display.update()
