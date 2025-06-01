"""
asteroid.py -- contains Asteroid class for the Asteroids game project
"""
import pygame, random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(surface = screen, color="white", center=self.position, radius = self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        # remove initial asteroid and split it into two smaller ones, if a smaller size exists
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return              #no need to do anything for small asteroids, exit early before following computations

        angle = random.uniform(20,50)
        new_vector1 = self.velocity.rotate(angle)
        new_vector2 = self.velocity.rotate(angle * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = new_vector1 * 1.2
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2.velocity = new_vector2 * 1.2

    
