import trans2D

def calcBezier(anchor0, anchor1, handle0, handle1, steps=20):
    t = 0
    pointlist = []
    p0 = anchor0 
    p1 = handle0
    p2 = handle1
    p3 = anchor1 
    while(t<1):
    	bx = ((1-t)*(1-t)*(1-t))*p0[0] + (3*((1-t)*(1-t))*t)*p1[0] + 3*(1-t)*(t*t)*p2[0] + (t*t*t)*p3[0] 
    	by = ((1-t)*(1-t)*(1-t))*p0[1] + (3*((1-t)*(1-t))*t)*p1[1] + 3*(1-t)*(t*t)*p2[1] + (t*t*t)*p3[1]
    	pointlist.append((bx,by))
    	t += 1.0/steps
    pointlist.append(anchor1)
    return pointlist

def calcArrow(pos, point0, point1, height=15):
    pointlist = [(0,0), (height, -height/3), (height, height/3)]
    newList = []
    sin = trans2D.sin(point0, point1)
    cos = trans2D.cos(point0, point1)
    for p in pointlist:
        p = trans2D.rotateTrig(p, (0,0), sin, cos)
        p = trans2D.translate(p, pos)
        newList.append(p)
    return newList 
