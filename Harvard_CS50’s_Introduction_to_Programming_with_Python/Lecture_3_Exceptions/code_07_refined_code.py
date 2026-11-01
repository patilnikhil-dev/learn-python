def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            pass
        else:
            return x
        

# main function - entry point function
def main():
    result = get_int("What's x? ")

    print(f"result is: {result}")

# call to main
main()