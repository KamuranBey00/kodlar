#include <stdio.h>
#include <string.h>

int main(){

char name[25];  //bytes
int age;

printf ("\nAdin ne?");
//scanf("%s", &name);

fgets(name, 25, stdin);
name[strlen(name) -1] = '\0';

printf("Kac yasindasin?");
scanf ("%d", &age);

printf("\nMerhaba %s, nasilsin?", name);
printf("\nsen %d yasindasin" , age);

return 0;
}