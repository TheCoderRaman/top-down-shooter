import pygame
import math
from Projectile import Projectile

def normalize_vector(vector):
    pythagoras = math.sqrt(vector[0]*vector[0] + vector[1]*vector[1])
    return (vector[0] / pythagoras, vector[1] / pythagoras)

class Enemy(pygame.sprite.Sprite):
    projectiles = pygame.sprite.Group()
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface([8, 8])
        self.image.fill(pygame.Color('black'))
        self.rect = self.image.get_rect(x=pos[0], y=pos[1])
        
        self.pos = list(pos)
        self.movementVector = [0, 0]
        self.movementSpeed = 1.5
        self.lastShot = pygame.time.get_ticks()
        # self.lastMoved = pygame.time.get_ticks()
        self.weaponCooldown = 1500
        
    def move(self, enemies, playerPos, tDelta):
        # currentTime = pygame.time.get_ticks()
        # otherEnemies = enemies.copy()
        # otherEnemies.remove(self)
        self.movementVector = (playerPos[0] - self.pos[0],
                               playerPos[1] - self.pos[1])
        if self.movementVector != (0, 0):
            self.movementVector = normalize_vector(self.movementVector)
        self.pos[0] += self.movementVector[0] * self.movementSpeed * tDelta
        self.pos[1] += self.movementVector[1] * self.movementSpeed * tDelta
        # for enemy in otherEnemies:
            # if abs(enemy.pos[0] - self.pos[0]) < self.rect.width - 2 and \
               # abs(enemy.pos[1] - self.pos[1]) < self.rect.width - 2 and \
               # currentTime - self.lastMoved > 200:
                # distance = normalize_vector((enemy.pos[0] - self.pos[0],
                                             # enemy.pos[1] - self.pos[1]))
                # self.pos[0] = enemy.pos[0] - distance[0]*self.rect.width
                # self.pos[1] = enemy.pos[1] - distance[1]*self.rect.width
                # self.lastMoved = currentTime
        self.rect.topleft = self.pos
    def shoot(self, playerPos):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastShot > self.weaponCooldown:
            direction = (playerPos[0] - self.pos[0], playerPos[1] - self.pos[1])
            self.lastShot = currentTime
            self.projectiles.add(Projectile(self.pos,
                                            normalize_vector(direction),
                                            3, 500, (255, 0, 0)))
    def render(self, surface):
        surface.blit(self.image, self.pos)
