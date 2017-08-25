

class vehicle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class car(vehicle):
    def __init__(self, x, y, color):
        vehicle.__init__(self, x,y)
        self.color = color
        
    def __str__(self):
        string = "The car is "+ str(self.color) +" and is is at "+ str(self.x)+", "+ str(self.y)
        return string



if __name__ == "__main__":
    
    magnusBil = car(4,6,0x444444)
    print magnusBil
