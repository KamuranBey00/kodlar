#include <stdio.h>

int main(){
    int num,n=0,max;
    int array[6];
    printf("How many elemetns do you wish to enter (maximum 6) : \n");
    scanf("%d",&num);

    printf("Enter your elements :\n ");
    for(n=0;n<num;n++){
        printf("Element %d :",n+1);
        scanf("%d",&array[n]);
    }
    max=array[0];
    for(int i=0;i<num;i++){
        if(max<array[i]){
            max = array[i];
        }
    }
    printf("largest element in your array is :%d \n",max);

    int sum = 0;
    for(int i=0; i < num;i++){
        sum+=array[i];
    }

    printf("your total elemets is =%d\n",sum);
}

