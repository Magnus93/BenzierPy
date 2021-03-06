import pygame
import math
import sys
import mouse
import SubCoordSys
import trans2D
import shapes 

screen = pygame.display.set_mode((800,600))
pygame.font.init()
mytimer = pygame.time.Clock()
font = pygame.font.SysFont("verdana", 11)

DRAW_GRID = False

class Moveble:
    def __init__(self, x, y, color=0xffffff):
        self.x = x
        self.y = y
        self.color = color
        self.hover = False
        self.active = False
        self.selected = False
        self.typeName = "Moveble"

    def select(self):
        self.selected = True

    def deselect(self):
        self.selected = False

    def setColor(self, color):
        self.color = color
    def setPos(self, x, y):
		self.x = x
		self.y = y

    def getTypeName(self):
        return self.typeName

    def isActive(self):
        return self.active 

    def getPos(self):
        return (self.x, self.y)

    def run(self):
        if (self.isHit() and mouse.down[0] and self.selected):
            self.active = True 
        if (mouse.up[0]):
                self.active = False 
        if (self.active):
            (MX, MY) = mouse.pos
            self.x = MX
            self.y = MY 

class Circle(Moveble):
    def __init__(self, x, y, r):
        Moveble.__init__(self, x, y)
        self.r = r

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.r, 1)
        if (self.selected):
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.r-4)
    
    def isHit(self):
        (MX, MY) = mouse.pos
        return ((self.x-MX)**2 + (self.y-MY)**2) < self.r**2

    def nearestEdge(self, (xIn, yIn)):
        distIn = trans2D.distance((self.x, self.y), (xIn, yIn))
        distEdge = self.r 
        xDistIn = xIn - self.x 
        yDistIn = yIn - self.y 
        xDistEdge = xDistIn*distEdge/(distIn+0.1)
        yDistEdge = yDistIn*distEdge/(distIn+0.1)
        xEdge = xDistEdge + self.x 
        yEdge = yDistEdge + self.y 
        return (int(xEdge), int(yEdge))

    def run(self):
        self.draw()
        Moveble.run(self) 

class Rect(Moveble):
    def __init__(self, x, y, w, h):
        Moveble.__init__(self, x, y)
        self.w = w 
        self.h = h
    
    def isHit(self):
        (MX, MY) = mouse.pos
        if (self.x-self.w/2 < MX < self.x+self.w/2):
            return self.y-self.h/2 < MY < self.y+self.h/2
        else:
            return False    

    def nearestEdge(self, (xIn, yIn)): 
        boxSlope = trans2D.slope(self.w, self.h)
        inputSlope = trans2D.slope(xIn - self.x, yIn - self.y )  
        if ( -boxSlope < inputSlope < boxSlope):
            sign = trans2D.sign(xIn-self.x)
            xEdge = sign*(self.w/2) + self.x 
            yEdge = sign*(self.w/2)*inputSlope + self.y 
        else:
            sign = sign = trans2D.sign(yIn-self.y) 
            xEdge = sign*(self.h/2)/(inputSlope) + self.x 
            yEdge = sign*(self.h/2) + self.y 
        return (int(xEdge), int(yEdge))

    def draw(self):
        rect = (self.x-self.w/2, self.y-self.h/2, self.w, self.h)
        pygame.draw.rect(screen, self.color, rect, 1)
        if (self.selected):
            rectIn = (self.x-self.w/2+3, self.y-self.h/2+3, self.w-6, self.h-6)
            pygame.draw.rect(screen, self.color, rectIn)

    def run(self):
        self.draw()
        Moveble.run(self)  
    

