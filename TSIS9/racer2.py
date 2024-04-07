#Imports
import pygame, sys
from pygame.locals import *
import random, time

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 550
SCREEN_HEIGHT = 825
SPEED = 5
speed=3
SCORE = 0

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load(r"C:\Users\user\Desktop\Pygame\TSIS8\AnimatedStreet2.png")

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((550,825))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\user\Desktop\Pygame\TSIS8\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load(r'C:\Users\user\Desktop\Pygame\TSIS8\coin.jpeg')
        self.rect=self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40), 0)
    
    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if (self.rect.bottom>600):
            self.rect.top=0
            self.rect.center= (random.randint(40, SCREEN_WIDTH - 40), 0)

class Coin2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load(r'C:\Users\user\Desktop\Pygame\TSIS8\coin2.png')
        self.rect=self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40), 0)
    
    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if (self.rect.bottom>600):
            self.rect.top=0
            self.rect.center= (random.randint(40, SCREEN_WIDTH - 40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\user\Desktop\Pygame\TSIS8\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                  

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1=Coin()
C2=Coin2()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
coins=pygame.sprite.Group()
coins2=pygame.sprite.Group()
enemies.add(E1)
coins.add(C1)
coins2.add(C2)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
all_sprites.add(C2)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#Game Loop
while True:
      
    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == INC_SPEED and SCORE%3==0:
              SPEED += 1      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (500,10))

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
        

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound(r"C:\Users\user\Desktop\Pygame\TSIS8\crash.wav").play()
          time.sleep(1)
                   
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
    
    collisions=pygame.sprite.spritecollide(P1, coins, True)
    for coin in collisions:
            SCORE+=1
            C1 = Coin()
            coins.add(C1)
            all_sprites.add(C1)
    collisions=pygame.sprite.spritecollide(P1, coins2, True)
    for coin in collisions:
            SCORE+=2
            C2 = Coin2()
            coins2.add(C2)
            all_sprites.add(C2)
    pygame.display.update()
    FramePerSec.tick(FPS)
