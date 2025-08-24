import consts
import random
import numpy as np

board_game = []

for i in range(consts.GAME_ROWS):
    row = []
    for j in range(consts.GAME_COLS):
        row.append(0)
    board_game.append(row)

print(board_game)


mine = [1,"mine"] #להוסיף את התמונה

for i in range(len(board_game)):
    for j in range(len(board_game[i])):
        board_game.insert(j,random.choice(mine))
print(board_game)

