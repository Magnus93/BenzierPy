import pygame 
import mouse
import controls
import moveble
import conn 
import trans2D

screen = pygame.display.set_mode((1200, 800))
pygame.font.init()
mytimer = pygame.time.Clock()

class state:
    def __init__(self):
        self.modes = ["select", "box", "sphere", "connection", "delete"]
        self.currentMode = self.modes[0]
        self.objList = []
        self.connList = []
        self.isCreatingConn = False 
        self.selectedObj = []
        self.myctrl = controls.controls(self.modes)
    
    def select(self, obj):
        obj.select()
        self.selectedObj.append(obj)

    def deselectAll(self):
        for obj in self.selectedObj:
            obj.deselect()
        self.selectedObj = []
        
    def runSelectMode(self):
        if (mouse.down[0]):
            hit = False 
            for o in self.objList:
                if (o.isHit()):
                    self.deselectAll()
                    self.select(o)
                    hit = True
                    break
            if (not hit):
                self.deselectAll()

    def runDeleteMode(self):
        if (mouse.down[0]):
            for o in self.objList:
                if (o.isHit()):
                    self.deselectAll()
                    self.objList.remove(o)
                    break

    def changeMode(self, mode):
        self.currentMode = mode
        self.myctrl.setMode(mode)

    def runCreationMode(self, objType):
        if mouse.pos[0] > 200:
            if mouse.down[0]:
                (x,y) = mouse.pos
                if (objType == "box"):
                    self.objList.append(moveble.Rect(x, y, 75, 55))
                elif (objType == "sphere"):
                    self.objList.append(moveble.Circle(x, y, 30))
                self.changeMode("select")
    
    def runCreateConnectionMode(self):
        if mouse.down[0]:
            startObj = self.isHitObjects()
            if startObj != None:
                self.isCreatingConn = True 
                self.connList.append(conn.Connection(startObj))
        
        if self.isCreatingConn:
            connect = self.getLastConnection()
            hitObject = self.isHitObjects()
            length = trans2D.distance(connect.getStartNode().getPos(), mouse.pos)
            connect.setStartVectorLength(0.4*length)
            if (connect.getStartNode().isHit()):
                connect.placeStartNode()
            elif(hitObject != None and hitObject != connect.getStartNode()):
                connect.setEndNode(hitObject)
                connect.setEndVectorLength(0.4*length)
            else:
                connect.removeEndNode()

        if mouse.up[0] and self.isCreatingConn:
            self.isCreatingConn = False
            self.changeMode("select")
            endObj = self.isHitObjects()
            if (endObj == None or endObj == self.getLastConnection().getStartNode()):
                self.deleteLastConnection()

    def getLastConnection(self):
        return self.connList[-1]

    def setLastConnectionEndNode(self, endObj):
        self.connList[-1].setEndNode(endObj)

    def deleteLastConnection(self):
        self.connList = self.connList[:-1]

    def isHitObjects(self):
        for o in self.objList:
            if (o.isHit()):
                return o
        return None

    def runMode(self):
        if self.currentMode == "select":
            self.runSelectMode()
        elif self.currentMode == "box":
            self.runCreationMode(self.currentMode)
        elif self.currentMode == "sphere":
            self.runCreationMode(self.currentMode)
        elif self.currentMode == "connection":
            self.runCreateConnectionMode()
        elif self.currentMode == "delete":
            self.runDeleteMode()

    def runObjects(self):
        for o in self.objList:
            o.run()

    def runConnections(self):
        for c in self.connList:
            c.run()

    def run(self): 
        mode = self.myctrl.run()
        if mode:
            print mode
            self.currentMode = mode
        self.runMode()
        self.runObjects()
        self.runConnections()

def loop():
    while(True):
        screen.fill(0x181818)
        mouse.run()
        mode = myctrl.run()
        if mode != None:
            print mode
            currentMode = mode

        mytimer.tick(30)
        pygame.display.flip()



def main():
    mystate = state()
    while(True):
        screen.fill(0x181818)
        mouse.run()
        mystate.run()
        mytimer.tick(60)
        pygame.display.flip()
        

if __name__ == "__main__":
    main()



