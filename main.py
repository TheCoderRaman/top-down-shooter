import pygame
import random
from Player import Player
from Enemy import Enemy
from Projectile import Projectile

pygame.init()
size    = (800, 600)
BGCOLOR = (255, 255, 255)
screen = pygame.display.set_mode(size)
font = pygame.font.Font(None, 30)
pygame.display.set_caption("Top Down")

done = False
clock = pygame.time.Clock()

def move_entities(timeDelta):
    hero.move(screen.get_size(), timeDelta)
    for proj in Player.projectiles:
        proj.move(screen.get_size(), timeDelta)
    for enemy in enemies:
        enemy.move(hero.rect.topleft, timeDelta)

def render_entities():
    hero.render(screen)
    for proj in Player.projectiles:
        proj.render(screen)
    for enemy in enemies:
        enemy.render(screen)    
    
def process_keys(keys):
    if keys[pygame.K_w]:
        hero.movementVector[1] -= 1
    if keys[pygame.K_a]:
        hero.movementVector[0] -= 1
    if keys[pygame.K_s]:
        hero.movementVector[1] += 1
    if keys[pygame.K_d]:
        hero.movementVector[0] += 1
        
def process_mouse(mouse):
    if mouse[0]:
        hero.shoot(pygame.mouse.get_pos())

hero = Player(screen.get_size())
enemies = pygame.sprite.Group()
lastEnemy = 0

while not done:
    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()
    currentTime = pygame.time.get_ticks()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(BGCOLOR)
    
    process_keys(keys)
    process_mouse(mouse)
    
    if lastEnemy < currentTime - 1000:
        spawnSide = random.random()
        if spawnSide < 0.25:
            enemies.add(Enemy((0, random.randint(0, size[1]))))
        elif spawnSide < 0.5:
            enemies.add(Enemy((size[0], random.randint(0, size[1]))))
        elif spawnSide < 0.75:
            enemies.add(Enemy((random.randint(0, size[0]), 0)))
        else:
            enemies.add(Enemy((random.randint(0, size[0]), size[1])))
        lastEnemy = currentTime
    
    move_entities(clock.get_time()/17)
    render_entities()
    
    # fps = font.render(str(len(Player.projectiles)), True, pygame.Color('black'))
    # screen.blit(fps, (20, 20))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
