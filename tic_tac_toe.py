import random

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

def check_winner(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]): return True
        if all([board[j][i] == player for j in range(3)]): return True
    if all([board[i][i] == player for i in range(3)]): return True
    if all([board[i][2 - i] == player for i in range(3)]): return True
    return False

def get_available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def user_move(board):
    while True:
        try:
            move = input("Enter your move (row and column: 0 1): ")
            r, c = map(int, move.split())
            if board[r][c] == " ":
                board[r][c] = "X"
                break
            else:
                print("Cell already taken. Try again.")
        except:
            print("Invalid input. Use format: row column (e.g., 0 2)")

def find_winning_move(board, player):
    for r, c in get_available_moves(board):
        board[r][c] = player
        if check_winner(board, player):
            board[r][c] = " "
            return (r, c)
        board[r][c] = " "
    return None

def computer_move(board):
    # Try to win
    move = find_winning_move(board, "O")
    if move:
        board[move[0]][move[1]] = "O"
        print(f"Computer plays to win at: {move[0]} {move[1]}")
        return

    # Try to block user
    move = find_winning_move(board, "X")
    if move:
        board[move[0]][move[1]] = "O"
        print(f"Computer blocks at: {move[0]} {move[1]}")
        return

    # Pick center, corners, or random
    for pref in [(1,1), (0,0), (0,2), (2,0), (2,2)]:
        if board[pref[0]][pref[1]] == " ":
            board[pref[0]][pref[1]] = "O"
            print(f"Computer plays at: {pref[0]} {pref[1]}")
            return

    move = random.choice(get_available_moves(board))
    board[move[0]][move[1]] = "O"
    print(f"Computer plays randomly at: {move[0]} {move[1]}")

def play_game():
    board = [[" "]*3 for _ in range(3)]
    print_board(board)

    for turn in range(9):
        if turn % 2 == 0:
            user_move(board)
        else:
            computer_move(board)
        print_board(board)

        if check_winner(board, "X"):
            print("🎉 You win!")
            return
        elif check_winner(board, "O"):
            print("🤖 Computer wins!")
            return

    print("😐 It's a draw!")

play_game()
