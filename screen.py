import pygame
import consts

def build_screen():
    pygame.font.init()
    screen = pygame.display.set_mode(consts.SCREEN_SIZE)
    pygame.display.set_caption(consts.WINDOW_TITLE)
    screen.fill(consts.BACKGROUND_COLOR)
    return screen

def flag():
    flag_img = pygame.image.load(consts.FLAG_IMAGE)
    flag_img = pygame.transform.scale(flag_img, (75, 100))
    return flag_img

def soldier():
    soldier_img = pygame.image.load(consts.SOLDIER_IMAGE)
    soldier_img = pygame.transform.scale(soldier_img, (50, 100))
    return soldier_img

def text():
    font = pygame.font.SysFont(consts.FONT, 20)
    text1 = font.render(consts.WELCOME, True, (consts.WHITE))
    text2 = font.render(consts.HAVE_FUN, True, consts.WHITE)
    return text1, text2

def normal_screen():
    screen = build_screen()
    text1, text2 = text()

    text_rect1 = text1.get_rect()
    text_rect2 = text2.get_rect()
    text_rect1.center = (140, 10)
    text_rect2.center = (85, 25)
    pygame.display.flip()
    running = True
    while running:
        screen.blit(text1, text_rect1)
        screen.blit(text2, text_rect2)
        screen.blit(soldier(), (0, 0))
        screen.blit(flag(), (1175, 525))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            pygame.display.update()

normal_screen()