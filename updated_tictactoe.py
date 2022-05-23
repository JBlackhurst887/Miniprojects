import sys


def format_user(element):
    """
    Return a string representation of a board position that can be logged to console.
    """
    if element is None:
        return '_'
    elif element:
        return 'x'
    else:
        return 'o'


def print_board(board):
    """
    Print the board to console.
    """
    for row in board:
        for position in row:
            print(f"{format_user(position)} ", end="")
        print()


def get_user_move():
    """
    Get the users move as an input from the console.  This method valids that the number
    is between 1 - 9 or "q" (for quiting the game).
    """
    user_input = input("Please enter a position 1 through 9 or enter \"q\" to quit: ")

    # Simply quit the program.
    if user_input == 'q':
        sys.exit()

    # Validate the number is in range 1 - 9.
    if user_input in [str(i) for i in range(1, 10)]:
        return int(user_input) - 1
    else:
        # Recurrive call this function to get the user to make a valid move.
        return get_user_move()


def get_board_coords(move):
    """
    Return the users move (int 1 - 9) into a tuple defining the index of the row and
    column in the board.
    """
    # Get the row of the move position using floor division (rounds number down to int).
    row = move // 3
    # Get the row of the position using modulo function. Return the remainder after
    # division.
    col = move % 3

    return row, col


def is_position_taken(board, move):
    """
    Return True if the user inputted move is already taken on the board. Otherwise
    return False.
    """
    row, col = get_board_coords(move)

    return board[row][col] == move


def place_move(board, move, user):
    """
    Places the user's move onto the board.
    """
    row, col = get_board_coords(move)

    board[row][col] = user


def is_winning_move(board, user):
    """
    Return True if the move causes a win for the user. False otherwise.
    """
    # Define the arguments passed to each checking function. Means we don't have to
    # repeat ourselves in the code.
    args = board, user

    # Using the spread operator to turn a list into elements.
    # *[1, 2, 3] = 1, 2, 3
    return any([check_rows(*args), check_columns(*args), check_diagonals(*args)])


def check_rows(board, user):
    """
    Check each row for a win, Returning True if so, False otherwise.
    """
    for row in board:
        if all([position == user for position in row]):
            return True
    return False


def check_columns(board, user):
    """
    Check each column for a win, Returning True if so, False otherwise.
    """
    for col in range(3):
        if all([board[row][col] == user for row in range(3)]):
            return True
    return False


def check_diagonals(board, user):
    """
    Check the diagonals for a win, Returning True if so, False otherwise.
    """
    if board[0][0] == user and board[1][1] == user and board[2][2] == user:
        return True
    elif board[0][2] == user and board[1][1] == user and board[2][0] == user:
        return True
    else:
        return False


def main():
    # Empty board position represented by None.
    board = [[None, None, None] for _ in range(3)]
    user = True

    while True:
        print_board(board)
        move = get_user_move()

        if is_position_taken(board, move):
            print("Position already taken. Please try again.", end='\n')
            continue

        place_move(board, move, user)

        if is_winning_move(board, user):
            print_board(board)
            print(f"{format_user(move)} won!")
            break

        user = not user


main()
