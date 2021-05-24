import pygame
import random

from version_2.app_img_funcs import create_img_surface, place_block, resize_block, display_img

# TODO
# Create one more block and make him move
    # If block goes out of the width screen, make him go back
# Move player with variables (speed, width and height) so we can track position of player
# Check if player hitted the floor, or pipes
# Create coins to build score


pygame.init()
clock = pygame.time.Clock()

# Sizes, colors, font and images 
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY = (102, 123, 249)
BACKGROUND = create_img_surface("media/back.jpg")
BACKGROUND = pygame.transform.scale(BACKGROUND, (500, 600))
FONT = pygame.font.Font("freesansbold.ttf", 22)
GAME_OVER_TEXT = FONT.render("GAME OVER", False, WHITE, BLACK)

# Screen settings
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy bird")
icon = create_img_surface("media/logo.jpg")
pygame.display.set_icon(icon)

# Create player/bird (left, top, width, height)
PLAYER_IMAGE = create_img_surface("media/bird.png")
player_speed = 2
jumping = False


# Create buildind blocks
block_1 = resize_block(create_img_surface("media/pipe.png"))
block_y_1 = [0, block_1[0].get_height() + 150]
block_x = SCREEN_WIDTH
blocks_speed = 1

# Create point
score = 0
# coin_1 = pygame.Rect(block_1[0].left + 30, block_1[0].height + 45, 10, 10)
# coin_2 = pygame.Rect(block_2[0].left + 30, block_2[0].height + 45, 10, 10)


# Draw floor (surface, color, start_pos, end_pos, width)
floor = pygame.draw.line(screen, WHITE, (0, SCREEN_HEIGHT - 100), (SCREEN_WIDTH, SCREEN_HEIGHT - 100), width=5)


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start_of_jump = pygame.time.get_ticks()
                jumping = True

    # Draw into the screen
    screen.fill(SKY)
    # screen.blit(BACKGROUND, (0, 0))
    display_img(screen, block_1[0], block_x, block_y_1[0])
    display_img(screen, block_1[1], block_x, block_y_1[1])
    pygame.draw.rect(screen, WHITE, floor)
    # pygame.draw.rect(screen, WHITE, coin_1)
    # pygame.draw.rect(screen, WHITE, coin_2)


    # screen.blit(PLAYER_IMAGE, (100, SCREEN_HEIGHT/2))
    # If bird jumps
    if jumping:
        end_of_jump = pygame.time.get_ticks()

        screen.blit(PLAYER_IMAGE, (30, player_speed))
        player_speed -= 4

        if end_of_jump - start_of_jump >= 200:
            jumping = False
    else:
        screen.blit(PLAYER_IMAGE, (30, player_speed))
        player_speed += 2


    # Make blocks move
    block_x -= 1

    # If bird touches bottom of screen

    # If bird collide with blocks or floor
        
    
    pygame.display.update()
    clock.tick(60)