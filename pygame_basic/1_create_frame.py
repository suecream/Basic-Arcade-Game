import pygame

pygame.init()

# screen size
screen_width = 800 # horizontal
screen_height = 640 # vertical
screen = pygame.display.set_mode((screen_width, screen_height))

# title
pygame.display.set_caption("NaDo GaMe")

# background set
background = pygame.image.load("C:/Users/HJ/Documents/PythonWorkSpace/pygame_basic/background.png")


# event loop
running = True
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트
            running = False
    screen.blit(background, (0,0)) # 배경 그리기
    # screen.fill((0,0,255)) fill로 채워도 된다

    pygame.display.update() # 배경 다시 그리기(반복)
pygame.quit()







