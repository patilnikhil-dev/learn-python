# function to print square with provided size
def print_square(size):

    for row in range(size):
        for col in range(size):
            print("#", end="")

        print() # for going to next line 


# smart approach for print_square to print square
def smart_print_square(size):
    for i in range(size):
        print("#" * size)

# entry point function
def main():
    # call to print_square
    print_square(3)

    print()

    # call to smart_print_square
    smart_print_square(3)

# call to main
main() 
