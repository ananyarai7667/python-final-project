# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    winner = None

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        row, col = map(int, input(f"Player {current_player}, enter your move (row and column): ").split())
        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("That position is already taken. Try again.")
            continue

        print_board(board)

        if check_winner(board, current_player):
            winner = current_player
            break

        if is_board_full(board):
            break

        current_player = "O" if current_player == "X" else "X"

    if winner:
        print(f"Player {winner} wins! Congratulations!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()
