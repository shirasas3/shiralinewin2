from numpy.ma.core import append
import pygame
import consts
import random
import main

board_game = []

def build_board():
    global board_game
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
            if i >= consts.GAME_COLS - consts.IMAGE_FLAG_HEIGHT:
                if j >= consts.GAME_ROWS - consts.IMAGE_FLAG_WIDTH:
                    board_game[i][j] = "flag"
            elif i < consts.IMAGE_SOLDIER_HEIGHT:
                 if j < consts.IMAGE_SOLDIER_WIDTH:
                    board_game[i][j] = "soldier"
    for i in board_game:
        for j in i:
            print(j, end=" ")
        print("\r")

    return board_game


game_board = build_board()


def index_flag(board):
    list_index_flag = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == "flag":
                index_row = board.index(board[row])
                index_col = board.index(board[col])
                list_index_flag.append((index_row,index_col))
    return list_index_flag

def index_mine(board):
    list_index_mine = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == "mine":
                index_row = board.index(board[row])
                index_col = board.index(board[col])
                list_index_mine.append((index_row, index_col))
    return list_index_mine
