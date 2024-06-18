## Big-O 
> Big-O is a measure of efficiency of algorithms & data structures
* Big-O belongs to a family of `asymptotic  notation`.
* Measure data structures based on their time & space efficiency/complexity
* The measure must be independent of both `hardware/software` environments
    * Code run on a very old computer will naturally run slower on a new computer
### Time Complexity
> How efficient the algorithm is in terms of input size

#### High-Level Description
* Analyze the run-time by defining a set of primitive operations in the code:
1. Assign value
2. Arithmetic Operations (+ - * /)
3. Comparing 2 entities
4. Method call or returns
5. Access element/references
* Primitive operations execute in `constant` time - very fast
> Algorithm run time = # of operations * how many times they execute

## Measuring efficiency as a function (fn)
>`fn()` = function of primitive operations of input size `n`

3 cases to consider:
1. `Worst-Case`: Algorithm with worst set of data + worst performance
2. `Best-Case`: Algorithm with best designed set of data + fastest performance
3. `Average`: Somewhere between best & worst case and is difficult to compute
> We tend to want to find the `Worst-Case` analysis for Big-O notation

## Big-O notation
> `O(f(n))` -- where `n` is the size of our inputs, `f(n)` is a function representing the scaling of the algorithm with `f(n)`
* Typically represents the upper bound or the `worst-case` scenario
* Everything in this course will be O(n^4) but not a `accurate description of performance`
* Still many other measures: o(n), theta(n), etc
* Safe to assume we are measuring `time complexity` if not specified

## Common Complexities
![This is meant to show the complexity image](https://github.com/Ben-Tay/Git/blob/main/Data%20Structures%20&%20Algo/src/Module%200/Complexity.png?raw=true)

* From top to bottom - in order of increasing complexity
* Typically, we wish to maintain a low complexity (top of table) at `constant` time complexity 
* By end of course, should have good idea to define complexity of operation & work towards `optimizing` it
## Asymptotic Notation: Another Look
> Simple outlook: time complexity = counting number of primitive operations
* Whilst primitive operations may seem trivial, if it involves large number of units it may still pose a significant computational task (ie. multiply 2 very long numbers)

Even though everything in this course is `O(n^4)` technically , whenever we ask for the Big-O of something, we are asking for the best reasonable upper bound you can give (i.e. if an operation is clearly `O(n)`, then you cannot just say it is `O(n^2)` even though that is technically correct).

Example explanation:
![meant to show image](https://github.com/Ben-Tay/Git/blob/main/Data%20Structures%20&%20Algo/src/Module%200/Asymptotic%20Complexity.png?raw=true)

## Big-O Conventions
> Big-O is meant to measure how performance scales as input grows towards infinity 
1. Drop constant factors
* As input size increases, constant factors grow `insignificantly` and can be disregarded
* Example: `O(5n) => O(n)` and `O(5n^2) => O(n^2)`
* 5 here is dropped
2. Drop Lower-Order terms
* As n approaches infinity, lower-order terms do not grow as fast so can just ignore
* Example: `O(n^2 + 1000n - 3) => O(n^2)` and `O(3n + 2log(n) + nlog(n)) => O(n(log(n)))`

## O(1) - Constant Complexity
Performance does not scale at all with input size, amount of time taken remains same

Example: Given an array, returning the 1st element is always O(1)
* Array 1: {5,8,1,4,9}
* Array 2: {1,2,3,4,5,6,7,8,9}
* Time taken to retrieve 1st element from both arrays will be the same regardless of number of inputs in each array

## O(n) - Linear Complexity
Performance scales proportionally with the input size
Example: Given an array of length n , sum all the elements in the array
* Array 1: {5,8,1,4,9}
* Array 2: {1,2,3,4,5,6,7,8,9}
* Time taken to traverse through Array 1 for summing elements will be lesser than Array 2 due to lesser elements
* Big O of the sum operation here will be `O(n)` --> time complexity increases with the number of inputs

## O(log(n)) - Logarithmic Complexity
* Performance scales with input size logarithmically
* Base doesn't matter as it is a constant, but usually CS uses base 2

$$
 logm(n) = \frac{log2(n)}{log2(m)} = Clog2(n) = O(logm(n)) = O(log(n))
$$

Example: given sorted array of length n, performing a binary search

> Finally; note that whilst we drop constant factors -- this is from a theoretical POV and constants may actually affect efficiency

Example: Given following 2 algorithms
1. Algorithm A - O(n) - on paper this scales better than B as its runtime does not grow as fast
2. Algorithm B - O(n^2)
> However, consider that:
Algorithm A performs 1000000000000n operations, whilst Algorithm B performs 2n^2 operations
* In such a case, without purely looking at the Big O notation, we will find that Algo B performs fewer operations than Algo A for smaller input sizes, so its wiser to use Algo B here