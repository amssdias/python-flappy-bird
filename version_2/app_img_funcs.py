from pygame import Rect, image, transform

import random

block_total_height = 500

def create_img_surface(path: str):
    """
    Create a Surface of the image
    """
    return image.load(path)


def resize_block(block) -> list:
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

