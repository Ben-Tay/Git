## Other Linear ADTS
> In this module, we will focus on two fundamental ADTs in computer science, `the Stack ADT and the Queue ADT`. These new ADTs, along with the List ADT, model data that is stored in a `linear manner`
* We will also look at 2 other related ADTS `priority queue` and `deque`
* Unlike Lists, `Stacks` and `Queues` are more concerned with operations at the ends of the data (front and back of a list), as opposed to assessing at any index in the list. Since we are working with a more limited set of operations, we'd like for the operations to be efficient without much overhead.
* `Dequeues` can be seen as a combination of stack & queues with `more operations`.

### What makes a linear ADT?
LINEAR 
* There must exist a `finite` collection of objects
* For a `linear collection`, each object must have a `predecessor` object and a `successor` object
* The only exceptions lie in the first object which has `no predecessor` and the last object which has `no successor`.
* Stacks are linear ADTs

Abstract Data Type, ADT
* Data structure is a container with a `finite` number of objects where there is a `relationship` betwene the objects stored
* Defined by the `operations or behaviours` of the operations used by the user from a high level pov, as opposed to looking at implementation

## Stack ADT
Stacks are one model for data that behave linearly.
Stacks can be implemented with or backed by various data structures such as the following: `Arrays` and `Singly LinkedLists`

> Stacks follow a `Last in First Out` principle, for instance, whatever was `added (pushed)` to the stack last would be the first one to be `retrieved (popped)` from the stack `(think of potato chips can)`
* Stacks , unlike lists are `not made for searching` beyond the element that was `last added`
* For instance, in a recursive stack, `each call` to the recursive method is `pushing` that call onto the stack and each `method termination` is popping that call off the stack 

#### Stack Supported Operations
```sh
void push(x) # takes in an element x to push on top of stack
x pop () # takes in no params, removes last added element 
x peek()/ x top() # shows last element at top of stack, but does not remove it
boolean isEmpty() # checks the size/if top of stack is null
void clear() # sets top of stack to null and clears it
```
#### Stack UnSupported Operations
Stacks `DO NOT search/access/add/remove` from anywhere `within` the stack
* Operations such as arbitary index access or remove are unsupported, should we want to use them we should find a different data structure for implementation

> Real life examples: History of last opened apps, always shows most recently used, or undo button in word doc always undoes the latest done procedure

## The call stack
In the video, we mentioned in passing that the method calls (and thus also recursion) exhibit Stack behavior. To see this, we need to recall two things about how method calls behave.

* When a method is called, the current method that is active is put on pause, and the new method that was just called begins execution. `(pushing method call to stack)`

* When a method call terminates (i.e. returns), the method call that was previously active unpauses and continues execution from where the method call was made. `(pop method call from the stack)`
> Currently executing method would be the `method call` currently at the top of the stack

```sh
public class CodeDemoBG {
    public static void main (String[] args) {
        recursion(0);
    }
    
    private static void recursion (int i) {
        if (i > = 5) {
            throw new StackOverFlowError("Exceeded max call depth.");
        }
        recursion(i + 1);
    }
}
## Infinite recursion leads to stack overflow errror
```
* First main is executed then the following:
    1. recursion(0), recursion(1), recursion(2), recursion(3), recursion(4), recursion(5)
    2. At `recursion(5)`, the if condition is met as i > =5, throwing the stackoverflow error
    3. I think its also pretty safe to assume that without this if block, since there is no progress to a base case here, `this would lead to infinite recursion` also causing stackoverflow error too.
## Singly Linked-List Backed Stacks
Adding to the stack
1. When stack is empty, head of SLL is `null`
2. Upon pushing to top of stack, we added to the head of the SLL `(O(1))`
3. Consider adding the following elements :`{1,3,3,2}` to the stack
4. Workflow:
    * `push(1)` - 1 is added to the stack and is the head
    * `push(3)` - 3 is added to top of the stack and becomes the new head
    * `push(3)` - 3 is added to top of the stack and becomes the new head
    * `push(2)` - 2 is added to top of the stack and becomes the new head

Popping from the stack `O(1)`
1.  `pop()` - 2 is removed and second 3 becomes the new head and top of stack
2.  `pop()` - second 3 is removed and first 3 becomes the new head and top of stack
3.  `pop()` - first 3 is removed and 1 becomes the new head and top of stack
4. `pop()` - SLL becomes empty and `head == null`

### Performance of Singly Linked-List backed stack
* No tail pointer, only use head reference
* Stacks are light weight and all operations only require `moving the head` which is an `O(1)` operation
* Doubly linked lists despite being able to support all operations have more memory overhead `(tail and previous)`


## Array Backed Stacks
> Look out for size of array, when stack is empty, `array.size() = 0`

Adding to the back
* Rather than adding to the front, we add to the back as adding to the front would result in shifting of the elements and thus `O(n)` complexity
* We can add to the back using the `size variable` to keep track of which index to push on
* Adding `{1,3,3,2}` will thus lead to an array in the same order

Removing from the back
* By using size variable, we can first decrement the size and then remove the element at the index size

## Clearing an array back stacked
1. Just leave data and overwrite as you go (not recommended)
    * By setting size variable to 0 and overwriting old data, data is sitting around and java cannot garbage collect it
    * Vulnerable for sensitive data