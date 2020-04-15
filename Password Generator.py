import string
import secrets
import random


""" Variables Section """


pass_length = 0
uppercase: bool = True
digit: bool = True
schar: bool = True

YesAnswers = ["yes", "yep", "yeah", "y", "aha", "ye"]
NoAnswers = ["no", "nope", "nay", "na", "n", "aa", "ne"]
MineAnswers = ["my", "mine", "ma", "me", "m", "my standards", "ma standards", "ma sta", "my sta"]
YoursAnswer = ["your", "yours", "you", "your standards", "your standard", "your sta"]


""" Functions Section """


def main():
    global pass_length
    run_again = "yes"

    print("*** Hi, I'm Password Generator ***\n")

    while run_again in YesAnswers:

        ran_or_no: str = input("You want me to generate a password by my standards? or yours? ").lower()
        if (ran_or_no in YesAnswers) or (ran_or_no in YoursAnswer):
            password = totally_random()
            print("\nHere is your " + str(len(password)) + " character password: " + password)
            run_again = input("\nDo you want to make another password or not? ").lower()
        if (ran_or_no in NoAnswers) or (ran_or_no in MineAnswers):
            print("Ok!\n")
            pass_length = 0
            password = password_with_user_variables()
            print("\nHere is your " + str(len(password)) + " character password: " + password)
            run_again = input("\nDo you want to make another password or not? ").lower()
        else:
            print("Invalid input, please answer with 'yes' or 'no'!!!\n")
            main()


def user_parameters():
    global pass_length, uppercase, digit, schar
    containing_uppercase = ''
    containing_digit = ''
    containing_schar = ''

    while pass_length <= 3:
        try:
            pass_length = int(input("1. How long do you want it to be?(It's recommended to be 6 characters"
                                    " at least!): "))
            if pass_length <= 3:
                print("Sorry but less than 4 characters is not allowed!\n")
            else:
                print("OK!\n")
        except ValueError or TypeError:
            print("Your input should be a number!!!\nTry again:\n")

    while containing_uppercase == '':
        containing_uppercase = input("2. Do you want it to contain uppercase letters or not?(It is recommended to"
                                     " contain!): ")
        if containing_uppercase in YesAnswers:
            uppercase = True
        elif containing_uppercase in NoAnswers:
            uppercase = False
        else:
            print("Sorry, but you should answer with 'yes' or 'no'!\n")
            containing_uppercase = ''

    while containing_digit == '':
        containing_digit = input("3. Do you want it to contain numbers or not?(It is recommended to contain!): ")
        if containing_digit in YesAnswers:
            digit = True
        elif containing_digit in NoAnswers:
            digit = False
        else:
            print("Sorry, but you should answer with 'yes' or 'no'!\n")
            containing_digit = ''

    while containing_schar == '':
        containing_schar = input("4. Do you want it to contain special characters (like: !@#$) or not?"
                                 "(It is recommended to contain!): ")
        if containing_schar in YesAnswers:
            schar = True
        elif containing_schar in NoAnswers:
            schar = False
        else:
            print("Sorry, but you should answer with 'yes' or 'no'!\n")
            containing_schar = ''

    password_with_user_variables()


def totally_random():
    pass_source = string.ascii_letters + string.digits + string.punctuation
    password = secrets.choice(string.ascii_lowercase)
    password += secrets.choice(string.ascii_uppercase)
    password += secrets.choice(string.digits)
    password += secrets.choice(string.punctuation)

    for i in range(0, random.randrange(4, 7)):
        password += secrets.choice(pass_source)

    pass_list = list(password)
    secrets.SystemRandom().shuffle(pass_list)
    password = ''.join(pass_list)
    return password


def password_with_user_variables():
    global pass_length, uppercase, digit, schar

    if (uppercase is True) and (digit is True) and (schar is True):
        pass_source = string.ascii_letters + string.digits + string.punctuation
        password = secrets.choice(string.ascii_lowercase)
        password += secrets.choice(string.ascii_uppercase)
        password += secrets.choice(string.digits)
        password += secrets.choice(string.punctuation)

        for i in range(0, (pass_length - 4)):
            password += secrets.choice(pass_source)

        pass_list = list(password)
        secrets.SystemRandom().choice(pass_list)
        password = ''.join(pass_list)
        return password

    if (uppercase is False) and (digit is True) and (schar is True):
        pass_source = string.ascii_lowercase + string.digits + string.punctuation
        password = secrets.choice(string.ascii_lowercase)
        password += secrets.choice(string.digits)
        password += secrets.choice(string.punctuation)

        for i in range(0, (pass_length - 3)):
            password += secrets.choice(pass_source)

        pass_list = list(password)
        secrets.SystemRandom().choice(pass_list)
        password = ''.join(pass_list)
        return password

    if (uppercase is False) and (digit is False) and (schar is True):
        pass_source = string.ascii_lowercase + string.punctuation
        password = secrets.choice(string.ascii_lowercase)
        password += secrets.choice(string.punctuation)

        for i in range(0, (pass_length - 2)):
            password += secrets.choice(pass_source)

        pass_list = list(password)
        secrets.SystemRandom().choice(pass_list)
        password = ''.join(pass_list)
        return password

    if (uppercase is False) and (digit is False) and (schar is False):
        pass_source = string.ascii_lowercase
        password = ''

        for i in range(0, pass_length):
            password += secrets.choice(pass_source)

        pass_list = list(password)
        secrets.SystemRandom().choice(pass_list)
        password = ''.join(pass_list)
        return password

    if (uppercase is True) and (digit is True) and (schar is False):
        pass_source = string.ascii_letters + string.digits
        password = secrets.choice(string.ascii_lowercase)
        password += secrets.choice(string.digits)
        password += secrets.choice(string.ascii_uppercase)

        for i in range(0, (pass_length - 3)):
            password += secrets.choice(pass_source)

        pass_list = list(password)
        secrets.SystemRandom().choice(pass_list)
        password = ''.join(pass_list)
        return password

    if (uppercase is True) and (digit is False) and (schar is False):
        pass_source = string.ascii_letters
        password = secrets.choice(string.ascii_lowercase)
        password += secrets.choice(string.ascii_uppercase)

        for i in range(0, (pass_length - 2)):
            password += secrets.choice(pass_source)

        pass_list = list(password)
        secrets.SystemRandom().choice(pass_list)
        password = ''.join(pass_list)
        return password

    if (uppercase is True) and (digit is False) and (schar is True):
        pass_source = string.ascii_letters + string.punctuation
        password = secrets.choice(string.ascii_lowercase)
        password += secrets.choice(string.punctuation)
        password += secrets.choice(string.ascii_uppercase)

        for i in range(0, (pass_length - 3)):
            password += secrets.choice(pass_source)

        pass_list = list(password)
        secrets.SystemRandom().choice(pass_list)
        password = ''.join(pass_list)
        return password

    if (uppercase is False) and (digit is True) and (schar is False):
        pass_source = string.digits
        password = ''

        for i in range(0, pass_length):
            password += secrets.choice(pass_source)

        pass_list = list(password)
        secrets.SystemRandom().choice(pass_list)
        password = ''.join(pass_list)
        return password


main()
