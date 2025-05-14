from circleshape import CircleShape
from constants import *
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.shot_type = set()

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2 )

    def update(self, dt):
        self.position += self.velocity * dt

    def hit(self, target):
        self.kill()
        if "breach_round" in self.shot_type:
            child_vector_1 = self.velocity.rotate(30)
            child_vector_2 = self.velocity.rotate(-30)
            child_vector_3 = self.velocity
            child_1 = Shot(
                target.position.x + child_vector_1.normalize().x * target.radius,
                target.position.y + child_vector_1.normalize().y * target.radius,
                SHOT_RADIUS,
            )
            child_2 = Shot(
                target.position.x + child_vector_2.normalize().x * target.radius,
                target.position.y + child_vector_2.normalize().y * target.radius,
                SHOT_RADIUS,
            )
            child_3 = Shot(
                target.position.x + child_vector_3.normalize().x * target.radius,
                target.position.y + child_vector_3.normalize().y * target.radius,
                SHOT_RADIUS,
            )
            child_1.velocity = child_vector_1
            child_2.velocity = child_vector_2
            child_3.velocity = child_vector_3

        