from re import T
import os 
import pygame
import random

# 초기화
pygame.init()

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

# background set
screen_width = 800
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Shooting_Game")
background = pygame.image.load("pygame_basic/background.png")

# sprite set
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

bullets =[]

c_to_y = 0
e_to_x = 0
b_to_y = 0
b_to_x = 0
character_speed = 0.5
enemy_speed = 0.1
bullet_speed = 1

running = True
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
                bullet_x_pos = character_x_pos + character_width
                bullet_y_pos = character_y_pos + (character_height / 2) - (bullet_height)
                bullets.append([bullet_x_pos,bullet_y_pos])

        if event.type == pygame.KEYUP:
            if pygame.K_UP or pygame.K_DOWN:
                c_to_y = 0
                b_to_y = 0

    character_y_pos = character_y_pos + c_to_y
    bullet_y_pos = bullet_y_pos + b_to_y
    enemy_1_x_pos = enemy_1_x_pos - enemy_speed
    enemy_2_x_pos = enemy_2_x_pos - enemy_speed
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # bullet position
    bullets = [[w[0],w[1] - bullet_speed] for w in bullets]
    bullets = [[w[0],w[1]] for w in bullets if w[0] < 800]

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    enemy_1_rect = enemy_1.get_rect()
    enemy_1_rect.left = enemy_1_x_pos
    enemy_1_rect.top = enemy_1_y_pos

    enemy_2_rect = enemy_2.get_rect()
    enemy_2_rect.left = enemy_2_x_pos
    enemy_2_rect.top = enemy_2_y_pos

    if character_rect.colliderect(enemy_1_rect):
        print("충돌!")
        running = False
    elif character_rect.colliderect(enemy_2_rect):
        print("충돌!")
        running = False

    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy_1,(enemy_1_x_pos,enemy_1_y_pos))
    screen.blit(enemy_2,(enemy_2_x_pos,enemy_2_y_pos))
    screen.blit(bullet,(bullet_x_pos,bullet_y_pos))


    pygame.display.update()

pygame.time.delay(3000)

pygame.quit()