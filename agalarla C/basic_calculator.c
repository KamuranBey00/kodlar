#include<stdio.h>
int main(){
    char condition;
    int num1,num2;
    printf("Enter first num : ");
    scanf("%d",&num1);
    printf("Enter second num : ");
    scanf("%d",&num2);
    printf("Enter your condition : ");
    scanf("%s",&condition);

    switch (condition)
    {
    case('+'):
        printf("%d + %d = %d",num1,num2,(num1+num2));
        break;
    case('-'):
        printf("%d - %d = %d",num1,num2,(num1-num2));
        break;
    case('*'):
        printf("%d * %d = %d",num1,num2,(num1*num2));
        break;
    case('/'):
        printf("%d / %d = %d",num1,num2,(num1/num2));
        break;
    default:
        printf("Something Went wrong please try again.");
        break;
    }

}