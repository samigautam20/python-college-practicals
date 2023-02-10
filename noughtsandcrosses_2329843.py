#importing necessary modules
import random
import os.path
import json
random.seed()

#defining a function draw_board
def draw_board(board):
    # code to draw the board
    print("--" * 9)
    for row in board:
        print(f"| {' | '.join(row)} |")
        print("--" * 9)


def welcome(board):
    # printing the welcome message
    # displaying the board by calling draw_board(board)
    print("Welcome to Noughts and Crosses!")
    draw_board(board)


def initialise_board(board):
    # developing code to set all elements of the board to one space ' '
    for row in range(len(board)):
        for col in range(len(board[row])):
            board[row][col] = ' '
    return board


def get_player_move(board):
    # developing code to ask the user for the cell to put the X in,
    # and return row and col
    while True:
        move = input("Choose a cell to make your move (1-9): ")
        row, col = (int(move[0]) - 1)//3, (int(move[0]) - 1)%3

        if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
            board[row][col] = 'X'
            return row, col
        else:
            print("Invalid cell! Please try again.")


def choose_computer_move(board):
    # developing code to let the computer chose a cell to put a nought in
    # and returns row and col
    while True:
        row, col = random.randint(0, 2), random.randint(0, 2)
        if board[row][col] == ' ':
            board[row][col] = 'O'
            return row, col


def check_for_win(board, mark):
    # developing code to check if either the player or the computer has won
    # returns True if someone won, False otherwise
    # checking for rows
    for row in board:
        if all(cell == mark for cell in row):
            return True
    # check columns
    for col in range(3):
        if all(board[row][col] == mark for row in range(3)):
            return True
    # check diagonals
    if all(board[i][i] == mark for i in range(3)):
        return True
    if all(board[i][2-i] == mark for i in range(3)):
        return True
    return False


def check_for_draw(board):
    # develop cope to check if all cells are occupied
    # return True if it is, False otherwise
    for row in board:
        if any(cell == ' ' for cell in row):
            return False
    return True


def play_game(board):
    # develop code to play the game
    # star with a call to the initialise_board(board) function to set
    # the board cells to all single spaces ' '
    # then draw the board
    initialise_board(board)
    draw_board(board)
    # then in a loop, get the player move, update and draw the board
    # check if the player has won by calling check_for_win(board, mark),
    # if so, return 1 for the score
    while True:
        row, col = get_player_move(board)
        draw_board(board)
        if check_for_win(board, 'X'):
            print("You won!")
            return 1
        # if not check for a draw by calling check_for_draw(board)
        elif check_for_draw(board):
            print("The game is a draw.")
            return 0
        # if not, then call choose_computer_move(board)
        # to choose a move for the computer
        row, col = choose_computer_move(board)
        draw_board(board)
        # update and draw the board
        # check if the computer has won by calling check_for_win(board, mark),
        if check_for_win(board, 'O'):
            print("Computer won!")
            return -1
        # if not check for a draw by calling check_for_draw(board)
        elif check_for_draw(board):
            print("The game is a draw.")
            return 0
        # repeat the loop
    return 0


def menu():
    # get user input of either '1', '2', '3' or 'q'
    # 1 - Play the game
    # 2 - Save score in file 'leaderboard.txt'
    # 3 - Load and display the scores from the 'leaderboard.txt'
    # q - End the program
    while True:
        choice = input("1. Play the game\n2. Save score in file\n3. Load and display scores from file\nq. Quit\nMake your choice: ")
        if choice in ['1', '2', '3', 'q']:
            return choice


def load_scores():
    # develop code to load the leaderboard scores
    # from the file 'leaderboard.txt'
    # return the scores in a Python dictionary
    # with the player names as key and the scores as values
    # return the dictionary in leaders
    if os.path.isfile('leaderboard.txt'):
        with open('leaderboard.txt', 'r') as f:
            leaders = json.load(f)
        return leaders
    else:
        return {}


def save_score(score):
    # develop code to ask the player for their name
    # and then save the current score to the file 'leaderboard.txt'
    name = input("Enter your name: ")
    leaders = load_scores()
    leaders[name] = score
    with open('leaderboard.txt', 'w') as f:
        json.dump(leaders, f)


def display_leaderboard(leaders):
    # develop code to display the leaderboard scores
    # passed in the Python dictionary parameter leader
    sorted_leaders = sorted(leaders.items(), key=lambda x: x[1], reverse=True)
    print("High Scores:")
    for name, score in sorted_leaders:
        print(f"{name}: {score}")
