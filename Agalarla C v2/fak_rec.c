#include<stdio.h>

int fak(int num){
    if (num==1 || num==0){
        return 1;
    }
    else{
        return num*fak(num-1);
    }
}




int main(){
    int num;
    printf("Enter a num : ");
    scanf("%d",&num);
    printf("%d fakoriyel = %d",num,fak(num));
}