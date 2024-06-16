## Value vs Reference Equality
### Reference Equality
* Also known as the `==` operator 
* Used to check if 2 objects are the exact same object in memory (occupy same space in memory)
* Mainly used to check if an object is `null` (empty/exceptional object)

> Null checking is usually done through `==`
#### Null Checking
* Done to check that the input to a method is valid, or to check for an exceptional situation.
* If you try to invoke a method or field of a `null` object, then the code will throw a `NullPointerException`, for instance `.equals()`.

```sh
String nullObject = null;
String normalObject = "normal";
# The correct way of checking if an object is null
nullObject == null;   // => true
normalObject == null; // => false

# The String class checks if argument is null, so it will throw NPE.  
# If a .equals() method doesn't check for a null argument, it will crash and throw a NPE.
# Here, we compare the value stored in normalObject to the values null, and nullObject
normalObject.equals(null);       // => false
normalObject.equals(nullObject); // => false

// However, here we invoking the .equals() method on a null object stored in nullOject
# This will cause a NPE to be thrown, regardless of the parameter in the .equals() method
nullObject.equals(normalObject); => causes NullPointerException
nullObject.equals(null);  => causes NullPointerException
```


### Value Equality
* Checks if 2 objects are equal based on the user's specific use case and design
* The `.equals()` method has a default implementation where `a.equals(b)` is the same as `a == b`
* To override its behavior, the user would have to override the `.equals()` method of the object and ideally its `.hashcode()` method as well

## Primitive Types
* Primitive Types such as `int, long, double, char, boolean etc` do not extend the Object class as most types do
* Hence, they do not have the `.equals()` method, and one must use `==` to check for equality (no differentiation between reference and value equality here)

```
int one1 = 1;
int one2 = 1;
int two1 = 2;
int two2 = 2;

one1 == one2; // => true
two1 == two2; // => true
one1 == two1; // => false
one1 == 1;    // => true
two1 == 2;    // => true
```
## String Literals
```sh
# Literals an easy way to create strings by putting it in quotes - assigning a constant to a String pool
String literal = "This is a string"
# Strings also have their own class that extends from Object and has .equals() method
String object = new String("This is a string.");
String unequal = "Nope.";

# Using == On Value Equal Strings
# literal is not == object as they DO NOT occupy same space in memory despite the same value
literal == object;  // => false 
literal == "This is a string."; // => true

// Using .equals() On Value Equal Strings
# Whereas, equals() only checks for the value hence true
literal.equals(object);    // => true
object.equals(literal);   // => true
```
## Wrapper Objects
* Just like how String literals & String objects are related to operate, we can do the same for primitive types using wrapper Objects
* `int => Integer, double => Double` etc
* Very useful because sometimes we need Objects for generic typings. Eg: To make a collection of Ints, we need to add `Integer` objects rather than primitive ints
* Such things are not known cause Java has `autoboxing/autounboxing` to streamline the experience

```sh
Integer primitive = 1;
Integer object = new Integer(1);
Integer unequal = 2;

# Using == On Value Equal Integers
primitive == object;        // => false
primitive == 1;             // => true
object == 1;                // => true
object == new Integer(1);   // => false

# Using .equals() On Value Equal Integers
primitive.equals(object);                 // => true
object.equals(primitive);                 // => true
primitive.equals(1);                      // => true
object.equals(1);                         // => true
(new Integer(1)).equals(1);               // => true
(new Integer(1)).equals(new Integer(1));  // => true

# Using == and .equals() on Unequal Integers
primitive == unequal;        // => false
object == unequal;           // => false
primitive.equals(unequal);   // => false
object.equals(unequal);      // => false

# If run, the following do not work since 1 is considered a primitive without autoboxing
1.equals(primitive);  // causes Error
1.equals(1);          // causes Error
``` 
## Use Case
* Most of the time, the use case for using `==` and `.equals()` will coincide for instance in comparing numbers
* But they may differ at times in following cases for instance:

1. We want to retrieve the records of all patients with the name "John Doe".
    * For this task, we would not be bothered with memory equality (==) but rather the information the memory holds (equals())
    
2. A patient has asked to have their profile removed from the system. (Note: This is usually not possible in the real world, but let's consider it anyway.)
    * Unless there is a Patient ID for uniqueness checking, we would make use of memory equality (==) to determine where in memory the patient's details are stored

## What About in This Course?
In this course, unless you are checking for nulls, you will overwhelmingly be using the .equals() method for value equality rather than using ==.

For perspective, you should imagine yourself as the writer of the Collections classes in Java such as ArrayList, LinkedList, etc. If you are working with data that the data structure is storing, then you should use value equality because the user is the one defining equality.

If the user wanted reference equality, they can simply not override the default implementation of .equals(). This approach, of assuming value equality, gives your code the most flexibility with the user.