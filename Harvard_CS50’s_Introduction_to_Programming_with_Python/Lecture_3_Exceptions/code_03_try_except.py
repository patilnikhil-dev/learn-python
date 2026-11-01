try:
    x = int(input("What's x? "))
    print(f"x is: {x}")
except ValueError:
    print("x is not an integer")

# above code will work for int type value 
# what if user entered string value, program gets terminated automatically with error
    # ValueError: invalid literal for int() with base 10

    # in above code we are handling ValueError
