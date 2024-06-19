## Recursion
A recursive method is one that `repeatedly` calls itself

Correct recursive method must have 3 following attributes:

`Base Case(s)`: Termination condition(s) that ensure all branches of recursion stop eventually
* Recursion w/o a base case will loop/run forever and causes a `stack overflow` error.
* To ensure that this process terminates, we need a base case that is simple enough to solve directly without further recursion, (ie left 1 step)

`Recursive Case(s)`: Method calls to itself
* Any time a recursive method is reached, current method call will block/pause at that line until the recursive call `returns a value`.

`Progress to Base Case`: Each recursive call must move towards the base case in some way (a parameter/combination of it)
* Not having such a parameter => `Infinite Recursion`

## Basic Structure
```sh
public return_type recursiveEx(param_1, ..., param_n) {
    if (base_case 1) {
        # termination logic for bc 1
    } else if (base_case 2) {   
        # termination logic for bc 2
    }
    else {
        # logic for recursive calls where a parameter MUST change to approach the base case
        return recursiveEx(newParam_1, ..., newParam_n);
    }
}
# Base cases never have a recursive call within them but may have a return statement based on return type & method
```
## Tips to finding the recursive sub problem
Try to first figure out recursive structure of problem if not already defined

#### Exponentiation by repeated squaring
> Example: Write a power function to calculation b^x where b is an integer and x is a power of 2

Possible ways to tackle:
* Substructure 1 = b^(x) = b * b^(x-1), b^0 = 1
* Substructure 2 = b^(x) = b^(x/2) * b^(x/2), b^0 = 1

> After which write the base case(s) first, then write the rest of method assuming recursive method already works
* Avoid overlapping base cases (arms-length recursion)

#### 3 questions to ask when designing the algorithm:
1. Is the algorithm correct - does it give correct ans for every input?
    * Yes => base case = b^1 where b^1 * b^1 = b^2
2. What is the algorithm efficency?
    * Multiplication is `O(1)`
    * But we are performing `O(log(x))` recursive calls as exponentiation is involved in Substructure 2 compared to O(x) in substructure 1
3. Is the efficiency of the analysis tight? can we do better?

 
#### Euclidean Algorithm for greatest Common Divisor, GCD
> Find the largest integer dividing both x and y with no remainder => gdc(x,y)
* Brute force method is to find all factors of x & y (looking at all numbers lesser than x and y)
* This is solved more easily w/ recursion
* Multiple ways to solve thru subproblems:
    1. `Subtraction` - smaller is subtracted from larger repeatedly
    2. `Divison` - Larger modulo against smaller to keep remainder - easier & more efficient than method # 1
    3. `Binary GCD` - Both numbers divided by 2 and tracks count of binary divisions
> Given x > y and x,y are non-zero 
```sh
    Eg: x = 1482, y = 819, r = 1482 % 819 = 663
    x = q * y + r (where q is the quotient and y is divisor)
    r = x mod y
    y > r 
    Recursive case => gcd(x,y) = gcd(y,r) 
    # Basically y and r becomes the new parameters in the next method call
    gcd(1482,819) = gcd(819,663) 
    gcd(663,156) = gcd(156,39)  156%39 = 0, gcd(39,0)

    Base case => gdc(z, 0) return z 
    # When reach 0, means that greatest common demonitator has been reached ==> 39 in this case
```

## Coding the Euclidean Algorithm
Method returns an integer and takes in 2 integer parameters x and y, and assumes that `x >= y`.
> Can always include error handling if incorrect parameters or x < y

This works because the common divisor between (x,y) is the same as (y,r)
* Eg: d is `common divisor` of x and y, where r = x - (q * y),`let x = 14, y = 4, q = 3, r = 2`
* We can rewrite this to be `x = (q * y) + r` where d is a common divisor of y and r 

```sh
public int gcd(int x, int y) {
    # define base case to terminate by returning int
    if (y == 0) {
        return x;
    }
    else {
        # perform a recursive call with the new parameters
        int remainder = x % y
        return gcd(y, remainder));
    }
}
```
## Structural Recursion
> In the past, we have worked on recursions that are more numerical oriented, but since we have a focus on data structures, we need to have our recursion acting on a data structure of some sort 

Java code to handle tiling problem:
```sh
public class Tiling {
    public static int countTilings(int n) {
        if (n == 0) return 1;  // Base case for a(0)
        if (n == 1) return 3;  // Base case for a(1)

        // Initialize base cases
        int a0 = 1;  // Corresponds to a(0)
        int a1 = 3;  // Corresponds to a(1)

        // Iterate from 2 to n to compute the number of ways for each grid size
        for (int i = 2; i <= n; i++) {
            int a2 = 3 * a1 + 4 * a0;  // Use the recursive formula to compute a(n)
            a0 = a1;  // Update a(0) to be the previous a(1)
            a1 = a2;  // Update a(1) to be the current a(n)
        }

        return a1;  // Return the number of ways for the 2x(n) grid
    }

    public static void main(String[] args) {
        int n = 10;  // Example value for n
        System.out.println("Number of ways to tile a 2x" + n + " grid: " + countTilings(n));
    }
}
```
#### Increasing subsequences in Arrays
Suppose that we have an array A of length `n` as input consisting of `n` distinct integers. A subsequence of the array is a sequence of some of the array entries in the order that they appear.
> Given the array `[1,7,3,5,2,8,10,24,-1,-5,4]`, then `3,2,-1,-5,4` is a valid subsequence since the numbers appear in the sequence in array order whilst `1,7,10,8` is not a valid subsequence as 10 is supposed to be after 8.
* An increasing subsequence is one where the numbers are `in increasing` order which is part of a `sorted array` and there are 2^n of them

Problem: count number of `increasing subsequences` in the array by counting & summing no.of possible sequences that can be formed at each index

```sh
public class IncreasingSubsequences {
    public static int countIncreasingSubsequences(int[] A) {
        int n = A.length;
        int[] dp = new int[n];

        // Initialize dp array: each element itself is a subsequence
        for (int i = 0; i < n; i++) {
            dp[i] = 1;
        }

        // Calculate number of increasing subsequences ending at each index
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (A[j] < A[i]) {
                    dp[i] += dp[j];
                }
            }
        }

        // Sum up all dp[i] values to get the total number of increasing subsequences
        int total = 0;
        for (int i = 0; i < n; i++) {
            total += dp[i];
        }

        return total;
    }

    public static void main(String[] args) {
        int[] A = {1, 3, 2, 4};
        System.out.println("Total number of increasing subsequences: " + countIncreasingSubsequences(A));
    }
}
```