#include <stdio.h>

int main(void) {

   float first_num = 0.0, second_num = 0.0; int func = 0;

   printf("1: subtraction\n2: addition\n3: multiplication\n4: division\nSelect function: ");
   scanf("%d", &func);

   printf("Enter the first number: ");
   scanf("%f", &first_num);
   printf("Enter the second number: ");
   scanf("%f", &second_num);

   switch (func) {
      case 1: {
         printf("%.2f-%.2f=%.2f", first_num, second_num, first_num - second_num);
         break;
      }
      case 2: {
         printf("%.2f+%.2f=%.2f", first_num, second_num, first_num + second_num);
         break;
      }
      case 3: {
         printf("%.2f*%.2f=%.2f", first_num, second_num, first_num * second_num);
         break;
      }
      case 4:{
        printf("%.2f/%.2f=%.2f",first_num,second_num,first_num / second_num);
      }
      default: {
         printf("An error has occurred while running the program.");
         break;
      }
   }

   return 0;

}