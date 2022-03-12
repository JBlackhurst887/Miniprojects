import random


options = ["rock", "paper", "scissors"]
user_wins = 0
computer_wins = 0

def score():
    print("User wins: ", user_wins, ", Computer wins: ", computer_wins)

def main():
    global user_wins
    global computer_wins
    while True:
        user_input = input("Type Rock/Paper/Scissors or q to quit: ").lower()
#quit system       
        if user_input == "q":
            print("Thank you for playing. ")
            break
          
        if user_input not in options:
            print("This is not a valid option")
            continue
    #assigning values to rock, paper, scissors. rock = 0, paper = 1, scissors = 2
        random_number = random.randint(0, 2)
        computer_pick = options[random_number]
        user_pick = user_input
        print("Computer picked: ", computer_pick + ".")

        if computer_pick == user_pick:
            print("Draw! Please try play again")
            continue
        
        if user_input == "rock" and computer_pick == "scissors":
            print("You won!")
            user_wins += 1
            score()
            continue
        
        elif user_input == "paper" and computer_pick == "rock":
            print("You won!")
            user_wins += 1
            score()
            continue

        elif user_input == "scissors" and computer_pick == "paper":
            print("You won!")
            user_wins += 1
            score()
            continue

        else:
            print("You lost!")
            computer_wins += 1
            score()

main()


