import pygame
import random

pygame.init()

screen_width = 800
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Shooting_Game")
background = pygame.image.load("pygame_basic/background.png")

character = pygame.image.load("pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]

enemy_1 = pygame.image.load("pygame_basic/enemy.png") 
enemy_1_size = enemy_1.get_rect().size
enemy_1_width = enemy_1_size[0]
enemy_1_height = enemy_1_size[1]

enemy_2 = pygame.image.load("pygame_basic/enemy.png") 
enemy_2_size = enemy_2.get_rect().size
enemy_2_width = enemy_2_size[0]
enemy_2_height = enemy_2_size[1]

bullet = pygame.image.load("pygame_basic/bullet.png")
bullet_size = bullet.get_rect().size
bullet_width = bullet_size[0]
bullet_height = bullet_size[1]


