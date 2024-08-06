#include <stdio.h>

int main(){
    int binary=0,num,remain,base=1;
    printf("Enter a number : ");
    scanf("%d",&num);

    while(num<=0){
        printf("Invalid number please enter a positive integer : ");
        scanf("%d",&num);
    }
    while(num>0){
        remain=num%2;
        num=num/2;
        binary=binary + remain*base;
        base = base*10;
    }
    printf("Binary equivalent:%d",binary);

    return 0;
}