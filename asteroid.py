import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self,x,y, radius):
        CircleShape.__init__(self,x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            positive_velocity = self.velocity.rotate(random_angle)
            negative_velocity = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            Asteroid(self.position.x,self.position.y,new_radius).velocity = positive_velocity * 1.2
            Asteroid(self.position.x,self.position.y,new_radius).velocity = negative_velocity * 1.2