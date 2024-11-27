import math

# Initialize the board as a 3x3 list
board = [["" for _ in range(3)] for _ in range(3)]

# Display the board
def print_board():
    for row in board:
        print(" | ".join([cell if cell else " " for cell in row]))
        print("-" * 9)

# Check if a player has won or if it's a draw
def check_winner():
    # Rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return board[0][2]
    # Check for draw
    if all(cell for row in board for cell in row):
        return "Draw"
    return None

# Get available moves
def available_moves():
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ""]

# Minimax algorithm with Alpha-Beta Pruning
def minimax(depth, is_maximizing, alpha, beta):
    winner = check_winner()
    if winner == "O":  # AI wins
        return 10 - depth
    elif winner == "X":  # Human wins
        return depth - 10
    elif winner == "Draw":
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in available_moves():
            i, j = move
            board[i][j] = "O"
            score = minimax(depth + 1, False, alpha, beta)
            board[i][j] = ""
            best_score = max(best_score, score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = math.inf
        for move in available_moves():
            i, j = move
            board[i][j] = "X"
            score = minimax(depth + 1, True, alpha, beta)
            board[i][j] = ""
            best_score = min(best_score, score)
            beta = min(beta, score)
            if beta <= alpha:
                break
        return best_score

# AI's best move
def best_move():
    best_score = -math.inf
    move = None
    for i, j in available_moves():
        board[i][j] = "O"
        score = minimax(0, False, -math.inf, math.inf)
        board[i][j] = ""
        if score > best_score:
            best_score = score
            move = (i, j)
    return move

# Play the game
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()
    while True:
        # Human move
        human_move = input("Enter your move (row and column, e.g., 1 2): ")
        i, j = map(int, human_move.split())
        if board[i][j] != "":
            print("Invalid move! Try again.")
            continue
        board[i][j] = "X"
        print_board()
        if check_winner():
            break

        # AI move
        ai_move = best_move()
        if ai_move:
            board[ai_move[0]][ai_move[1]] = "O"
            print("\nAI's Move:")
            print_board()
        if check_winner():
            break

    # Announce result
    result = check_winner()
    if result == "Draw":
        print("It's a draw!")
    else:
        print(f"{result} wins!")

play_game()
