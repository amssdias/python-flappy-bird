import pygame
import random

from version_2.sprites_class import Player, BlockTop, BlockBottom

# TODO
# Create sprite for blocks
    # Create different widths for each block
    # Update them to move
# Check if player hitted the floor, or blocks
# Create coins to build score


pygame.init()
clock = pygame.time.Clock()

# Sizes, colors, font and images 
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY = (102, 123, 249)
BACKGROUND = pygame.image.load("media/back.jpg")
BACKGROUND = pygame.transform.scale(BACKGROUND, (500, 600))
FONT = pygame.font.Font("freesansbold.ttf", 22)
GAME_OVER_TEXT = FONT.render("GAME OVER", False, WHITE, BLACK)

# Screen settings
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy bird")
icon = pygame.image.load("media/logo.jpg")
pygame.display.set_icon(icon)

# Create player
player = Player("media/bird.png")
jumping = False

# Create blocks
random_height = random.randint(100, 250)
blocks = []

for i in range(3):
    block_top = BlockTop("media/pipe.png", random_height, SCREEN_WIDTH)
    block_bottom = BlockBottom("media/pipe.png", 350 - random_height, SCREEN_WIDTH, block_top.rect.bottom + 150)
    blocks.append([block_top, block_bottom])


all_sprites = pygame.sprite.Group()
block_sprites = pygame.sprite.Group()
all_sprites.add(player)

for block_top, block_b in blocks:
    all_sprites.add(block_top, block_bottom)
    block_sprites.add(block_top, block_bottom)


# Create point
score = 0

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

    pygame.draw.rect(screen, WHITE, floor)
    all_sprites.draw(screen)
    block_sprites.update()
    player.update(jumping)

    if jumping:
        end_of_jump = pygame.time.get_ticks()

        if end_of_jump - start_of_jump >= 200:
            jumping = False
            

    # # If blocks go out of screen width (block width = 200)
    # for index, x in enumerate(blocks_x):
    #     if x <= -200:
    #         blocks[index] = resize_block(block_img)
    #         blocks_y[index][1] = blocks[index][0].get_height() + 150
    #         blocks_x[index] = SCREEN_WIDTH + 30
        

    pygame.display.update()
    clock.tick(60)