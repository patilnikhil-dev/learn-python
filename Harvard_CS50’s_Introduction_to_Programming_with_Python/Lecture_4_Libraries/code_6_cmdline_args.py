import sys

print("file name:",sys.argv[0])

try:
    print("hello, my name is",sys.argv[1])
except IndexError:
    print("missing argument.")

# without exception handling
if len(sys.argv) < 2:
    print("missing argument")
elif len(sys.argv) > 2:
    print("too many arguments")
else:
    print("hello, my name is",sys.argv[1])