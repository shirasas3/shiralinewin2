import time

import pygame
import game_field
import soldier
import screen


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

def main():
    pygame.init()
    screen.normal_screen()
    while state['running']:
        handle_user_events()






def handle_user_events():
    pygame.init()
    keys = pygame.key.get_pressed()
    x = 0
    y = 0
    if keys[pygame.K_UP]:
        soldier.key_up(y)
        state["up"] = True
    if keys[pygame.K_DOWN]:
        soldier.key_down(y)
        state["down"] = True
    if keys[pygame.K_RIGHT]:
        soldier.key_right(x)
        state["right"] = True
    if keys[pygame.K_LEFT]:
        soldier.key_left(x)
        state["left"] = True
    if keys[pygame.K_RETURN]:
        screen.night_screen()
        time.sleep(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["running"] = False
    return

def move_soldier(board):
    handle_user_events()
    if state["up"] == True:
        for i in range(len(board)):
            for j in range(len(board(i))):
                if board[i][j] == "soldier":
                    board[i][j] = 0
                    board[i + 1][j] = "soldier"
    if state['down'] == True:
        for i in range(len(board)):
            for j in range(len(board(i))):
                if board[i][j] == "soldier":
                    board[i][j] = 0
                    board[i - 1][j] = "soldier"
    if state['left'] == True:
        for i in range(len(board)):
            for j in range(len(board(i))):
                if board[i][j] == "soldier":
                    board[i][j] = 0
                    board[i][j - 1] = "soldier"
    if state['down'] == True:
        for i in range(len(board)):
            for j in range(len(board(i))):
                if board[i][j] == "soldier":
                    board[i][j] = 0
                    board[i][j + 1] = "soldier"
    return board





move_soldier(game_field.game_board)


def is_win(index_):
    return index_ in game_field.index_flag(game_field.game_board)



def is_lose(index_):
    return index_ in game_field.index_mine(game_field.game_board)










