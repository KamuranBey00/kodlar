#include <stdio.h>

int main() {
    int value = 42;        // Bir tam sayı değişkeni tanımla
    int *p = &value;       // İşaretçi p, value değişkeninin adresini tutar

    printf("Değer: %d\n", value);                // 42
    printf("İşaretçinin gösterdiği değer: %d\n", *p);  // 42
    printf("İşaretçinin tuttuğu adres: %p\n", (void *)p);  // İşaretçinin tuttuğu adres (hexadecimal formatta)
    printf("İşaretçinin adresi: %p\n", (void *)&p);      // İşaretçinin kendisinin adresi (hexadecimal formatta)

    return 0;
}
