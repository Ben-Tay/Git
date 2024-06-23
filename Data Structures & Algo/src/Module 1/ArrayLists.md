## Abstract Data Types (ADTs)
An abstract data type (ADT) is a model description of a data type that is defined by its behaviors and operations. 

They set the `framework` for what operations (methods) are available as well as what these operations do `BUT` does not handle implementation

Actual concrete implementations of data handling are called `data structures`.

## List ADT
* Defined as a `sequence of values` that are accessible via indexing.
* Required operations are kept to a minimum:
```sh
# Adds the data to the list at the specified index. Any data with index i >= index has a new index i + 1 to make room for the new data.
addAtIndex(int index, T data)

#  Removes the data at the specified index from the list. Any data with index   i <= index has a new index i - 1 to maintain the sequence.
removeAtIndex(int index)

# Returns the data at the specified index.
get(int index) 
#  Returns whether the list is empty or not.
isEmpty()
# Resets the list to an initial configuration with no data.
clear()
# Returns the number of data currently stored in the list.
size(): 
```
Efficiency of such operations & its implementations are left to its implementations and not in the ADT - specifically we will look at 2 data structures that implement it `ArrayLists` and `LinkedLists`.

When these data structures are explored in depth, we will often consider the operations such as `addToFront(T data), addToBack(T data), removeFromFront(T data), and removeFromBack(T data)`, in order to, emphasize how the functionality and efficiency of the operations work at the extremities of the List. While these operations aren't strictly necessary in the List ADT, they are useful for transitioning to future topics, Stacks and Queues.

## ArrayLists
* Data is `contiguously` allocated - not the same as `contiguous` memory in Arrays.
* Data must be zero-aligned => starts from index 0
* Essentially a `List` backed by an `Array`.
* As Lists are `ADTs`, so are ArrayLists

Java Syntax:
```sh
# ArrayLists can only store objects, or primitive types within their wrapper classes: Integer, Boolean
import java.util.ArrayList

# Instantiating 
ArrayList<String> list = new ArrayList<>();
# Default capacity is set to 10
```
* Unlike arrays, ArrayLists:
    1. Are automatically resized when capacity is reached
    2. Makes uses of automatic dynamic memory allocation as opposed to static -- no need to call a specific `resize()` method
* However, ArrayLists still have the limitation of needing to be `resized` which takes `O(n)` time.

#### ArrayList Terminology
1. Size - Number of objects being stored in the arraylist
2. Capacity - Number of cells/data that can be stored in the array without a resize 

## Adding to the back of an ArrayList
Constant Complexity `O(1)`
* This is when we know the `size()` of the array and array capacity `has not been reached`
* Example: Capacity of 5, current arraylist has 3 elements so we add 1 more element. Size => 4 
* Also considered as `best-case` scenario

Linear Complexity `O(n)`
* This is when we know the `size()` of the array but array capacity `has not been reached
* Current capacity: 5 & number of elements = 5
* To add a 6th element => we need to resize the array which takes `O(n)` time to do so.
* Note that this is considered as the `worst-case` scenario as resizing is required, but this is `pessimistic` as resizing rarely occurs.

#### Armotized Analysis
* `Armortized analysis` of adding to the back:
    * In the very rare event of having to resize, by comparing the no. of occurrences of having to resize as opposed to a number of occurences of other O(1) operations
    * We can take the average and argue that adding to the back is technically an `O(1)` operation overall as opposed to looking at its single cost of `O(n)`.
    * To keep it short -  rather than looking at the per operation cost, we instead consider `all sequences of  operation`s and `average the cost` over the number of operations as shown below:

$$
Armotized Cost = \frac{total cost of all operations}{no.of operations} = \frac {2n}{n} = 2 = O(1)
$$
> Here we use `2n` because resizing typically involves doubling the capacity of the arraylist `n`. Example: Capacity of 8 when full will be doubled to `2(8) = 16 `

## Adding Elsewhere
* Arbitary index or front of ArrayList
* Cost is always going to be `O(n)` as we need to shift up all data by 1 cell in order to insert the new data => `to keep our data contiguous`
* Example: Given the following array: {a,g,h,q,z}
    * Element g is at index 1 
    * By doing this: `AddAtIndex(f,1)` means that we would have to add element f at index 1, thus needing to `shift g,h,q and z by 1 cell` backwards

## Removing Elements
* Removing from the back is always `O(1)`.
* Removing from anywhere else in the array is always `O(n)`.
    * Likewise, given an arraylist of size 5, removing an element at index 1, would require elements at indexes `2,3,4` to shift forward by 1 cell to make the data `contiguous` which leads to `O(n)` complexity

### Soft vs Hard Removals
`Hard Removal` 
*  Ensure that data removed is `completely removed` from backing structure
* (i.e. if you searched the entire array, you would not find the data). In an ArrayList, this often happens naturally in the shifting process, but when necessary, you may need to manually set an array position to null in order to perform a hard removal.

`Soft Removal` 
* When you leave the data in the data structure unless it is absolutely necessary to get rid of it.
* Example: in the ArrayList, the "end" of the ArrayList is controlled by the size variable. So, it may not be strictly necessary to completely remove the data at the end if it's removed since the end can just be controlled by the size if it's done carefully.

> Typically expected to perform `hard removals` unless absolutely necessary (HashMaps)
* Reason being that if the data being stored is sensitive, we will want to ensure that when the user removes data, the data is truly removed from the data structure so that no adversaries can access it.
* Also makes data structures' implementation details cleaner to work with


## Adding at Index
```sh
/**
 * Your implementation of an ArrayList.
 */
public class ArrayList<T> {

    /*
     * The initial capacity of the ArrayList.
     *
     * DO NOT MODIFY THIS VARIABLE!
     */
    public static final int INITIAL_CAPACITY = 9;

    /*
     * Do not add new instance variables or modify existing ones.
     */
    private T[] backingArray;
    private int size;

    /**
     * This is the constructor that constructs a new ArrayList.
     * 
     * Recall that Java does not allow for regular generic array creation,
     * so instead we cast an Object[] to a T[] to get the generic typing.
     */
    public ArrayList() {
        //DO NOT MODIFY THIS METHOD!
        backingArray = (T[]) new Object[INITIAL_CAPACITY];
    }

    /**
     * Adds the data to the specified index.
     *
     * Must be O(1) for index size and O(n) for all other cases.
     * 
     * ASSUMPTIONS:
     * - You may assume that the backingArray will not need to be resized.
     * - You may assume that the index is valid [0, size].
     * - You may assume that the data will never be null.
     *
     * @param index the index at which to add the new data
     * @param data  the data to add at the specified index
     */
    public void addAtIndex(int index, T data) {
        if (size == 0) {
            // Directly insert the element if the list is empty
            backingArray[index] = data;
        } else {
            // Shift elements to the right to make space for the new element
            for (int i = size; i > index; i--) {
                backingArray[i] = backingArray[i - 1];
            }
            // Insert the new element at the specified index
            backingArray[index] = data;
        }
        // Increment the size of the ArrayList
        size++;
    }

    /**
     * Returns the backing array of the list.
     *
     * For grading purposes only. You shouldn't need to use this method since
     * you have direct access to the variable.
     *
     * @return the backing array of the list
     */
    public T[] getBackingArray() {
        // DO NOT MODIFY THIS METHOD!
        return backingArray;
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
```