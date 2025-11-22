import numpy as np
import pygame
import os

class bar(pygame.sprite.Sprite):
    def __init__(self):
        super(bar, self).__init__()
        self.image = os.path.realpath("bar.png")
        self.image = pygame.image.load(self.image)

        self.num = 4.5
        self.size = (619 / self.num, 302 / self.num)
        self.image = pygame.transform.scale(self.image, self.size)
        self.surface = self.image.convert()

        self.index = 0
        self.sin = np.sin(np.linspace(0, 2 * np.pi, 50)) * 15

        self.x = 300 - (619 / (self.num * 2))
        self.y = 20

    def draw(self, window, speed):
        self.index = self.index + speed
        if round(self.index, 1) >= 49.5:
            self.index = 0
        window.blit(self.image, [self.x, self.y + self.sin[round(self.index)]])
