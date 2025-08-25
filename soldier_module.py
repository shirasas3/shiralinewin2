import consts
import pygame

def key_up(y):
    y -= 25
    return y

def key_down(y):
    y += 25
    return y

def key_right(x):
    x += 25
    return x

def key_left(x):
    x -= 25
    return x

def in_screen(x, y):
    if x > consts.SCREEN_SIZE[0] or x < 0 or y > consts.SCREEN_SIZE[1] or y < 0:
        return False
    else:
        return True


def soldier():
    soldier_img = pygame.image.load(consts.SOLDIER_IMAGE)
    soldier_img = pygame.transform.scale(soldier_img, (50, 100))
    return soldier_img

def night_soldier1():
    soldier_night_img = pygame.image.load(consts.SOLDIER_NIGHT_IMAGE)
    soldier_night_img = pygame.transform.scale(soldier_night_img, (50, 100))
    return soldier_night_img