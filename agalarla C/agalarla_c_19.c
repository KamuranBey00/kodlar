#include <stdio.h>
#include <string.h>
 
int main(){
  
   char string1[] = "Alper";
   char string2[] = "Ahmet";
 
   strlwr(string1);                              // stringi küçük karakterlre dönüştürür
   //strupr(string1);                           // stringi büyük karakterlre dönüştürür
   //strcat(string1, string2);             // string2 yi string1'in sonuna ekler
   //strncat(string1, string2, 1);       // string2'nin n sayıda karakterini string1 e ekler
   //strcpy(string1, string2);             // string2 yi string1 e kopyalar
   //strncpy(string1, string2, 3);      // string2'nin n sayıda karakterini string1 e kopyalar
   
   //strset(string1, '!');        //Stringin tüm karakterlerini verdiğimiz karaktere dönüştürür
   //strnset(string1, 'x', 1);  //Stringin n sayıda karakterini verdiğimiz karaktere dönüştürür
   //strrev(string1);             //Stringi terse çevirir

   //int result = strlen(string1);                          // tring uzunluğunu int olarak geri döndürür
   //int result = strcmp(string1, string2);         // Stringler arası karakterleri karşılaştırır
   //int result = strncmp(string1, string2, 2);   // Stringler arası n sayıda karakteri karşılatırır
   //int result = strcmpi(string1, string1);        // Stringler arası karakterleri karşılaştırır (büyük küçük farketmez)
   //int result = strnicmp(string1, string1, 1);  // Stringler arası n sayıda karakteri karşılatırır (büyük küçük farketmez)

   printf("%s", string1);

   
   //if(result == 0)
   //{
   //   printf("Stringler birbiriyle aynı");
   //}
   //else
   //{
   //   printf("Stringler birbirinden farklı");
   //}
   

   return 0;
}