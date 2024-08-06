//#include <stdio.h>
//void naturalnum(int num);
//int main(){
//    int num;
//    printf("Enter the number: ");
//    scanf("%d",&num);
//    naturalnum(num);
//
//}
//void naturalnum(int num){
//    int i,sum;
//    sum=0;
//    for(i=1,i<num;i++){
//        if(i%3==0) || (i%5==0)
//            sum = sum+i;
//    }
//    printf("%d",num);
//}

#include <stdio.h>

void naturalnum(int num);

int main() {
    int num;
    printf("Enter the number: ");
    scanf("%d", &num);
    naturalnum(num);
    return 0;
}

void naturalnum(int num) {
    int i, sum;
    sum = 0;
    for (i = 1; i < num; i++) {
        if ((i % 3 == 0) || (i % 5 == 0))
            sum = sum + i;
    }
    printf("Sum of natural numbers less than %d and divisible by 3 or 5 is: %d", num, sum);
}
