import pygame
 
# здесь определяются цвета, время
FPS = 10
clock = pygame.time.Clock()

WIN_WIDTH = 512
WIN_HEIGHT = 600
 
WHITE = (255, 255, 255)
BLUE = (0, 177, 252)

# загружаем картиночки
pygame.init()
sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
sc.fill(BLUE)

nature_surf = pygame.image.load('nature.png').convert()
nature_surf.set_colorkey((WHITE))
nature_rect = nature_surf.get_rect(center=(256, 344))
sc.blit(nature_surf, nature_rect)

eagle1_surf = pygame.image.load('eagle1.png').convert()
eagle1_surf.set_colorkey((WHITE))
eagle1_rect = eagle1_surf.get_rect(center=(450, 60))

eagle2_surf = pygame.image.load('eagle2.png').convert()
eagle2_surf.set_colorkey((WHITE))
eagle2_rect = eagle2_surf.get_rect(center=(450, 60))

mouse_surf = pygame.image.load('mouse.png').convert()
mouse_surf.set_colorkey((WHITE))
mouse_rect = eagle2_surf.get_rect(center=(30, 450))


pygame.display.update()

flag = True
n = 0

# главный цикл
while True:
    # задержка
    clock.tick(FPS)

    # цикл обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

    # фон заново
    sc.fill(BLUE)
    sc.blit(nature_surf, nature_rect)
    sc.blit(mouse_surf, mouse_rect)

    # манипуляции над орлом
    if n < 3:
        eagle2_rect.x -= 10
        sc.blit(eagle2_surf, eagle2_rect)
        flag = False
    else:
        eagle1_rect.x -= 10
        sc.blit(eagle1_surf, eagle1_rect)
        flag = True
        if n == 5:
            n = -1
    
    if eagle1_rect.x < -50:
        eagle1_rect.x = 550
        eagle2_rect.x = 550

    # двигаем мышку
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        mouse_surf = pygame.image.load('mouse2.png').convert()
        mouse_surf.set_colorkey((WHITE))
        mouse_rect.x -= 15
    elif keys[pygame.K_RIGHT]:
        mouse_surf = pygame.image.load('mouse.png').convert()
        mouse_surf.set_colorkey((WHITE))
        mouse_rect.x += 15
    elif keys[pygame.K_UP]:
        if mouse_rect.y > 355:
            mouse_rect.y -= 15
    elif keys[pygame.K_DOWN]:
        mouse_rect.y += 15

    n+=1
    # обновление экрана
    pygame.display.update()