#include<stdio.h>
#include<ctype.h>
int main(){
    char unit;
    float temp;
    printf("\n Please enter your temperature measurement (F) or (C) : ");
    scanf("%c",&unit);

    if (unit=='C'){
        printf("\n Enter your temperature in celcius kind : ");
        scanf("%f",&temp);
        temp=(temp*9/5)+32;
        printf("\n temperature in fahrenheit kind : %.1f",temp);

    }
    else if(unit=='F'){
        printf("\n Enter your temperature in fahrenheit kind : ");
        scanf("%f",&temp);
        temp=((temp-32)*5)/9;
        printf("\n temperature in celcius kind : %.1f",temp);

    }
    else{
        printf("\n %c is not a tempereature measurment ",unit);
    }
    return 0;
}