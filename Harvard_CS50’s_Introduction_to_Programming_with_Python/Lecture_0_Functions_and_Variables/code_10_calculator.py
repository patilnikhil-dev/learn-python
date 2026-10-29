x = float(input("What's x? "))
y = float(input("What's y? "))

z = x + y

# rounding z value
z = round(z)

print(z) # we get value of z rounded to nearest int value

# what if we want only 2 numbers after decimal point
z = x + y # calculated to get result again

z = round(z, 2) # rounding z and allowing only two numbers after decimal point

print(z)