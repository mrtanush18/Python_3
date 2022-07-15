#include <stdio.h>

int fn4(int n){
    int x = 1, k;
    if(n == 1){
        return x;
    }
    for(k=1; k<n; k++){
        x = x + fn4(k) * fn4(n-k);
    }
    return x;
}

int main(){
    int x;
    x = fn4(5);
    printf("%d",x);
}

// o/p : 51