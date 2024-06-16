## Pass by value
```sh
public static void main(String[] args) {
    int count = 0;
    helper(count);
    System.out.println(count);
}

public static void helper(int x) {
    x = x + 1;
}
```
> Note that when we run main, we get an output of 1 instead of 1 even though count was passed into helper (why did count's value not change?)
* In this case, this is an example of `Pass By Value`. Whilst helper takes in count with a value of 0, the value will change only under the local variable in `helper` and not the value of the original variable in `main`
* This is because they reference to `2 different` locations in memory

#### Pass by Value with Objects
Let's consider the following Container class which holds a single field called item, which is of type int 
```sh
class Container {
    private int item;

    public Container(int item) {
        this.item = item;
    }

    public void setItem(int item) {
        this.item = item;
    }
    # getter method to access private item property 
    public int getItem() {
        return item;
    }
}
# Say we run the following code:
public static void main(String[] args) {
    # Step 1: create new Container named count
    Container count = new Container(0);     
    # Step 2: call the helper method on count
    helper(count);                         
    # Step 4: print the value of count's item (0 here)
    System.out.println(count.getItem());  
}

public static void helper(Container x) {
    # Step 3: create a new object reference with its item 
    #         set to x's item + 1
    x = new Container(x.getItem() + 1); 
}
```
* Outcome of this would still be 0 rather than 1, because count itself is `NOT A` Container object but rather stores a value that `points` to a Container object. Here, count is a `reference` variable
## Pass by Reference
* The helper method takes in the reference for what was passed in. Changing its value will change the value of both the local variable and the original variable (because they reference the same location in memory).
* However, Java is a `Pass by value` language hence the output here does not change

#### Pass by reference with primitives
* Consider this - what if we really want to store the value given by our "helper method"

By modifying original example
```sh
public static void main(String[] args) {
    # Step 1: create a new int named count
    int count = 0;     
    # Step 2: call helper on count       
    # Step 5: assign the returned value to count (to update its value)     
    count = helper(count);             
    # Step 6: print the value of count
    System.out.println(count);          
}

public static int helper(int x) {
    # Step 3: increment the value of x
    x = x + 1;                 
    # Step 4: return the value of x        
    return x;                           
}
```
> Output here would be 1 instead of 0, because we actually updated the value of count by returning the value from the helper method into main and reassigning that value into count
#### Pass by reference with Objects
Let's also consider a scenario where we'd like to modify an object. Here's a modification of the second example (and we'll use the Container class from earlier):

```sh
public static void main(String[] args) {
    # Step 1: create new Container named count
    Container count = new Container(0);     
    # Step 2: call helper on count
    helper(count);                
    # Step 4: print the value of count          
    System.out.println(count.getItem());    
}

public static void helper(Container x) {
    # Step 3: set x's item to x's item + 1, modifying the original objec
    x.setItem(x.getItem() + 1);             t
}
```
* In this case the original container object's item property would be set to the new value of 1 as well
* (Notice that our helper method is void rather than int because we don't have to return anything, and that we `don't` reassign count in the main method)
> Just to point out, this method is possible cuz we didnt use `private final` on the item property of Container, else it wouldnt be allowed (typically we do not want outsiders to be able to change object's values) to be in line with encapsulation principle
