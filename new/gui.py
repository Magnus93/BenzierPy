import pygame
# from pygame.locals import *
import sys
import mouse
screen = pygame.display.set_mode((800,600))#,pygame.FULLSCREEN)
mytimer = pygame.time.Clock()
pygame.font.init()
smallfont = pygame.font.SysFont("verdana", 14)

class button:															# button class
    def __init__(self, name, x, y, action, w=200, h = 26, color1 = (120,120,140), color2 = (0,140,200)):
        self.name = name
        self.x = x
        self.y = y
        self.action = action
        self.w = w
        self.h = h
        self.color = color1
        self.color1 = color1
        self.color2 = color2

    def __str__(self):
        string = "Button: "+self.name + "\n"
        string += " pos:    " + str((self.x, self.y)) + "\n"
        string += " size:   " + str((self.w, self.h)) + "\n"
        string += " action: " + str(self.action) + "\n"
        string += " color1: " + str(self.color1) + "\n"
        string += " color2: " + str(self.color2) + "\n"
        return string

    def run(self):
        (x,y) = mouse.pos
        if self.x < x < (self.x+self.w) and self.y < y < (self.y+self.h):
            self.color = self.color2
            textcolor = (255,255,255)
            if mouse.down[0]:
                self.action()
        else:
            self.color = self.color1
            textcolor = (0,0,0)
        self.draw(textcolor)

    def draw(self, textcolor):
        face = pygame.Surface((self.w,self.h))
        face.fill(self.color)
        TEXT = smallfont.render(self.name, 1, textcolor)
        face.blit(TEXT, (6,3))
        screen.blit(face,(self.x,self.y))

    def set_pos(self, x, y):
        (self.x, self.y) = (x, y)

class slider:															# slider class
    def __init__(self, name, x, y, lower, upper, value, color0=(0,0,0), color1=(90,90,90), color2=(0,140,200)):
        self.name   = name
        self.x      = x
        self.y      = y
        self.xoff   = 18                # offset x
        self.yoff   = 22                # offset y
        self.xoff2  = self.xoff+200     # offset x end
        self.x1      = x+self.xoff
        self.y1      = y+self.yoff
        self.endx1   = self.x1+200
        self.lower  = lower				# lower value limit
        self.upper  = upper				# upper value limit
        self.color0 = color0
        self.color  = color1
        self.color1 = color1
        self.color2 = color2
        self.active = False
        self.value  = value
        self.Const  = (upper-lower)/float(200)
        self.posx   = ((value-lower)/self.Const)+self.xoff
        self.low_string= smallfont.render(str(self.lower),1, (230,230,230))		# lower value
        self.upp_string= smallfont.render(str(self.upper),1, (230,230,230))     # upper value
        self.change = False
    def run(self):
        self.change = False
        (x,y) = mouse.pos
        if self.x+self.xoff< x <self.x+self.xoff2 and self.y < y < self.y+2*self.yoff:
            if mouse.down[3]:
                self.posx += 5
                self.change = True
            if mouse.down[4]:
                self.posx -= 5
                self.change = True
            if mouse.down[0]:
                self.active = True
        if self.active:
            self.change = True
            self.posx = x-self.x
            self.color = self.color2
            if mouse.up[0]:
                self.active = False
                self.color = self.color1
        if self.posx < self.xoff:          # limit the handles position
            self.posx = self.xoff
        if self.posx > self.xoff2:
            self.posx = self.xoff2
        self.value=self.Const*(self.posx-self.xoff)+self.lower
        self.draw()
    def draw(self):
        face0 = pygame.Surface((240,46))
        face0.fill(self.color0)
        pygame.draw.line(face0, (70,70,70), (self.xoff,self.yoff),(self.xoff2,self.yoff),4)
        #pygame.draw.circle(face0, self.color, (int(self.posx), self.yoff), 10)
        pygame.draw.line(face0,self.color,(int(self.posx)-2, self.yoff-4),(int(self.posx)-2, self.yoff+16),4)
        self.name_string = smallfont.render((self.name+" "+str(self.value)),1, (230,230,230))               # name value
        face0.blit(self.name_string, (4,0))
        face0.blit(self.low_string,(self.xoff-10,self.yoff+3))
        face0.blit(self.upp_string,(self.xoff2-10,self.yoff+3))
        screen.blit(face0,(self.x,self.y))
    def set_name(self, name):
        self.name = name
        self.name_string= smallfont.render(name,1, (230,230,230))
    def set_value(self, value):
        self.posx   = ((value-self.lower)/self.Const)+self.xoff
        self.value=self.Const*(self.posx-self.xoff)+self.lower
        self.change = True
    def get_value(self):
        return self.value
    def set_pos(self, x, y):
        (self.x, self.y) = (x, y)

