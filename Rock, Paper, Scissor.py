import random

# Variables Section
# I use global variables to sync them between multiple functions.
user_win = 0
computer_win = 0
tries = 0
yes_values = ["yes", "yep", "yeah", "y", "aha", "ohom", "ye", "yey"]
no_answers = ["no", "nope", "nay", "na", "n", "aa", "ne", "ney", "na"]
# Dictionary below defines the possible answers for every element, and containers can be considered as a list and be
# used for random function to get a random value of "rock", "paper", or "scissor"
choices_dict = {
    "rock": ["rock", "r", "rk", "rck", "rack", "rak", "1"],
    "paper": ["paper", "p", "pr", "ppr", "peper", "peiper", "pa", "2"],
    "scissor": ["scissor", "s", "sc", "scr", "skisor", "scisor", "sci", "ski", "sksr", "scsr", "skisr", "scisr", "3"]
}


# Main Function
def main():
    play = "yes"  # This defines whether the game should start and be played or not; and we use it to ask for replay.
    global tries, user_win, computer_win

    print("*** Hi, Welcome to the Rock, Paper, Scissor game ***\n")
    user_manual = input("Do you want to read user manual before playing? ").lower()

    if user_manual in yes_values:
        user_manual_func()
    elif user_manual in no_answers:
        print("Ok, lest's get into playing...\n")

    while play in yes_values:  # While play variable has a value of yes list the game will play again and again.
        try:
            tries = int(input("\nWhat is the maximum try you want? "))
        except ValueError or TypeError:
            print("Invalid input! Your input should be a number!")

        game()
        # Code below returns the result of the game after the game() function is done and closed.
        if user_win > computer_win:
            print("You Win!")
            play = input("Do you want to play again? ")
            tries = 0
            user_win = 0
            computer_win = 0
        elif user_win < computer_win:
            print("You Lose!")
            play = input("Do you want to play again? ")
            tries = 0
            user_win = 0
            computer_win = 0
        elif user_win == computer_win:
            print("Draw!")
            play = input("Do you want to play again? ")
            tries = 0
            user_win = 0
            computer_win = 0


# Game's section
def game():
    global user_win, computer_win, tries
    win_edge = (tries // 2) + 1  # This should be here to give the game a sense of logic. More info in user manual.

# The while loop below plays the game again and again until there is no attempt left or one is absolutely the winner.
    while (tries != 0) and (user_win < win_edge) and (computer_win < win_edge):

        computer = random.choice(list(choices_dict))

        user = input("What is your choice? ").lower()
        
# Code below checks the users answer and it must be in the choices_dic dictionary and replaces the correct value.
        if user in (choices_dict.get("rock")):
            user = "rock"
        elif user in (choices_dict.get("paper")):
            user = "paper"
        elif user in (choices_dict.get("scissor")):
            user = "scissor"
        else:
            print("Invalid Input!!!")

        if user not in list(choices_dict):  # This code check if the user input is not in dictionary re-asks question.  
            game()
        elif user == computer:  # This is for the correct answer.
            print("Correct!")
            tries -= 1
            user_win += 1
            print("You: " + str(user_win))
            print("Computer: " + str(computer_win))
            print("Left tries: " + str(tries) + "\n")
        else: # This is for wrong answer.
            print("Wrong!")
            print("Correct answer: " + computer)
            tries -= 1
            computer_win += 1
            print("You: " + str(user_win))
            print("Computer: " + str(computer_win))
            print("Left tries: " + str(tries) + "\n")


# User manual section
def user_manual_func():
    print("First, you should choose what is the maximum time you wanna try and play, but you should consider that:")
    print("1. If each of the players, I mean 'You' and 'Computer', win more than half of the maximum try, that guy"
          " will be the winner and the game will be closed. Because if somebody gets more score than half of the "
          "maximum try, it means they are the absolute winner and playing more will not change the result!")
    print("2. Valid 'yes' answers are: " + str(yes_values))
    print("3. Valid 'no' answers are: " + str(no_answers))
    print("4. Possible answers for 'rock': " + str(list(choices_dict.get("rock"))))
    print("5. Possible answers for 'paper': " + str(list(choices_dict.get("paper"))))
    print("6. Possible answers for 'scissor': " + str(list(choices_dict.get("scissor"))))


main()
