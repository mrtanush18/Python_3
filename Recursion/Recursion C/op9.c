#include <stdio.h>

void gate(int n){
    if(n < 1){
        return;
    }
    gate(n-1);
    gate(n-3);
    printf("%d ",n);
}

int main(){
    gate(6);
}

// o/p : 1 2 3 1 4 1 2 5 1 2 3 6