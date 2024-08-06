#include <stdio.h>

int main(){
    const double pi = 3.14159;
    double radius;
    double circumference;
    double area;
    
    printf("\n please enter the radius : ");
    scanf("%lf",&radius);
    circumference = 2 * pi * radius;
    area = pi * radius*radius;
    printf("\n your circumference = %lf",circumference);
    printf("\n your area = %lf",area);

}