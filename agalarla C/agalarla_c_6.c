#include <stdio.h>

int main(){
    /* Atama operatörleri = değişkenlere değer atamak için kullanılan simgelerdir
    */
    
    int x = 10;
    
    //x = x + 2;
    x += 2;
    
    //x = x - 3;
    x -= 3;
    
    //x = x * 5;
    x *= 5;
    
    //x = x / 5;
    x /= 5;
    
    //x = x % 2
    x %= 2;
    
    printf("%d", x);
    
    return 0;
}