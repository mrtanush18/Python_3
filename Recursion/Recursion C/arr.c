// Program to print the largest and second largest element of the array.

#include <stdio.h>

void main(){

int arr[100],size,largest;

printf("Enter size of array: ");
scanf("%d",&size);

printf("Enter elements of array: ");
for(int i = 0 ; i < size ; i++){
    scanf("%d",&arr[i]);
}
largest = arr[0];

for(int i = 1 ; i < size ; i++){
    if(arr[i]>largest){
        largest = arr[i];
    }
}

printf("Largest is %d",largest);
}

/* o/p :
Enter size of array5
Enter elements of array60
-70
30
25
10
Largest is 60
*/

// https://www.javatpoint.com/passing-array-to-function-in-c