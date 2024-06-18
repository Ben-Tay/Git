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