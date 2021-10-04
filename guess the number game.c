#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main()
{
    int number, guess, No_Of_Guesses = 1;
    srand(time(0));
    number = rand() % 100 + 1; // generate random number between 1 to 100
    // printf("the number is:%d\n", number);
    // keep running the loop until the nmber is guessed
    do
    {
        printf("guess the number between 1 to 100\n");
        scanf("%d", &guess);
        if (guess > number)
        {
            printf("enter a lower number!\n");
        }
        else if (guess < number)
        {
            printf("enter a higher number!\n");
        }
        else
        {
            printf("Hurray! You have guessed the number in %d attempts\n", No_Of_Guesses);
        }
        No_Of_Guesses++;
    } while (guess != number);

    return 0;
}
