from turtle import Screen
import pygame

pygame.init()

# screen size
screen_width = 800 # horizontal
screen_height = 640 # vertical
screen = pygame.display.set_mode((screen_width, screen_height))

# title
pygame.display.set_caption("NaDo GaMe")

# FPS
clock = pygame.time.Clock()

# background set
background = pygame.image.load("C:/Users/HJ/Documents/PythonWorkSpace/pygame_basic/background.png")

# 스프라이트(캐릭터) 불러오기
character = pygame.image.load("C:/Users/HJ/Documents/PythonWorkSpace/pygame_basic/character.png")
character_size = character.get_rect().size # 이미지 크기를 구해옴
character_width = character_size[0] # 가로크기
character_height = character_size[1] # 세로크기
character_x_pos = (screen_width / 2) - character_width/2 # 화면 가로의 절반에 위치
character_y_pos = screen_height -character_height# 화면 세로의 가장 아래 위치

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 1

# event loop
running = True
while running:
    dt = clock.tick(60) # FPS 설정

    print("FPS : "+ str(clock.get_fps())) # FPS 확인
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트
            running = False
        
        if event.type == pygame.KEYDOWN: # 키가 눌러 졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed 
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed 
            elif event.key == pygame.K_UP:
                to_y -= character_speed 
            elif event.key == pygame.K_DOWN:
                to_y += character_speed 

        if event.type == pygame.KEYUP: # 키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0     

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

# 가로 경계 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
# 세로 경계 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height


    screen.blit(background, (0,0)) # 배경 그리기
    # screen.fill((0,0,255)) fill로 채워도 된다

    screen.blit(character, (character_x_pos,character_y_pos)) # 캐릭터 그리기


    pygame.display.update() # 배경 다시 그리기(반복)
pygame.quit()








