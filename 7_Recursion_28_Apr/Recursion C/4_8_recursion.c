#include<stdio.h>

void fn1(int n){
    if(n == 0)
    {
        return;
    }
    printf("%d", n);

    fn2(n-2);
    // printf("%d", n);
}

void fn2(int n){
    if(n == 0)
    {
        return;
    }
    printf("%d", n); 

    fn1(++n);  
    // printf("%d", n);
}

void main(){
    fn1(5);
}

// o/p : 5 3 4 2 3 1 1 1 1 3 2 4 3 5

// correct : 5 3 4 2 3 1 2 2 2 3 3 4 4 5