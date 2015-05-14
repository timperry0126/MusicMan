#Developed by: Timothy Perry, Simone Boyd, Quinn Daugherty, and Paul Tuttle
#Class: CST 205

import random
import pygame

GROUND = 300
WHITE = (255,255,255)
LEVEL_ONE = 351
LEVEL_TWO = 238
LEVEL_THREE = 114

class Player(object):   #Player class written by Tim

    def __init__(self, option): #Constructor
        self.image = pygame.image.load(option + "1.png").convert()  #Loads Character
        self.image.set_colorkey(WHITE)  #Sets color to turn transparent
        self.x = 140 # x position object is drawn at
        self.y = 300 # y position object is drawn at
        self.width = 28 # width of pic
        self.height = 62 # height of pic
        self.stat = 1 # counter for update()
        self.walk = 12 # Controls how fast animation loops
        self.isJump = False #returns true if player is currently jumping
        self.stable = False #returns true if player is on platform
        self.jumpHeight = 128
        self.jumpCounter = 0

    def isPlatform(self, collision, platAmount):
        #Collion: multidimentional [platAmount][x,y,width]

        for x in range(0, platAmount):
            if((self.y + self.height) == collision[x][1]):
                if(self.x >= collision[x][0] and self.x <= (collision[x][0] + collision[x][2])):
                    self.stable = True
                    return
        self.stable = False
        

    def handle_keys(self, mod):
        #Handles all key down events

        keys = pygame.key.get_pressed()

        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]): #Speeds character up
            if(mod[0] < 6):
                mod[0] += 1
                
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]): #Slows Character Down
            if(mod[0] > 0):
                mod[0] -= 1

        #---Jumping----------------------------
        if(self.jumpCounter != -1): #Makes sure the character is not currently falling
            if (keys[pygame.K_w] or keys[pygame.K_UP]):  #Marks character as currently jumping
                self.isJump = True

        if(self.isJump == True and self.jumpCounter != self.jumpHeight):  #Jumps the character upwards
            self.y -= 2
            self.jumpCounter += 2
            self.isJump == False

        if(self.stable):    # Marks the character as not jumping if on platform
            self.isJump = False
            self.jumpCounter = 0

        if(self.y == GROUND):   #Declares the ground as a platform
            self.stable = True
            self.jumpCounter = 0
            self.isJump = False
            
        if((self.isJump == False and self.stable == False)):    #Bring character back to ground
            self.y += 2
            self.jumpCounter = -1 # Marks the character as currently falling

        if(self.jumpCounter == self.jumpHeight and self.stable == False):  #Second condition for bringing character back to the ground
            self. y += 2
                
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y)) #draws player to screen

    def update(self, mod, option):
        if (self.stat < self.walk * 2):    #draws first animation
            self.image = pygame.image.load(option + "1.png").convert()
            self.image.set_colorkey(WHITE)
            
        if (self.stat >= self.walk * 2 and self.stat < self.walk * 4):   #draws second animation
            self.image = pygame.image.load(option + "2.png").convert()
            self.image.set_colorkey(WHITE)
            
        if (self.stat >= self.walk * 4 and self.stat < self.walk * 6):  #draws third animation
            self.image = pygame.image.load(option + "3.png").convert()
            self.image.set_colorkey(WHITE)
            
        if (self.stat >= self.walk * 6 and self.stat < self.walk * 8):  #draws fourth animation
            self.image = pygame.image.load(option + "4.png").convert()
            self.image.set_colorkey(WHITE)

        if (self.stat >= self.walk * 8 and self.stat < self.walk * 10):  #draws fourth animation
            self.image = pygame.image.load(option + "5.png").convert()
            self.image.set_colorkey(WHITE)

        if (self.stat >= self.walk * 10 and self.stat < self.walk * 12):  #draws fourth animation
            self.image = pygame.image.load(option + "6.png").convert()
            self.image.set_colorkey(WHITE)

        if (self.stat >= self.walk * 12 and self.stat < self.walk * 14):  #draws fourth animation
            self.image = pygame.image.load(option + "7.png").convert()
            self.image.set_colorkey(WHITE)

        if (self.stat >= self.walk * 14 and self.stat < self.walk * 16):  #draws fourth animation
            self.image = pygame.image.load(option + "8.png").convert()
            self.image.set_colorkey(WHITE)

        if(self.isJump != True): #prevents animation from changing while jumping
            self.stat += 5 + mod[0] #how fast animation moves plus speed of character
        
        if (self.stat > self.walk * 16):   #loops back to beginning animation
            self.stat = 1


