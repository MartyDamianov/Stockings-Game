import pygame
import os

class stocking(pygame.sprite.Sprite):
    def __init__(self):
        super(stocking, self).__init__()
        self.image = os.path.realpath("stockings.png")
        self.image = pygame.image.load(self.image)

        self.velocity = 0
        self.right = True
        self.left = True
        
        self.num = 2
        self.size = (320 / self.num, 500 / self.num)
        self.image = pygame.transform.scale(self.image, self.size)
        self.surface = self.image.convert()

        self.x = 300 - (320 / (self.num * 2))
        self.y = 330
        self.offset = 0

        self.rectangle = self.surface.get_rect()
        self.rectangle.center = [self.x, self.y]

    def pos(self, x):
        if x <= 0:
            self.left = False
        elif x > 0:
            self.left = True
        if x >= (600 - (320 / self.num)):
            self.right = False
        elif x < (600 - (320 / self.num)):
            self.right = True
              
    def update(self, speed, speed2):#speed is the speed for moving, speed2 is the speed for drag and accleraoation
        Key = pygame.key.get_pressed()
        self.num2 = 600 - (320 / self.num)
        
        if self.x < self.num2 or self.x > 0:
            self.velocity = 0
        if Key [pygame.K_RIGHT] and self.right and self.x < self.num2:# == pygame.K_LEFT:
            self.velocity = self.velocity = speed
        elif Key [pygame.K_LEFT] and self.left and self.x > 0:# == pygame.K_LEFT:
            self.velocity = self.velocity = -speed
            

        if self.velocity > 0 and Key[pygame.K_RIGHT] == False:
            self.velocity = self.velocity - speed2
        elif self.velocity < 0 and Key[pygame.K_LEFT] == False:
            self.velocity = self.velocity + speed2

        if self.velocity > speed2 or self.velocity < -speed2:
            self.x = self.x + self.velocity
        #self.pos(self.x)
        self.rectangle.center = [self.x, self.y]

    def draw(self, window, y):
        self.offset = y
        self.rectangle.center = [self.x, self.y + y]
        window.blit(self.image, self.rectangle.center)

        
