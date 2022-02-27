package lib;

public class LinkedListArray {
    int data;
    LinkedListArray next;

    public  LinkedListArray(){
        data = -999;
        next = null;
    }
    public int getData() {
        return data;
    }
    public void setData(int data) {
        this.data = data;
    }
    public LinkedListArray getNext() {
        return next;
    }
    public void setNext(LinkedListArray next) {
        this.next = next;
    }
}
