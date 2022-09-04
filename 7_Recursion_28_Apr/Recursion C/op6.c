# include <stdio.h>

void fn3(int n, int sum){
    int k = 0, j = 0;

    if(n == 0){
        return;
    }

    k = n % 10;
    j = n/10;
    sum = sum + k;
    fn3(j,sum);
    printf("%d ",k);
}

int main(){
    int a = 2048, sum = 0;
    fn3(a,sum);
    printf("%d ",sum);
}

// o/p : 2 0 4 8 0