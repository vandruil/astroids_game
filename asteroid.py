import random

import pygame.draw

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if (self.radius) <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        x, y = self.position
        positiv_velocity = self.velocity.rotate(random_angle)
        negative_velocity = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        split_asteroid_1 = Asteroid(x, y, new_radius)
        split_asteroid_2 = Asteroid(x, y, new_radius)
        split_asteroid_1.velocity = positiv_velocity * 1.2
        split_asteroid_2.velocity = negative_velocity * 1.2
