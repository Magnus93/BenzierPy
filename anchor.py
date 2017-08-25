import pygame
from math import *
import sys
import mouse

screen = pygame.display.set_mode((800,600))
pygame.font.init()
mytimer = pygame.time.Clock()
font = pygame.font.SysFont("verdana", 11)



class moveble:
    def __init__(x,y):
        self.x
        self.y
        self.hover
        self.active


class circle(moveble):
    def __init__(self, name, x, y):
        self.name = name
        self.r = 30
        self.offCol = 0x999999 
        self.onCol  = 0xffffff
        self.col    = self.offCol
        self.hover = False
        self.active = False
        
    def draw(self):
        pygame.draw.circle(screen, self.col, (self.x, self.y), self.r+3)
        pygame.draw.circle(screen, 0x000000, (self.x, self.y), self.r)
        text = font.render(self.name, 1, (0,200,200))
        
        screen.blit(text, (self.x,self.y))
    
    def run(self):
        self.draw()
        (MX, MY) = mouse.pos
        if (((self.x-MX)**2 + (self.y-MY)**2) < self.r**2):
            self.hover = True
        else:
            self.hover=False
        
        if self.hover and mouse.down[0]:
            self.active = True
            self.col = self.onCol
        if mouse.up[0]:
            self.active = False
            self.col = self.offCol
        if self.active:
            self.x = MX
            self.y = MY


class line:
    def __init__(self, circle1, circle2):
        self.c1 = circle1
        self.c2 = circle2
        deltaX = circle2.x - circle1.x
        deltaY = circle2.y - circle1.y
        self.handle1 = (int(circle1.x + deltaX*0.25), int(circle1.y + deltaY*0.25))
    
    def draw(self):
        
        pygame.draw.line(screen, 0x00ff00, (self.c1.x, self.c1.y), (self.c2.x, self.c2.y))
        pygame.draw.circle(screen, 0xff0000, (self.handle1), 5)


if __name__ == "__main__":
    
    circ1 = circle("Magnus", 40, 40)
    circ2 = circle("Arne", 60, 200)
    line1 = line(circ1, circ2)
    
    while(True):
        
        screen.fill(0x222222)
        
        circ1.run()
        circ2.run()
        line1.draw()
        
        mouse.run()
        pygame.display.flip()
        mytimer.tick(24)
