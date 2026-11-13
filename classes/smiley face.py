# template code for you to fill in when creating basic pygame art


# dimensions of the window
width = 700
height = 500

class Smiley:
    def __init__(self, size, color, eyeColor, x, y):
        self.x=x
        self.y=y
        self.size = size
        self.color = color
        self.eyeColor = eyeColor

    def draw(self, canvas):
        pygame.draw.circle(canvas, self.color, (self.x, self.y), self.size)
        pygame.draw.circle(canvas, self.eyeColor, (self.x - self.size//3, self.y - self.size//4), self.size//10)
        pygame.draw.circle(canvas, self.eyeColor, (self.x + self.size//3, self.y - self.size//4), self.size//10)
        pygame.draw.rect(canvas, self.eyeColor, (self.x - self.size//4, self.y + self.size//4, self.size//2, self.size//8))

face1 = Smiley(100, (255, 255, 0), (0, 0, 255), 200, 200)
face2 = Smiley(50, (200, 100, 0), (0, 0, 0), 400, 400)
face3 = Smiley(150, (0, 100, 0), (0, 0, 0), 400, 200)


def draw(canvas):
    # makes the background white
    canvas.fill((255,255,255))

    face1.draw(canvas)
    face2.draw(canvas)
    face3.draw(canvas)



# don't touch the below code!
################################

import pygame, sys
from pygame.constants import KEYDOWN
from pygame.locals import QUIT

pygame.init()
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Graphics Starter')
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
while True:
    draw(window)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()


















