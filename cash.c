#include <cs50.h>
#include <stdio.h>

int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{
    // Ask how many cents the customer is owed
    int cents = get_cents();

    // Calculate the number of quarters to give the customer
    int quarters = calculate_quarters(cents);
    cents = cents - quarters * 25;

    // Calculate the number of dimes to give the customer
    int dimes = calculate_dimes(cents);
    cents = cents - dimes * 10;

    // Calculate the number of nickels to give the customer
    int nickels = calculate_nickels(cents);
    cents = cents - nickels * 5;

    // Calculate the number of pennies to give the customer
    int pennies = calculate_pennies(cents);
    cents = cents - pennies * 1;

    // Sum coins
    int coins = quarters + dimes + nickels + pennies;

    // Print total number of coins to give the customer
    printf("%i\n", coins);
}

//Code below gets the user input as cents
int get_cents(void)
{
    int cents;

    do
    {
        cents = get_int("Change owed: ");
    }
    while (cents < 0);

    return cents;
}

//Code below calculates howmany qurter coins we should return
int calculate_quarters(int cents)
{
    int quarter_count = 0;

    while (cents >= 25)
    {
        cents -= 25;
        quarter_count++;
    }

    return quarter_count;
}

//Code below calculates howmany dime coins we should return
int calculate_dimes(int cents)
{
    int dimes_count = 0;

    while (cents >= 10)
    {
        cents -= 10;
        dimes_count++;
    }

    return dimes_count;
}

//Code below calculates howmany nickel coins we should return
int calculate_nickels(int cents)
{
    int nickels_count = 0;

    while (cents >= 5)
    {
        cents -= 5;
        nickels_count++;
    }

    return nickels_count;
}

//Code below calculates howmany penny coins we should return
int calculate_pennies(int cents)
{
    int pennies_count = 0;

    while (cents >= 1)
    {
        cents--;
        pennies_count++;
    }

    return pennies_count;
}
