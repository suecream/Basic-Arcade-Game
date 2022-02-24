from turtle import Screen
import pygame
###############################################################
# 0. 기본 초기화 (반드시 해야함)
pygame.init()

# screen size
screen_width = 800
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# title
pygame.display.set_caption("NaDo GaMe")

# FPS
clock = pygame.time.Clock()

###############################################################

# 1. 사용자 게임 초기화 (배경, 게임 이미지, 좌표, 폰트, 속도 등)

# background set
background = pygame.image.load("C:/Users/HJ/Documents/PythonWorkSpace/pygame_basic/background.png")

# 스프라이트(캐릭터) 불러오기
character = pygame.image.load("C:/Users/HJ/Documents/PythonWorkSpace/pygame_basic/character.png")
character_size = character.get_rect().size 
character_width = character_size[0]
character_height = character_size[1] 
character_x_pos = (screen_width / 2) - character_width/2 
character_y_pos = screen_height -character_height 

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 1

# 적 enemy 캐릭터
enemy = pygame.image.load("C:/Users/HJ/Documents/PythonWorkSpace/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size 
enemy_width = enemy_size[0]
enemy_height = enemy_size[1] 
enemy_x_pos = (screen_width / 2) - enemy_width/2
enemy_y_pos = (screen_height / 2) - enemy_height/2


# 폰트 정의 
game_font = pygame.font.Font(None,40)

# 총 시간 
total_time = 10

# 시작 시간 계산
start_ticks = pygame.time.get_ticks()
# event loop
running = True
while running:
    dt = clock.tick(60) 

    print("FPS : "+ str(clock.get_fps())) 

###############################################################

    # 2. 이벤트 처리
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT:
                to_x -= character_speed 
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed 
            elif event.key == pygame.K_UP:
                to_y -= character_speed 
            elif event.key == pygame.K_DOWN:
                to_y += character_speed 

        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0     
###############################################################
    # 3. 게임 캐릭터 위치값 처리
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

###############################################################

# 4. 충돌 처리 (collision)를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌!")
        running = False
###############################################################
# 5. 화면에 그리기
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos,character_y_pos)) 
    screen.blit(enemy, (enemy_x_pos,enemy_y_pos))

    # 타이머
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 
    
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))

    screen.blit(timer,(10,10))

    if total_time - elapsed_time <=0:
        print("타임 아웃")
        running = False

    pygame.display.update() 


pygame.time.delay(2000) 

pygame.quit()








