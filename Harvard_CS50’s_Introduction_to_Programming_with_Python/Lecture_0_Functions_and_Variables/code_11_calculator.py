x = float(input("What's x? "))
y = float(input("What's y? "))

z = x / y # using division operator 

# rounding z value
z = round(z, 2)

print(z)

# if we forget about round function we can round by using formatted string
z = x / y # getting again division to get same result

print(f"{z:.2f}")
