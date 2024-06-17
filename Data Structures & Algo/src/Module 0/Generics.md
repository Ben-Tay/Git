## Why Generics?
When writing data structures - we want them to be able to contain any type of Object (String/Integer or any user defined type)
> For Instance: Consider the following Container class that stores a single value and is not using generics.
```sh
public class Container {
    private Object object;

    public void set(Object object) {
        this.object = object;
    }

    public Object get() {
        return object;
    }
}
# We can then run the following code which will set and get a value from the container:

Container c1 = new Container();
c1.set("hello");
String s = (String)c1.get();

# Notice that even if we only wanted to use c1 for String s, we'd always have to cast the result of get() to a String.

# At the same time, we have allowed our Container class to accept multiple types of objects at the same time! This can introduce errors that the compiler cannot catch. For example, if we run:

Container c2 = new Container();
c2.set("hello");
Integer i = (Integer)c2.get();

# We will get a ClassCastException. Though we can see that we cannot cast a String to an Integer, this error will only occur at runtime.
```
## Generics: The Fix
Instead, we parameterize classes based on type, allowing classes to use a `specific type throughout` as follows:
> Lets make Container a generic class

```sh
public class Container<T> {
    private T t;

    public void set(T t) {
        this.t = t;
    }

    public T get() {
        # t is of type T hence this is allowed
        return t;
    }
}
```
> Now that we declare the type parameter Container<T>, we can then use T anywhere inside our class to refer to the `same type` Modifying the 1st example from above:

```sh
Container<String> c1 = new Container<String>();
c1.set("hello");
# Removes the need for type casting as Java knows that c1.get() will always be a String 
String s = c1.get(); 

# Also, modifying the second example from above:
Container<String> c2 = new Container<String>();
c2.set("hello");
Integer i = (Integer)c2.get();

# When we try to cast the result of get() to an Integer, Java will now recognize the error at compile time.
> Java expects a string but we trying to cast to an integer so it still raises the exception
```
## Generics Syntax
> We can declare generic clasees with `one (or more)` type parameters in <> after the class name.
```sh
# Type parameters are usually a single, capital letter, usually <T>
class ArrayList<T> { ... }
```
### Declaring/Initializing Instances of Generic Classes
```sh
# Initialize instances of generic classes
ArrayList<Integer> listOne = new ArrayList<Integer>();

# Java has feature to remove explicit type argument from initialization where compiler infers type argument hence this works too:
ArrayList<String> list = new ArrayList<>();
```
## Generic Arrays
> In this course, we'll commonly need to create arrays of generic types. The following code, however, causes an error:
```
T[] backingArray = new T[10];
```
Java does not allow us to create arrays of generic types. Instead, we can do the following:
```
T[] backingArray = (T[]) new Object[10];
```
We create a new array of Objects, which we then cast to an array of T's.
### Multiple type parameters
> Some classes require multiple type parameters:
```sh
class HashMap<K, V> { ... }
# They are declared & instantiated similarly with single type parameters
HashMap<String, Integer> = new HashMap<>();
```
### Generic classes as Type parameters
> Might need to "nest" type parameters when declaring and instantiating collections of generic types:
```
ArrayList<BSTNode<T>> nodeList = new ArrayList<>();
```

Note that nodeList is an ArrayList which contains instances of the BSTNode class, which itself uses T as its type parameter.