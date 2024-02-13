#include<stdio.h>
long long factorial(long long num){
    long long fact = 1;
    while(num>0){
        fact *= num;
        num--;
    }
    return fact;
}

int main(){
    long long num=0;
    printf("Enter a Number : ");
    scanf("%lld",&num);
    long long fact = factorial(num);
    printf("%lld",fact);
    return 0;
}
