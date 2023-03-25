import pygame
import math
import random


pygame.init()

width,height = 1200,1000

screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
pygame.display.set_caption("Double Pendulum")


class Main():
    def __init__(self,angle1,angle2,armVal, color) -> None:
        self.r1 = 300.0 #length of arm1
        self.r2 = 300.0 #length of arm 2
        self.m1 = 14.0 #mass of circle at the end of arm 1
        self.m2 = 14.0 #mass of circle at the end of arm 1
        self.a1 = angle1 #angle for arm 1
        self.a2 = angle2 #angle for arm 2
        self.a1_v = 0#angle velocity for arm 1
        self.a2_v = 0#angle velocity for arm 2
        self.g = 1.0
        self.color = color #(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.armVal = armVal
        self.coveredValues = []

    def draw(self):
        #the pendulum equation for arm1 angle acceleration
        num1 =-self.g * (2 * self.m1 + self.m2) * math.sin(self.a1)
        num2 =-self.m2 * self.g * math.sin(self.a1 -2 * self.a2)
        num3 =-2* math.sin(self.a1 - self.a2)*self.m2
        num4 =self.a2_v**2*self.r2 + self.a1_v**2*self.r1*math.cos(self.a1-self.a2)
        denominator = self.r1 * (2*self.m1 + self.m2-self.m2 * math.cos(2* self.a1-2*self.a2))

        self.a1_a = (num1 + num2 + num3 * num4) / denominator
        #the pendulum equation for arm2 angle acceleration
        num1 = 2* math.sin(self.a1-self.a2)
        num2 = (self.a1_v**2*self.r1*(self.m1+self.m2))
        num3 = self.g * (self.m1 + self.m2) * math.cos(self.a1)
        num4 = self.a2_v**2 * self.r2 * self.m2 * math.cos(self.a1-self.a2)
        denominator = self.r2 * (2*self.m1 + self.m2-self.m2 * math.cos(2* self.a1-2*self.a2))

        self.a2_a = (num1*(num2+num3+num4)) / denominator

        self.x1 = self.r1 * math.sin(self.a1) + 600 # translating so x = 600 y = height / 2 
        self.y1 = self.r1 * math.cos(self.a1) + height/2
        self.x2 = self.x1 + self.r2 * math.sin(self.a2)
        self.y2 = self.y1 + self.r2 * math.cos(self.a2)

        self.a1 +=self.a1_v
        self.a2 +=self.a2_v
        self.a1_v += self.a1_a
        self.a2_v +=self.a2_a

        self.a1_v *=0.999
        self.a2_v *=0.999
        #drawing the pendulum arms and circles
        if self.armVal:
            pygame.draw.line(screen,(self.color[0],self.color[1],self.color[2]),(600,height/2),(self.x1,self.y1),10) #arm 1 line
            pygame.draw.line(screen,(self.color[0],self.color[1],self.color[2]),(self.x1,self.y1),(self.x2,self.y2),10) #arm 2 line
        
        pygame.draw.circle(screen,(self.color),(self.x1,self.y1),self.m1)#arm 1 circle
        pygame.draw.circle(screen,(self.color),(self.x2,self.y2),self.m1)#arm 2 circle
        
    def trace(self):
        self.coveredValues.append((self.x2,self.y2))
        for i in range(len(self.coveredValues)):
            if i > 1:
                pygame.draw.line(screen,(self.color),(self.coveredValues[i-1][0],self.coveredValues[i-1][1]),(self.coveredValues[i][0],self.coveredValues[i][1]),1)
        #in the future this will be used to draw the pattern the pendulum makes --- COMPLETED 25/03/2023
    


#testing value:   math.pi / 4 angle for arm 1
#testing value:   math.pi / 8 angle for arm 2

values = []
"""
amount = int(input("How many double pendulums would you like: "))
armVisible = input("Would you like to see the arms(y/n): ")
armVal = False


#plan on adding error handing in the future
if armVisible.lower() == "y":
    armVal = True
else:
    pass

for i in range(amount):
    a1 = int(input("angle for arm1:"))
    a2 = int(input("angle for arm2:"))
    values.append([Main(a1,a2,armVal)])
    """


colours = []


for r, g, b in zip( # this gets all the rainbow colours into a list 
    (list(reversed(range(256))) + [0] * 256),
    (list(range(256)) + list(reversed(range(256)))),
    ([0] * 256 + list(range(256)))):
    colours.append([r, g, b])

amountOfPend = 1 #MAX 1000

for i in range(amountOfPend):#MAX 1000
    x = i
    if x > 500:
        x = i-500 #512 RAINBOW COLOUR VALUES (RGB)                                                            v1            v2             v3
    values.append([Main(60+(random.randint(0,100)/1_000_000),60+(random.randint(0,100)/1_000_000),True,(colours[x][2],colours[x][1],colours[x][0]))])
    # If the amountOfPend is equal to 1 then the color will be blue, can change by changing the variables below v1,v2,v3 to a number > 0 and < 255
    

while 1:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
            
    screen.fill((0,0,0)) # background color change 0,0,0 to 255,255,255 for white
    for arm in range(amountOfPend):
        values[arm][0].draw()#Draws the arms
        values[arm][0].trace()#Traces the circle at the end of line 2
    clock.tick(60) #fps
    pygame.display.flip()

pygame.quit()
