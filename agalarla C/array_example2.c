#include <stdio.h>
int main(){
    int gradenum;
    int arr[10];
    printf("how many grade do you wish to enter : \n");
    scanf("%d",&gradenum);

    printf("Enter your grades : \n");
    for(int i=0;i<gradenum;i++){
        printf("Grade %d \n",i+1);
        scanf("%d",&arr[i]);
    }
    int sum=0;
    for(int a=0;a<gradenum;a++){
        sum+=arr[a];
    }
    printf("Your grades totam equals to %d",sum);
}