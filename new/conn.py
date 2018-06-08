import moveble 
'''
class Connection:
    def __init__(self, node0, node1=None):
        self.node0 = node0 # StartNode
        self.anchor0 = None
        self.handle0 = None
        self.setStartNode(node0)
        self.node1 = node1
        if (node1):
            self.setEndNode(node1) # EndNode
        else:
            self.anchor1 = Anchor(mouse.pos[0], mouse.pos[1])
        self.path = []
        self.calcPath(False)
        self.color = (255, 255, 255)

    def setStartNode(self, node):
        self.node0 = node
        (nx, ny) = node.nearestEdge(mouse.pos)
        self.anchor0 = Anchor(nx, ny)
        20*trans2D.sin((node.x, node.y), (nx, ny))
        20*trans2D.cos((node.x, node.y), (nx, ny))
        self.handle0 = Handle(node.x-nx, node.y-ny)
        
    def setEndNode(self, node):
        self.node1 = node
        (MX, MY) = mouse.pos
        (nx, ny) = node.nearestEdge(MX, MY)
        self.anchor1 = Anchor(nx, ny)

    def runWithoutEndNode(self):
        pass

    def setEndNode():
        pass 

    def getStartNode(self):
        return self.node0

    def setEndNode(self, node1):
        self.node1 = node1
        self.calcPath()

    def isHit(self):
        return False

    def draw(self):
        self.anchor0.run()    
        self.handle0.run()
        if (self.anchor1 and self.handle1):
            self.anchor1.run()
            self.handle1.run()
        pygame.draw.aalines(screen, self.color, False, self.path, 1)
        pygame.draw.line(screen, self.color, self.anchor0.getPos(), self.handle0.getPos(), 1)
        pygame.draw.line(screen, self.color, self.anchor1.getPos(), self.handle1.getPos(), 1)
        arrow = shapes.calcArrow((self.x1, self.y1) ,self.path[-1], self.path[-2])
        pygame.draw.polygon(screen, self.color, arrow, 1)

    def calcPath(self, hasEndNode):
        # choose anchor points
        # choose handle points 
        anchor0 = self.anchor0.getPos()
        handle0 = self.handle0.getPos()
        if (hasEndNode):
            anchor1 = self.anchor1.getPos()
            handle1 = self.handle1.getPos()
        else:
            anchor1 = mouse.pos
            handle1 = anchor1 
        self.path = shapes.calcBezier(anchor0, anchor1, handle0, handle1)

    def run(self):
        self.draw()
        if (self.node1):
            self.calcPath(False)
        else:
            self.calcPath(True)
'''

class Connection:
    
class Vector:
    def __init__(self):
        self.anchor
        self.posA  
        self.handle
    
    def setAnchor(self, node):
        self.anchor = node
        

class Handle(Rect):
    def __init__(self, x, y):
        Rect.__init__(self, x, y, 10, 10) 

class Anchor(Circle):
    def __init__(self, x, y):
        Circle.__init__(self, x, y, 8)

    def __str__(self):
        return "This is an anchor at "+ str(self.getPos())