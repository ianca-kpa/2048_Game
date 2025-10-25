#!/usr/bin/python
import numpy as np
import random

"""
function initialize_board():
The goal is to create a 4x4 grid where all spaces are empty (value 0).

function generate_new_tile(board):
The goal is to place a new tile ('2' or '4') in a random empty position (value 0) on the board.

function display_board(board,score):
The goal is to present the 4x4 grid legibly in the console for the player.
"""

def initialize_board():
    board = np.zeros((4,4))

    return board

def generate_new_tile(board):
    empty_cells = []
    
    for row in range(4):
        for column in range(4):
            if board[row][column] == 0:
                empty_cells.append((row,column))
    
    if len(empty_cells) != 0:
        (random_row,random_col) = random.choice(empty_cells)
        random_number = random.randint(0, 9)
        
        if random_number < 9:
            tile_value = 2
        else:
            tile_value = 4
        
        board[random_row][random_col] = tile_value

    return board

def display_board(board,score):
    print("----------------")
    print(f'Current score: {score}')
    print("----------------")
    
    for row in board:
        formatted_row = "|"
        for value in row:
            if value == 0:
                value_to_display = " ".center(4)
            else:
                value_to_display = str(value).center(4) 
            formatted_row += value_to_display + "|"
        
        print(formatted_row)
        print("----------------")

    print("Movement instructions: 'W', 'A', 'S', 'D' or 'Quit'")