## Queues
> Like stacks, queues are a `linear` ADT - where objects in queues have one predecessor and one successor object, except for edge cases. 
* Like stacks, it can be `backed by` variety of data structures
* Unlike stacks which are `last in first out`, queues are `first in first out`.
* First element added = First element removed
* Examples:
    1. Printer prints documents in order of arriving orders
    2. Customer queue when purchasing air tickets online
### Queue supported operations
```sh
void enqueue(x) # adds data to back of queue
x dequeue() # removes data from front of queue
# first in first out

# The ones below similar to that of stack
x peek()/x top() # returns data at front of queue, but not remove
boolean isEmpty() # checks size or if front is null
void clear() # checks front of queue to be null
```
> Just like stacks, queues are linear ADTs and can be implemented with various linear data structures (arrays & LLs)

### Queue unsupported operations
Similar to that of stack:
* Not designed to search data at a certain index
* No arbitrary index accessing or adding and removing

## Linked List Backed Queues
Queues are defined by performing `operations` at both ends of the queue, so we need a tail & head reference.
* Given an LL with the following data `{1,3,3,2}`, set `head = 1` and `tail = 2`.
> Recall that we want to make adding/removing as efficient as possible with `O(1)` time complexity
* In a linked list:
    1. Adding at head, removing at head => `O(1)`, because no need to traverse the list
    2. Adding at tail is `O(1)`, but removing at tail is `O(n)` because need to traverse LL for 2nd last node
    3. So the wisest choice with a queue where you can add/remove at both ends would be to:
        * Add/enqueue at the tail => `O(1)`
        * Remove/dequeue at the head => `O(1)`

#### Enqueueing/Dequeue 
* Given the initial data `{1,3,3,2}`, with 2 as the tail, we:
1. `Enqueue 5` at the tail, by making the tail reference point to 5
2. `Dequeue 1` at the head, by making head point to `head.next`, so 3 becomes the new head and make `1.next() == null`.
3. We typically do not use Doubly-Linked Lists for queues, as it supports the same set of functionalities yet has a `higher space complexity`.

## Array Backed Queues (ABQ)
> Note that now the queue works with `both ends` of the linear data
* We use arrays instead of array lists because we want to avoid shifting all together when adding/removing from front which would lead to `O(n)` time complexity
* Instead, we introduce a wrap-around or circular array, which allows data elememnts to wrap-around the ends of the array (not the same as CCL)

Important variables in ABQ
* Given an array of `{1,3,3,2}`, enqueued in order accordingly
1. Size = 4
2. Capacity = 7 
3. Front-Index = 0 `tracks the first element` 
4. Back-Index = 4 (not always same as size) `tracks the last element`

> Likewise, we `enqueue` from the back and `dequeue` from the front

#### Enqueuing 
* Back index is the one that shifts right, whilst front index stays at 0

If only have front variable:
* index of most recently enqueued = `front + size % arraylength`

If only have back variable:
* enqueue at `back + 1`

Upon reaching capacity, there needs to be a `wrap-around` for the back index by doing the following: `back % capacity`
* Example: Size = 7, Capacity = 7, Back index = 7, 
* We wrap around the back index by doing 7 % 7 = 0
* The back index becomes 0 now (wrap-around)

#### Dequeuing 
* Front index is the one that shifts right/increments, whilst back index stays at 0
* Size decrements at the same time
* Edge case: `if front variable is last index of backingArray and there is an element at the index`, what does front variabnle be after call dequeue => make it front index = 0

