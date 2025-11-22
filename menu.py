import numpy as np
import pygame
import os

pygame.init()
class button(pygame.sprite.Sprite):
    def __init__(self, image, func, speed, x, y, num, mul):
        super(button, self).__init__()
        self.Image = image
        self.image_name = os.path.realpath(f"{image}.png")
        self.image = pygame.image.load(self.image_name)

        self.count = 0
        self.num = num
        self.size2 = pygame.image.load(self.image_name).get_rect().size
        self.size = (self.size2[0] / self.num, self.size2[1] / self.num)
        self.image = pygame.transform.scale(self.image, self.size)
        self.surface = self.image.convert(self.image)

        self.func = func
        self.x = x - (667 / (self.num * 2))
        self.y = y - (290 / (self.num * 2))

        self.index = 0
        self.speed = speed
        self.sin = np.sin(np.linspace(0, 2 * np.pi, 50)) * mul

        self.rectangle = self.surface.get_rect()
        self.rectangle.center = [self.x, self.y]

    def shared(self, image):
        self.Image = image
        self.image_name = os.path.realpath(f"{image}.png")
        self.image = pygame.image.load(self.image_name)
        self.size2 = pygame.image.load(self.image_name).get_rect().size
        self.size = (self.size2[0] / self.num, self.size2[1] / self.num)
        self.image = pygame.transform.scale(self.image, self.size)

    def update(self, images):
        self.count = self.count + 1
        if self.count > 1:
            self.count = 0
        image = images[self.count]
        self.shared(image)

    def set(self, image):
        self.count = 0
        self.shared(image)
        
    def collide(self):
        x2, y2 = self.rectangle.center
        x, y = pygame.mouse.get_pos()
        if x > x2 and x < (x2 + self.size[0]) and y > y2 and y < (y2 + self.size[1]):
            return True
        return False

    def draw(self, window):
        self.index = self.index + self.speed
        if round(self.index, 1) == 49.5:
            self.index = 0
        self.rectangle.center = [self.x, self.y + self.sin[round(self.index)]]

        collide = self.collide()#self.rectangle.collidepoint(pygame.mouse.get_pos())
        if collide and pygame.mouse.get_pressed()[0] and self.click:
            self.func()

        self.click = True
        if pygame.mouse.get_pressed()[0]:
            self.click = False
        window.blit(self.image, self.rectangle.center)

#b = button()
image = os.path.realpath("cover.png")
image = pygame.image.load(image)

def draw(window, buttons):
    window.blit(image, [0, 0])
    for b in buttons:
        b.draw(window)
    
'''
def Image(image, num, angle):
    name = f"C:\\Users\\nteme\\OneDrive\\Desktop\\Christmas\\{image}.png"
    image = pygame.image.load(name)
    size = pygame.image.load(name).get_rect().size
    size = (size[0] / num, size[1] / num)
    image = pygame.transform.scale(image, size)
    image = pygame.transform.rotate(image, angle)
    return image

def draw(window):
    font = pygame.font.SysFont(None, 100)#64
    font2 = pygame.font.SysFont(None, 70)
    window.blit(Image("Present", 2, -25), [-40, 320])
    window.blit(Image("Present 2", 1.5, 15), [320, 350])
    window.blit(render("Settings", font), (300 - (100 * (len("Settings") - 2) / 4), 30))
    window.blit(render("Speed", font2), (300 - (100 * (len("Speed") - 0) / 4), 140))
    window.blit(render("Music", font2), (300 - (100 * (len("Music") - 0) / 4), 205))
    window.blit(render("Sound", font2), (300 - (100 * (len("Sound") - 0) / 4), 270))
'''
'''def draw(window):
    #font = pygame.font.SysFont(None, 100)#64)
    window.blit(Image("Candy 1", 3.5, 120), [50, 120])
    window.blit(Image("carrot", 3.5, -25), [220, 370])
    window.blit(Image("present 2", 3.5, -50), [430, 90])
    window.blit(Image("Stockings", 1.5, 0), [350, 260])
    window.blit(Image("Stocking 2", 1.7, 15), [-20, 270])
    window.blit(render("Stocking", font), (300 - (100 * (len("Stocking") - 1) / 4), 30))
    window.blit(render("Run", font), (300 - (100 * (len("Run") - 1.2) / 2), 100))
'''

          