#---Sound Controls------------------------Paul----
#Func Desc.-------------------------
#The following fuctions would have controlled sound for the game. It would take
#the players y axis and compare it to the y-values of the platforms. So
#depending on the character and the platform there would be a different song.
#---Problem
#The issue I am facing with this function is getting the screen to
#update when it was playing music. It will either play music and freeze the screen
#or not play music until the screen froze.
    #def platformSound(self, choice):
        #while pygame.mixer.get_busy() == False:
            #if self.y >= 351:
                #pygame.mixer.music.load(choice + '1.wav')
                #pygame.mixer.music.play(-1)
            
            #if self.y < 351 and self.y >= 238
                #pygame.mixer.music.load(choice + '2.wav')
                #pygame.mixer.music.play(-1)
            #if self.y <238
                #pygame.mixer.music.load(choice + '3.wav')
                #pygame.mixer.music.play(-1)

#Func. Desc.------------------------------
#This function will pick and play a random sound from the predetermined list. This
#function uses the random.choice function built into pygame.
#Problem----------------------------------
#I am not sure the issue with this function it would cause both the shell and IDLE
#crash when running. I was able to get a simplified version of the function to work
#although it would have the same problem with the other function and would freeze the screen.
            
    #def play_sound():
        #next_sound = random.choice(sound_Effects)
        #while next_sound == currently_playing_sound:
           # next_song = random.choice(sound_Effects)
        #currently_playing_sound = next_sound
        #pygame.mixer.music.load(next_sound)
        #pygame.mixer.music.play()
        #if pygame.mixer.music.get_busy() == False:
            #pygame.mixer.music.stop()

class Platform(object):     #Platform class written by Tim
    def __init__(self, xPos, yPos, image, h, l):
        self.x = xPos # x position of platform
        self.y = yPos # y position of platform
        self.image = pygame.image.load(image + ".png").convert()
        self.image.set_colorkey(WHITE)
        self.height = h # height of picture
        self.length = l # length of picture
        
    def draw(self, window):
        window.blit(self.image, (self.x, self.y)) #draws platform to screen

    def update(self, mod, uni):
        self.x -= 1 + mod[0] #how fast plaform is moving

        if(self.x < -100): #if platform goes out of screen, re-appear on right side
            uni.pop(0)

    def coord(self):
        return [self.x, self.y, self.length]

    def posX(self):
        return self.x

class CharacterSelector(object):
    def __init__(self, xPos, yPos, option):
        self.x = xPos
        self.y = yPos
        self.stat = 1 # counter for update()
        self.walk = 12 # Controls how fast animation loops
        self.image = pygame.image.load(option + "1.png").convert()
        self.image.set_colorkey(WHITE)
              
        
    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
        

    def update(self, mod, option):
        if (self.stat < self.walk * 2):    #draws first animation
            self.image = pygame.image.load(option + "1.png").convert()
            self.image.set_colorkey(WHITE)
            
        if (self.stat >= self.walk * 2 and self.stat < self.walk * 4):   #draws second animation
            self.image = pygame.image.load(option + "2.png").convert()
            self.image.set_colorkey(WHITE)
            
        if (self.stat >= self.walk * 4 and self.stat < self.walk * 6):  #draws third animation
            self.image = pygame.image.load(option + "3.png").convert()
            self.image.set_colorkey(WHITE)
            
        if (self.stat >= self.walk * 6 and self.stat < self.walk * 8):  #draws fourth animation
            self.image = pygame.image.load(option + "4.png").convert()
            self.image.set_colorkey(WHITE)

        if (self.stat >= self.walk * 8 and self.stat < self.walk * 10):  #draws fourth animation
            self.image = pygame.image.load(option + "5.png").convert()
            self.image.set_colorkey(WHITE)

        if (self.stat >= self.walk * 10 and self.stat < self.walk * 12):  #draws fourth animation
            self.image = pygame.image.load(option + "6.png").convert()
            self.image.set_colorkey(WHITE)

        if (self.stat >= self.walk * 12 and self.stat < self.walk * 14):  #draws fourth animation
            self.image = pygame.image.load(option + "7.png").convert()
            self.image.set_colorkey(WHITE)

        if (self.stat >= self.walk * 14 and self.stat < self.walk * 16):  #draws fourth animation
            self.image = pygame.image.load(option + "8.png").convert()
            self.image.set_colorkey(WHITE)

        self.stat += 5 + mod[0] #how fast animation moves plus speed of character
        
        if (self.stat > self.walk * 16):   #loops back to beginning animation
            self.stat = 1


