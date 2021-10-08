import pygame
class Planet_Collision():
    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y
    def has_colided(self, ora, ox, oy):
        
        self.ora = ora
        self.ox = ox
        self.oy =oy
        
        if (((self.x - self.y)**2)+((self.y-self.oy)**2))**0.5 >= self.ora+self.r:
            return True
        return False