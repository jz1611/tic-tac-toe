# Globally define game board variable and player turn
game_board = [' ']*10

def print_board(board):
    '''
    Display a tic tac toe board given a passed in list.
    '''

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

def setup_game(board):
    '''
    Have players choose pieces and determine first player.
    '''

    piece = input("Player 1: X or O? ")
    if piece == 'X':
        board[0] = {"player1": piece, "player2": 'O'}
    else:
        board[0] = {"player1": piece, "player2": 'X'}

    if random.randint(0,1) == 0:
        print('Player 1 goes first!')
        return 0
    else:
        print('Player 2 goes first!')
        return 1

def turn(board):
    
