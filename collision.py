import pygame
class Planet_Collision():
    def __init__(self, r, x, y, ora, ox, oy):
        self.r = r
        self.ora = ora
        self.x = x
        self.y = y
        self.ox = ox
        self.oy =oy
    def has_colided(self):
        if (((self.x - self.y)**2)+((self.y-self.oy)**2))**0.5 <= self.ora+self.r:
            return True
        return False