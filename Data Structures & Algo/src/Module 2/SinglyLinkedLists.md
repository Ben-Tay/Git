## LinkedLists
Linked lists are also known as a `Linked Data Structure`
* As opposed to an array which requires `contiguous` memory, linked data structures stores data `anywhere` in memory
* It then connects the data by keeping `references/pointers/relationships` between the locations, allowing a more flexible approach to data storage to better accomodate dynamic nature of `linked DS`

There are 3 variables of Linkedlists that implements the List ADT as follows:
* `Singly-Linked Lists`
* `Doubly-Linked Lists`
* `Circularly-Linked Lists`

#### Learning Objectives

Students will:
* Learn the basics of linked data structures by learning about the Singly-Linked List, an implementation of the List ADT.
* Practice the ideas of iteration and recursion on Linked Lists both conceptually and through code.
* Learn about variations of the Linked List concept: `Doubly-Linked Lists and Circularly-Linked Lists`.

## Singly-Linked Lists (SLL)
* As compared to ArrayLists, LinkedLists are considered `dynamic` because they `do not require resizing` operations & can expand indefinitely & they do not store data contiguously as well.
* In a way, Linkedlists are used to overcome some of the drawbacks of arrays
* A linked list data structure is a `collection of nodes that stores data` which can be put anywhere in memory
* These nodes have very `different addreseses in memory` and are linked through pointers from one node to another to keep track of who is in the list
    * Ie. the memory addresses of the nodes are not sequential in order
* Nodes in a Singly Linked List only has a `single pointer` to the next node on the list
* Every linkedlist must have a `HEAD` pointer which points to the first node in the list 

#### Example
How SLL may look in memory due to noncontiguous locations:
* Data 2, Data 4, Data 3, Data 1 (Head)

How SLL Looks in diagram
* Data 1 => Data 2 => Data 3 => Data 4
* Each => represents what each node points to

Empty SSL (Head is null)
* Indicates the list is empty

## The Node Class
> Has to be made `private` so that other external classes outside cannot access, only SLL class shd be able to access

Outer class: `SinglyLinkedList` has direct access to private inner node class members `int data` and `Node next`. 
```sh
public class SinglyLinkedList {
    # A node is an object that contains data + reference to another node object
    private static class Node {
        # Assume data type is int but this is dynamic & not fixed
        private int data;
        private Node next;   # reference to next node object

        private Node(int data, Node next) {
            this.data = data;
            this.next = next;
        }
        # Create overloaded constructor that does not have a next node (constructor chaining)
        private Node (int data) {
            this(data, null);
        }

        # Return toString of data in Node
        public String toString() {
            return Integer.toString();
        }
    }
}
```
## SLL class 
```sh
public class SinglyLinkedList {
    # Node class omitted for brevity
    private Node head;
    # Easy way to add new node w/o having to traverse to end of linkedlist
    public void addToFront(int data) {
        # Step 1: Create the new node
        Node newNode = new Node(data);
        # Must be done in correct order

        # Step 2: Point the next reference to where the head is pointed to
        newNode.next = head; 
        
        # Step 3: Point head to where the new node is located
        head = newNode;  
        # New node becomes the new head and u can still access rest of the list
    } 

    # Iterate thru the list to print out the SLL data
    public String toString() {
        # Step 1: Create empty string to print final list
        String answer = "";
        # Step 2: Keep track of node we looking at in list
         # current is the pointer that moves thru the SLL
        Node current = head;
        # Step 3: Iterate thru LL while current not null, as last node in linked list points to null (next)
        while (current != null) {
            # Step 4: append node's data to answer string
            answer += current + "";
            current = current.next; # moves to next node
        }
    }
}
```
> When reassigning pointers, need to be careful so that we do `not lose` access to the rest of the list