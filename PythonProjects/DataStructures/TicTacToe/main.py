"""
TicTacToe Game - A 2-Player Game
"""


def instruction_details():
    """
    Function to Print Instructions to the user to play the game.
    """
    print('Introduction:')
    print('This is a 2-Player Game. A Player has to pick either X or O as their symbol.')
    print('Once the symbol is selected then the game begins.')
    print('Use the Number pad of the keyboard to let the game know which position you are choosing.')
    print('Below is the reference layout guide for your reference.')
    print('7|8|9')
    print('4|5|6')
    print('1|2|3')


def capture_user_symbol(p1_symbol, p2_symbol):
    """
    This method captures Player-1 Symbol and defaults the other symbol to Player-2
    """
    while p1_symbol not in ['X', 'O']:
        p1_symbol = input('Pick Player-1 Symbol either X or O:')
        if p1_symbol not in ['X', 'O']:
            print('Sorry wrong Input provided!')
        else:
            if p1_symbol == 'X':
                p2_symbol = 'O'
            else:
                p2_symbol = 'X'

    return p1_symbol, p2_symbol


def print_game_pos():
    """
    This method diplays the game state
    """
    print(game_arr[6] + '|' + game_arr[7] + '|' + game_arr[8])
    print('-' + '-' + '-' + '-' + '-')
    print(game_arr[3] + '|' + game_arr[4] + '|' + game_arr[5])
    print('-' + '-' + '-' + '-' + '-')
    print(game_arr[0] + '|' + game_arr[1] + '|' + game_arr[2])


def validating_input_data(pp_moves, player,p_symbol):
    """
    This method Validates Player Data input and marks the position accordingly
    """
    p_move_data = '-1'
    while p_move_data not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        p_move_data = input(f'{player}: Enter your position from (1-9) for {p_symbol}:')
        if p_move_data not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print('Sorry the input not valid. Please try again')
        else:
            if int(p_move_data) in pp_moves:
                p_move_data = '-1'
                print('Sorry this position is already taken!')
            else:
                return p_move_data


def game_closure_check():
    """
    This method checks if any player has won the game
    :return:
    6 7 8
    3 4 5
    0 1 2
    """
    # Criss Cross Line Join Matching
    if (game_arr[0] == game_arr[4] == game_arr[8] and game_arr[4] != ' ') \
            or (game_arr[2] == game_arr[4] == game_arr[6] and game_arr[4] != ' '):
        if game_arr[4] == player_1_symbol:
            print('Tic Tac Toe - Player-1 Won')
        else:
            print('Tic Tac Toe - Player-2 Won')
        return 1
    # Horizontal Line Join Matching
    j = 0
    for i in range(0, 3):
        if game_arr[i + j] == game_arr[i + j + 1] == game_arr[i + j + 2] and game_arr[i + j] != ' ':
            if game_arr[4] == player_1_symbol:
                print('Tic Tac Toe - Player-1 Won')
            else:
                print('Tic Tac Toe - Player-2 Won')
            return 1
        j += 2
    # Vertical Line Join Matching
    for i in range(0, 3):
        if game_arr[i] == game_arr[i + 3] == game_arr[i + 6] and game_arr[i] != ' ':
            if game_arr[4] == player_1_symbol:
                print('Tic Tac Toe - Player-1 Won')
            else:
                print('Tic Tac Toe - Player-2 Won')
            return 1
    return 0


def game_logic():
    """
    This method Holds Actual Logic of TicTacToe
    """
    p1_move = []
    p2_move = []
    quit_game = False
    while not quit_game:
        quit_game_flag = 'X'
        result = int(validating_input_data(p1_move+p2_move, 'Player-1', player_1_symbol))
        if result != -1:
            p1_move.append(result)
            game_arr[result-1] = player_1_symbol
            print_game_pos()
            res = game_closure_check()
            if res == 1:
                break
        if len(p1_move+p2_move) == 9:
            res = game_closure_check()
            if res == 0:
                print('There is a TIE in the game.')
                break
        result = int(validating_input_data(p1_move + p2_move, 'Player-2', player_2_symbol))
        if result != -1:
            p2_move.append(result)
            game_arr[(result - 1)] = player_2_symbol
            print_game_pos()
            res = game_closure_check()
            if res == 1:
                break
        while quit_game_flag not in ['Y', 'N']:
            quit_game_flag = input('Please Enter Y to quit the game and N to Continue.')
            if quit_game_flag not in ['Y', 'N']:
                print('Sorry Wrong Input Provided!')
            else:
                if quit_game_flag == 'Y':
                    quit_game = True


instruction_details()
game_arr = list(' '*9)
player_1_symbol, player_2_symbol = capture_user_symbol('M', 'N')
print('Selected Symbol for Player-1 - ' + player_1_symbol)
print('Defaulted Symbol for Player-2 - ' + player_2_symbol)
game_logic()
