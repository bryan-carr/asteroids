"""
shot.py -- class for Bullets/Shots in the Asteroids game project

Shots are sent out from the Player, and collide with Asteroids.
On collision, they should split the Asteroid into two.
"""

from circleshape import CircleShape
from constants import SHOT_RADIUS
import pygame

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
    
    def draw(self, screen):
        pygame.draw.circle(surface = screen, color="white", center=self.position, radius = self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    