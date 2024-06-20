## Iterables in LinkedLists
* Unlike arraylists, unable to access elements at a specific index in linkedlists as `nodes are processed` 1 at a time
* Reach/scope of a node is `only to the next node`

## Iterating thru a Linked List (While loop)
```sh
Node curr = head
while (curr != null) {
    # do work here
    curr = curr.next;
}

# Drawback lies in its terminating conditions
```
## Iterables in Linkedlists
Unlike while loops, iterators do not have that problem as they `maintain` a current cursor which advances and returns data based on `hasnext()` and `next()`.
```sh
# Recall that iterable relies on Iterator, so we still have to import it
import java.util.Iterator
public class LinkedList<T> implements Iterable<T> {
    # other methods omitted

    # Remember need to overwrite iterator() method that returns an Iterator
    public Iterator<T> iterator() {
        return new LLIterator<>();
    }
}
```
> Create a class for the LL iterator within LinkedList class which overrides the `next` and `hasnext()` methods
```sh
private class LLIterator implements Iterator<T> {
    private Node<T> curr;
    LLIterator() {
        # set current node to head of linked list upon instantiation
        # Linkedlist class has head variable since LL iterator is inner class of it, it can access
        curr = head;
    }

    public boolean hasNext() {
        # here we use curr because curr is iterated to the next node in the LL, if curr.next = null, curr is assigned to become null and hence hasNext() returns false
        return curr != null;
    }

    public T next() {
        if(hasNext()) {
            # Step 1: first retrieve data from current node
            T temp = curr.data;  
            # Step 2: Move to the next node in the LL since this is the next() method
            curr = curr.next; 
            return temp; 
        }
        return null; # return null if no other nodes in LL
    }
}
```
## Using the iterator
> Assume the following code are written in some `main` method.
```sh
LinkedList<String> courses = new LinkedList<>();
# List has been populated

# Implictly use iterator through iterable (for-each loop)
for (String course: courses) {
    # do work that should not modify data or list here   
}

# Explictly use iterator using Iterator interface
Iterator<String> courseIt = courses.iterator();
while (courseIt.hasNext()) {
    String data = courseIt.next();
    # do work with the data here
}
```
## SLL class (repeat for reference)
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
## Recursion in SinglyLinkedLists
Problem: Given internal access to a Singly-Linked List with Comparable data, where all of the data is guaranteed to be in sorted order, remove all duplicates from the list so that there is at most one of each data. This task should be done in `O(n)` time and `O(1)` space (there is space overhead for using recursion in the first place, but by  space here, we are referring to external memory such as creating new nodes, data, etc.).

> Can think of it as the following:
* All data elements are in sorted order, such that all duplicates are `contigious`
* `{Node 1, Node 1, Node 2, Node 2, Node 3, Node 3}`
* Aim is to write a function that recursively removes all duplicate elements in LL
* `{Node 1, Node 2, Node 3}`
```sh
# Create public wrapper method for user to use the functionality, without knowing implementation
public void removeDuplicates() {
    head = rRemove(head);
}

# recursive method to remove
private Node<T> rRemove(Node<T> curr) {
    # base case because curr = null indicates end of LL, and an empty list is devoid of duplicates 
    if (curr == null){
        return null;
    } 
    # Assignment here not made until return from recursive call - basically we want the curr.next to keep updating until we reach the end of the list till curr = null
    curr.next = rRemove(curr.next);
    # make use of value_equality (equals) here to remove duplicates
    if (curr.next != null && curr.data.equals(curr.next.data)) {
        return curr.next;
    }
    return curr; # signals no duplicates found in the 2 nodes
}
```
How the code works for understanding:
* Given the following data `{2,3,3}`
* User calls `removeDuplicates()`
* `removeDuplicates()` makes a call to `rRemove(2)` which is the head
* At curr.next it is only assigned when `rRemove(3)` is returned because curr.next is 3. 
* If there were much more 3s, the `last occurrence` of a 3 is the one that is preserved, other duplicates have nothing pointing to them anymore and become garbage collected.
* Note that all recursive calls have to take place first before `if conditions` are executed because of "stack and heap: logic
    * eg: when curr = 3 (last node), curr.next = null, so return curr, returns 3 (last node)
    * when curr = 3 (2nd last node), curr.next = 3 (last node), since 3 = 3, if condition is met and curr.next(3) is returned, effectively getting rid of curr = 3 (2nd last node) which is a duplicate
    * when curr = 2 (1st node), curr.next = 3 (2nd last node), they are not the same so return curr, returns 2 and since curr.next is set to whatever is returned from the recursive call, the link to the last node is not lost
    * eventually once whole rRemove has been executed, head is set back to the 1st head assigned in `removeDuplicates()` method
> This concept of relinking the nodes is known as `Pointer Reinforcement` => by making curr.next = whatever is returned from the recursive call, we do not lose access to the linkedlist