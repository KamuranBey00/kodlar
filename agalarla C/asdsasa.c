#include<stdio.h>
#define N 5
int main(){
    int a[N],*p;
    printf("Enter %d elemests in in the array \n ",N);
    for(p=a;p<=a+N-1;p++){
        scanf("%d",p);
    }
}