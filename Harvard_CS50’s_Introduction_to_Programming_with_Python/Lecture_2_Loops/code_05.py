# function to print meow n times
def print_meow(n):
    for _ in range(n):
        print("Meow")


# function to take number and only return if that number is positive
def get_number():
    while True:
        n = int(input("What's number? "))        

        if n > 0:
            break # n is positive, break the loop

    return n

# entry point of code
def main():
    number = get_number()
    print_meow(number)


# call to main
main()