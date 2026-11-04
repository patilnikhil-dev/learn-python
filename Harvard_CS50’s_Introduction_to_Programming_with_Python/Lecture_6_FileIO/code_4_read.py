with open("names.txt", "r") as file:
    lines = file.readlines() # gives total lines

for line in lines:
    print(line.rstrip())

print("-------")

# enhanced code
with open("names.txt", "r") as file:
    for line in file:
        print("hello,",line.rstrip())

print("-------")

# printing after sorting content in file
with open("names.txt", "r") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())