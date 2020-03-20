from IPython.display import clear_output

# Define starting blank board.and current player
board = ['',' ',' ',' ',' ',' ',' ',' ',' ',' ']
current = 1
win = False
answer = "Y"

def reset():
    board = ['',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    current = 1
    win = False

def display_board():
    """
    Display the board given a list of information.
    """
    # Clear current view.
    clear_output()
    print("   |   |   ")
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print("   |   |   ")

def setup():
    """
    Have first player select shape.
    """
    board[0] = input("Player 1: X or O? ")
    display_board()

def move():
    spot = input(f"Player {current}'s Turn: ")
    board[int(spot)] = board[0]
    if board[0] == 'X':
        board[0] = 'O'
    else:
        board[0] = 'X'
    if current == 1:
        current == 2
    else:
        current == 1
    display_board()

def check_win():
    # Check horizontal wins
    if board[7] == board[8] and board[8] == board[9] and board[7] != ' ':
        print(f"{board[7]}'s Win!")
        win = True
    elif board[4] == board[5] and board[5] == board[6] and board[4] != ' ':
        print(f"{board[4]}'s Win!")
        win = True
    elif board[1] == board[2] and board[2] == board[3] and board[1] != ' ':
        print(f"{board[1]}'s Win!")
        win = True
    # Check vertical wins.
    elif board[7] == board[4] and board[4] == board[1] and board[7] != ' ':
        print(f"{board[7]}'s Win!")
        win = True
    elif board[8] == board[5] and board[5] == board[2] and board[8] != ' ':
        print(f"{board[2]}'s Win!")
        win = True
    elif board[9] == board[6] and board[6] == board[3] and board[9] != ' ':
        print(f"{board[9]}'s Win!")
        win = True
    # Check diagonal wins
    elif board[7] == board[5] and board[5] == board[3] and board[7] != ' ':
        print(f"{board[7]}'s Win!")
        win = True
    elif board[9] == board[5] and board[5] == board[1] and board[9] != ' ':
        print(f"{board[9]}'s Win!")
        win = True

# Play the game.
def play():
    setup()
    while(not win):
        move()
        check_win()
    answer = input("Play again? (Y/N): ")

while answer == 'Y':
    play()
