import consts
import random

board_game = []

def build_board():
    counter_20 = 0
    for i in range(consts.GAME_COLS):
        counter = 0
        row = []
        for j in range(consts.GAME_ROWS):
            if counter >= 1 or counter_20 >= 20:
                row.append(0)
            else:
                row.append("mine")
                counter += 1
                counter_20 += 1
        board_game.append(row)
        random.shuffle(board_game[i])
        for h in range(len(row)):
            if row[h] == "mine":
                if h < 24 and h > 0:
                    row[h + 1] = 1
                    row[h - 1] = 1
                elif h == 24:
                    row[h - 1] = 1
                    row[h - 2] = 1
                else:
                    row[h + 1] = 1
                    row[h + 2] = 1
    random.shuffle(board_game)
    for i in range(consts.GAME_COLS):
        for j in range(consts.GAME_ROWS):
            if board_game[i][j] == 1:
                board_game[i][j] = "mine"
    (21, 46)(21, 47)(21, 48)(21, 49)
    (22, 46)(22, 47)(22, 48)(22, 49)
    (23, 46)(23, 47)(23, 48)(23, 49)
    for i in board_game:

        for j in i:
            print(j, end=" ")
        print("\r")

    return board_game


build_board()
