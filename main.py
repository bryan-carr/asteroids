import pygame, sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

#troubleshooting - boots suggested setting this to help VcXsrv find the display. Doesn't seem to help.
#import os
#os.environ['DISPLAY'] = ':0.0'

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    #initialize pygame
    pygame.init()

    #troubleshooting tips from Boots
    #print(pygame.display.get_driver())      #output: offscreen
    #print(pygame.display.get_wm_info())     #output: {}

    #initialize clock
    internal_clock = pygame.time.Clock()
    dt = 0   #delta time variable

    #initialize screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #create 2 groups to track objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #add Class instances to the containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    #instantiate the Player object
    player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)

    #instantiate an Asteroid Field
    field = AsteroidField()





    # infinite loop to run game
    while True:
       # print("Game loop running") #troubleshooting - display this line to confirm loop is running
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #fill screen with black    
        screen.fill("black")

        #Update player's position, then Draw the player
        updatable.update(dt)           #checks for input, then updates rotation

        #check for collisions between Asteroids and Player
        for ast in asteroids:
            if ast.collision_check(player):
                print("Game Over!")
                sys.exit()
            
            #check for collisions between Shots and Asteroids
            for shot in shots:
                if ast.collision_check(shot):
                    ast.split()
                    shot.kill()            


        for obj in drawable:
            obj.draw(screen)            #draws all objects on screen
        pygame.display.flip()           #refresh the screen


        #slow loop down to 1/60s ticks -- limits frame rate to 60 fps
        dt = internal_clock.tick(60)/1000


if __name__ == "__main__":
    main()