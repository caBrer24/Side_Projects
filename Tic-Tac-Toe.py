table = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

winner = None

game_on = True


current_player = "X"  # which player's turn?


# When in game
def play_game():
    show_table()


    while game_on:  # Until game ends

        passTurn(current_player)

        # Checks if game has ended
        gameOver_o_que()

        # Flip to the other player
        change_x0()

    # When game is over
    if winner == "X" or winner == "O":
        print(winner + " winner.")
    elif winner == None:
        print("Draw")


def show_table():
    print("\n")
    print(table[0] + " | " + table[1] + " | " + table[2] + "     1 | 2 | 3")
    print(table[3] + " | " + table[4] + " | " + table[5] + "     4 | 5 | 6")
    print(table[6] + " | " + table[7] + " | " + table[8] + "     7 | 8 | 9")
    print("\n")


def passTurn(player):

    print(player + "'s turn")
    position = input("Make your move (1-9): ")

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Press a number 1-9: ")

        position = int(position) - 1

        if table[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")

    table[position] = player

    show_table()


def gameOver_o_que():
    look_for_winner()
    check_for_tie()


def look_for_winner():

    global winner

    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonal()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_rows():

    global game_on

    st_row = table[0] == table[1] == table[2] != "-"
    nd_row = table[3] == table[4] == table[5] != "-"
    rd_row = table[6] == table[7] == table[8] != "-"

    if st_row or nd_row or rd_row:
        game_on = False

    if st_row:
        return table[0]
    elif nd_row:
        return table[3]
    elif rd_row:
        return table[6]

    else:
        return None


def check_columns():

    global game_on

    st_column = table[0] == table[3] == table[6] != "-"
    nd_column = table[1] == table[4] == table[7] != "-"
    rd_column = table[2] == table[5] == table[8] != "-"

    if st_column or nd_column or rd_column:
        game_on = False

    if st_column:
        return table[0]
    elif nd_column:
        return table[1]
    elif rd_column:
        return table[2]

    else:
        return None


def check_diagonal():

    global game_on

    st_diagonal = table[0] == table[4] == table[8] != "-"
    nd_diagonal = table[2] == table[4] == table[6] != "-"

    if st_diagonal or nd_diagonal:
        game_on = False

    if st_diagonal:
        return table[0]
    elif nd_diagonal:
        return table[2]

    else:
        return None


def check_for_tie():

    global game_on

    if "-" not in table:
        game_on = False
        return True

    else:
        return False


def change_x0():

    global current_player

    if current_player == "X":
        current_player = "O"

    else:
        current_player = "X"


play_game()


