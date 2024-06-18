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
* `Armortized analysis` of adding to the back:
    * In the very rare event of having to resize, by comparing the no. of occurrences of having to resize as opposed to a number of occurences of other O(1) operations
    * We can take the average and argue that adding to the back is technically an `O(1)` operation overall as opposed to looking at its single cost of `O(n)`.

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