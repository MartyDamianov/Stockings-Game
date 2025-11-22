import pygame
import os

class lives(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(lives, self).__init__()
        self.image = os.path.realpath("heart.png")
        self.image = pygame.image.load(self.image)

        self.x = x
        self.y = y

        self.num = 10
        self.size = (510 / self.num, 510 / self.num)
        self.image = pygame.transform.scale(self.image, self.size)

    def draw(self, window):
        window.blit(self.image, [self.x, self.y])
