from circleshape import *
import pygame
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255),self.position,self.radius, width=2)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS: return
        random_angle = random.uniform(20,50)
        vect1 = self.velocity.rotate(random_angle)
        vect2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        astro = Asteroid(self.position.x, self.position.y, new_radius)
        astro2 = Asteroid(self.position.x, self.position.y, new_radius)
        astro.velocity = vect1 * 1.2
        astro2.velocity = vect2 * 1.2




