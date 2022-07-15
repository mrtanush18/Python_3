#include <stdio.h>

void fn(int n){
    if(n > 0){
        fn(n-1); 
        printf("%d ",n);
        fn(n-1);
    }
}

int main(){
    fn(4);
    return 0;
}

// o/p : 1 2 1 3 1 2 1 4 1 2 1 3 1 2 1 

/* Explanation :
Refer stack tree 
fn(4) is passed which results in fn(3), print(4), fn(3)
now taking leftmost fn(3) results in f(2), p(3) , f(2) which goes deeper 
till we reach f(0) and print 1 & leftmost fn(1) ends. now move right & print 2, then again f(1) so print 1 as before.
Leftmost fn(2) ends. Then moving right we print 3. Then fn(2). As before we get f(1), p(2) and f(1). So o/p will be 1 2 1.
fn(3) ends. Now rightwards we print 4. Then rightmost fn(3) so print same sequence of nos as above i.e 1 2 1 3 1 2 1
*/