## ArrayQueue Implementation
```sh
import java.util.NoSuchElementException;

/**
 * Your implementation of an ArrayQueue.
 */
public class ArrayQueue<T> {

    /*
     * The initial capacity of the ArrayQueue.
     *
     * DO NOT MODIFY THIS VARIABLE.
     */
    public static final int INITIAL_CAPACITY = 9;

    /*
     * Do not add new instance variables or modify existing ones.
     */
    private T[] backingArray;
    private int front;
    private int size;

    /**
     * This is the constructor that constructs a new ArrayQueue.
     * 
     * Recall that Java does not allow for regular generic array creation,
     * so instead we cast an Object[] to a T[] to get the generic typing.
     */
    public ArrayQueue() {
        // DO NOT MODIFY THIS METHOD!
        backingArray = (T[]) new Object[INITIAL_CAPACITY];
    }

    /**
     * Adds the data to the back of the queue.
     *
     * If sufficient space is not available in the backing array, resize it to
     * double the current length. When resizing, copy elements to the
     * beginning of the new array and reset front to 0.
     *
     * Method should run in amortized O(1) time.
     *
     * @param data the data to add to the back of the queue
     * @throws java.lang.IllegalArgumentException if data is null
     */
    public void enqueue(T data) {
        // WRITE YOUR CODE HERE (DO NOT MODIFY METHOD HEADER)!
        if (data == null) {
            throw new IllegalArgumentException("Data cannot be null");
        } 
        
        // Check if the array needs to be resized
        if (size == backingArray.length) {
            T[] newArray = (T[]) new Object[backingArray.length * 2];
            for (int i = 0; i < size; i++) {
                newArray[i] = backingArray[(front + i) % backingArray.length];
            }
            // Updates the backing array with the new array
            backingArray = newArray;
            // Reset front index to 0 because new elements start from beginning of the array
            front = 0;
        }
        
        // Add the new element to the back of the queue
        int backIndex = (front + size) % backingArray.length;
        backingArray[backIndex] = data;
        size++;
    }

    /**
     * Removes and returns the data from the front of the queue.
     *
     * Do not shrink the backing array.
     *
     * Replace any spots that you dequeue from with null.
     *
     * If the queue becomes empty as a result of this call, do not reset
     * front to 0.
     *
     * Method should run in O(1) time.
     *
     * @return the data formerly located at the front of the queue
     * @throws java.util.NoSuchElementException if the queue is empty
     */
    public T dequeue() {
        // WRITE YOUR CODE HERE (DO NOT MODIFY METHOD HEADER)!
        if (size == 0) {
            throw new NoSuchElementException("Queue is empty");
        }
        // Deque removes the element at the front
        T removedData = backingArray[front];
        backingArray[front] = null; // set removedData to be null
        front = (front + 1) % backingArray.length; // update front index 
        size--;
        return removedData;
    }

    /**
     * Returns the backing array of the queue.
     *
     * For grading purposes only. You shouldn't need to use this method since
     * you have direct access to the variable.
     *
     * @return the backing array of the queue
     */
    public T[] getBackingArray() {
        // DO NOT MODIFY THIS METHOD!
        return backingArray;
    }

    /**
     * Returns the size of the queue.
     *
     * For grading purposes only. You shouldn't need to use this method since
     * you have direct access to the variable.
     *
     * @return the size of the queue
     */
    public int size() {
        // DO NOT MODIFY THIS METHOD!
        return size;
    }
}
```

## Useful Tips
  How do we access the most recently enqueued element? How do we access the next element to be dequeued? Assume that you have access to the backingArray, a front variable that keeps track of the index of the next element to be dequeued, and a size variable that keeps track of the number of elements in your ArrayQueue.
  * Enqueue at `front + size` % array.length
  * Suppose you dequeued, front index moves from ` 0 to 1`  and size decrements
  * Lets say given dequeued size of 7, we would enqueue at `front (1) + size(7)` % `array.length` where array.length remains same as before dequeueing

  How would we track then if only had back variable?
  * Next element to be enqueued = `back index + 1`
  * Next element to be dequeued = `array.length % size`
  * note that array.length remains same even after dequeue operation



#### Locality of reference
NOTE that whilst Big-(O) provides a sense of efficiency, it may not be true due to `spatial locality`
* For instance, given a remove operation, whilst it may state that removing in arraylists from the back is an `O(n)` operation, it might be better than removing from the front of a linkedlist which is `O(1)` because it is able to fetch adjacent memory faster through an arraylist