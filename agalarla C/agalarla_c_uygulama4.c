#include <stdio.h>

int main(){

   char operator;
   double num1;
   double num2;
   double result;

   printf("\n What kind of operation do you want to make ?  (+  -  *  /): ");
   scanf("%c", &operator);

   printf("\n Enter first number : ");
   scanf("%lf", &num1);

   printf("\n Enter second number : ");
   scanf("%lf", &num2);

   switch(operator){
      case '+':
         result = num1 + num2;
         printf("\nResult = %.2lf", result);
         break;
      case '-':
         result = num1 - num2;
         printf("\nResult = %.2lf", result);
         break;
      case '*':
         result = num1 * num2;
         printf("\nResult = %.2lf", result);
         break;
      case '/':
         result = num1 / num2;
         printf("\nResult =%.2lf", result);
         break;
      default:
         printf("%c is not a valid operation", operator);
   }

   return 0;
}