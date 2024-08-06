#include <stdio.h>

int main(){

     // format belirleyiciler % = Görüntülenecek veri türünü tanımlama ve biçimlendirme

    // %c = character
    // %s = string 
    // %f = float 
    // %lf = double
    // %d = integer

    // %.1 = basamak sayısı belirleme
    // %1 = Sol taraftan boşluk bırakma
    // %- = Sağ taraftan boşluk bırakma
    
    float item1 = 5.75;
    float item2 = 10.00;
    float item3 = 100.99;

    printf("Item 1 = %10.2f ₺\n", item1);
    printf("Item 2 = %-10.2f ₺\n", item2);
    printf("Item 3 = %10.2f ₺\n", item3);

    return 0;
}