'''
class Handle(Circle):
    def __init__(self, mv1, mv2, dist, angle):
        mvAngle = math.atan((mv2.y-mv1.y)/(mv2.x-mv1.x))
        self.m1 = mv1
        self.m2 = mv2
        
        x = int(mv1.x+dist*math.cos(angle+mvAngle))
        y = int(mv1.y+dist*math.sin(angle+mvAngle))
        Circle.__init__(self, x, y, 6)
        #self.dist = dist
        #self.angle = angle
    
    def getPos(self):
		return (self.x, self.y)
    
    def run(self):
        Circle.run(self)
        pygame.draw.line(screen, 0x00ffff, (self.x, self.y), (self.m1.x, self.m1.y), 1)
        pass
    
class Anchor:
    def __init__(self, mv, hd):
        self.m = mv
        self.h = hd
        #Radie = 30
        dist = math.sqrt((self.h.x-self.m.x)**2 +((self.h.y-self.m.y)**2))
        #self.x = self.m.x + (self.m.x * (self.h.x-self.m.x))/()
        self.x = self.m.x + (self.m.y * (self.h.x-self.m.x) / dist)
        self.y = self.m.y + (self.m.y * (self.h.y-self.m.y) / dist)
        
    def draw(self):
        dist = math.sqrt((self.h.x-self.m.x)**2 +((self.h.y-self.m.y)**2))
        self.x = self.m.x + (self.m.r * (self.h.x-self.m.x) / dist)
        self.y = self.m.y + (self.m.r * (self.h.y-self.m.y) / dist)
        top = (self.x, self.y) 
        left  = (self.x-5, self.y+15)
        right = (self.x+5, self.y+15)
        pygame.draw.polygon(screen, (0xff0000), [top, left, right])

class Line:
    def __init__(self, move1, move2):
        self.m1 = move1
        self.m2 = move2
        self.cooSys = SubCoordSys.CoordSys(move1, move2)
        self.deltaX = self.m2.x - self.m1.x
        self.deltaY = self.m2.y - self.m1.y
        self.distance = math.sqrt((self.deltaX**2)+(self.deltaY**2))
        self.rotation = math.atan(self.deltaY/self.deltaX)
        
        ##-------Handle------
        self.handle1 = Handle(self.m1, self.m2, 0.25*self.distance, 0)
        self.handle1LocalPos = self.cooSys.worldToLocal(self.handle1.getPos())
  
        self.handle2 = Handle(self.m2, self.m1, 0.25*self.distance,0 )
        self.handle2LocalPos = self.cooSys.worldToLocal(self.handle2.getPos())
        
        ##-----Handle End -----
        
        self.anchor1 = Anchor(self.m1, self.handle1)
        self.anchor2 = Anchor(self.m2, self.handle2)
    
    def checkCoordUpdate(self):
		if (self.handle1.active or self.handle2.active):
			self.handle1LocalPos = self.cooSys.worldToLocal(self.handle1.getPos())
			self.handle2LocalPos = self.cooSys.worldToLocal(self.handle2.getPos())
		if (self.m1.active or self.m2.active):
			h1Pos = self.cooSys.localToWorld(self.handle1LocalPos)
			(self.handle1.x, self.handle1.y) = h1Pos
			h2Pos = self.cooSys.localToWorld(self.handle2LocalPos)
			(self.handle2.x, self.handle2.y) = h2Pos
        
    def draw(self, drawGrid=False):
		self.checkCoordUpdate()
		if drawGrid:
			self.cooSys.drawGrid()
		self.handle1.run()
		self.handle2.run()
		self.anchor1.draw()
		self.anchor2.draw()
        
		t = 0
		pointlist = []
		p0 = (self.m1.x, self.m1.y) 
		p1 = (self.handle1.x, self.handle1.y)
		p2 = (self.handle2.x, self.handle2.y)
		p3 = (self.m2.x, self.m2.y) 
		while(t<1):
			bx = ((1-t)*(1-t)*(1-t))*p0[0] + (3*((1-t)*(1-t))*t)*p1[0] + 3*(1-t)*(t*t)*p2[0] + (t*t*t)*p3[0] 
			by = ((1-t)*(1-t)*(1-t))*p0[1] + (3*((1-t)*(1-t))*t)*p1[1] + 3*(1-t)*(t*t)*p2[1] + (t*t*t)*p3[1]
			pointlist.append((bx,by))
			t += 0.02
		pygame.draw.aalines(screen, (100,255,255), False, pointlist)
'''  

if __name__ == "__main__":
    
    box = Circle(400, 300, 40)
    
    while(True):
        
        screen.fill(0x101010)
        mouse.run()

        box.run()
        edge = box.nearestEdge(mouse.pos)
        pygame.draw.circle(screen, (255,255,255), edge, 5, 5)


        mouse.run()
        pygame.display.flip()
        mytimer.tick(24)
