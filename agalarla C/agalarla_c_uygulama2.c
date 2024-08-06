#include <stdio.h>
#include <math.h>

int main(){
    double A;
    double B;
    double C;

    printf("\n Please enter side A : ");
    scanf("%lf",&A);
    printf("\n Please enter side B : ");
    scanf("%lf",&B);
    C = sqrt(A*A+B*B);
    printf("Side C's length = %.2lf",C);

    return 0;

}