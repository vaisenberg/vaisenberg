
board = [[' ', ' ', ' '], 
         [' ', ' ', ' '],  
         [' ', ' ', ' ']] 
 
winning_combinations = [
    [[1, 1], [1, 2], [1, 3]],  
    [[2, 1], [2, 2], [2, 3]],  
    [[3, 1], [3, 2], [3, 3]],  
    [[1, 1], [2, 1], [3, 1]],  
    [[1, 2], [2, 2], [3, 2]],  
    [[1, 3], [2, 3], [3, 3]],  
    [[1, 1], [2, 2], [3, 3]],  
    [[1, 3], [2, 2], [3, 1]],  
]

def display_board(board):
    print('Welcome to TIC TAC TOE')
    print('*'*11)
    for row in board:
        print(f" {row[0]} | {row[1]} |  {row[2]}")
        print("-"*11) 
    print("\n")

display_board(board)

def player_input(player):
    while True:
        row_input = input(f"Player {player}, enter your move row (1-3): ")
        col_input = input(f"Player {player}, enter your move column (1-3): ")
        
        if row_input and col_input: 
           
            if len(row_input) == 1 and row_input in "123" and len(col_input) == 1 and col_input in "123":
                row = int(row_input) - 1  
                col = int(col_input) - 1  
                if 0 <= row <= 2 and 0 <= col <= 2:
                    if board[row][col] == ' ':
                        board[row][col] = player
                        break  
                    else:
                        print("That position is already taken! Choose another one.")
                else:
                    print("Invalid input! Row and column must be between 1 and 3.")
            else:
                print("Invalid input! Please enter numbers between 1 and 3.")
        else:
            print("Invalid input! Please enter valid row and column numbers.")

def check_win(board, player):
    for combination in winning_combinations:
        if all(board[row-1][col-1] == player for row, col in combination):
            return True
    return False

def play():
    display_board(board)  
    current_player = 'X'  
    
    for turn in range(9):  
        player_input(current_player)  
        display_board(board) 
        if check_win(board, current_player):
            print(f"Player {current_player} wins!")
            break  
        current_player = 'O' if current_player == 'X' else 'X'
    else:
        print("It's a tie! No more moves left.")
play()