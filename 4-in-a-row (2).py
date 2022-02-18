board = [
    ["_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_"],
]

def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot} ", end="")
        print()

#Allows user to exit the application
def quit(user_input):
    if user_input == "q":
        print("Thank you for playing.")
        return True
    else:
        return False

 #Limiting inputs
 #check if user input is a number
def check_input(user_input):
    if not isnum(user_input):
        return False
    user_input = int(user_input)
#check if between 1 and 7
    if bounds(user_input):
        return True

def isnum(user_input):
    if not user_input.isnumeric():
        print("This is not a valid number.")
        return False
    else:
        return True

def bounds(user_input):
    if user_input > 7 or user_input < 1:
        print("That number is out of bounds. Please select a number between 1 and 7. ")
        return False
    else: return True

while True:
    print_board(board)
    user_input = input("Please enter select a column between 1 and 7. Press q to stop playing. ")
    if quit(user_input):
        break
    if not check_input(user_input):
        print("Please try again. ")
        continue
    