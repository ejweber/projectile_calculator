import math

class Projectile:

    GRAVITY = -9.81

    def __init__(self, v=None, angle=None, t=None, deltax=None,
                 deltay=None, vx=None, viy=None, vfy=None):
        self.v = v
        self.angle = angle
        self.vx = vx
        self.viy = viy
        self.vfy = vfy
        self.t = t
        self.deltax = deltax
        self.deltay = deltay

    def resolve(self):
        self.vx = self.v * math.cos(math.radians(self.angle))
        self.viy = self.v * math.sin(math.radians(self.angle))

    def add(self):
        self.angle = math.degrees(math.atan(self.viy / self.vx))
        self.v = math.sqrt(self.vx ** 2 + self.viy ** 2)

    def solve(self):
        loop_number = 0
        while True:
            # check for successful calculation of all values
            if None not in self.__dict__.values():
                print('success')
                return 'success'

            # various mathematical methods to calculate variables
            if self.v != None and self.angle != None and self.vx == None and self.viy == None:
                self.resolve()
            if self.vx != None and self.viy != None and self.v == None and self.angle == None:
                self.add()
            if self.viy != None and self.deltay != None and self.vfy == None:
                self.vfy = -math.sqrt(self.viy ** 2 + 2 * self.GRAVITY * self.deltay)
            if self.viy != None and self.vfy != None and self.t == None:
                self.t = (self.vfy - self.viy) / self.GRAVITY
            if self.vx != None and self.t != None and self.deltax == None:
                self.deltax = self.vx * self.t
            if self.deltax != None and self.vx != None and self.t == None:
                self.t = self.deltax / self.vx
            if self.t != None and self.viy != None and self.deltay == None:
                self.deltay = ((self.viy * self.t) +
                              (self.GRAVITY * self.t ** 2) / 2)
            if self.deltax != None and self.t != None and self.vx == None:
                self.vx = self.deltax / self.t
            if self.angle != None and self.deltay != None and self.deltax != None and self.t == None:
                self.t = math.sqrt(2 * (self.deltay - self.deltax * math.tan(math.radians(self.angle))) / self.GRAVITY)
            if self.deltay != None and self.t != None and self.viy == None:
                self.viy = (self.deltay / self.t) - (self.GRAVITY * self.t / 2)
            if self.viy != None and self.vx != None and self.v == None:
                self.v = math.sqrt(self.viy ** 2 + self.vx ** 2)

            # track number of loops and break out if calculation unsuccessful
            loop_number += 1
            if loop_number >= 3:
                print('Calculation was not completed successfully')
                return 'failure'
