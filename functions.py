# Importing libraies

import sys

# Convert from character to index

def transform_alpha(alpha):
    numeric = ord(alpha) - ord('A') # using ascii order of A as starting point
    return numeric

# Determine winner

def determine_win(board, player_1, player_2):
    # Setting  defaults

    winner = '' 

    # Searching in rows for possible winner

    for row in board: 
        if len(set(row)) == 1 and row != ['.', '.', '.']: # checking if all spots in a row are filled with the same player sign
            winner = row[0]
            print(f"Player {'1' if winner == player_1 else '2'} wins")
            sys.exit()

    # Searching in cols for possible winner

    for col in range(3):

        if all(board[row][col] == player_1 for row in range(3)): # checking if all spots of a col (same index of a row) are filled with the same player sign
            winner = player_1
            print('Player 1 wins')
            sys.exit()
        elif all(board[row][col] == player_2 for row in range(3)):
            winner = player_2
            print('Player 2 wins')
            sys.exit()

    # Searching in diagonals for possible winner

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '.':
         winner = board[0][0]
         print(f"Player {'1' if winner == player_1 else '2'} wins")
         sys.exit()

    elif board[2][0] == board[1][1] == board[0][2] and board[2][0] != '.':
         winner = board[2][0]
         print(f"Player {'1' if winner == player_1 else '2'} wins")
         sys.exit()

    # Searching in rows for possible draw

    if all('.' not in row for row in board): # checking if all spots in a row are filled with a player sign
        print('Draw')
        sys.exit()
