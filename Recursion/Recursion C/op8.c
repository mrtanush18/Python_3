#include <stdio.h>

void fn5(int n){
    if(n == 0){
        return;
    }
    printf("%d ",n);
    fn6(n-2);
    printf("%d ",n);
}

void fn6(int n){
    if(n == 0){
        return;
    }
    printf("%d ",n);
    fn5(++n);
    printf("%d ",n);
}

int main(){
    fn5(5);
}

// o/p :  5 3 4 2 3 1 2 2 2 3 3 4 4 5