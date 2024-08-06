#include <stdio.h>

int main(){
    int lim,factorial=1;
    printf("Enter limit of factorial : ");
    scanf("%d",&lim);

    int i = lim;
    while(i>0){
        factorial*=i;
        i--;
    }
    printf("%d ! is %d\n",lim,factorial);
    return 0;
}