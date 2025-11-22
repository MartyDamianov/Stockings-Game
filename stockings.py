from math import floor
from player import *
from candy import *
from lives import *
from menu import *
from bar import *
import pygame.freetype
import pygame
import random
import os

pygame.init()
pygame.freetype.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode([600, 600])

pygame.display.set_caption("Stocking Run")
icon = pygame.image.load(os.path.realpath("present.png"))
pygame.display.set_icon(icon)

class text:
    def __init__(self, text, x, y, color, font, size, window):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.font = font
        self.size = size
        self.window = window
        
        self.ft_font = pygame.freetype.SysFont(self.font, self.size)

    def update(self):
        self.ft_font = pygame.freetype.SysFont(self.font, round(self.size))

    def draw(self, y):
        #self.x = self.x - ((len(num) * self.size) / 2)
        text_rect = self.ft_font.get_rect(self.text)
        text_rect.center = (self.x, self.y + y)#(self.x - ((len(str(self.text)) * (self.size / 2)) / 2), self.y)
        self.ft_font.render_to(self.window, text_rect.topleft, f"{self.text}", self.color)

def destroy(c, index):
    global candys
    candys[index].kill()
    candys.pop(index)
    if len(candys) <= 12:
        candys.append(create_candy())

def candy_check(c, index):
    global candys, spawn, count, hearts, running, run
    collide = c.collide(s.x, s.y + s.offset)

    if c.y < 250:
        return

    if c.draw(window):
        destroy(c, index)
        return True
    
    if c.collide(s.x, s.y + s.offset):            
        if c.check():
            score.text = str(int(score.text) + 1)
            Sound("Jingle Ring.mp3")

            destroy(c, index)
            if count >= (3 * spawn) // 1.25:
                spawn = spawn + 1
                count = 0

                for x in range(floor(spawn)):
                    candys.append(create_candy())
                    if len(candys) > 12:
                        break
            count = count + 1
            return True

        destroy(c, index)
        hearts[len(hearts) - 1].kill()
        hearts.pop(len(hearts) - 1)
        Sound("Bell Ringing.mp3")
        if hearts == []:
            running = False
            run = True
            front()
            Set()
        return True
        
def create_candy():
    rand = random.randint(1, 12)
    name = ""
    if rand <= 4:
        rand = random.choice(["Candy 1", "Candy 2", "Candy 3"])
    elif rand == 5 or rand == 6:
        rand = random.choice(["present", "present 2", "present 3"])
    elif rand == 7:
        rand = "chocolate"
    elif rand == 8:
        rand = "candy cane"
    elif rand >= 9 and rand <= 12:
        rand = random.choice(["broccoli", "carrot", "coal"])
    return candy(rand)
    

def Set():
    global spawn, count, s, candys, b, score, hearts
    spawn = 0
    count = 1
    s = stocking()
    candys = [create_candy()]#candy("carrot")
    b = bar()
    score = text("0", 300, 50, (0, 0, 0), None, 40, window)

    hearts = []
    for x in range(3):
        hearts.append(lives(10 + (x * 55), 10))
Set()

image = os.path.realpath("background.png")
image = pygame.image.load(image)

image2 = os.path.realpath("settings.png")
image2 = pygame.image.load(image2)

mode = 2
speed = 1
sound = True
music = True
songs = ["Christmas Story", "Happy Santa", "Joyful Snowman", "Christmas Eve"]
def new_song(songs):
    global music
    if music:
        song = random.choice(songs)
        pygame.mixer.music.load(os.path.realpath(f"{song}.mp3"))
        pygame.mixer.music.play(1)
new_song(songs)

def Sound(name):
    global sound
    if sound:
        bell = pygame.mixer.Sound(os.path.realpath(name))
        bell.play()

def func():
    global run, running
    run = False
    running = True
    B.kill()
    B1.kill()
def func2():
    global Run
    Run = False
def func3():
    global speed, mode
    switch3[0].update(["x2 (light)", "x2 (dark)"])
    switch3[1].set("SAS (light)")
    speed = 2
    mode = 1
def func4():
    global music
    switch1[0].update(["on (light)", "on (dark)"])
    switch1[1].set("off (light)")
    pygame.mixer.music.unpause()
    music = True
def func5():
    global music
    switch1[1].update(["off (light)", "off (dark)"])
    switch1[0].set("on (light)")
    pygame.mixer.music.pause()
    music = False
def func6():
    global sound
    switch2[0].update(["on (light)", "on (dark)"])
    switch2[1].set("off (light)")
    sound = True
def func7():
    global sound
    switch2[1].update(["off (light)", "off (dark)"])
    switch2[0].set("on (light)")
    sound = False
def func8():
    global mode
    switch3[1].update(["SAS (light)", "SAS (dark)"])
    switch3[0].set("x2 (light)")
    mode = 2

global Run
global buttons, switch1, switch2
Run = True
Exit= button("exit", func2, 0.015, 620, 40, 4, 5)
switch1 = [button("on (dark)", func4, 0, 380, 225, 8, 0), button("off (light)", func5, 0, 450, 225, 8, 0)]
switch2 = [button("on (dark)", func6, 0, 380, 287, 8, 0), button("off (light)", func7, 0, 450, 287, 8, 0)]
switch3 = [button("x2 (light)", func3, 0, 380, 160, 8, 0), button("SAS (dark)", func8, 0, 457, 162, 7.2, 0)]

def Settings():
    global running, run, Run, buttons, switch1, switch2, music, mode, speed
    
    while Run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                run = False
                Run = False
                for b in switch1 + switch2 + switch3:
                    b.kill()
                Exit.kill()

        if pygame.mixer.music.get_busy() == False and music:
            new_song(songs)

        window.blit(image2, [0, 0])
        Exit.draw(window)
        for s in switch1:
            s.draw(window)
        for s2 in switch2:
            s2.draw(window)
        for s3 in switch3:
            s3.draw(window)
        pygame.display.flip()
    Run = True

    if switch3[0].Image == "x2 (light)" and switch3[1].Image == "SAS (light)":
        mode = 1
        speed = 1

run = True
running = True
B = button("button", func, 0.015, 300, 300, 3, 15)
B1 = button("button 2", Settings, 0.015, 300, 550, 4, 10)
def front():
    global running, run, B, B1
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                run = False

        if pygame.mixer.music.get_busy() == False and music:
            new_song(songs)
                
        window.fill((0, 0, 0))
        draw(window, [B, B1])
        pygame.display.flip()
front()

for x in range(10):#This is here becuase of a "wake up call" for clock.get_fps()
    clock.tick()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            pass

    if pygame.mixer.music.get_busy() == False and music:
        new_song(songs)

    #window.fill((204, 243, 255))
    window.fill((0, 0, 0))
    window.blit(image, [0, 0])

    for c in range(len(candys)):
        candys[c].move(0.1 * speed, 0.25 * speed)
        candys[c].draw(window)
        candy_check(candys[c], c)
        #if candy_check(candys[c], c): break

    s.update(0.5 * speed, 0.005 * speed)
    s.draw(window, b.sin[round(b.index)] / 1.5)

    b.draw(window, 0.02 * speed)
    score.draw(b.sin[round(b.index)])
    for l in hearts:
        l.draw(window)

    #pygame.draw.line(window,(0, 255, 0), (s.x + 60, s.y + 40 + s.offset), (s.x + (320 / 2), s.y + 40 + s.offset))

    clock.tick()
    if mode == 2:
        speed = 746 / clock.get_fps()
    
    pygame.display.flip()

pygame.quit()
