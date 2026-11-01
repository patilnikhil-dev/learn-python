def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            return x
        

# main function - entry point function
def main():
    result = get_int()

    print(f"result is: {result}")

# call to main
main()