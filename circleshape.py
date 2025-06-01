"""
circleshape.py -- a Sprite class to be used in the Asteroids game project.


"""

import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        #to use this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub classes must override
        pass

    def update(self, dt):
        #sub classes must override
        pass

    def collision_check(self, target):
        # checks for collision with another CircleShape, the "target"

        dist = self.position.distance_to(target.position)       #calculate Distance between centers
        return dist <= (self.radius + target.radius)
