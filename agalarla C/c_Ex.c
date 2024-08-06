#include<stdio.h>
int main(){
    int arr[9]={34,56,54,32,67,89,90,30,21};
    for(int i=0;i<9;i++){
        printf("%d,",arr[i]);    
    }
    printf("\n");
    for(int i=8;i>=0;i--){
        printf("%d,",arr[i]);
    }
}