import pygame
import game_field
import consts

state = {
    'up':False,
     'down':False,
     'left':False,
     'right':False,
    'change_game' : False,
    'running' : True,
    'touch_flag' : False,
    'touch_mine' : False,
}


def handle_user_events():
    pygame.init()
    keys = pygame.key.get_pressed()
    x = 0
    y = 0
    if keys[pygame.K_UP]:
        y -= 25
    if keys[pygame.K_DOWN]:
        y += 25
    if keys[pygame.K_RIGHT]:
        x += 25
    if keys[pygame.K_LEFT]:
        x -= 25
    if keys[pygame.K_RETURN]:
        state["change_game"] = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["running"] = False
    return (x,y), state["change_game"], state["running"]



def is_win():
    for i in range(4):
        if i <= 2:
            for j in range(2):
                if (i,j) in game_field.index_mine(game_field.game_board):
                    return True
    return False

def is_false():
    for i in range(4):
        if i > 2:
            for j in range(consts.LEGS_SOLDIER):
                if (i,j) in game_field.index_flag(game_field.game_board):
                    return True
    return False










