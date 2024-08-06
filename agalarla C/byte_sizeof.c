#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define size 10

void initArrayRand(int arr[],int length);   
void dispArr(int arr[],int length);

int main(){
    srand(time(NULL));
    int arr1[size];
    puts("ARRAY before init: ");
    dispArr(arr1,size); //display array (size ı gösteriyor)
    initArrayRand(arr1,size);
    puts("ARRAY after init: ");
    dispArr(arr1,size);//display array (size ı gösteriyor)
    printf("Size of array : %zu Bytes \n",sizeof(arr1));// arrayin ne kadar alan kapladınığını gösteriyor byte deeğrleri için %zu kullanıyoruz
    printf("Size of one element in array : %zu bytes",sizeof(arr1)/size);//arrayin 1 karaterinin kaç yer kapladığını gösteriyor

}   

void initArrayRand(int arr[],int length){
    int i;
    for(i=0;i< length;i++){
        arr[i]=rand()%100 + 1;
    }
}
void dispArr(int arr[],int length){
    int i;
    for(i=0;i<length-1;i++){
        printf("%d, ",arr[i]);
    }

    printf("%d ,",arr[i]);
    puts("");
}