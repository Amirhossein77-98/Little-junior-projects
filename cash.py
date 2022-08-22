# TODO

dollars = -1

# This while loop runs until the input is a number and it's more than 0
while dollars < 0:
    dollars = input("Change Owed: ")

    # These if and else's check for the input to be a number first and then not be empty and at last if it is a number converts it to float
    if dollars.isalpha():
        dollars = -1
    elif dollars == "":
        dollars = -1
    else:
        dollars = float(dollars)

# The following line of code turns dollars into cents
cents = round(dollars * 100)

# This variable is the number of coins we should give to the customer
coin_count = 0

# The following while loops check the remaining change owed and count the number of coins we should pass to the customer
while cents >= 25:
    cents -= 25
    coin_count += 1

while cents >= 10:
    cents -= 10
    coin_count += 1

while cents >= 5:
    cents -= 5
    coin_count += 1

while cents >= 1:
    cents -= 1
    coin_count += 1

print(coin_count)