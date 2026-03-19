import java.util.*;
class Main {
    public static int search(int[] arr, int k) {
        int low=0;
        int high=arr.length-1;
        while(low<=high){
            int mid=low+(high-low)/2;
            if(arr[mid]==k){
              return mid;
            } 
            if(arr[low]<=arr[mid]){
                if(k>=arr[low] && k<arr[mid]){
                    high=mid-1;
                }
                else{
                    low=mid+1;
                }
            }
            else{
                if(k<=arr[high] && k>arr[mid]){
                    low=mid+1;
                }
                else{
                    high=mid-1;
                }
            }
        }
        return -1;
    }
       public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter size of an array");
        int length=sc.nextInt();
        int[] arr=new int[length];
        System.out.println("Enter array elements:");
        for(int i=0;i<length;i++){
            arr[i]=sc.nextInt();
        }
        System.out.print("Enter Target");
        int target=sc.nextInt();
        System.out.print(search(arr,target));
       }
    
}
