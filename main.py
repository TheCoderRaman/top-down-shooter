import pygame
import Player
from Projectile import *

pygame.init()
size    = (800, 600)
BGCOLOR = (255, 255, 255)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Top Down")

done = False
clock = pygame.time.Clock()

def move_entities():
    hero.move(screen.get_size())
    for proj in Projectile.projectiles:
        proj.move(screen.get_size())

def render_entities():
    hero.render(screen)
    for proj in Projectile.projectiles:
        proj.render(screen)
    
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

hero = Player.Player(screen.get_size())

while not done:
    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(BGCOLOR)
    
    process_keys(keys)
    process_mouse(mouse)
        
    move_entities()
    render_entities()
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()