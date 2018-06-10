import moveble 
import mouse 
import trans2D 
import shapes 
import pygame 

screen = pygame.display.set_mode((800,600))

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
    def __init__(self, startNode, color=(255, 255, 255)):
        self.vector0 = Vector(startNode)
        self.vector1 = None 
        self.color = color 

    def setStartVectorLength(self, length):
        self.vector0.setLength(length)

    def setEndVectorLength(self, length):
        self.vector1.setLength(length)

    def getStartNode(self):
        return self.vector0.getAnchorNode()

    def placeStartNode(self):
        self.vector0.setAnchorNode(self.vector0.getAnchorNode())

    def setEndNode(self, node):
        self.vector1 = Vector(node) 
    
    def removeEndNode(self):
        self.vector1 = None  

    def isHitControllers(self):
        ctrl = self.vector0.isHitControllers()
        if (ctrl):
            return ctrl 
        if (self.vector1):
            ctrl = self.vector1.isHitControllers()
        return ctrl

    def getPath(self):
        anchor0 = self.vector0.getAnchorPos()
        handle0 = self.vector0.getHandlePos()
        if (self.vector1 != None):
            anchor1 = self.vector1.getAnchorPos()
            handle1 = self.vector1.getHandlePos()
        else: 
            anchor1 = mouse.pos
            handle1 = mouse.pos     
        return shapes.calcIntegerBezier(anchor0, anchor1, handle0, handle1)

    def draw(self):
        pygame.draw.aalines(screen, self.color, False, self.getPath(), 1) 
        self.vector0.draw()
        if (self.vector1 != None):
            self.vector1.draw()

    def run(self):
        self.draw()
        self.vector0.run()
        if (self.vector1):
            self.vector1.run() 


class Vector:
    def __init__(self, anchorNode, color=0xffffff):
        self.anchorNode = anchorNode 
        self.anchor = Anchor(0,0)
        self.handle = Handle(0, 0)
        self.setAnchorNode(anchorNode)
        self.color = color 

    def restrainAnchor(self, pos):
        (anchorX, anchorY) = self.anchorNode.nearestEdge(pos)
        self.anchor.setPos(anchorX, anchorY)  

    def setAnchorNode(self, node, vectorLength=100):
        self.restrainAnchor(mouse.pos)
        self.setLength(vectorLength)
    
    def setLength(self, length):
        if (length == 0):
            length = 10
        nodeCenterPos = self.anchorNode.getPos() 
        (handleX, handleY) = trans2D.getHandlePos(self.anchor.getPos(), nodeCenterPos, length)
        self.handle.setPos(handleX, handleY) 

    def setHandleAtMouse(self): 
        pass 

    def setAnchorAtMouse(self):
        pass 

    def removeAnchor(self):
        self.anchorNode = None 

    def getAnchorNode(self):
        return self.anchorNode 

    def getAnchorPos(self):
        return self.anchor.getPos() 

    def getHandlePos(self):
        return self.handle.getPos() 

    def isHitControllers(self):
        if (self.anchor.isHit()):
            return self.anchor  
        elif (self.handle.isHit()):
            return self.handle 
        return None 

    def draw(self):
        pygame.draw.line(screen, self.color, self.getAnchorPos(), self.handle.getPos(), 1)

    def runDynamicMovement(self):
        if (self.handle.isActive()):
            self.restrainAnchor(self.handle.getPos())
        if (self.anchor.isActive()):
            self.restrainAnchor(mouse.pos) 
            vectorLength = trans2D.distance(self.anchor.getPos(), self.handle.getPos())
            self.setLength(vectorLength)


    def run(self):
        self.draw() 
        self.handle.run() 
        self.anchor.run() 
        self.runDynamicMovement()

class Handle(moveble.Rect):
    def __init__(self, x, y):
        moveble.Rect.__init__(self, x, y, 18, 18)
        self.typeName = "Handle"  

class Anchor(moveble.Circle):
    def __init__(self, x, y):
        moveble.Circle.__init__(self, x, y, 8)
        self.typeName = "Anchor" 