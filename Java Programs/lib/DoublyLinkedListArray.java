package lib;

public class DoublyLinkedListArray {
    int data;
    DoublyLinkedListArray next;
    DoublyLinkedListArray prev;

    public  DoublyLinkedListArray(){
        data = -999;
        next = null;
        prev = null;
    }
    public DoublyLinkedListArray getPrev() {
        return prev;
    }
    public void setPrev(DoublyLinkedListArray prev) {
        this.prev = prev;
    }
    public int getData() {
        return data;
    }
    public void setData(int data) {
        this.data = data;
    }
    public DoublyLinkedListArray getNext() {
        return next;
    }
    public void setNext(DoublyLinkedListArray next) {
        this.next = next;
    }
}
