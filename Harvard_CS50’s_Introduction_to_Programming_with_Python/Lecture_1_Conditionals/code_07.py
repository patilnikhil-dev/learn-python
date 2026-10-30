# function to check number is even or not
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

# entry function of program
def main():
    x = int(input("What's x? "))
    
    if is_even(x):
        print("Even")
    else:
        print("Odd")

# calling main
main()