import sys

# check for errors
if len(sys.argv) < 2:
    sys.exit("missing argument")
elif len(sys.argv) > 2:
    sys.exit("too many arguments")

# print name tag
print("hello, my name is",sys.argv[1])