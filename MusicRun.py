# Import a library of functions called 'pygame'
import pygame
import random
from Draw import *

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 60, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (200, 0, 255)
YELLOW = (255, 255, 0)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
GROUND = 250 #pixel ground level

mod = 0
        
def main():
    
    pygame.init()# Initialize the game engine

    size = (700, 500)   #Window Size
    screen = pygame.display.set_mode(size)  #Window Creation
    pygame.display.set_caption("MusicRun")  #Displays Window Title

    
    done = False # Loop until the user clicks the close button.

    clock = pygame.time.Clock() # Used to manage how fast the screen updates
    
    velocity = 4 #speed of character

    flowX1, flowX2, flowX3, flowX4, flowX5 = SCREEN_WIDTH, SCREEN_WIDTH, SCREEN_WIDTH, SCREEN_WIDTH, SCREEN_WIDTH #starting pos of flowers
    cloudX, cloudY = SCREEN_WIDTH, random.randrange(10, 100) #Starting pos of clouds
    player = Player()
    Player()
    global mod
    mod = [0] #determines how fast scenery moves

    jump_sound = pygame.mixer.Sound("spin_jump.wav") #Jump Sound

    # -------- Main Program Loop -----------    
    while not done:
        # --- Main event loop
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop

        # --- Game logic should go here
        
        # --- Drawing code should go here
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(WHITE)

        pygame.draw.rect(screen, (100,100,200), [0, 0, SCREEN_WIDTH, SCREEN_HEIGHT - 200]) #Sky Backdrop
        pygame.draw.rect(screen, GREEN, [0, 300, 700, 200]) #Floor drawn
        player.draw(screen)
        player.update(mod)

        pygame.draw.rect(screen, WHITE, [cloudX, cloudY, 50, 30]) #Cloud Drawn

        pygame.draw.ellipse(screen, YELLOW, [flowX1, 310, 2,2]) #Flower drawn
        pygame.draw.ellipse(screen, YELLOW, [flowX2, 350, 4,4]) #Flower drawn
        pygame.draw.ellipse(screen, YELLOW, [flowX3, 390, 6,6]) #Flower drawn
        pygame.draw.ellipse(screen, YELLOW, [flowX4, 430, 8,8]) #Flower drawn
        pygame.draw.ellipse(screen, YELLOW, [flowX5, 470, 10,10]) #Flower drawn

#------------------------------------------------
    #Cloud Behavior
        cloudX -= .5 + mod[0] #Moves Cloud to the left plus how fast the character is going

        if (cloudX < -50):  #When Cloud moves off left screen, respawn on right side
            cloudX = SCREEN_WIDTH
            cloudY = random.randrange(10, 100)

#------------------------------------------------
    #Flower Behavior

        flowX1 -= 1.1 + mod[0] #Moves flower to the left plus how fast the character is going
        flowX2 -= 1.3 + mod[0]
        flowX3 -= 1.5 + mod[0]
        flowX4 -= 1.7 + mod[0]
        flowX5 -= 1.9 + mod[0]
        
        
        if (flowX1 < -10):  #When flower moves off left screen, respawn on right side
            flowX1 = SCREEN_WIDTH
        if (flowX2 < -10):  
            flowX2 = SCREEN_WIDTH
        if (flowX3 < -10):  
            flowX3 = SCREEN_WIDTH
        if (flowX4 < -10):  
            flowX4 = SCREEN_WIDTH
        if (flowX5 < -10):  
            flowX5 = SCREEN_WIDTH

#------------------------------------------------
        #Handles all key down events

        player.handle_keys(mod)
    

#-------------------------------------------------

        # updates the screen with what we've drawn.
        pygame.display.flip()
        # Limit to 60 frames per second
        clock.tick(60)
    pygame.quit()
    
main()
