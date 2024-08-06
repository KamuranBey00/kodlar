#include <stdio.h>

void birthday(char x[] , int y)
{
   printf("\nIyi ki dogdun! %s", x);
   printf("\n%d yasina girdin", y);
}

int main()
{

  char name[] = "Sabri";
  int age=18;

   birthday(name, age);
   birthday("Elif", 20);

   return 0;
}
