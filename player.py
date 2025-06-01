"""
player.py -- contains Player class, for the Asteroids game project
"""

import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot

class Player(CircleShape):

   # Player.containers = ()          #class variable - tupple to hold all containers

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0.0
    
    def triangle(self):
        """
        Triangle shape for Player's avatar
        Triangle to be displayed, but hidden within a Circle. Circle will be used for game's hitbox
        A, B, C are the vertices of the triangle
        """
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        right = pygame.Vector2(0,1).rotate(self.rotation + 90) * self.radius/1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right

        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(surface=screen, color="white", points=self.triangle(), width=2)
    
    # rotate the player's avatar (triangle)
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shot_timer -= dt

        if keys[pygame.K_a]:
            self.rotate(dt * -1.0)      #turn left if A pressed, i.e. negative rotation
        if keys[pygame.K_d]:
            self.rotate(dt * 1.0)       #turn Right if D pressed, i.e. positive rotation
        if keys[pygame.K_w]:
            self.move(dt * 1.0)         # move forward if W pressed
        if keys[pygame.K_s]:
            self.move(dt * -1.0)        #move backward if S pressed
        if keys[pygame.K_SPACE]:
            self.shoot()
    
    #move the player's avatar around the screen, left or right
    def move(self, dt):
        u = pygame.Vector2(0,1).rotate(self.rotation)           #unit vector pointing straight up
        self.position += u * PLAYER_SPEED * dt                  #add change in position (direction * speed * tick time) to old position

    def shoot(self):
        if self.shot_timer > 0:
            return

        self.shot_timer = PLAYER_SHOOT_COOLDOWN
        new_shot = Shot(self.position.x, self.position.y)
        new_shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
