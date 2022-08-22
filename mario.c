#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //Here we declared some variables
    int height;
    int rows;
    int columns;

    //In this scope we get the height as an input from the user and it should be something between 1 and 8
    do
    {
        height = get_int("Please enter your preferred height: ");
    }
    while (height < 1 || height > 8);

    //In this section we print the Hashes and spaces. Firsr "for loop" is for making rows and second one is for making columns, and the third one makes second block of hashes
    for (rows = 0; rows < height; rows++)
    {
        for (columns = 0; columns < height; columns++)
        {
            if (rows + columns < height - 1)
            {
                printf(" ");
            }
            else
            {
                printf("#");
            }
        }
        printf("  ");

        for (columns = -1; columns < rows; columns++)
        {
            printf("#");
        }
        //We have to add new lines
        printf("\n");
    }
}