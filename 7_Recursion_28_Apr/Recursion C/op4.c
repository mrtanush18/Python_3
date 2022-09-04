#include <stdio.h>

void fn(int n){
    if(n <= 1){
        printf("%d ",n);
    }
    else{
        fn(n/2);
        printf("%d ",n%2);
    }
}

void main(){
    fn(173);
}

// o/p : 1 0 1 0 1 1 0 1