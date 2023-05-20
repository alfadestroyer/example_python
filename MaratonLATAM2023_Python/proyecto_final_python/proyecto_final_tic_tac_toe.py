# Proyecto Final del curso de Python
#  Juego Tic-Tac-Toe
print()
print("Juego de Tic-Tac-Toe.")
print()

from random import randrange

def display_board(board):
    print("+-------" * 3,"+",sep="")
    for row in range(3):
        print("|       " * 3,"|",sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3,"|",sep="")
        print("+-------" * 3,"+",sep="")
def make_list_of_free_fields(board):
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['X', 'O']:
                free_fields.append((row, col))
    return free_fields

def victory_for(board, sign):
    if (board[0][0] == sign and board[0][1] == sign and board[0][2] == sign) or \
       (board[1][0] == sign and board[1][1] == sign and board[1][2] == sign) or \
       (board[2][0] == sign and board[2][1] == sign and board[2][2] == sign) or \
       (board[0][0] == sign and board[1][0] == sign and board[2][0] == sign) or \
       (board[0][1] == sign and board[1][1] == sign and board[2][1] == sign) or \
       (board[0][2] == sign and board[1][2] == sign and board[2][2] == sign) or \
       (board[0][0] == sign and board[1][1] == sign and board[2][2] == sign) or \
       (board[0][2] == sign and board[1][1] == sign and board[2][0] == sign):
        return True
    return False

def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    if len(free_fields) > 0:
        move = randrange(len(free_fields))
        row, col = free_fields[move]
        update_board((row * 3) + col + 1, board, 'X')

def update_board(move, board, player):
    row = (move - 1) // 3
    col = (move - 1) % 3
    board[row][col] = player

def is_free(move, board):
    row = (move - 1) // 3
    col = (move - 1) % 3
    return board[row][col] not in ['X', 'O']       
def play_game():
    # Initialize the game
    board = [[col + (row * 3) + 1 for col in range(3)] for row in range(3)]
    update_board(5, board, 'X')
    
    # Play the game
    while True:
        display_board(board)
        valid_move = enter_move(board)
        if valid_move:
            if victory_for(board, 'O'):
                display_board(board)
                print("♪♪♪♫♫♫ Ganaste! ♫♫♫♪♪♪")
                break
            draw_move(board)
            if victory_for(board, 'X'):
                display_board(board)
                print("☺☺☺☺☺☺ Perdiste! ☺☺☺☺☺☺")
                break
        if len(make_list_of_free_fields(board)) == 0:
            display_board(board)
            print(""±±±±±± Es un empate! ±±±±±±")
            break

def enter_move(board):
    move = int(input("Ingresa tu movimiento: "))
    while not (move > 0 and move < 10) or not is_free(move, board):
        move = int(input("Movimiento inválido. Ingresa tu movimiento: "))
    if is_free(move, board):
        update_board(move, board, 'O')
        return True
    return False

play_game()
