## Looping 
Iterables & Iterators are tools we use to `iterate` through the data contained in a data structure

## Iterable Interface 
> Dependent on `Iterator` & provides more direct control of object iteration for `custom behaviour`

> An object that implements the `Iterable` iterface can be iterated through a `for-each` loop
*  Has an abstract method called `iterator()` that returns an `Iterator` object to handle traversing the data structure
* To implement the Iterable interface, a class must `override` the iterator method
* Contained in `java.lang` package
## Iterator Interface
> Independent of `Iterable` & abstracts control away from user to allow convenience for more generic needs

> An object that implements `Iterator` interface has methods `directly` for iterating through the data structure
* To implement the Iterator interface, a class must override the `next` & `hasNext` methods.
* Also an optional `remove()` method.
* Consists of a 'cursor' variable that keeps track of the `current` data.
* `java.util` package
```sh
1. Abstract Methods
# Returns next data in iteration order that the cursor is tracking
# It then removes the cureser to the next element
public abstract T next();

# Returns whether there is more data
# Returns true when cursor is not null
public abstract boolean hasNext();

2. Non-Abstract method
# Removes the data returned by next();
# Default behaviour of throwing exception unless overriden
public void remove();
```
### Printing data using Iterator
> Implement iterator to traverse a BookList
```sh
import java.util.Iterator;

public class BookList<Book> implements Iterator<Book> {
    # Implementations omitted
    # Override the next() & hasNext() as we implemented Iterator
    public void next() {..}
    public boolean hasNext() {...}
}

# Assuming we have a BookList object called bookList:
while (bookList.hasNext()) {
    System.out.println(bookList.next());
}
```
### Printing data using Iterable
> Iterable is located in `java.lang` hence we dont have to explicitly import it
* However, to override `iterator()` method, we still need to import `Iterator`
```sh
import java.util.Iterator;

public class BookList<Book> implements Iterable<Book> {
    # Implementation omitted
    public Iterator<Book> iterator() {...}
}
# Assuming we have a BookList object called bookList:
Iterator<Book> bookIterator = bookList.iterator(); 
# 1st method: make use of iterator() method
while(bookIterator.hasNext()) {
    System.out.println(bookIterator.next());
}
# 2nd method: use for-each loop without using iterator methods
for (Book book : bookList) {
    System.out.println(book);
}
```