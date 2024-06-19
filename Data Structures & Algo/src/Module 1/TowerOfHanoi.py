# Python program for Tower of Hanoi recursion
# Aim is to move disks from Source peg A to dest Peg C 
# using Peg B as an aux in the same order

def move_tower(size, src, dest, aux):
    print("BEFORE RECURSION")
    print(src) 
    print(dest)
    print(aux)
    # Base case to terminate recursion
    if size == 0:
        return True;
    # recursion case, where size is the parameter that changes to 
    # progress towards base case
    else:
        move_tower(size - 1, src, aux, dest)
        print("-----------------------")
        print(src) 
        print(dest)
        print(aux)
        print_move(src,dest)
        move_tower(size - 1, aux, dest, src)
        print("-----------------------")
        print(src) 
        print(dest)
        print(aux)

def print_move(src, dest) :
        print("move top_disk from " + src + " to " + dest)

if __name__ == "__main__":
    number_of_disks = 3  # You can change this to any number of disks
    move_tower(number_of_disks, 'A', 'C', 'B')