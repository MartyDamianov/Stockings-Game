from random import randint
import pygame
import os

class candy(pygame.sprite.Sprite):
    def __init__(self, imageName):
        super(candy, self).__init__()
        self.imageName = imageName
        self.image = os.path.realpath(f"{imageName}.png")
        self.image = pygame.image.load(self.image)

        self.x = randint(75, 530)
        self.y = 0
        
        self.num = 7#5.5
        self.angle = 0
        self.size2 = pygame.image.load(os.path.realpath(f"{imageName}.png")).get_rect().size

        self.size = (self.size2[0] / self.num, self.size2[1] / self.num)
        self.image = pygame.transform.scale(self.image, self.size)
        self.control = self.image
        self.surface = self.image.convert()

        self.rectangle = self.surface.get_rect()
        self.rectangle.center = [self.x, self.y]

    def check(self):
        if self.imageName == "carrot" or self.imageName == "broccoli" or self.imageName == "coal":
            return False
        return True

    def collide(self, x, y):
        x2 = self.x + (self.size2[0] / self.num / 2)
        y2 = self.y + (self.size2[1] / self.num / 2)
        if y2 < y + 25 and y2 > y - 1 and x2 > x + 60 and x2 < (x + (320 / 2) - 30):
            return True
        return False

    def move(self, speed, angle):
        self.y = self.y + speed
        self.rotate(angle)

    def rotate(self, angle):
        self.angle = self.angle + angle
        self.image = pygame.transform.rotate(self.control, self.angle)

    def draw(self, window):
        self.rectangle.center = [self.x, self.y]
        window.blit(self.image, self.rectangle.center)

        if self.y > 600:
            return True
        return False
