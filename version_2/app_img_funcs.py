import random
from pygame import Rect, image, transform

block_total_height = 500


def create_img_surface(path: str):
    """
    Create a Surface of the image
    """
    return image.load(path)


def resize_block(block):
    """
        Resize/recreate buildind blocks to avoid (width, height)
        Space where bird can pass is 150
        Total height of block is 600 - 100(floor) - 150
    """

    # Minimum height of one of blocks is 100
    block_height = random.randint(100, 250)
    block_1_top = transform.scale(block, (200, block_height))
    block_1_bottom = transform.scale(block, (200, 350 - block_height))

    return [block_1_top, block_1_bottom]


def display_img(screen, block, width, height):
    """
    Display images
    """
    screen.blit(block, (width, height))


def place_block(block_top, block_bottom, screen_width: int):
    """
    Place building blocks at the beggining of screen width.
    """
    # block_total_height = 500
    block_top.x = screen_width
    block_bottom.x = screen_width

    block_1_top_height = random.randrange(50, 300)
    block_1_bottom_height = block_total_height - (block_1_top_height+100)
    block_top.height = block_1_top_height
    block_bottom.top = block_1_top_height + 100
    block_bottom.height = block_1_bottom_height