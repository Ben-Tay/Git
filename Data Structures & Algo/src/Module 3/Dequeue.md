## Deque Abstract Data Type (ADT)
Acts as a natural extension of both `stacks and queues`, rather than specifying an end to add/remove from:
* Means `double-ended queue` which has the ability to add and remove from both ends efficiently
* Removal occurs `in any order` data may have arrived into the `deque`.
> Can be backed by both an `array` and a `doubly-linked-list` (Not singly-linked because need .previous()), allows all methods to have `Time complexity of O(1)`

#### Supported Operations
```sh
void addFirst()
void addLast()
x removeFirst()
x removeLast()
boolean isEmpty()
int size()
```
#### Unsupported Operations
* Searching for data
* Arbitary index access
* Adding/removing on arbitrary index

## Array Backed Deques
* Just like array-backed queues, consists of a `front` and `back` index which uses the `circular wrapping principle` when the array capacity is full
#### Supported operands
`addLast()` 
* add at back (works like enqueue)
* Increment `back index` (% by capacity)
`addFirst()`
* add at front 
* Decrement `front` (check if < 0, if so, set front = capacity - 1)

`removeFirst()` 
*  remove from front (works like dequeue)
*  Increment `front` (% by capacity)
`removeLast()`
* remove at back
* Decrement `back` (check if < 0, if so, set back = capacity - 1)
> Add/remove methods are `armortized O(1)` due to resizing that may happen

## Doubly-Linked List Backed Deques
> All operations have `O(1)` time complexity

Operands dealing w first element:
* Performed at the `head`
* `addFirst()` - adding to the head
* `removeFirst()` - removing from the head

Operands dealing w last element:
* Performed at the `tail`
* `addLast()` - adding to the tail
* `removeLast()` - removing from the tail

#### Deque Real Life Examples
For instance: Online Purchasing System
* Customer sends purchase request which is `sent to front of deque`
* When purchase is made, `it is dequeued` from front of dequeue
* However, customer can immediately enqueue to front of deck again if `they need to make changes` to their purchase

## Java's % Operator
* Taking an integer modulo `n` would gives us `n` different classes of numbers based on `what remainder is` when dividing by `n`
* For negative numbers, instead of `-9 % 5 = 1`, it would give us the smallest negative remainder closest to 0 => `-9 % 5 = 4`
* Need to have helper methods to `handle negative numbers`.
