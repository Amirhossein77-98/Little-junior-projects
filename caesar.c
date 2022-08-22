#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

//This part gives the user input from consol
int main(int argc, string argv[])
{
    //This if statement checkes whether the consol code has only one argv
    if (argc != 2)
    {
        printf("Usage: ./saesar key\n");
        return 1;
    }

    //This code checks the argv to be numerical and if it is anything else returns a problem in program
    for (int j = 0; j < strlen(argv[1]); j++)
    {
        if (!isdigit(argv[1][j]))
        {
            printf("Usage: ./saesar key\n");
            return 1;
        }
    }

    //This code converts argv (which is a string) into an integer
    int k = atoi(argv[1]);

    //Code below gets the user input
    string PlainText = get_string("Text: ");

    printf("ciphertext: ");

    //The following segment checks the user input character by character and keep the letters case as it is, and it just encrypts the letters
    for (int i = 0; i < strlen(PlainText); i++)
    {
        if (isupper(PlainText[i]))
        {
            //This formula first makes the ascii number of letters countable from 1 and then adds the key to them and shifts them key levels
            //Then it devides the number by 26 (for we have 26 letters in alphabet) and then turns it into an ascii by adding 65 to it
            printf("%c", (PlainText[i] - 65 + k) % 26 + 65);
        }
        else if (islower(PlainText[i]))
        {
            printf("%c", (PlainText[i] - 97 + k) % 26 + 97);
        }
        else
        {
            printf("%c", PlainText[i]);
        }
    }
    printf("\n");
}