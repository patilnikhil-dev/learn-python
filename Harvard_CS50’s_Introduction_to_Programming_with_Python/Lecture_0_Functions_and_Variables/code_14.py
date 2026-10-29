# function which returns square of value
def square(n):
    return n * n # we can use pow(n, 2) --- predefined function for power

def main():
    x = int(input("What's x? "))

    print("x squared is", square(x))

# calling main
main()

