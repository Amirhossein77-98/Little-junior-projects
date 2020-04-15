import random

user_win = 0
computer_win = 0
tries = 0
yes_values = ["yes", "yep", "yeah", "y", "aha", "ohom", "ye", "yey"]
no_answers = ["no", "nope", "nay", "na", "n", "aa", "ne", "ney", "na"]

choices_dict = {
    "rock": ["rock", "r", "rk", "rck", "rack", "rak", "1"],
    "paper": ["paper", "p", "pr", "ppr", "peper", "peiper", "pa", "2"],
    "scissor": ["scissor", "s", "sc", "scr", "skisor", "scisor", "sci", "ski", "sksr", "scsr", "skisr", "scisr", "3"]
}


def main():

    play = "yes"
    global tries, user_win, computer_win

    print("*** Hi, Welcome to the Rock, Paper, Scissor game ***\n")
    user_manual = input("Do you want to read user manual before playing? ").lower()

    if user_manual in yes_values:
        user_manual_func()
    elif user_manual in no_answers:
        print("Ok, lest's get into playing...\n")

    while play in yes_values:
        try:
            tries = int(input("\nWhat is the maximum try you want? "))
        except ValueError or TypeError:
            print("Invalid input! Your input should be a number!")

        game()

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


def game():

    global user_win, computer_win, tries
    win_edge = (tries // 2) + 1

    while (tries != 0) and (user_win < win_edge) and (computer_win < win_edge):

        computer = random.choice(list(choices_dict))

        user = input("What is your choice? ").lower()

        if user in (choices_dict.get("rock")):
            user = "rock"
        elif user in (choices_dict.get("paper")):
            user = "paper"
        elif user in (choices_dict.get("scissor")):
            user = "scissor"
        else:
            print("Invalid Input!!!")

        if user not in list(choices_dict):
            game()
        elif user == computer:
            print("Correct!")
            tries -= 1
            user_win += 1
            print("You: " + str(user_win))
            print("Computer: " + str(computer_win))
            print("Left tries: " + str(tries) + "\n")
        else:
            print("Wrong!")
            print("Correct answer: " + computer)
            tries -= 1
            computer_win += 1
            print("You: " + str(user_win))
            print("Computer: " + str(computer_win))
            print("Left tries: " + str(tries) + "\n")


def user_manual_func():
    print("First, you should choose what is the maximum time you wanna try and play, but you should consider that:")
    print("1. If each of the players, I mean 'You' and 'Computer', win more than half of the maximum try, that guy"
          " will be the winner and the game will be closed. Because if somebody gets more score than half of the "
          "maximum try, it means they are the absolute winner and playing more will not change the result!")
    print("2. Valid yes answers are: " + str(yes_values))
    print("3. Valid no answers are: " + str(no_answers))


main()
