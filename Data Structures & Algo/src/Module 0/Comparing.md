## Comparing
> Used to compare objects where `comparable` and `comparator` are completely independent of each other - neither needs the other to operate
* Note that if 0 is returned, need to use another property of the object to determine which will be first in the order/queue

## Comparable Interface (Own class)
https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html
> Object using the `Comparable` interface can directly compare itself to another object using the `compare to` method
* Establishes a `natural ordering` for instances of the class based on the return value shown below:
* Example: In Java, natural ordering for Integers is in `ascending` order
* CompareTo method will be called if we pass in a collection of these objects into `collection.sort` method
* Used in the nodes of `BINARY SEARCH TREES` for ordering
```sh
# Example: x.compareTo(y)
public int compareTo(T y); 
# returns -ve if x < y 
# returns 0 if x = y
# returns +ve if x > y
```
## Comparator Interface (Different Class)
https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html
> User can use a Comparator to compare 2 objects of the `same type` using the compare method
* Used when we want to define a custom ordering as compared to the natural ordering in Comparable
* Example: we can redefine integers to be in `descending` order rather than ascending
```sh
public int compare(T x, T y);
# Example: comp.compare(x,y)
# returns -ve if x < y 
# returns 0 if x = y
# returns +ve if x > y
```

### Comparable Example
> A part of `java.lang` package so no need to explicitly import
```sh
public class HDTV implements Comparable<HDTV> {
    private int size;
    private String brand;
    public int getSize() { return size; }
    public String getBrand() { return brand; }

    # We need to override compareTo method using the same type parameter as that of Comparable 
    public int compareTo(HDTV tv) {
        if (size < tv.size) {
            return -1;
        }
        else if (size > tv.size) {
            return 1;
        }
        else { # size is equal
            return 0;
        } 
    }
    # A much faster way
     public int compareTo(HDTV tv) {
        return size - tv.size;
     }
}
```
> In the example above, the current instance's size is being compared to the passed in parameter

### Comparator Example
> Used in the event we can't make the object `Comparable`
```sh
import java.util.Comparator; 
public class HDTV implements Comparable<HDTV> {
    private int size;
    private String brand;
    public int getSize() { return size; }
    public String getBrand() { return brand; }
}
# We also require a SizeComparator
class SizeComparator implements Comparator<HDTV> {
    public int compare(HDTV tv1, HDTV tv2) {
        return tv1.getSize() - tv2.getSize();
    }
}
```