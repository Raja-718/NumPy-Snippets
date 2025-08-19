import numpy as np

board = np.full((3, 3), ' ')
players = ['X', 'O']
turn = 0

def print_board(b):
    print("\nCurrent Board:")
    for row in b:
        print(" | ".join(row))
        print("-" * 9)

while True:
    print_board(board)
    player = players[turn % 2]
    print(f"Player {player}'s turn")
    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))
    
    if board[row, col] == ' ':
        board[row, col] = player
        turn += 1
    else:
        print("Cell already taken! Try again.")

    # Win check (basic, horizontal only for simplicity)
    for i in range(3):
        if np.all(board[i] == player) or np.all(board[:, i] == player):
            print_board(board)
            print(f"🎉 Player {player} wins!")
            exit()
    if turn == 9:
        print_board(board)
        print("Draw!")
        break
