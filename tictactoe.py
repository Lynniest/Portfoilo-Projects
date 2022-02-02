# pos_dict = {
#     "a1": "", "a2": "", "a3": "", "b1": "", "b2": "", "b3": "", "c1": "", "c2": "", "c3": ""
# }
# a1, a2, a3, b1, b2, b3, c1, c2, c3 = "", "", "", "", "", "", "", "", ""
player_scores = {1: 0, 2: 0}
CURRENT_PLAYER = 1
WINNING_PLAYER = None


def bring_the_board():
    t_board = '''
            OX: C1    C2     C3
            =====================
            R1:  {} |  {}  |  {}
            ---------------------
            R2:  {} |  {}  |  {}
            ---------------------
            R3:  {} |  {}  |  {}
            '''.format(row1[0], row1[1], row1[2], row2[0], row2[1], row2[2], row3[0], row3[1], row3[2], )
    return t_board


def play_a_turn(user_input):
    global CURRENT_PLAYER, WINNING_PLAYER

    chosen_row_num = int(user_input[0]) - 1
    chosen_col_num = int(user_input[1]) - 1

    if len(user_input) != 2 or user_input.isalnum() is False or \
      rows[chosen_row_num][chosen_col_num] != " " or (-1 > chosen_row_num > 3 or -1 > chosen_col_num > 3):
        user_input = input(f"Invalid position! Please enter a valid one player{CURRENT_PLAYER}: ")
        play_a_turn(user_input)
    else:
        if CURRENT_PLAYER == 1:
            sym = "X"
        else:
            sym = "O"
        rows[chosen_row_num][chosen_col_num] = sym
        WINNING_PLAYER = got_a_winner_or_not(rows, sym)
        if WINNING_PLAYER is None:
            if CURRENT_PLAYER == 1:
                CURRENT_PLAYER += 1
            else:
                CURRENT_PLAYER -= 1


def got_a_winner_or_not(board, symbol):
    global CURRENT_PLAYER

    vict_player = None
    if (board[0][0] == board[1][1] == board[2][2] == symbol) or (board[0][2] == board[1][1] == board[2][0] == symbol):
        vict_player = CURRENT_PLAYER
    else:
        for num in range(3):
            if (board[0][num] == board[1][num] == board[2][num] == symbol) or \
                    (board[num][0] == board[num][1] == board[num][2] == symbol):
                vict_player = CURRENT_PLAYER
                break
    return vict_player


row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
rows = [row1, row2, row3]

print("Welcome players! This is a tic tac toe game. R represents row and C represents column.")
game_over = False
while not game_over:
    print(f"Current Score  -  {player_scores[1]}:{player_scores[2]}")
    for _ in range(9):
        print(bring_the_board())
        player_input = input(f"Its Player{CURRENT_PLAYER} turn! "
                             f"please enter row number first followed by the collum number (eg.11):  ")
        play_a_turn(player_input)
        if WINNING_PLAYER is not None:
            print(bring_the_board())
            player_scores[WINNING_PLAYER] += 1
            break
    if WINNING_PLAYER is None:
        print(bring_the_board())
        print("Draw! No one gets a point.")
    play_again_or_not = input(f"Player{WINNING_PLAYER} wins this round.\n"
                              f" Enter 'again' to play one more match or "
                              f"enter whatever you want to finish the game and see who's the final winner: ")
    if not play_again_or_not == 'again':
        game_over = True
    else:
        CURRENT_PLAYER = 1
        row1 = [" ", " ", " "]
        row2 = [" ", " ", " "]
        row3 = [" ", " ", " "]

print(f"The final result is{player_scores[1]}:{player_scores[2]}.")
if player_scores[1] == player_scores[2]:
    print("Draw! Thanks for playing the game. Psst, No winner's here for now.")
else:
    winner_point = max(player_scores.values())
    for key in player_scores:
        if player_scores[key] == winner_point:
            winner = key
            print(f"Behold the winner of the game! It's player{winner}. \n Thanks for playing the game.")
            break
