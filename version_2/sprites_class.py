from pygame.sprite import Sprite
from pygame import image, transform


class Player(Sprite):
    def __init__(self, path):
        super().__init__()
        self.image = image.load(path)
        self.rect = self.image.get_rect()
        self.rect.x = 30

    def update(self, jumping):
        if jumping:
            self.rect.y -= 4
        else:
            self.rect.y += 4


class Blocks_top(Sprite):
    """
        Space where bird can pass is 150
        Total height of block is 600 - 100(floor) - 150
    """

    def __init__(self, path, height, pos_x):
        super().__init__()
        self.original_image = image.load(path)
        self.image = transform.scale(self.original_image, (200, height))
        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = pos_x

    def update(self):
        self.rect.x -= 3


class Blocks_bottom(Sprite):
    def __init__(self, path, height, pos_x, pos_y):
        super().__init__()
        self.original_image = image.load(path)
        self.image = transform.scale(self.original_image, (200, height))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def update(self):
        self.rect.x -= 3