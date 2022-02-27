#include<stdio.h>
#include<malloc.h>

struct myarray{

    int total_size;
    int used_size;
    int *ptr;
};

void createArray(struct myarray *a, int tSize, int uSize){
  a->total_size = tSize;
  a->used_size = uSize;
  a->ptr = (int *)malloc(tSize*sizeof(int));
}

void show(struct myarray *a){
  for(int i=0; i< a->used_size; i++){
    printf("%d\n",(a->ptr)[i]);
  }
}

void setVal(struct myarray *a){
    int n;
    for (int i=0; i< a->used_size; i++){
        printf("Enter element %d",i);
        scanf("%d", &n);
        (a->ptr)[i] = n;
    }
}

void main(){
  struct myarray marks;
  createArray(&marks,10,2);
  printf("We are running setVal now \n");
  setVal(&marks);

  printf("We are running show now\n");
  show(&marks);

}