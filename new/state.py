import pygame
import sys
import gui
import mouse


class state:
    def __init__(self, modeNameList):
        self.modeList = modeNameList
        self.currentMode = self.modeList[0]  
        self.objectList = []
        self.selectedObjects = []

    def setMode(self, mode):
        self.currentMode = mode
        
    def getMode(self):
        return self.currentMode

    def addObject(self, obj):
        self.objectList.append(obj)

    def run(self):
        pass

# State attributes
selected = []
objects = []


def initButtonControls(x, y):
    selectButton = gui.button("Select", 10+x, 5+y, selectHandler)
    pass

def runButtonControls():
    pass

def run():
    
    pass


if __name__ == "__main__":
    screen = pygame.display.set_mode((800, 600))
    mytimer = pygame.time.Clock()

    def toolHandler(selectedTool):
        global tool
        tool = selectedTool
        printTool()

    def selectHandler():
        toolHandler(SELECT)
    selectButton = gui.button("Select", 10, 5, selectHandler)


    def createBoxHandler():
        toolHandler(CREATEBOX)
    boxButton = gui.button("Box", 10, 35, createBoxHandler)

    def createSphereHandler():
        toolHandler(CREATESPHERE)
    sphereButton = gui.button("Sphere", 10, 65, createSphereHandler)

    def createConnectionHandler():
        toolHandler(CREATECONNECTION)
    connectionButton = gui.button("Connection", 10, 95, createConnectionHandler)

    def printTool():
        print TOOLS[tool]
    printToolButton = gui.button("print tool", 300, 5, printTool)

    while(True):
        screen.fill(0xf6f6f6)
        
        mouse.run()
        selectButton.run()
        boxButton.run()
        sphereButton.run()
        connectionButton.run()   
        printToolButton.run()
        
        run()

        mytimer.tick(30)
        pygame.display.flip() 
