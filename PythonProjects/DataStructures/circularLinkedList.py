"""
Program to
1. create Linked List
2. Add a node if Linked List is empty
3. Append a node to the end of the linked list
4. Insert a node at any given position
5. delete a node at any given position
6. traverse and print data in Linked List
Time Complexity - Best O(1), Worst O(n) for Insertion and Deletion
"""
from lib.linkedListArray import LinkedListArray


def display_array(head):
    """
    This method prints the Linked List
    :param head:
    :return head:
    """
    ptr = head
    while True:
        print(ptr.get_data(), end=",")
        ptr = ptr.get_next_addr()
        if ptr == head:
            break
    print()


def append(head, value):
    """
    This method checks if the list is empty if it is empty it adds a node else appends the node to the existing list
    :param head:
    :param value:
    :return head:
    """
    ptr = head
    new_node = LinkedListArray()
    new_node.set_data(value)

    # Inserting at the 1st position if list is empty
    if ptr.get_data() == -999:
        new_node.set_next_addr(new_node)
        head = new_node
    else:
        while ptr.get_next_addr() is not None and ptr.get_next_addr() != head:
            ptr = ptr.get_next_addr()
        new_node.set_next_addr(head)
        ptr.set_next_addr(new_node)
    return head


def insert_node_at(head, pos, value):
    """
    This method inserts a node any given position
    :param head:
    :param pos:
    :param value:
    :return head:
    """
    ptr = head
    new_node = LinkedListArray()
    new_node.set_data(value)
    # logic to insert the node at position 1
    if pos == 1:
        while ptr.get_next_addr() is not None and ptr.get_next_addr() != head:
            ptr = ptr.get_next_addr()
        new_node.set_next_addr(head)
        ptr.set_next_addr(new_node)
        head = new_node
    else:
        # logic to insert at any other position
        for i in range(0, pos-2):
            if ptr.get_next_addr() == head:
                print("Cannot Insert in that position. Hence appending at the last")
                break
            ptr = ptr.get_next_addr()
        new_node.set_next_addr(ptr.get_next_addr())
        ptr.set_next_addr(new_node)
    return head


def delete_at_index(head, pos):
    """
    This method deletes the element from the given position
    :param head:
    :param pos:
    :return head:
    """
    ptr = head
    back = head
    forward = head.get_next_addr()
    # logic to delete the element from position 1
    if pos == 1:
        while ptr.get_next_addr() is not None and ptr.get_next_addr() != head:
            ptr = ptr.get_next_addr()
        ptr.set_next_addr(forward)
        head = forward
        back = None
    else:
        # logic to delete the element from any other position
        for i in range(0, pos - 2):
            if forward.get_next_addr() == head:
                print("Cannot Delete in that position. Hence deleting at the last")
                break;
            back = back.get_next_addr()
            forward = forward.get_next_addr()
        back.set_next_addr(forward.get_next_addr())
        forward = None
    return head


array = LinkedListArray()
# Adding data to the Linked List
array = append(array, 10)
array = append(array, 20)
array = append(array, 30)
array = append(array, 40)
# Display the Linked List
display_array(array)
# Insert Node at any position
array = insert_node_at(array, 1, 90)
display_array(array)
# Delete the Node from any position
array = delete_at_index(array, 6)
display_array(array)

