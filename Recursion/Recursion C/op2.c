#include <stdio.h>

int fn2(int n, int k){
    if(n == 0){
        return 0;
    }
    else if(n%2){
        return fn2(n/2,2*k)+k;
    }
    else{
        return fn2(n/2,2*k)-k;
    }
}

int main(){
    printf("%d ",fn2(20,1));
    return 0;
}

// o/p : 9