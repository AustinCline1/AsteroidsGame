import pygame
from constants import SHOT_RADIUS
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self,x,y,radius):
        CircleShape.__init__(self,x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"red",self.position,self.radius,SHOT_RADIUS)

    def update(self,dt):
        self.position += (self.velocity* dt)