import random
from pygame import Rect

block_total_height = 500

def create_block(screen_width):
    """
        Create buildind blocks to avoid (left, top, width, height)
        Space where bird can pass is 100
        Total height of block is 500 - 100(floor)
    """

    block_1_top_height = random.randrange(50, 300) # Get height of top block
    block_1_bottom_height = block_total_height - (block_1_top_height + 100) # Get height of bottom block
    block_1_top = Rect(screen_width, 0, 70, block_1_top_height)
    block_1_bottom = Rect(screen_width, block_1_top_height + 100, 70, block_1_bottom_height)

    return [block_1_top, block_1_bottom]



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