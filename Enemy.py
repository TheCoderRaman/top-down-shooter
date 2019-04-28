import pygame
import operator
import math

def normalize_vector(vector):
    pythagoras = math.sqrt(vector[0]*vector[0] + vector[1]*vector[1])
    return (vector[0] / pythagoras, vector[1] / pythagoras)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface([8, 8])
        self.image.fill(pygame.Color('black'))
        self.rect = self.image.get_rect(x=pos[0], y=pos[1])
        
        self.pos = list(pos)
        self.movementVector = [0, 0]
        self.movementSpeed = 2
    def move(self, playerPos, tDelta):
        self.movementVector = (playerPos[0] - self.pos[0],
                               playerPos[1] - self.pos[1])
        if self.movementVector != (0, 0):
            self.movementVector = normalize_vector(self.movementVector)
        self.pos[0] += self.movementVector[0]*self.movementSpeed*tDelta
        self.pos[1] += self.movementVector[1]*self.movementSpeed*tDelta
        self.rect.topleft = self.pos
    def render(self, surface):
        surface.blit(self.image, self.pos)
