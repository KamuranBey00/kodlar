
#include <stdio.h>

int multiplication(int number1, int number2)
{
    int result;
    if (number2 == 1)
    {
        result = number1;
    }
    
    else
    {
        result = number1 + multiplication(number1, number2 - 1);
    }
}


int main()
{
    int n1, n2;
    printf("Enter The First Number: ");
    scanf("%d", &n1);
    printf("Enter The Second Number: ");
    scanf("%d", &n2);
    printf("The Result Is: %d", multiplication(n1, n2));
}