for i in [0, 1, 2]:
    print("Meow")

print("----------")

# better way do to above code
for i in range(3):
    print("Meow")

print("----------")

# if we don't care abour variable
for _ in range(3):
    print("Meow")

print("----------")

print("Meow\n" * 3, end="")