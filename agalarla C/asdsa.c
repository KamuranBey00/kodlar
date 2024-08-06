#include<stdio.h>
int main(){
    int arr[]={0,1,2,3,4,5,6};
    int *p;
    p=&arr[0];
    printf("%d\n",*p);
    printf("%d\n",p);
    printf("%p\n",*p);
    printf("%p\n",p);
    printf("%d\n",&p);
    printf("%p\n",&p);
    

}