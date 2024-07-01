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

    # If adding to the back, while loop changes a bit
    public void addToBack(int data) {
        # handle edge case where linkedlist is empty
        if (head == null) {     
            head = new Node(data);
        } else {
            Node current = head;
            while(current.next != null) {
                current = current.next;
            }
            # Reset the reference for current.next to the new node (to ensure we stop at the end)
            current.next = new Node(data);
        }
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
        return answer;
    }
}
```
> When reassigning pointers, need to be careful so that we do `not lose` access to the rest of the list
## Basic Remove operations in SLL

# handle edge case where linkedlist is empty> Head will be reassigned to the next node
* Eg: U removed data 1 from the front, so head will now be reassigned to data 2 in the linked list
```sh
public class SinglyLinkedList {
    # other class details omitted for brevity
    public void removeFromFront() {
        head = head.next;
    }
}
```
> Unnecessary to explicitly delete previous node that was the `head` as Java has garbage collection
* `GC` essentially frees up any memory that is no longer accessible, so once head is removed from data 1, it is no longer accessible to access the old head 
* Does not matter if old head still points to next node in linkedlist, as nothing can ever reach it `anymore`

#### Remove from back
* Modifications to loop are required
```sh
public class SinglyLinkedList {
    # other class details omitted for brevity
    public void removeFromBack() {
        if (head == null) {
            # handle edge case where list is empty
            return null; # can throw exception too
        } else if (head.next == null) {
            # head is the only current node
            # removing from the back = getting rid of head
            head == null;  #hence we just need to make head null
        } else {
            Node current = head;
            while (current.next.next != null) {
                current = current.next;
            }
            current.next = null;
        }
    }
```
> Explaining else block above:
* Given 3 nodes: Node 1 (head & current points to node 1),2,3
* current.next = node 2, current.next.next = node 3 
* Basically while `(current.next.next != null)  ==> last node 3 is not null`
* We then set `current = current.next` => current points to node 2 now
* We then set `current.next = null`, so meaning that node 2 is now `disengaged from node 3` which was the last node, in a way removing node 3 from the linkedlist
* Node 2 becomes new last node 

## Optimizing Linked Lists
> We can introduce a `size` variable to keep track of no.of nodes in linked list 
* Increment size when `adding` and decrement size when `removing`
* Can then use `size` variable to handle edge cases as mentioned in codes above

## Optimizing with `Tail` reference
> We can also introduce a pointer to the last node in the linkedlist also known as the `tail`.
* Adding to the back becomes `O(1)` time complexity because we do not have to iterate the linkedlist from the front to add to the back `O(n)`.
    * Set the `current` node's`.next` pointer and the `tail` pointer to the new last node 
* Does not solve the problem of `removing` from the back as we still need access to the 2nd last node `O(n)` to traverse thru linked list
* However, it also adds a few edge cases:
1. Size 0 (List is empty)
    * When list is empty - both `head & tail` must be set to null
2. Size 1:
    * Add To Front
    * Remove From Front
    * When list = size 1, both `head and tail` must point to same node

## Adding Generic Types
* In node class above, only `int data` is able to be stored, to make linkedlists flexible we introduce `generic types` to make it dynamic to store any kind of data user wants
```sh
public class SinglyLinkedList<T> {
    private static class Node<T> {
        private T data;
        private Node<T> next;

        private Node(T data, Node<T> next) {
            this.data = data;
            this.next = next;
        }
        # Overloaded constructor when there is no next node
        private Node(T data) {
            this(data, null); # constructor chaining
        }
    }
};
```
## SLL Implementation
```sh
import java.util.NoSuchElementException;

/**
 * Your implementation of a Singly-Linked List.
 */
public class SinglyLinkedList<T> {

    /*
     * Do not add new instance variables or modify existing ones.
     */
    private SinglyLinkedListNode<T> head;
    private SinglyLinkedListNode<T> tail;
    private int size;

    /*
     * Do not add a constructor.
     */

    /**
     * Adds the element to the front of the list.
     *
     * Method should run in O(1) time.
     *
     * @param data the data to add to the front of the list
     * @throws java.lang.IllegalArgumentException if data is null
     */
    public void addToFront(T data) {
        // WRITE YOUR CODE HERE (DO NOT MODIFY METHOD HEADER)!
        
        if (data == null) {
            throw new IllegalArgumentException("Data cannot be null.");
        }
        
        SinglyLinkedListNode<T> newNode = new SinglyLinkedListNode<>(data);

        if (size == 0) {
            head = newNode;
            tail = newNode;
        } else {
            newNode.setNext(head); // make the next node of the new head the old head
            head = newNode; // make the head the new Node since adding to the front
        }
        size++;
            
    }

