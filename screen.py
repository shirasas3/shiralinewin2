import sys
import pygame
import consts
import random
import game_field
from game_field import build_board

build_board()

def build_screen():
    pygame.font.init()
    screen = pygame.display.set_mode(consts.SCREEN_SIZE)
    pygame.display.set_caption(consts.WINDOW_TITLE)
    screen.fill(consts.BACKGROUND_COLOR)
    return screen

def grass():
    grass_img = pygame.image.load(consts.GRASS_IMAGE)
    grass_img = pygame.transform.scale(grass_img, (50, 50))
    return grass_img

def flag():
    flag_img = pygame.image.load(consts.FLAG_IMAGE)
    flag_img = pygame.transform.scale(flag_img, (75, 100))
    return flag_img

def soldier():
    soldier_img = pygame.image.load(consts.SOLDIER_IMAGE)
    soldier_img = pygame.transform.scale(soldier_img, (50, 100))
    return soldier_img

def night_solider():
    night_soldier_img = pygame.image.load(consts.SOLDIER_NIGTH_IMAGE)
    night_soldier_img = pygame.transform.scale(night_soldier_img, (50, 100))
    return night_soldier_img

def text():
    font = pygame.font.SysFont(consts.FONT, 20)
    text1 = font.render(consts.WELCOME, True, (consts.WHITE))
    text2 = font.render(consts.HAVE_FUN, True, consts.WHITE)
    return text1, text2

def mine_matrix():


def draw_grid():
    block_size = 25
    for x in range(0, consts.SCREEN_SIZE[0], block_size):
        for y in range(0, consts.SCREEN_SIZE[1], block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(screen, consts.GREEN, rect, 1)

def normal_screen():
    screen = build_screen()
    text1, text2 = text()
    text_rect1 = text1.get_rect()
    text_rect2 = text2.get_rect()
    text_rect1.center = (140, 10)
    text_rect2.center = (85, 25)
    pygame.display.flip()
    running = True
    for i in range(20):
        cord1 = random.randint(0, 1200)
        cord2 = random.randint(0, 570)
        screen.blit(grass(), (cord1, cord2))

    while running:
        screen.blit(text1, text_rect1)
        screen.blit(text2, text_rect2)
        screen.blit(soldier(), (0, 0))
        screen.blit(flag(), (1175, 525))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            pygame.display.update()

def night_screen():
    global screen, clock
    running = True
    pygame.init()
    screen = pygame.display.set_mode(consts.SCREEN_SIZE)
    clock = pygame.time.Clock()
    screen.fill(consts.BACKGROUND_NIGHT_COLOR)

    while running:
        draw_grid()
        screen.blit(night_solider(), (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            pygame.display.update()

# normal_screen()
night_screen()