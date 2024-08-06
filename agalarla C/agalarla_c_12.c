#include <stdio.h>

int main(){
 
    // mantıksal operatörler = || (OR) koşullardan sadece birinin doğru olmasının yeterli olduğunda kullanılır.
    
    float temp = 25;

    if(temp <= 0 || temp >= 30 || temp  <= 15){
        printf("\nHava kotu durumda!");
    }
    else{
        printf("\nHava gayet iyi!");
    }
   
    return 0;
}