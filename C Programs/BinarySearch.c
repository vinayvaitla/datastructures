#include<stdio.h>
#include<malloc.h>
/*Program to perform Binary Search on an Array using ADT to store and retrieve Elements.
1. Array should be in the Sorted Fashion
2. Time Complexity is 
   Best Case - O(1)
   Worst Case - O(logn)
   Average Case - O(logn)
*/
struct myArray{
    int total_size;
    int used_size;
    int *ptr;
};

void createArray(struct myArray *arr, int tSize){
    arr->total_size = tSize;
    arr->used_size = 0;
    arr->ptr = (int *)malloc(tSize*sizeof(int));
}

void show(struct myArray *a){
  for(int i=0; i< a->used_size; i++){
    printf("%d\n",(a->ptr)[i]);
  }
}

void setVal(struct myArray *arr, int position, int data){
    (arr->ptr)[position] = data;
    arr->used_size = arr->used_size+1;
}

/*
Logic goes based on low high mid indices. It starts searching with mid and tries to find if the number is greater or lesser than mid
accordingly new low high mid values will be set. This goes on either until the element is found or until the low > high
*/
int binarySearch(struct myArray *arr, int data){
    int low, mid, high;
    high = (arr->used_size);
    low = 0;
    mid = high/2;
    for(int i = 0; i<(arr->used_size)-1; i++){
        mid = (low+high)/2;
        printf("Number of Seaches %d\n",i+1);
        if(low>high){
            printf("Element Not Found!");
            break;
        }
       if ((arr->ptr)[mid] > data){
           high = mid-1;
       }else if  ((arr->ptr)[mid] < data){
           low = mid+1;
       }else{
           printf("Element Found at %d Position",mid+1);
           break;
       }
    }
    
}
// Binary Searching for Sorted Arrays.
void main(){
    struct myArray arrData;
    //Create an Array
    createArray(&arrData, 10 );
    //Set the data to an Array
    setVal(&arrData,0, 5);
    setVal(&arrData,1, 9);
    setVal(&arrData,2, 11);
    setVal(&arrData,3, 17);
    setVal(&arrData,4, 20);
    setVal(&arrData,5, 45);
    setVal(&arrData,6, 78);
    setVal(&arrData,7, 99);
    //Display array Data
    show(&arrData);
    //Calling Binary Search on Array
    binarySearch(&arrData,46);
}