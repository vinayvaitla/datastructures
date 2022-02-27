import lib.LinkedListArray;

/*
Program to 
1. create Linked List
2. Add a node if Linked List is empty
3. Append a node to the end of the linked list
4. Insert a node at any given position
5. delete a node at any given position
6. traverse and print data in Linked List
Time Complexity - Best O(1), Worst O(n) for Insertion and Deletion
*/
public class CircularLinkedList {
    //This method checks if the list is empty if it is empty it adds a node else appends the node to the existing list
    LinkedListArray append(LinkedListArray head, int value) {
        LinkedListArray ptr = head;
        LinkedListArray newNode = new LinkedListArray();
        newNode.setData(value);
        
        // Inserting at the 1st position if list is empty
        if (ptr.getData() == -999) {
            
            head = newNode;
        } else {
            // System.out.println(ptr.getData());
            while (ptr.getNext() != null && ptr.getNext()!= head) {
                
                ptr = ptr.getNext();
            }
            newNode.setNext(head);
            ptr.setNext(newNode);
        }
        return head;
    }
    //This method prints the Linked List
    void displayArray(LinkedListArray head) {
        LinkedListArray ptr = head;
        do{
            System.out.print(ptr.getData() + "-");
            ptr = ptr.getNext();
        }
        while (ptr != null && ptr!= head);
        System.out.println();
    }
    //This method inserts a node any given position
    LinkedListArray insertNodeAt(LinkedListArray head, int pos, int value) {
        LinkedListArray ptr = head;
        LinkedListArray newNode = new LinkedListArray();
        newNode.setData(value);
        
        //logic to insert the node at position 1
        if (pos == 1) {
            while (ptr.getNext() != null && ptr.getNext()!= head) {
                
                ptr = ptr.getNext();
            }
            newNode.setNext(head);
            ptr.setNext(newNode);
            head = newNode;
        } else {
            //logic to insert at any other position
            for (int i = 0; i < pos - 2; i++) {
                if (ptr.getNext() == head) {
                    System.out.println("Cannot Insert in that position. Hence appending at the last");
                    break;
                }
                ptr = ptr.getNext();
            }
            newNode.setNext(ptr.getNext());
            ptr.setNext(newNode);
        }
        return head;
    }
    //This method deletes the element from the given position
    LinkedListArray deleteAtIndex(LinkedListArray head, int pos){
        LinkedListArray back = head;
        LinkedListArray ptr = head;
        LinkedListArray forward = head.getNext();
        //logic to delete the element from position 1
        if(pos==1){
            while (ptr.getNext() != null && ptr.getNext()!= head) {
                
                ptr = ptr.getNext();
            }
            ptr.setNext(forward);
            head = forward;
            back = null;
        }else{
            //logic to delete the element from any other position
            for (int i = 0; i < pos - 2; i++)
            {
                if (forward.getNext() == head)
                {
                    System.out.println("Cannot Delete in that position. Hence deleting at the last");
                    break;
                }
                back = back.getNext();
                forward = forward.getNext();
            }
            back.setNext(forward.getNext()); 
            forward = null;
        }

        return head;
    }
    //Main Method
    public static void main(String[] args) {
        CircularLinkedList dataList = new CircularLinkedList();
        LinkedListArray array = new LinkedListArray();
        //Adding data to the Linked List
        array = dataList.append(array, 10);
        array = dataList.append(array, 20);
        array = dataList.append(array, 30);
        array = dataList.append(array, 40);
        //Display the Linked List
        dataList.displayArray(array);
        //Insert Node at any position
        array = dataList.insertNodeAt(array, 6, 90);
        dataList.displayArray(array);
        //Delete the Node from any position
        array = dataList.deleteAtIndex(array, 5);
        dataList.displayArray(array);
    }
}
