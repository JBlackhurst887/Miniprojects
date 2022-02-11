board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]

user = True


def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot} ", end="")
        print()


def quit(user_input):
    if user_input == "q":
        print("Thanks for playing")
        return True
    else:
        return False


def check_input(user_input):
    # check if its a number
    if not isnum(user_input):
        return False
    user_input = int(user_input)
    # check if its 1 - 9
    return True


def isnum(user_input):
    if not user_input.isnumeric():
        print("This is not a valid number")
        return False
    else:
        return True


def bounds(user_input):
    if user_input > 9 or user_input < 1:
        print("This number is out of bounds")
        return False
    else:
        return True


def istaken(coords, board):
    row = coords[0]
    col = coords[1]
    if board[row][col] != "_":
        print("This position is already taken.")
        return True
    else:
        return False


def coordinates(user_input):
    row = int(user_input / 3)
    col = user_input
    if col > 2:
        col = int(col % 3)
    return (row, col)


def add_to_board(coords, board, active_user):
    row = coords[0]
    col = coords[1]
    board[row][col] = active_user


def current_user(user):
    if user:
        return "x"
    else:
        return "o"


def wincondition(user, board):
    if check_row(user, board):
        print('row')
        return True
    if check_col(user, board):
        print('col')
        return True
    if check_diag(user, board):
        print('diag')
        return True
    return False


def check_row(user, board):
    # Here was are checking that all the elements in the row equal the user counter.
    # This uses list comprehension. This is Python's way of iterating through lists and
    # is preferred to for loops.
    #
    # For instance, row = ["x", "_", "x"]
    # [x for x in row] == ["x", "_", "x"]
    # We are iterating over each element in the list and putting them into a new list.
    #
    # [elem == user for elem in row]. Now this is not just adding the elements to the
    # new list but also making a comparison to the player who just made a turn.
    # If for instance player x just made a turn, the list would interally be doing:
    # ["x" == "x", "_" == "x", "x" == "x"]
    # These comparisions are made by Python and thus the list would equal.
    # [True, False, True]
    #
    # Now the final stage is using the all function. This checks that all elements in a
    # list are True. So calling
    # all([True, False, True]) would return False, so we know the user has no completed
    # this given row. Where are all([True, True, True]) returns True, so we know the
    # user has completed the row and has won the game.

    for row in board:
        if all([elem == user for elem in row]):
            return True
    return False


def check_col(user, board):
    # Exactly the same login here applied as above.
    for col in range(3):
        if all([board[row][col] == user for row in range(3)]):
            return True
    return False


def check_diag(user, board):
    # Forgot to include "== user" for board[2][2].
    if board[0][0] == user and board[1][1] == user and board[2][2] == user:
        return True
    elif board[0][2] == user and board[1][1] == user and board[2][0] == user:
        return True
    else:
        return False


while True:
    active_user = current_user(user)
    print_board(board)
    user_input = input("Please enter a position 1 through 9 or enter \"q\" to quit ")
    if quit(user_input):
        break
    if not check_input(user_input):
        print("Please try again.")
        continue
    user_input = int(user_input) - 1
    coords = coordinates(user_input)
    if istaken(coords, board):
        print("Please try again.")
        continue
    add_to_board(coords, board, active_user)
    if wincondition(active_user, board):
        print(f"{active_user} won!")
        break

    user = not user
