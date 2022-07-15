// How to pass array to a function
// Don't forget to put [] while declaring array & in function(arr[]), 
// import java.util.*;
public class Array{
    public static void main(String[] args){
        // Scanner sc = new Scanner(System.in);
        
        int a[] = new int[5];
        a[0] = 1;
        printArray(a);
    }

    public static void printArray(int arr[]){
        for(int i = 0 ; i < arr.length ; i++){
            System.out.print(arr[i] + " ");
        }
    }


}