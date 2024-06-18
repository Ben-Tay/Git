## Arrays

* `Contiguous memory allocation` - memory address of element at index 1 is right after that of element at index 0

Benefits of Contiguous:
1. `Faster to access elements` - as easy to track memory address of next element in list
2. `Locality of Reference`: Contiguous allocation can improve cache performance due to better spatial locality - accessing 1 element is likely to bring nearby elements into cache => speeding up `subsequent access`.

#### Arrays definition:
* Provides O(1) - `constant time complexity` access to a data of single type stored at a specified index
* Unlike primitive types, arrays are used to store a sequence of `related objects or values`
* All elements in array must be of `same type`
* Able to store wide variety of data types - `Strings, objects, references, primitive types etc`

#### Arrays use case
* Declaring an array != immediately constructing the array
* We can either:
    1. Initialize the array with specified values
    2. Create array to specified capacity & populate cells with default values
* All elements are stored in `n` locations from and including `index 0`
* Example: if an element is stored in array of capacity `n`, we should be able to find it in `O(n)` time`

Accessing Elements:
*  Location is known so time complexity is `O(1)`
    * Data at index 5 is just 5 memory locations away from index 0
    * Can be accessed just by adding to memory address of index 0
    * This is possible due to the following:
        * Contiguous memory allocation - each array index occupies adjacent memory locations
        * Array needs to know memory location of index 0
        * Array's data typing needs to be `defined beforehand`.
> By knowing the data type to store, we know exactly how much memory is required for storage, example: `int` always requires 32-bits

Searching Elements:
* . Location is unknown - time complexity of `O(n)`
    * Example: retrieve specific value in the array but do not know which index it is at
    * Need to traverse the array hence involves linear time complexity 

#### Static Memory
* Arrays involve static memory allocation - once the array capacity has been reached, need to resize the array manually and `move` it to a larger chunk of memory
* Time complexity to move to new array for larger capacity => `O(n)`
* Must copy all `n` elements from original array into new array

## Pointer Arithmetic
Since arrays are `contiguous` in nature, the process of accessing elements in the array index `i` is essentially O(1)

$$
newaddr = startaddr (index 0 ) + i * datasize
$$

* This is because it involves only 3 arithmetic operations (as opposed to n, the size of the array)