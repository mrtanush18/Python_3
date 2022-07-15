#include <stdio.h>

int counter = 0;

int f(int a, int b){
    int c;
    counter++;
    if(b == 3){
        return a*a*a;
    }
    else{
        c = f(a,b/3);
        return c*c*c;
    }
}

int main(){
    f(4,81);
    printf("%d",counter);
    return 0;
}

// o/p : 4