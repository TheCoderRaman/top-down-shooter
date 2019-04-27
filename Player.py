import pygame
import math
from Projectile import *

PLAYERCOLOR = (255,   0,   0)

def normalize_vector(vector):
    pythagoras = math.sqrt(vector[0]*vector[0] + vector[1]*vector[1])
    return (vector[0]/pythagoras, vector[1]/pythagoras)

class Player(pygame.sprite.Sprite):
    def __init__(self, screenSize):
        super().__init__()
        self.image = pygame.Surface([8, 8])
        self.image.fill(PLAYERCOLOR)
        self.rect = self.image.get_rect()
        print(self.rect)
        
        self.x = screenSize[0]//2
        self.y = screenSize[1]//2
        self.movementVector = [0, 0]
        self.movementSpeed = 3
        self.lastShot = 0
        self.weaponCooldown = 200

    def move(self, screenSize):
        if self.movementVector != [0, 0]:
            self.movementVector = normalize_vector(self.movementVector)
        newPos = (self.x + self.movementVector[0]*self.movementSpeed,
                  self.y + self.movementVector[1]*self.movementSpeed)
        if newPos[0] < 0:
            self.x = 0
        elif newPos[0] > screenSize[0]-self.rect.width:
            self.x = screenSize[0]-self.rect.width
        else:
            self.x = newPos[0]

        if newPos[1] < 0:
            self.y = 0
        elif newPos[1] > screenSize[1]-self.rect.height:
            self.y = screenSize[1]-self.rect.width
        else:
            self.y = newPos[1]

        self.movementVector = [0, 0]
    def shoot(self, mousePos):
        if pygame.time.get_ticks() - self.lastShot > self.weaponCooldown:
            direction = (mousePos[0]-self.x, mousePos[1]-self.y) \
                if mousePos != (self.x, self.y) else (1, 1)
            proj = Projectile((self.x, self.y),
                              normalize_vector(direction),
                              5)            
            del proj
            self.lastShot = pygame.time.get_ticks()        
    def render(self, surface):
        surface.blit(self.image, (self.x, self.y))