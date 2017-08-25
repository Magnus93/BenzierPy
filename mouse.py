import pygame
from pygame.locals import *
import sys
import random
screen=pygame.display.set_mode((800,600))#,pygame.FULLSCREEN)
mytimer = pygame.time.Clock()

down    	= [False, False, False, False, False]						# [Left, Middle, Right, forward, back] mouse button
up      	= [False, False, False]						                # [Left, Middle, Right] mouse button
pos 		= (0,0)														# mouse position
drag_stop	= (0,0)														# drag value when mouse release (mouse up)
drag_curr	= (0,0)														# drag value while being draged
drag_active = False														# currently draging
start 		= (0,0)															# draging from pixel position
ifevent = False
def print_all():	
	print "Down :",down
	print "Up   :",up
	print "Pos  :",pos
	print "Stop :",drag_stop
	print "Curr :",drag_curr
	

def reset_values():
    global down, up, drag_stop, drag_curr, ifevent
    down 	= [False, False, False, False, False]
    up 		= [False, False, False]
    drag_stop	= (0,0)
    #drag_curr	= (0,0)
    ifevent     =  False
    
	
def run():																# sets values to all outputs
	global pos,start, drag_stop, drag_curr, drag_active, ifevent
	reset_values()
	events = pygame.event.get()
	for event in events:
		ifevent = True
		if event.type == MOUSEMOTION:
			pos = event.pos
		if event.type == MOUSEBUTTONDOWN:
			down[event.button-1] = True
			if event.button == 1:
				start = pos
				drag_active = True
		if event.type == MOUSEBUTTONUP and event.button < 4:
			up[event.button-1] = True
			if event.button == 1:
				drag_stop = (pos[0]-start[0], pos[1]-start[1])
				drag_curr = (0,0)
				drag_active = False
            
		if drag_active:
			drag_curr = (pos[0]-start[0], pos[1]-start[1])



# -----------------------------Testing code ----------------------------
if __name__ == "__main__":
    def main():
        run()
        if ifevent:
            print_all()
        mytimer.tick(60)
            
            
    while True:
        main()
        
        
        

