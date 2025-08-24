import pygame
import screen
import consts

state = {
    'up':False,
     'down':False,
     'left':False,
     'right':False,
    'change_game' : False,
    'running' : True
    'touch_flag' : False
    'touch_mine' : False
}


def handle_user_events(player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["running"] = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                state["up"] = True
            elif event.key == pygame.K_DOWN:
                state["down"] = True
            elif event.key == pygame.K_LEFT:
                state["left"] = True
            elif event.key == pygame.K_RIGHT:
                state["right"] = True
            elif event.key == pygame.K_RETURN:
                state["change_game"] = True
    # if state['up']:
    #     player.pos[1] -= 1
    # if state['down']:
    #     player.pos[1] += 1
    # if state['left']:
    #     player.pos[0] -= 1
    # if state['right']:
    #     player.pos[0] += 1



def is_win(player,flag):
    for i in range(len(player)):
        if i <= 2:
            for j in range(2):
                if player[i][j] == flag[i][j]:
                    return True
    return False

def is_false(player,mine):
    for i in range(len(player)):
        if i > 2:
            for j in range(consts.LEGS_SOLDIER):
                if player[i][j] == mine[i][j]:
                    return True
    return False










