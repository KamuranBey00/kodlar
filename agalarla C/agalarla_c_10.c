#include <stdio.h>

int main(){

    /* Switch =  else if yerine kullanabileceğimiz alternatif bir durumdur */

   char grade;

   printf("\nNotunuzu giriniz: ");
   scanf("%c", &grade);

   switch(grade){
      case 'A':
         printf("Sen bu dersin hocasi misin?!\n");
         break;
      case 'B':
         printf("Oyy ha ! \n");
         break;
      case 'C':
         printf("Iyisin iyi\n");
         break;
      case 'D':
         printf("Bala gectin\n");
         break;
      case 'F':
         printf("Zortladin\n");
         break;
      default:
         printf("Gecerli bir not gireydin iyiydi");
   }
   return 0;
}