# TODO

User_Input = input("Your Input: ")

symbols_list = [".", "!", "?"]
char_count = 0
word_count = 1
sentence_count = 0

for i in User_Input:
    if i.isalpha():
        char_count += 1
    if i.isspace():
        word_count += 1
    if i in symbols_list:
        sentence_count += 1

L = (char_count * 100.0) / word_count
S = (sentence_count * 100.0) / word_count

index = int((0.0588 * L - 0.296 * S - 15.8) + 0.5)

if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print("Grade ", str(index))