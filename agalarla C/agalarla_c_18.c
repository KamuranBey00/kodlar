#include <stdio.h>

void hello(char[], int); // fonksiyon prototipi

int main()
{
   /* Fonksiyon Prototipi

   Nedir?
    Body partı olmadan, main öncesine fonksiyon tanımlama
    Bir fonksiyon çağrılırken doğru argümanların girilmesini sağlar

   Önemli Notlar
    Birçok C derleyicisi parametreleri kontrol etmez
    Eksik argümanlar beklenmeyen davranışlara neden olur
    Argümanlar eksikse derleyicinin bir hata vermesine neden olur */

    char name[] = "Sabri";
    int age = 18;

    hello(name, age);



   return 0;
}

void hello(char name[], int age)
{
   printf("\nMerhaba %s", name);
   printf("\n%d yasindasin", age);
}