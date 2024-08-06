#include <stdio.h>
int main(){
    int age;
    printf("Enter your age : ");
    scanf("%d",&age);

    if(age>=18){
        printf("You registered our course ! ");
    }
    else if(age<0){
        printf("If you are not born you cannot register ! ");
    }
    else if (age==0){
        printf("You can not register because you already born ! ");
    }
    else{
        printf("You have to be over 18 years old if you want to register this course ! ");
    }
    
    return 0;
}