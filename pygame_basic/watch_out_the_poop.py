from tokenize import Double
from tracemalloc import start
from turtle import Screen
import pygame
import random

pygame.init()

# background set
screen_width = 800
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("watch_out_the_poop")

clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()

background = pygame.image.load("C:/Users/HJ/Documents/PythonWorkSpace/pygame_basic/background.png")

# character sprite set
character =pygame.image.load("C:/Users/HJ/Documents/PythonWorkSpace/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width /2) - character_width/2
character_y_pos = screen_height - character_height

# poop sprite set
poop = pygame.image.load("C:/Users/HJ/Documents/PythonWorkSpace/pygame_basic/enemy.png")
poop_size = poop.get_rect().size
poop_width = poop_size[0]
poop_height = poop_size[1]
poop_x_pos = random.randint(0,800)
poop_y_pos = 0

game_font = pygame.font.Font(None,40)
score_font = pygame.font.Font(None,100)
to_x = 0
character_speed = 0.5
poop_speed = 0.5

running = True
while running:
    dt = clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
        if event.type == pygame.KEYUP:
            if pygame.K_LEFT or pygame.K_RIGHT:
                to_x = 0   

    character_x_pos = character_x_pos + (to_x*dt)
    poop_y_pos = poop_y_pos + (poop_speed*dt)
    
    if poop_y_pos >= 640:
        poop_x_pos = random.randint(0,800)
        poop_y_pos = 0
    
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    poop_rect = poop.get_rect()
    poop_rect.left = poop_x_pos
    poop_rect.top = poop_y_pos

    if character_rect.colliderect(poop_rect):
        print("실패!")
        running = False

    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(poop,(poop_x_pos,poop_y_pos))

    elapsed_time = (pygame.time.get_ticks()-start_ticks) /1000

    timer = game_font.render(str(int(elapsed_time)),True,(255,255,255))

    screen.blit(timer,(10,10))
    pygame.display.update()

score = score_font.render("score : "+str(int(elapsed_time)),True,(255,0,255))
screen.blit(score,(340,300))
pygame.display.update()

pygame.time.delay(5000)

pygame.quit()