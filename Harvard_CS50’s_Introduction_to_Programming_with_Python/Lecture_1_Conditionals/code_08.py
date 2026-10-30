# improved version of code_07.py using pythonic way
# function to check number is even or not
def is_even(n):
    return True if n % 2 == 0 else False


# we can do like this also, because condition is returing True or False
#def is_even(n):
#    return ( n % 2 == 0)


# entry function of program
def main():
    x = int(input("What's x? "))
    
    if is_even(x):
        print("Even")
    else:
        print("Odd")

# calling main
main()

