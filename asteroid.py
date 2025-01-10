from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position), self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_first_vector = self.velocity.rotate(random_angle)
        new_second_vector = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_first_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        new_second_asteroid = Asteroid(self.position, self.position.y, new_radius)
        new_first_asteroid.velocity = new_first_vector * 1.2
        new_second_asteroid.velocity = new_second_vector * 1.2
        