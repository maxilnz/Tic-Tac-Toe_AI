# Importing libraries

import functions
import sys

# Defining variables

running = True # for main loop

board = [['.','.','.'],
         ['.','.','.'],
         ['.','.','.']]

cols = ['A','B','C'] # possible cols
rows = [1,2,3] # possible rows

player_1 = 'X'
player_2 = 'O'

k = 1 # running variable for determination of player sign

# Welcome message

print('--- Welcome to Tic-Tac-Toe ---')
print('Enter "exit" to leave the game')

# Main loop

while running:
    col_row_input = input('Enter your coordinates (format A1): ') # user input
    
    try:
        if col_row_input == 'exit' or col_row_input == 'Exit': # exit
            sys.exit()
        
        if len(col_row_input) != 2: # check for valid lenght of user input
            raise ValueError('Invalid input. Please enter a valid amount of columns (1) and a valid amount of rows (1).')
        
        col_input = col_row_input.capitalize()[0] # accessing user input
        row_input = col_row_input[1] # accessing user input
        
        if col_input not in cols  or not row_input.isdigit() or int(row_input) not in rows: # check if entered col and row are in valid area and if row is a number
            raise ValueError('Invalid input. Please enter a valid column (A to C) and row (1 to 3).')
        
        row_idx = int(row_input) - 1 # convert entered row in index
        col_idx = functions.transform_alpha(col_input) # convert entered col in index
            
        if board[row_idx][col_idx] == '.': # check if spot is empty

            k += 1
            player = player_1 if k % 2 == 0 else player_2 # determine player order
    
            board[row_idx][col_idx] = player # place player sign in chosen spot
            
            for row in board: # printing current state of board
                print(" ".join(map(str,row)))
                    
        else:
            print('This field is already occupied. Please choose another one.')
                
    except ValueError as ve:
        print(ve)
        
    functions.determine_win(board, player_1, player_2) # determine winner
    