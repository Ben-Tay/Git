// Understanding visibility modifiers
// Public - viewable by class & inner classes, packages, subclasses, world
// Protected - viewable by class & inner classes, packages, subclasses
// Package-Private (not indicated) - viewable by class & inner classes, packages
// Private - viewable by class & inner classes
class Point {
    private double x;
    private double y;

    public Point(double x, double y) {
        // this - acts as a reference to the current class instance 

        this.x = x;
        this.y = y;
    }

    // Overloaded constructor - take 1 coord instead
    public Point(double a) {
        /* Perform constructor chaining - make use of above constructor 
            by passing in known value a as a parameter & default y value of 0 */
        this(a, 0);
        // Allows for providing only portion of object's entities w/o knowing all parameter values
    }

    public String toString() {
        return String.format("the full coordinates are (%d, %d)", this.x, this.y);
    }
    public static void main(String[] args) {
    }
}