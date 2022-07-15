#include <stdio.h>

int fact(int);  // prototype

int main(){
    int n,f;
    printf("Enter number: ");
    scanf("%d",&n);
    f = fact(n);
    printf("Factorial = %d",f);
}

int fact(int n){
    if(n == 0){
        return 0;
    }
    else if(n == 1){
        return 1;
    }
    else{
        return n*fact(n-1);
    }
}

// o/p : Enter number: 6
// Factorial = 720