
import java.util.*;
class bubble{
    public static void main(String[] args) {
        new bubble().solution();
    }
    void solution(){
        int[] arr = create();
        arr = sort(arr);
        print(arr);
    }
    int randomnum(){
        return (int)(Math.random()*10)+1;
    }
    int[] create(){
        int[] arr = new int[10];
        for(int i=0; i<arr.length; i++){
            arr[i] = randomnum();
            for(int j =0; j<i; j++){
                if(arr[i] == arr[j]){i--;}
            }
        }
        return arr;
    }
    int[] sort(int[] arr){
        for(int i=0; i<arr.length; i++){
            for(int j =0; j<arr.length-1; j++){
                if(arr[j] > arr[j+1]){
                int t = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = t;
                }
            }
        }    
        return arr;
    }
    void print(int[] arr){
        for(int i =0; i<arr.length; i++){
            System.out.println(arr[i]);
        }
    }
}


