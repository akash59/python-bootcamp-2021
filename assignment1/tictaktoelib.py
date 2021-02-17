from IPython.display import clear_output
import random


def display_board(board):
    clear_output()
    print(f'| {board[7]} | {board[8]} | {board[9]} |')
    print('-------------')
    print(f'| {board[4]} | {board[5]} | {board[6]} |')
    print('-------------')
    print(f'| {board[1]} | {board[2]} | {board[3]} |')


def player_input():
    choice_list = ['X', 'O']
    player1_choice = ''
    while player1_choice not in choice_list:
        player1_choice = input('Choose from (X, O): ')
        if player1_choice not in choice_list:
            print('Invalid input, please choose from (X, O): ')
            player1_choice = input('Choose from (X, O): ')
    if player1_choice == 'X':
        player2_choice = 'O'
    else:
        player2_choice = 'X'
    return player1_choice, player2_choice


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    win_pattern = mark * 3
    if board[1] + board[2] + board[3] == win_pattern:
        return True
    elif board[4] + board[5] + board[6] == win_pattern:
        return True
    elif board[7] + board[8] + board[9] == win_pattern:
        return True
    elif board[1] + board[4] + board[7] == win_pattern:
        return True
    elif board[2] + board[5] + board[8] == win_pattern:
        return True
    elif board[3] + board[6] + board[9] == win_pattern:
        return True
    elif board[1] + board[5] + board[9] == win_pattern:
        return True
    elif board[3] + board[5] + board[7] == win_pattern:
        return True
    else:
        return False


def choose_first():
    rand_choice = random.randint(1, 2)
    if rand_choice == 1:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if board[i] != ' ':
            return False
    return True


def player_choice(board):
    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        position = int(input('choose your next position (1-9): '))
    return position


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
