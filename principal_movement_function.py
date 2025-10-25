import copy
import basic_movement as b_m
import board as bd

def move_board(board,direction,current_score):
    initial_board = copy.deepcopy(board)
    board_modified = False
    
    prepared_board = copy.deepcopy(board)
    score = current_score
    
    if direction == "w" or direction == "W":
        prepared_board = b_m.transpose_board(prepared_board)
    elif direction == "s" or direction == "S":
        prepared_board = b_m.transpose_board(prepared_board)
        prepared_board = b_m.invert_rows(prepared_board)
    elif direction == "d" or direction == "D":
        prepared_board = b_m.invert_rows(prepared_board)
    elif direction == "a" or direction == "A":
        prepared_board = prepared_board
    else:
        return
    
    for i in range(4):
        current_line = prepared_board[i]
        (new_line, new_score, line_changed) = b_m.process_line(current_line, score)
        
        prepared_board[i] = new_line
        score = new_score
        
        if line_changed == True:
            board_modified = True
    
    final_board = prepared_board
    
    if direction == "d" or direction == "D":
        final_board = b_m.invert_rows(final_board)
    elif direction == "s" or direction == "S":
        final_board = b_m.invert_rows(final_board)
        final_board = b_m.transpose_board(final_board)
    elif direction == "w" or direction == "W":
        final_board = b_m.transpose_board(final_board)
    
    if board_modified == True:
        final_board = bd.generate_new_tile(final_board)
    
    return final_board, score, board_modified