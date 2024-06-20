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
Useful when we are trying to model something with `circular behaviour`: eg: repeat music playlist when it ends
* Unlike previous linked lists, the `tail` or last node points to the `head` rather than `null`.
* Does not have a `tail` reference but could be included yet does not provide any `increased efficiency` for adding/removing
* Termination logic is not the same as that of other linked lists as there is `no end`, so we do not terminate upon `curr = null`
* Termination condition changes to checking for if `curr.next` == `head` (ref equality not value equality) or check the size if a `size variable` is maintained
> Circular linked lists can be `singly or doubly linked` 

## Adding to front (CLL)
* Unlike a normal SSL, to add to the front of a list, we cannot just do the following:
    1. `new node().next() = head`
    2. `head = new node()`  
    3. This is because the last node's.`next()` is still pointing to the old head and we have no way to access the last node easily w/o a tail pointer and have to traverse thru the list leading to an `O(n)` process

Instead we do the following for `O(1)` efficient adding to front of a CLL:
1. Create a new empty node `w/o any data`
2. Insert new node directly after head (index 1)
3. Connect the new node().`next` to the initial `.next` of the head and then redirect the head.`next` to the new node
    * Eg: `node1(head).next = node 3` at first
    * We introduce a new node 2 after node 1
    * `node.next points to node 3` as initially `data1.next = data3`
    * now we change `node1.next = node 2 (new node)`
4. Copy the data from the ` head (data 1)` into the empty new node 2 
5. Add the new data into the head node 
6. This becomes an `O(1)` operation as do not need to traverse thru the list to find the last node

## Adding to back (CLL)
1. Just like adding to front, add new empty node 2 into index 1 of the list (after the head)
2. The new data we want to add the back of the list is `data 5`
3. Copy head data from node 1 into new empty node 2
4. Add the new data 5 into the head node
5. Reset `head` reference such that it points to    `head.next` such that node 2 becomes the new head and intial node 1 becomes the back

## Removing from the front
1. Move the data from `head.next` into the head
2. Redirect `head.next` to the 3rd node 
3. Remove the 2nd node from the list which will be physically removed and garbage collected
> This essentially works because u replaced the inital data in the head with that of the 2nd node which indirectly `removes from the front` and u got rid of duplicate data
4. Cost of this operation is `O(1)` 
5. Need to also consider edge case where ` size = 1`, head must be set to null and `head.next = head` as circular list and nothing gets removed

## Removing from the back
1. No special `O(1)` technique
2. Must use a loop to stop on 2nd last node and gain access to its `.next` 
3. Redirect the `.next` of the 2nd last node to the head, in turn breaking the link of the initial last node to the list which will be handled by `garbage collection`

## Removing from the middle
1. Same as removing from SLL
2. Traverse to the node before the node u wish to remove (Eg: want to remove Node 4, so traverse till Node 3)
3. Redirect `.next` of Node 3 to node 5 (the one after Node 4)
4. Since Node 4 is skipped, it will be no longer accesible and picked up by `garbage collection`

## Examples of Linked Lists
`Singly Linked Lists`:
*  history of web browser, head shows what was most recently visited

`Doubly Linked Lists`:
* Most recently used cache
* Eg: music app that keeps track of most recent songs --> you can move to next and to previous as you want 

`Circularly Linked Lists`:
* Music playlist that starts over once completed

## Flexibility of linked structures
Some might argue what is the point of learning `CLL` when it only adds a tad bit of variation.

> We can think of it in this way to learn the power of linked structures: 
* Unlike arrays, where data has to be contigous, linked structures allow us to place and imagine data arranged in any way we like (cuz we can modify the pointers)

#### Tree
What if instead we modify linked lists such that it can `only have 1 receiving pointer` but multiple `outgoing pointers` => this would lead to a `Tree` 
* A common system of this would be `file systems`, thinking of each folder as a node and each file as the `end` of these paths

#### Disjoint Set
> Think about it the other way where have multiple `incoming` pointers and only `1 outgoing`, we would achieve a disjoint set 
* Advantage lies in that each grouping is made in such a way that every sequence of node connections eventually lead to a single, unique node (the blue node). 

#### Graph
> If we forgo all the restrictions of `in and out pointers`, we would obtain a graph, which is used to `model relationships between data`.

Good example would be that of social media platforms
* Eg: Node = people and connections between the nodes could be like 2 people being friends online, which could branch into further connections like being on the same group etc 
* Many possiblilities with this linked structures