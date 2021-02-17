from tictaktoelib import *

print('Welcome to Tic Tac Toe!')

while True:

    # Set the game up here
    test_board = [' '] * 10

    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to play? y or n: ')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        # Player 1 Turn
        if 'Player 1' == turn:

            print('Player 1 is playing its turn')
            display_board(test_board)

            # choose a position
            position = player_choice(test_board)

            # place a marker on the position
            place_marker(test_board, player1_marker, position)

            # check if they won
            if win_check(test_board, player1_marker):
                display_board(test_board)
                print('Player 1 has won')
                game_on = False
                break

            # or check if there is a tie
            else:
                if full_board_check(test_board):
                    display_board(test_board)
                    print("Tie Game !!")
                    game_on = False
                    break
                # No tie or no win? then player's turn
                else:
                    turn = 'Player 2'

        # Player2's turn.
        else:
            print('Player 2 is playing its turn')
            display_board(test_board)

            # choose a position
            position = player_choice(test_board)

            # place a marker on the position
            place_marker(test_board, player2_marker, position)

            # check if they won
            if win_check(test_board, player2_marker):
                display_board(test_board)
                print('Player 2 has won')
                game_on = False
                break

            # or check if there is a tie
            else:
                if full_board_check(test_board):
                    display_board(test_board)
                    print("Tie Game !!")
                    game_on = False
                    break
                # No tie or no win? then player's turn
                else:
                    turn = 'Player 1'

    if not replay():
        break
