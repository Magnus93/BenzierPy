import mouse
import pygame
import gui

def doNothing():
    print "Nothing"


class controls:
    def __init__(self, modeNameList):
        self.buttonList = []
        self.modeList = modeNameList
        for i in range(0, len(modeNameList)):
            butt = gui.button(modeNameList[i], 0, 30*i, doNothing)
            butt.setAction(butt.getName)
            self.buttonList.append(butt)
        self.selectedToolText = gui.justText("This is a piece of text", 0, 30*(i+1))

    def setMode(self, string):
        self.selectedToolText.setText(string)

    def run(self):
        for b in self.buttonList:
            newMode = b.run()
            if newMode:
                self.setMode(newMode)
                return newMode
        self.selectedToolText.run()
        


if __name__ == "__main__":
    screen = pygame.display.set_mode((800, 600))
    myctrl = controls(["mode1", "mode zwei", "anouther mode"])

    while(True):
        screen.fill(0x202020)
        
        mouse.run()
        myctrl.run()
        
        pygame.display.flip()