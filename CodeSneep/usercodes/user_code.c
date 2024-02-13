#include<stdio.h>

int factorial(long long num){
   long long fact=1;
   while(num){
       fact*=num--;

   }
   return fact;

}

    
    
    