package lib;
public class SingleArray {

    public SingleArray(int tSize){
      this.totalSize = tSize;
      this.usedSize = 0;
      this.data = new int[tSize];
    }

    int totalSize,  usedSize;
    int [] data;

    public void setData(int data){
      this.data[this.usedSize]=data;
      this.usedSize++;
    }

    public void showArray(){
        for(int i=0;i<usedSize;i++){
            System.out.println(this.data[i]);
        }
    }
    public int getTotalSize(){
        return this.totalSize;
    }

    public int getUsedSize(){
        return this.usedSize;
    }

    public int[] getData(){
        return this.data;
    }
}
