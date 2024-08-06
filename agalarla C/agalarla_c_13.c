#include <stdio.h>
#include <stdbool.h>  
 
int main(){
 
    // mantıksal operatörler = ! (NOT) koşulları tersine çevirirken kullanılır.
    
    bool sunny = false;
    
    if(!sunny){
        printf("\nHava bulutlu!");
    }
    else{
        printf("\nHava gunesli!");
    }

    return 0;
}