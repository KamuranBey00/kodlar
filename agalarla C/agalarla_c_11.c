#include <stdio.h>
#include <stdbool.h>

int main(){
// mantıksal operatörler = && (AND) 2 veya daha fazla koşulun aynı anda doğru olduğunu kontrol ederken kullanılır.
float temp= 25;
bool sunny = true;
if(temp >= 0 && temp <= 30 && sunny){
printf("\nHava gayet iyi");
}
else{
printf("\nHava kotu durumda");
}

return 0;
}