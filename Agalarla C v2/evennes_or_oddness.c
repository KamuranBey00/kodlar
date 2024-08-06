#include <stdio.h>

int main(){
    int num;
    printf("Enter a positive integer number : ");
    scanf("%d",&num);
    if(num<0){
        printf("I just told you enter a POSITIVE integer.");
        return 0;
    }
    if(num>0){
        if(num%2==0){
            printf("Even");
        }
        else{
            printf("Odd");
        }
    }
    return 0;
}