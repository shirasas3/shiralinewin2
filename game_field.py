import consts
import random
import numpy as np

board_game = []

def build_board():
    counter_20 = 0
    for i in range(consts.GAME_COLS):
        counter = 0
        row = []
        for j in range(consts.GAME_ROWS):
            if counter >= 1:
                row.append(0)
            else:
                row.append("mine")
                counter += 1
                counter_20 += 1

        board_game.append(row)
        random.shuffle(board_game[i])
    for i in board_game:
        for j in i:
            print(j, end=" ")
        print("\r")


    return board_game






# def mine_img():
#     soldier_img = pygame.image.load(consts.MINE_IMAGE)
#     soldier_img = pygame.transform.scale(soldier_img, (75, 25))
#     return soldier_img
#
# screen.blit(soldier(), (0, 0))
    # print(board_game)

build_board()
# random_mines()