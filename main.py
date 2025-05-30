import pygame
from constants import *

#import os
#os.environ['DISPLAY'] = ':0.0'

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    #initialize pygame
    pygame.init()

    #initialize screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # infinite loop to run game
    while True:
       # print("Game loop running")
       # pygame.event.get()
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #fill screen with black    
        screen.fill("black")

        #refresh the screen
        pygame.display.flip()





if __name__ == "__main__":
    main()