# Tic Tac Toe Game in Python
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]): return True
        if all([board[j][i] == player for j in range(3)]): return True
    if all([board[i][i] == player for i in range(3)]): return True
    if all([board[i][2 - i] == player for i in range(3)]): return True
    return False

def is_draw(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def get_move(player, board):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid move. Choose between 1 and 9.")
                continue
            row, col = (move - 1) // 3, (move - 1) % 3
            if board[row][col] in ['X', 'O']:
                print("Cell already taken. Try again.")
                continue
            return row, col
        except ValueError:
            print("Please enter a number between 1 and 9.")

def play_game():
    board = [['1','2','3'], ['4','5','6'], ['7','8','9']]
    current_player = 'X'
    print_board(board)

    while True:
        row, col = get_move(current_player, board)
        board[row][col] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

def main():
    while True:
        play_game()
        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
