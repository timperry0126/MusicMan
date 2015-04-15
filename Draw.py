import random
import pygame

GROUND = 250

class Player(object):

    def __init__(self): #Constructor
        self.image = pygame.image.load("RunningMan.png")
        
        self.x = 140 # x position object is drawn at
        self.y = 250 # y position object is drawn at
        self.stat = 1 # counter for update()

    def handle_keys(self, mod):
        #Handles all key down events

        keys = pygame.key.get_pressed()

        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]): #moves character to the right 
            if(mod[0] < 6):
                mod[0] += .5
                
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]): #moves character to the left
            if(mod[0] > 0):
                mod[0] -= .5
                
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and (self.y == GROUND): #jumps character
            for n in range(0, 100):
                self.y -= 1

        if (self.y != GROUND):  #bring player back to ground level if not on ground
            self.y += 2
                
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y)) #draws player to screen

    def update(self, mod):
        if (self.stat < 50):    #draws first animation
            self.image = pygame.image.load("RunningMan.png")
            
        if (self.stat >= 50 and self.stat < 100):   #draws second animation
            self.image = pygame.image.load("RunningMan2.png")
            
        if (self.stat >= 100 and self.stat < 150):  #draws third animation
            self.image = pygame.image.load("RunningMan3.png")
            
        if (self.stat >= 150 and self.stat < 200):  #draws fourth animation
            self.image = pygame.image.load("RunningMan4.png")
            
        self.stat += 2 + mod[0] #how fast animation moves plus speed of character
        
        if (self.stat > 200):   #loops back to beginning animation
            self.stat = 1
