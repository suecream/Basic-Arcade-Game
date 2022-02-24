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
character_y_pos = screen_height -character_height # 화면 세로의 가장 아래 위치

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
game_font = pygame.font.Font(None,40) # 폰트 객체 생성 (폰트, 크기)

# 총 시간 
total_time = 10

# 시작 시간 계산
start_ticks = pygame.time.get_ticks() #시작 tick 을 받아옴 
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

# 충돌 처리 (collision)를 위한 rect 정보 업데이트
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

    screen.blit(background, (0,0)) # 배경 그리기
    # screen.fill((0,0,255)) fill로 채워도 된다
    screen.blit(character, (character_x_pos,character_y_pos)) # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos,enemy_y_pos))

    # 타이머
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # ms단위
    
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))

    screen.blit(timer,(10,10))

    if total_time - elapsed_time <=0:
        print("타임 아웃")
        running = False

    pygame.display.update() # 배경 다시 그리기(반복)


pygame.time.delay(2000) # 종료 후 대기

pygame.quit()








