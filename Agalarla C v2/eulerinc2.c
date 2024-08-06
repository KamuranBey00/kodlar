#include <stdio.h>
int fibonacci(int limited);
int main(){
    int limited;
    printf("Enter the top value which does not exceed 4 million : ");
    scanf("%d",&limited);
    if(limited>4000000){
        printf("You gotta be kidding right?\n");
        printf("I'll show you now!\n");
        printf("System32 Deleting...");
        return 0;
    }
    printf("%d",fibonacci(limited));
}
int fibonacci(int limited){
    int a1=0,a2=1,b,i,sum=0;
    for(i=1;i<limited;i++){
        b=a1+a2;
        if(b>4000000)
            break;
        else if(b%2==0)
            sum+=b;
        a1=a2;
        a2=b;
    }
    return sum;
}