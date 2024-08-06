#include <stdio.h>

int findMax(int x ,int y){
    return (x>y)? x : y;
}

int main(){

    // ternary operator = bir değeri döndürürken if else yerine kullanılacak kısa yol
    // (koşul) ? doğruysa değer : yanlışsa değer
    int max = findMax(3,4);

    printf("%d",max);
    return 0;
}