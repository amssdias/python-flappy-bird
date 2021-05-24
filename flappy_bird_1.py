import pygame
import random

from version_1.app_rects_funcs import place_block, create_block


pygame.init()
clock = pygame.time.Clock()

# Sizes, colors and font
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY = (102, 123, 249)
FONT = pygame.font.Font("freesansbold.ttf", 22)
GAME_OVER_TEXT = FONT.render("GAME OVER", False, WHITE, BLACK)

# Screen settings
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy bird")
icon = pygame.image.load("media/logo.jpg")
pygame.display.set_icon(icon)

# Create player/bird (left, top, width, height)
bird = pygame.Rect(100, SCREEN_HEIGHT/2 - 5, 20, 20)
bird_speed = 2
jumping = False

# Create buildind blocks 
block_total_height = 500
block_1 = create_block(SCREEN_WIDTH)
block_2 = create_block(SCREEN_WIDTH + 300)
blocks = block_1 + block_2
block_speed = 1

# Create point
score = 0
coin_1 = pygame.Rect(block_1[0].left + 30, block_1[0].height + 45, 10, 10)
coin_2 = pygame.Rect(block_2[0].left + 30, block_2[0].height + 45, 10, 10)

# Draw floor (surface, color, start_pos, end_pos, width)
floor = pygame.draw.line(screen, WHITE, (0, SCREEN_HEIGHT - 100), (SCREEN_WIDTH, SCREEN_HEIGHT - 100), width=5)

# So user can't jump anymore
game_over = False


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                start_of_jump = pygame.time.get_ticks()
                jumping = True


    # Draw into the screen
    screen.fill(SKY)
    pygame.draw.rect(screen, WHITE, bird)
    pygame.draw.rect(screen, WHITE, floor)
    for block in blocks:
        pygame.draw.rect(screen, WHITE, block)
    pygame.draw.rect(screen, WHITE, coin_1)
    pygame.draw.rect(screen, WHITE, coin_2)

    # If bird jumps
    if jumping:
        end_of_jump = pygame.time.get_ticks()
        bird.y -= 4

        if end_of_jump - start_of_jump >= 200:
            jumping = False
    else:
        bird.y += bird_speed
    
    block_1[0].x -= block_speed
    block_1[1].x -= block_speed
    block_2[0].x -= block_speed
    block_2[1].x -= block_speed
    coin_1.x -= block_speed
    coin_2.x -= block_speed

    # If blocks go out of the screen
    if block_1[0].x and block_1[1].x <= -70:
        place_block(block_1[0], block_1[1], SCREEN_WIDTH)
        coin_1.left = block_1[0].left + 30
        coin_1.top = block_1[0].height + 45

    if block_2[0].x and block_2[1].x <= -70:
        place_block(block_2[0], block_2[1], SCREEN_WIDTH)
        coin_2.left = block_2[0].left + 30
        coin_2.top = block_2[0].height + 45


    # If player touches floor or building blocks
    if bird.colliderect(block_1[0]) or bird.colliderect(block_1[1]) or \
        bird.colliderect(block_2[0]) or bird.colliderect(block_2[1]) or \
        bird.colliderect(floor):

        bird_speed = 0
        block_speed = 0
        screen.blit(GAME_OVER_TEXT, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        game_over = True
        
    if bird.colliderect(coin_1) or bird.colliderect(coin_2):
        score += 1
        if bird.colliderect(coin_1):
            coin_1.x = -10
        else:
            coin_2.x = -10

    score_text = FONT.render(f"Score: {score}", False, WHITE, BLACK)
    screen.blit(score_text, (20, 20))
    
    
    pygame.display.update()
    clock.tick(60)