# include <stdio.h>

int fn2(int n){
    static int i = 1;

    if(n >= 5){
        return n;
    }
    n = n + i;
    i++;
    return fn2(n);
}

int main(){
    int x;
    x = fn2(1);
    printf("%d",x);
    return 0;
}

// o/p : 7