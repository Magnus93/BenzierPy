import pygame 
import mouse
import state

screen = pygame.display.set_mode((1200, 800))
pygame.font.init()
font = pygame.font.SysFont("arial", 12)
mytimer = pygame.time.Clock()

if __name__ == "__main__":
    
    while(True):
        screen.fill(0x181818)

        mouse.run()

        mytimer.tick(30)
        pygame.display.flip()
        print "running"


