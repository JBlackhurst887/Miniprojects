from re import I
from shutil import move
import sys



#returns a string representation of a board position that can be logged to console.
def format_user(element):
    if element is None:
        return "_"
    elif element:
        return "x"
    else:
        return "o"

def print_board(board):
    for row in board:
        for position in row:
            print(f"{format_user(position)}", end="")
        print()


def get_user_move():
#get users move as an input from the console. Validate the number is between 1 - 7 or "q" (for quitting the game).
    user_input = input("Please enter a position 1 through 7 or enter \"q\" to quit: ")
    if user_input == "q":
        print("Thank you for playing. ")
        sys.exit()
#validate the number is in range 1 - 7.
    if user_input in [str(I) in range(1, 8)]:
        return int(user_input) - 1
    else:
        print("Try again. ")
        return get_user_move()

#quit the program    
#def quit(user_input):
    #if user_input == "q":
        #print("Thank you for playing. ")
        #sys.exit()


#def check_input():
    #get users move as an input from the console. Validate the number is between 1 - 7 or "q" (for quitting the game).
    #user_input = input("Please enter a position 1 through 7 or enter \"q\" to quit: ")
#validate the number is in range 1 - 7.
    #if user_input in [str(i) in range(1, 8)]:
        #return int(user_input) - 1
    #else:
        #return True

def get_board_coords(move):
#row is inverted and starts at 0. If user input = 1 then to correlate to row must minus 1
    row = int(move - 1)
#col starts at 1 so user input = column selected
    col = int(move)
    return row, col


def add_to_board(board, user, move):
#Place user's move onto board
    row, col = get_board_coords(move)
    board[row][col] = user

def main():
    board = [[None for _ in range(7)] for _ in range(6)]
    user = True

    while True:
        print_board(board)
        move = get_user_move()

        add_to_board(board, move, user)
        
main()
    
