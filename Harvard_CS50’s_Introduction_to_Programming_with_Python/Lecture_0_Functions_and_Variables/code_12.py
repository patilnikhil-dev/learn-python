# making our own function
def hello(to= "World"):
    print("Hello,",to)


# calling hello function
hello() 
    # here we get Hello, World in output. 
    #   because we have not passed any arguments and hence
    #       parameters default value is used

    
# asking user for his name
name = input("What's your name? ")

# calling hello function
# passing argument to function while calling
hello(name)