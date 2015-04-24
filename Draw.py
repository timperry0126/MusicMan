import random
import pygame

GROUND = 300
WHITE = (255,255,255)

class Player(object):

    def __init__(self): #Constructor
        self.image = pygame.image.load("Eye_walk_1.png").convert()
        self.image.set_colorkey(WHITE)
        self.x = 140 # x position object is drawn at
        self.y = 300 # y position object is drawn at
        self.stat = 1 # counter for update()
        self.walk = 12 # Controls how fast animation loops
        self.isJump = False

    def handle_keys(self, mod):
        #Handles all key down events

        keys = pygame.key.get_pressed()

        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]): #moves character to the right 
            if(mod[0] < 6):
                mod[0] += 1
                
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]): #moves character to the left
            if(mod[0] > 0):
                mod[0] -= 1

        #---Jumping---------------------------- 
                
        if (keys[pygame.K_w] or keys[pygame.K_UP]): #jumps character
            self.y -= 2
        if(not(keys[pygame.K_w] or keys[pygame.K_UP]) and self.y != GROUND):
            self.y += 2
                
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y)) #draws player to screen

    def update(self, mod):
        if (self.stat < self.walk * 2):    #draws first animation
            self.image = pygame.image.load("Eye_walk_1.png").convert()
            self.image.set_colorkey(WHITE)
            
        if (self.stat >= self.walk * 2 and self.stat < self.walk * 4):   #draws second animation
            self.image = pygame.image.load("Eye_walk_2.png").convert()
            self.image.set_colorkey(WHITE)
            
        if (self.stat >= self.walk * 4 and self.stat < self.walk * 6):  #draws third animation
            self.image = pygame.image.load("Eye_walk_3.png").convert()
            self.image.set_colorkey(WHITE)
            
        if (self.stat >= self.walk * 6 and self.stat < self.walk * 8):  #draws fourth animation
            self.image = pygame.image.load("Eye_walk_4.png").convert()
            self.image.set_colorkey(WHITE)

        if (self.stat >= self.walk * 8 and self.stat < self.walk * 10):  #draws fourth animation
            self.image = pygame.image.load("Eye_walk_5.png").convert()
            self.image.set_colorkey(WHITE)

        if (self.stat >= self.walk * 10 and self.stat < self.walk * 12):  #draws fourth animation
            self.image = pygame.image.load("Eye_walk_6.png").convert()
            self.image.set_colorkey(WHITE)

        if (self.stat >= self.walk * 12 and self.stat < self.walk * 14):  #draws fourth animation
            self.image = pygame.image.load("Eye_walk_7.png").convert()
            self.image.set_colorkey(WHITE)

        if (self.stat >= self.walk * 14 and self.stat < self.walk * 16):  #draws fourth animation
            self.image = pygame.image.load("Eye_walk_8.png").convert()
            self.image.set_colorkey(WHITE)

        self.stat += 5 + mod[0] #how fast animation moves plus speed of character
        
        if (self.stat > self.walk * 16):   #loops back to beginning animation
            self.stat = 1

class Platform(object):
    def __init__(self, xPos, yPos):
        self.x = xPos
        self.y = yPos
        
    def draw(self, window):
        pygame.draw.rect(window, (0,0,0), [self.x, self.y, 100, 20])

    def update(self, mod):
        self.x -= 1 + mod[0]

        if(self.x < -100):
            self.x = 700
