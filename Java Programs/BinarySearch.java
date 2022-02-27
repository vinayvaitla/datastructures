import lib.SingleArray;
/*
Program to perform Binary Search on an Array using ADT to store and retrieve Elements.
1. Array should be in the Sorted Fashion
2. Time Complexity is 
   Best Case - O(1)
   Worst Case - O(logn)
   Average Case - O(logn)
*/
public class BinarySearch {
    public static void main(String[] args) {
        //Instantiation of Class
        SingleArray myArray = new SingleArray(10);
        //Set Array Elements
        myArray.setData(5);
        myArray.setData(9);
        myArray.setData(11);
        myArray.setData(17);
        myArray.setData(20);
        myArray.setData(45);
        myArray.setData(78);
        myArray.setData(98);
        //Display array Data
        myArray.showArray();
        //Instantiating Parent Class
        BinarySearch bs = new BinarySearch();
        //Calling Binary Search on Array
        int foundPos = bs.binarySearch(myArray,46);
        if (foundPos!=-1)
        System.out.println("Element Found at:"+foundPos);
        else
        System.out.println("Element Not Found.");
    }
   //Method to search an element in a given array
   int binarySearch(SingleArray myArray, int data){
        //Logic goes based on low high mid indices. It starts searching with mid and tries to find if the number is greater or lesser than mid
        //accordingly new low high mid values will be set. This goes on either until the element is found or until the low > high
        int low,high,mid;
        low = 0;
        high = myArray.getUsedSize();
        
        while(low<=high){
            mid = (low+high)/2;
            if(data<myArray.getData()[mid]){
                high = mid-1;
            }else if (data > myArray.getData()[mid]){
                low = mid+1;
            }else{
               return mid+1;
            }
        }
        return -1;
    }
}