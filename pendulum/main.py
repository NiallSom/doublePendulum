import pygame,math

#translated from @TheCodingTrain. Processing -> Python.

pygame.init()

width,height = 1200,900

screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
pygame.display.set_caption("Double Pendulum")


class Main():
    def __init__(self) -> None:
        self.r1 = 400.0 #length of arm1
        self.r2 = 400.0 #length of arm 2
        self.m1 = 40.0 #mass of circle at the end of arm 1
        self.m2 = 40.0 #mass of circle at the end of arm 1
        self.a1 = math.pi / 4 #angle for arm 1
        self.a2 = math.pi / 8 #angle for arm 2
        self.a1_v = 0#angle velocity for arm 1
        self.a2_v = 0#angle velocity for arm 2
        self.g = 1.0


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

        self.x1 = self.r1 * math.sin(self.a1) + 600 # translating so x = 300 y = 50 
        self.y1 = self.r1 * math.cos(self.a1) + 100
        self.x2 = self.x1 + self.r2 * math.sin(self.a2)
        self.y2 = self.y1 + self.r2 * math.cos(self.a2)

        self.a1 +=self.a1_v
        self.a2 +=self.a2_v
        self.a1_v += self.a1_a
        self.a2_v +=self.a2_a

        self.a1_v *=0.999
        self.a2_v *=0.999
        #drawing the pendulum arms and circles
        pygame.draw.line(screen,(0,0,0),(600,100),(self.x1,self.y1),20)
        pygame.draw.circle(screen,(0,0,0),(self.x1,self.y1),self.m1)

        pygame.draw.line(screen,(0,0,0),(self.x1,self.y1),(self.x2,self.y2),20)
        pygame.draw.circle(screen,(0,0,0),(self.x2,self.y2),self.m1)
    def trace(self):
        pass
        #in the future this will be used to draw the pattern the pendulum makes
    



main = Main()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    screen.fill((255,255,255))
    main.draw()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
