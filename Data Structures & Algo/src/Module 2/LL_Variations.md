## Doubly Linked Lists
Similar to Singly Linked Lists, except it allows for traversing in `both directions`, can consider it as a variation of SLL.
> Recall: In Singly Linked Lists, to remove from the back, we had to traverse through the LL from the front, which was `highly inefficient`
* Different from SLL, because its node contains not just a `data` and `next` pointer, but also a `previous` pointer.
* Also almost always contains a `head` and `tail` reference
* Comes with its cons: `more memory is used` because overhead for more pointers, but pros lies in `time efficiency` for operations => `O(1) for time complexity, O(n) for space`

## Adding to Doubly Linked Lists
* Works similarly to SLLs, but comes with a few edge cases
* Need to consider following edge cases:
    1. `Empty DLL (Size 0)` => `Both head and tail to be set to null`
    2. `Adding 1st element (Size 1)` => `Both head and tail need to be set to the new node` 

#### Adding to the front
Steps involved:
1. Create the new node
2. Set the new node's `.next()` to the current head => so as to prevent losing linkage to rest of the DLL
3. Set current head's `previous` pointer to the new node
4. Set the head to be the new node => new node becomes the new head

#### Adding to the back
1. Create the new node
2. Set the new node's `previous` pointer to the `tail`
3. Set the tails `next` pointer to the new node
4. Make the new node the new `tail`

> General consensus is to `first connect the new node to the linked list` before altering the pointers of the linked list or else we may lose `O(1)` access to the nodes

#### Removing from the back
* Through DLL, can remove from back with `O(1)` instead of `O(n)` time efficiency due to `tail` reference
1. Set the tail to the current tails `previous` node
2. Set the `next` of the new tail to be null

Edge case: removing from a DLL of size 1:
* Point `head and tail` to null to effectively remove the node which is then `garbage collected` as that node is no longer accessible in memory

## Circularly Linked List
Useful when we are trying to model something with `circular behaviour`
* Unlike previous linked lists, the `tail` or last node points to the `head` rather than `null`.
