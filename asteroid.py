from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
       

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2 )

    
    def update(self, dt):
        self.position += self.velocity * dt

    # split the asteroid into smaller ones
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        child_vector_1 = self.velocity.rotate(angle)
        child_vector_2 = self.velocity.rotate(-angle)
        child_radius = self.radius - ASTEROID_MIN_RADIUS
        child_1 = Asteroid(self.position.x, self.position.y, child_radius)
        child_2 = Asteroid(self.position.x, self.position.y, child_radius)
        child_1.velocity = child_vector_1 * 1.2
        child_2.velocity = child_vector_2 * 1.2