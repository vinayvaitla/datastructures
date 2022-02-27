#include <stdio.h>
#include <malloc.h>

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
struct Node
{
    int data;
    struct Node *next;
};
//This method checks if the list is empty if it is empty it adds a node else appends the node to the existing list
struct Node *append_node(struct Node *head, int value)
{
    if (head == 0)
    {
        // Inserting at the 1st position if list is empty
        struct Node *new_node = (struct Node *)malloc(sizeof(struct Node));
        new_node->data = value;
        new_node->next = new_node;
        return (new_node);
    }
    else
    {
        struct Node *ptr = head;
        while (ptr->next != head)
        {
            ptr = ptr->next;
        }
        struct Node *new_node = (struct Node *)malloc(sizeof(struct Node));
        new_node->data = value;
        new_node->next = head;
        ptr->next = new_node;
        return head;
    }
}
//This method inserts a node any given position
struct Node *insert_node_at(struct Node *head, int position, int value)
{
    struct Node *ptr = head;
    //logic to insert the node at position 1
    if (position == 1)
    {   
        while(ptr->next != head){
            ptr=ptr->next;
        }
        struct Node *new_node = (struct Node *)malloc(sizeof(struct Node));
        new_node->data = value;
        new_node->next = head;
        ptr->next = new_node;
        head = new_node;
    }
    //logic to insert at any other position
    else
    {
        for (int i = 0; i < position - 2; i++)
        {
            if (ptr->next == head)
            {
                printf("Cannot Insert in that position. Hence appending at the last\n");
                break;
            }
            ptr = ptr->next;
        }

        struct Node *new_node = (struct Node *)malloc(sizeof(struct Node));
        new_node->data = value;
        new_node->next = ptr->next;
        ptr->next = new_node;
    }
    return head;
}

//This method deletes the element from the given position
struct Node *delete_element(struct Node *head, int position)
{
    struct Node *back = head;
    struct Node *ptr=head;
    struct Node *forward = head->next;
    //logic to delete the element from position 1
    if (position == 1)
    {
        while(ptr->next != head){
            ptr = ptr-> next;
        } 
        ptr->next = forward;
        head = forward;
        
        free(back);
    }
    //logic to delete the element from any other position
    else
    {

        for (int i = 0; i < position - 2; i++)
        {
            if (forward->next == head)
            {
                printf("Cannot Delete in that position. Hence deleting at the last\n");
                break;
            }
            back = back->next;
            forward = forward->next;
        }
        back->next = forward->next;
        free(forward);
    }
    return head;
}
//This method prints the Linked List
void display_array(struct Node *head)
{
    struct Node *ptr = head;
    do{
        printf("%d - ", ptr->data);
        ptr = ptr->next;
    }
    while (ptr != head);
    
    printf("\n");
}
//Main Method
void main()
{
    struct Node *array = NULL;
    //Adding data to the Linked List
    array = append_node(array, 10);
    array = append_node(array, 20);
    array = append_node(array, 30);
    array = append_node(array, 40);
    //Display the Linked List
    display_array(array);
    //Insert Node at any position
    array = insert_node_at(array, 7, 90);
    display_array(array);
    //Delete the Node from any position
    array = delete_element(array, 6);
    display_array(array);
}