class toggle():                                                         # toggle class
    def __init__(self, name, x, y, value = False, color1=(60,60,80), color2=(0,160,220)):
        self.name = name
        self.x = x
        self.y = y
        self.value = value
        self.color = color1
        self.color1 = color1
        self.color2 = color2
        self.namerender = smallfont.render(self.name ,1, (230,230,230))
    def run(self):
        (x,y) = mouse.pos
        if self.x < x < (self.x+26) and self.y < y < (self.y+26):
            if mouse.down[0]:
                self.value = not self.value
        if self.value:
            self.color = self.color2
        else:
            self.color = self.color1
        self.draw()
    def draw(self):
        box = pygame.Surface((26,26))
        box.fill(self.color1)
        #pygame.draw.circle(box, self.color, (10,10), 8)
        if self.value:
            pygame.draw.line(box, self.color2, (4,4),(20,20),6)
            pygame.draw.line(box, self.color2, (4,20),(20,4),6)
        screen.blit(box, (self.x,self.y))
        screen.blit(self.namerender, (self.x+31,self.y+3))
    def get_value(self):
        return self.value
    def set_value(self, value):
        self.value = value
    def set_pos(self, x, y):
        (self.x, self.y) = (x, y)

class dropdown:                                                         # dropdown class
    def __init__(self, name, x, y, options, select = 0, color1=(120,120,140), color2=(0,140,200)):
        (self.x, self.y) = (x,y)
        self.options = [name]+options
        self.optlen = len(self.options)
        self.color = color1
        self.color1 = color1
        self.color2 = color2
        (self.w,self.h) = (200,26)
        self.drophight = (self.optlen)*self.h
        self.active = False
        self.optrenders = []
        for opt in self.options:
            self.optrenders.append(smallfont.render(opt,1, (0,0,0)))    # text renders
        self.select = select
        self.change = False
    def run(self):
        self.change = False
        (x,y) = mouse.pos
        if self.x< x <self.x+self.w and self.y < y < self.y+self.h:
            if mouse.down[0]:
                self.active = True
        if mouse.up[0] and self.active:
            self.active = False
            if self.select != 0:
                self.change = True
        if self.active:
            for i in range(self.optlen):
                if self.y+(i+1)*self.h < y < self.y+(i+2)*self.h:
                    self.select = i
            self.color = self.color2
        else:
            self.color = self.color1
        self.draw()
    def draw(self):
        face0 = pygame.Surface((self.w, self.h))
        face0.fill((self.color))
        face0.blit(self.optrenders[self.select], (6,3))
        pygame.draw.polygon(face0, (0,0,0), [(175,6),(193,6),(184,18)])
        if self.active:
            face1 = pygame.Surface((self.w, self.drophight))
            face1.fill(self.color1)
            face2 = pygame.Surface((self.w-6, self.h-6))
            face2.fill(self.color2)
            face1.blit(face2, (3, self.select*self.h+3))
            for i in range(self.optlen):
                face1.blit(self.optrenders[i], (6, (i)*self.h+3))
            linelen = int(self.w/10)
            for i in range(10):
                pygame.draw.line(face1, (0,0,0), (linelen*i+5, self.h), (linelen*i+15, self.h))
            screen.blit(face1, (self.x,self.y+self.h))
        screen.blit(face0, (self.x, self.y))
    def set_value(self, value):
        self.select = value
        self.change = True
    def get_value(self):
        return self.select
    def get_string(self):
        return self.options[self.select]
    def set_pos(self, x, y):
        (self.x, self.y) = (x, y)

def exit():                                                             # exit function
    pygame.quit()
    sys.exit()

def exit_butt(x=700, y=0):                                              # create exit button
    return button("   X   ", x ,y, exit, w = 52, color1 = (120,100,100), color2 = (170,100,100))








# -----------------------------Testing code ----------------------------
if __name__ == "__main__":
    exitbutton = exit_butt(730)
    myslider = slider("My uber Slider:", 40,50, 4, 19, 15)

    def set_to_ten():
        myslider.set_value(10)

    mybutton = button("Set slider to 10", 40, 100, set_to_ten)
    mytoggle = toggle("my toggle YEAH!!", 40, 130)
    mydrop = dropdown("This is a drop down", 40, 160, ["awesome","very cool","Nice!","Charlston", "Dance!"])

    def say_hello():
        print "hi to you!!!"
    def main():

        print exitbutton
        while True:
            screen.fill(0x222222)
            mybutton.run()
            exitbutton.run()
            myslider.run()
            mytoggle.run()
            mydrop.run()
            if mydrop.change:
                print mydrop.change
            pygame.display.flip()
            mytimer.tick(60)
            mouse.run()
            #print mouse.pos
            #print mouse.drag_curr

    main()
