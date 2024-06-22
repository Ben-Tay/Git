## Priority Queues
* Can add/remove data as necessary and are similar to stacks and queues as they are `linear`
* Have specified expected behaviour when removing
* Is an `abstract data type` with multiple implementations
#### Stack ADT
Remove -> Most recently added element (from front, added from front)
#### Queue ADT
Remove -> First added element (from front too, as we added from back)
#### Priority Queue ADT
Remove -> Element with highest priority
* Eg: waiting of emergency room
* Common uses:
    * Extract out min/max values from a data collection
* Highest priority implementation is custom decided - ie smaller values have higher priority
* PQ stores `comparable` data to determine priority
* Upon removal, the priority of the `next element` to be removed is reassesed - `priority only decided upon removal operation`

### Implementations of PQ
Problem: Efficiently ranking by priority so that element of highest priority is `always accessible`
* `Inefficient` to sort data for every `add` operation and search through data for every `remove` operation 
* In turn, heaps are used to `back priority queues`which gives a unique pov
* Other examples of PQ: Plane boarding by` first class, biz class etc `

### PQ: A Linear Model?
> Consider array-backed priority queues and linkedlist-backed priority queues
 * PQs require the data to be `sorted in some sense`
 #### Array Backed PQ
 * Similar to array-backed queue, enqueue from the back (lowest priority) and dequeue from the front (highest priority)
* However, difference lies in that whilst `dequeuing and peeking` remains at `O(1)`, enqueuing becomes an `O(n)` operation to maintain sorted order of data

#### Linked Backed PQ
* Similar to linked-backed queue, element at highest priority would be the `head` to be dequeued, and element at lowest priority would be the `tail` when enqueued
* However, difference lies in that whilst `dequeuing and peeking` remains at `O(1)`, enqueuing becomes an `O(n)` operation to maintain sorted order of data