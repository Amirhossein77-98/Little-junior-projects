import random


def main():
    play_again_values = ["yes", "yep", "yeah", "y", "aha"]
    username = input("Hello, I'm guessing game.\nWhat is your name? ")
    play = "yes"
    while play in play_again_values:
        print("\n")
        game(username)
        play = input("Do you want to play again? ").lower()
    print("Thank you for playing!!!")


def game(username):
    chance = None
    start_num = None
    end_num = None
    guess = None
    tries = int()
    try_again_messages = ["Try again!", "Let's have another try!", "Let's try again!", "One more try!",
                          "Try another time!"]
    its_higher_messages = ["Nope! it's HIGHER!", "NO, it's HIGHER!", "NO, it's more than this!",
                           "Nope, it's more than this!"]
    win_messages = ["You Win!", "Congratulations, You Win!", "You Won the Game!",
                    "Congratulations, You Guessed Correctly!", "You Guessed Correctly, Congrats!", "You Win, Congrats!"]
    lose_messages = ["You Lose!", "You Lost the Game!", "You couldn't guess it!"]

    while chance is None:
        try:
            chance = abs(int(input("How many times do you want to try " + username + "? ")))
        except ValueError or TypeError:
            print("You must put an integer!!!\n" + random.choice(try_again_messages) + "\n")
            chance = None
        if chance == 0:
            print("You have only one chance!\n")
            chance += 1
        else:
            print("You have " + str(chance) + " chances left!\n")

    while start_num is None or end_num is None:
        while start_num is None:
            try:
                start_num = int(input("What should be the start number? "))
            except ValueError or TypeError:
                print("Your input should be an integer!\n" + random.choice(try_again_messages) + "\n")
                start_num = None
        while end_num is None:
            try:
                end_num = int(input("What should be the end number? "))
            except ValueError or TypeError:
                print("Your input must be an integer!\n" + random.choice(try_again_messages) + "\n")
                end_num = None
        if start_num >= end_num:
            print("End number must be higher than start number!\nTry another time!\n")
            start_num = None
            end_num = None
        elif (end_num - start_num) < 10:
            print("The difference between two numbers must be at least 10!\n")
            start_num = None
            end_num = None
    print("Your start number is " + str(start_num) + " and your end number is " + str(end_num) + "\n")

    our_random_number = int(random.randrange(start_num, end_num))

    while chance != 0 or None:
        try:
            guess = int(input("What is your guess?\n> "))
        except ValueError or TypeError:
            print("Your input should be an integer!\n" + random.choice(try_again_messages) + "\n")

        if (guess > end_num) or (guess < start_num):
            print("Your guess should be between " + str(start_num) + " and " + str(end_num))
            chance -= 1
            print("You have " + str(chance) + " chances left!\n")
            guess = None
            tries += 1
        elif guess == our_random_number:
            print(random.choice(win_messages))
            tries += 1
            print("Your tries: " + str(tries))
            break
        elif guess < our_random_number:
            print(random.choice(its_higher_messages))
            chance -= 1
            print("You have " + str(chance) + " chances left!\n")
            guess = None
            tries += 1
        elif guess > our_random_number:
            print("Nope, it's LOWER!")
            chance -= 1
            print("You have " + str(chance) + " chances left!\n")
            guess = None
            tries += 1

    if chance == 0:
        print(random.choice(lose_messages))
        print("Correct answer is " + str(our_random_number) + "!")
        print("Your tries: " + str(tries) + "\n")


main()
