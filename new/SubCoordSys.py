import anchor02
import pygame
import mouse
import trans2D

screen = pygame.display.set_mode((800,600))
mytimer = pygame.time.Clock()

class CoordSys:
	def __init__(self, mv0, mv1):
		self.p0 = mv0
		self.p1 = mv1
		self.scale = 1
		self.sin = 1
		self.cos = 1
		self.calcValues()
		
		
	def calcValues(self):
		self.scale = (trans2D.distance((self.p0.x, self.p0.y),(self.p1.x, self.p1.y)))/100.0
		self.sin = trans2D.sin((self.p0.x,self.p0.y), (self.p1.x,self.p1.y))
		self.cos = trans2D.cos((self.p0.x,self.p0.y), (self.p1.x,self.p1.y))
		
	def worldToLocal(self, pWorld):
		#inv = inverse
		# pLocal(pWorld) = inv(S)*inv(R)*inv(T)*pWorld
		iTpW = trans2D.translate(pWorld, trans2D.negate((self.p0.x, self.p0.y)))
		iRiTpW = trans2D.rotateTrig(iTpW, (0,0), -self.sin, self.cos)
		pLocal = trans2D.scale(iRiTpW, (0,0) ,(1.0/self.scale))
		return pLocal
		
	def localToWorld(self, pLocal):
		# pWorld(pLocal) = T*R*S*pLocal
		self.calcValues()
		SpL = trans2D.scale(pLocal, (0,0), self.scale)
		RSpL = trans2D.rotateTrig(SpL, (0,0), self.sin, self.cos)
		pWorld = trans2D.translate(RSpL, (self.p0.x, self.p0.y))
		return pWorld
		
	
	def drawGrid(self):
		for i in range(0,101, 10):
			pWorldStart = self.localToWorld((0,i-50))
			pWorldEnd   = self.localToWorld((100,i-50))
			pygame.draw.line(screen, 0xff0000, pWorldStart, pWorldEnd, 1)
			pWorldStart = self.localToWorld((i,-50))
			pWorldEnd   = self.localToWorld((i,50))
			pygame.draw.line(screen, 0x00ff00, pWorldStart, pWorldEnd, 1)
		

if __name__ == "__main__":
	circ1 = anchor02.Variable("start", 500, 400)
	circ2 = anchor02.Variable("end", 40, 30)
	coo = CoordSys(circ1, circ2)
	
	
	### --- Testing world to local localto world ---
	a0 = (3,0)
	a1 = coo.localToWorld(a0)
	a2 = coo.worldToLocal(a1)
	print a0, a1, a2
	print "________________________"
	
	a0 = (100,100)
	a1 = coo.localToWorld(a0)
	a2 = coo.worldToLocal(a1)
	print a0, a1, a2
	###
	
	while(True): 
		screen.fill(0x222222)
		circ1.run()
		circ2.run()
		mouse.run()
		coo.drawGrid()
		pygame.display.flip()
		mytimer.tick(24)




