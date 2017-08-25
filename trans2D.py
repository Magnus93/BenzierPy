import math


def negate(point):
	return (point[0], point[1])


def translate(point, translation):
	return (point[0]+translation[0], point[1]+translation[1])

### point to be rotated in integer tuple
### pivot to rotate around in tuple
### angle in radians to rotate
def rotate(point, pivot, angle):
	a = translate(point, negate(pivot))
	cos = math.cos(angle)
	sin = math.sin(angle)
	b = (a[0]*cos - a[1]*sin, a[0]*sin + a[1]*cos)
	return translate(b, pivot)
	
def rotateTrig(point, pivot, sin, cos):
	a = translate(point, negate(pivot))
	b = (a[0]*cos - a[1]*sin, a[0]*sin + a[1]*cos)
	return translate(b, pivot)	
	


def scale(point, pivot, scale):
	a = translate(point, negate(pivot))
	b = (a[0]*scale, a[1]*scale)
	return translate(b, pivot)


def midPoint(pStart, pEnd):
	x = (pStart[0]+pEnd[0])/2
	y = (pStart[1]+pEnd[1])/2
	return (x,y)
	

def getAngle(pStart, pEnd):
	pass
	
	
def distanceX(point1, point2):
	return (point2[0]-point1[0])

def distanceY(point1, point2):
	return (point2[1]-point1[1])
	
def distance(point1, point2):
	x = distanceX(point1,point2)
	y = distanceY(point1,point2)
	return math.sqrt((x*x)+(y*y))


def cos(point1, point2):
	dist = distance(point1, point2)
	return distanceX(point1,point2)/(dist+0.0)
	
def sin(point1, point2):
	dist = distance(point1, point2)
	return  distanceY(point1,point2)/(dist+0.0)
	
