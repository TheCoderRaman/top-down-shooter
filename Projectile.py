import pygame

PROJECTILECOLOR = (255,   0,   0)

class Projectile(pygame.sprite.Sprite):
    projectiles = []
    def __init__(self, source, target, speed):
        super().__init__()
        self.image = pygame.Surface([4, 4])
        self.image.set_colorkey(pygame.Color('black'))
        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image, PROJECTILECOLOR,
                           (self.rect.width//2, self.rect.height//2), 2)
        
        self.x = source[0]
        self.y = source[1]
        self.movementVector = [target[0], target[1]]
        self.speed = speed
        self.projectiles.append(self)
    def move(self, surfaceSize, tDelta):
        self.x += self.movementVector[0] * self.speed * tDelta
        self.y += self.movementVector[1] * self.speed * tDelta
        if self.x > surfaceSize[0] or self.x < 0  or \
           self.y > surfaceSize[1] or self.y < 0:
            self.projectiles.remove(self)
    def render(self, surface):
        surface.blit(self.image, (self.x, self.y))
        