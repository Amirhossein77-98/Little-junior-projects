#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <math.h>

int Char_Counter(string UserInput);
int Word_Counter(string UserInput);
int Sentence_Counter(string UserInput);


int main(void)
{
    //Code below gets the user input
    string UserInput = get_string("Text: ");

    //Codes below pass the user input to functions that count requirements and saves them into Three variables
    int CharCount = Char_Counter(UserInput);
    int WordCount = Word_Counter(UserInput);
    int SentenceCount = Sentence_Counter(UserInput);

    //This part is for calculating L & S in order to use them for the Kolman-Liau formula
    float L = (float) CharCount / (float) WordCount * 100;
    float S = (float) SentenceCount / (float) WordCount * 100;

    int index = round(0.0588 * L - 0.296 * S - 15.8);

    //This section identifies the Grade of each Input and brings it back to the user
    if (index >= 1 && index <= 16)
    {
        printf("Grade %i\n", index);
    }
    else if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade 16+\n");
    }

}

//Function below calculates the number of letters in user's input
int Char_Counter(string UserInput)
{
    int CharacterCount = 0;

    for (int i = 0; i < strlen(UserInput); i++)
    {
        if ((UserInput[i] > 64 && UserInput[i] < 91) || (UserInput[i] > 96 && UserInput[i] < 123))
        {
            CharacterCount++;
        }
        else
        {
            CharacterCount += 0;
        }
    }
    return CharacterCount; //This returns the result into the main function
}

//This function calculates the number of words in user's input
int Word_Counter(string UserInput)
{
    int SpaceCount = 0;

    for (int i = 0; i < strlen(UserInput); i++)
    {
        if (UserInput[i] == 32)
        {
            SpaceCount++;
        }
        else
        {
            SpaceCount += 0;
        }
    }
    return SpaceCount + 1; //This returns the result into the main function
}

//The following function calculates the number of sentences in user's input
int Sentence_Counter(string UserInput)
{
    int SentenceCount = 0;

    for (int i = 0; i < strlen(UserInput); i++)
    {
        if (UserInput[i] == 33 || UserInput[i] == 46 || UserInput[i] == 63)
        {
            SentenceCount++;
        }
        else
        {
            SentenceCount += 0;
        }
    }
    return SentenceCount; //This returns the result into the main function
}