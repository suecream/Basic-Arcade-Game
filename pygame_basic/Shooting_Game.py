from re import T
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
character_x_pos = 10
character_y_pos = (screen_height/2)-(character_height/2)

enemy_1 = pygame.image.load("pygame_basic/enemy.png") 
enemy_1_size = enemy_1.get_rect().size
enemy_1_width = enemy_1_size[0]
enemy_1_height = enemy_1_size[1]
enemy_1_x_pos = screen_width - enemy_1_width
enemy_1_y_pos = random.randint(0,640-enemy_1_height)

enemy_2 = pygame.image.load("pygame_basic/enemy.png") 
enemy_2_size = enemy_2.get_rect().size
enemy_2_width = enemy_2_size[0]
enemy_2_height = enemy_2_size[1]
enemy_2_x_pos = screen_width - enemy_2_width
enemy_2_y_pos = random.randint(0,640-enemy_2_height)

bullet = pygame.image.load("pygame_basic/bullet.png")
bullet_size = bullet.get_rect().size
bullet_width = bullet_size[0]
bullet_height = bullet_size[1]
bullet_x_pos = character_x_pos + character_width
bullet_y_pos = character_y_pos + (character_height/2) - (bullet_height/2)

c_to_y = 0
e_to_x = 0
b_to_y = 0
b_to_x = 0
character_speed = 0.5
enemy_speed = 0.5
bullet_speed = 1

running = True
shooting = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                c_to_y -= character_speed
                b_to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                c_to_y += character_speed
                b_to_y += character_speed
            elif event.key == pygame.K_SPACE:
                shooting = True

        if event.type == pygame.KEYUP:
            if pygame.K_UP or pygame.K_DOWN:
                c_to_y = 0
                b_to_y = 0

    character_y_pos = character_y_pos + c_to_y
    bullet_y_pos = bullet_y_pos + b_to_y

    if character_y_pos < 0:
        character_y_pos = 0
        bullet_y_pos = (character_height/2) - (bullet_height/2)
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
        bullet_y_pos = screen_height - character_height + (character_height/2) - (bullet_height/2)

    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy_1,(enemy_1_x_pos,enemy_1_y_pos))
    screen.blit(enemy_2,(enemy_2_x_pos,enemy_2_y_pos))
    screen.blit(bullet,(bullet_x_pos,bullet_y_pos))


    pygame.display.update()

pygame.quit()