    /**
     * Adds the element to the back of the list.
     *
     * Method should run in O(1) time.
     *
     * @param data the data to add to the back of the list
     * @throws java.lang.IllegalArgumentException if data is null
     */
    public void addToBack(T data) {
        // WRITE YOUR CODE HERE (DO NOT MODIFY METHOD HEADER)!

        if (data == null) {
            throw new IllegalArgumentException("Data cannot be null.");
        }

        SinglyLinkedListNode<T> newNode = new SinglyLinkedListNode<>(data);

        if (size == 0) {
            head = newNode;
            tail = newNode;
        } else {
            tail.setNext(newNode); // change old tail.next to new node
            tail = newNode; // make the new node the new tail
        }
        size++;
    }

    /**
     * Adds the element to the specified index.
     *
     * Must be O(1) for indices 0 and size and O(n) for all other cases.
     * 
     * ASSUMPTIONS:
     * - You may assume that the index will always be valid [0, size]
     * - You may assume that the data will not be null
     *
     * @param index the index to add the new element
     * @param data  the data to add
     */
    public void addAtIndex(int index, T data) {
        // WRITE YOUR CODE HERE (DO NOT MODIFY METHOD HEADER)!  
        // Create a new node with the given data
        SinglyLinkedListNode<T> newNode = new SinglyLinkedListNode<>(data);

        if (index == 0) { // Adding at the front
            newNode.setNext(head);
            head = newNode;
            if (size == 0) { // If the list was empty, update the tail
                tail = newNode;
            }
        } else if (index == size) { // Adding at the end
            if (size == 0) { // If the list was empty, update both head and tail
                head = newNode;
                tail = newNode;
            } else {
                tail.setNext(newNode);
                tail = newNode;
            }
        } else { // Adding at any other index
            SinglyLinkedListNode<T> current = head;
            // Traverse to the node just before the specified index
            for (int i = 0; i < index - 1; i++) {
                current = current.getNext();
            }
            // Insert the new node in between
            newNode.setNext(current.getNext());
            current.setNext(newNode);
        }

        // Increment the size of the list
        size++;
    }

    /**
     * Removes and returns the first data of the list.
     *
     * Method should run in O(1) time.
     *
     * @return the data formerly located at the front of the list
     * @throws java.util.NoSuchElementException if the list is empty
     */
    public T removeFromFront() {
        // WRITE YOUR CODE HERE (DO NOT MODIFY METHOD HEADER)!
        if (size == 0) {
            throw new NoSuchElementException("Cannot remove from an empty linkedlist");
           
        } 
        
        T data = head.getData(); // retrieve the data of the head to return back
        
        if (size == 1) {
            head = null;
            tail = null;
        } else {
            head = head.getNext(); // tail does not have to be updated 
        }
        
        size--;
        return data;
            
    }

    /**
     * Removes and returns the last data of the list.
     *
     * Method should run in O(n) time.
     *
     * @return the data formerly located at the back of the list
     * @throws java.util.NoSuchElementException if the list is empty
     */
    public T removeFromBack() {
        // WRITE YOUR CODE HERE (DO NOT MODIFY METHOD HEADER)!
        if (size == 0) {
            throw new NoSuchElementException("Cannot remove from an empty linkedlist");
           
        } 
        
        T data = tail.getData(); // retrieve the data of the last node to return 
        
        if (size == 1) {
            head = null;
            tail = null;
        } else {
            // traverse to 2nd last node in the list
            SinglyLinkedListNode<T> current = head;
            while (current.getNext() != tail) {
                current = current.getNext();
            }
            current.setNext(null);
            tail = current;
        }
        size--;
        return data;
    }

    /**
     * Returns the head node of the list.
     *
     * For grading purposes only. You shouldn't need to use this method since
     * you have direct access to the variable.
     *
     * @return the node at the head of the list
     */
    public SinglyLinkedListNode<T> getHead() {
        // DO NOT MODIFY THIS METHOD!
        return head;
    }

    /**
     * Returns the tail node of the list.
     *
     * For grading purposes only. You shouldn't need to use this method since
     * you have direct access to the variable.
     *
     * @return the node at the tail of the list
     */
    public SinglyLinkedListNode<T> getTail() {
        // DO NOT MODIFY THIS METHOD!
        return tail;
    }

    /**
     * Returns the size of the list.
     *
     * For grading purposes only. You shouldn't need to use this method since
     * you have direct access to the variable.
     *
     * @return the size of the list
     */
    public int size() {
        // DO NOT MODIFY THIS METHOD!
        return size;
    }
}