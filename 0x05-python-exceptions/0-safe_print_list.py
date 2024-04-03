#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0  # Initialize counter variable
    for cnt in range(x):  # Iterate up to x
        try:
            print("{}".format(my_list[cnt]), end="")  # Try to print the element at index cnt
        except IndexError:
            break  # Exit the loop if IndexError occurs
        else:
            count += 1  # Increment counter variable
    print()
    return count  # Return the counter variable
