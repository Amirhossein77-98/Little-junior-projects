# TODO

height = 0

# This while loop runs until the input is a number and it's between 1 & 8
while height < 1 or height > 8:
    height = input("Height: ")

    # These if and else's check for the input to be a number first and then not be empty and at last if it is a number converts it to int
    if height.isalpha():
        height = 0
    elif height == "":
        height = 0
    else:
        height = int(height)

# Section below prints the blocks
for i in range(height):
    for j in range(height):
        if ((i + j) >= (height - 1)):
            print("#", end="")
        else:
            print(" ", end="")

    print()