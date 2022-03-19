BOARD_COLS = 7
BOARD_ROWS = 6

class Board():
    def __init__(self):
        self.board = [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
        self.turns = 0
        self.last_move = [-1, -1] # row, col

    def print_board(self):
        #Number the columns
        print("\n")
        for col in range(BOARD_COLS):
            print(f"   ({col + 1}) ", end="")
        print("\n")

        #Print the slots of the game board
        for row in range(BOARD_ROWS):
            print("|", end="")
            for col in range(BOARD_COLS):
                print(f"    {self.board[row][col]} |", end="")
            print("\n")

        print(f"{'-' * 35}\n")
    
    def which_turn(self):
        players = ['X', 'O']
        return players[self.turns % 2]

    def turn(self, column):
        #search from bottom up
        for row in range(BOARD_ROWS-1, -1, -1):
            if self.board[row][column] == ' ':
                self.board[row][column] = self.which_turn()
                self.last_move = [row, column]

                self.turns += 1
                return True
        return False

    def in_bounds(self, row, col):
        return (row >= 0 and row < BOARD_ROWS and col >= 0 and col < BOARD_COLS)

    def check_winner(self):
        last_row = self.last_move[0]
        last_col = self.last_move[1]
        last_letter = self.board[last_row][last_col]

        #test row and col direction, matching letter count, locked bool
        directions = [
            [[-1, 0], 0, True],
            [[1, 0], 0, True],
            [[0, -1], 0, True],
            [[0, -1], 0, True],
            [[-1, -1], 0, True],
            [[1, 1], 0, True],
            [[-1, 1], 0, True],
            [[1, 1], 0, True],
        ]

        # search outwards looking for matching letters
        for a in range(4):
            for d in directions:
                row = last_row + (d[0][0] * (a+1))
                col = last_col + (d[0][1] * (a+1))

                if d[2] and self.in_bounds(row, col) and self.board[row][col] == last_letter:
                    d[1] += 1
                else:
                    #Stop searching in this direction
                    d[2] = False
        #Check possible direction pairs for 4 pieces in a row
        for i in range(0, 7, 2):
            if (directions[i][1] + directions[i+1][1] >= 3):
                self.print_board()
                print(f"{last_letter} is the winner!")
                return last_letter 
        #Did not find a winner
        return False

def play():
    game = Board()

    game_over = False
    while not game_over:
        #continue playing

        game.print_board()

        valid_move = False
        while not valid_move:
            user_move = input(f"{game.which_turn()}'s turn - pick 1 - 7: ")

            try:
                valid_move = game.turn(int(user_move) - 1)
            except:
                print(f"Please chosoe a number betwwen 1 and {BOARD_COLS}")

        game_over = game.check_winner()

        if not any(' ' in x for x in game.board):
            print("The game is a draw...")
            return

if __name__ == '__main__':
    play()
