import pygame

class Projectile():
    projectiles = []
    def __init__(self, source, target, speed):
        self.x = source[0]
        self.y = source[1]
        self.movementVector = [target[0], target[1]]
        self.speed = speed
        self.projectiles.append(self)
    def move(self, surfaceSize):
        self.x += self.movementVector[0] * self.speed
        self.y += self.movementVector[1] * self.speed
        if self.x > surfaceSize[0] or self.x < 0  or \
           self.y > surfaceSize[1] or self.y < 0:
            self.projectiles.remove(self)
    def draw(self, surface):
        pygame.draw.circle(surface, (255, 0, 0), (int(self.x), int(self.y)), 2)