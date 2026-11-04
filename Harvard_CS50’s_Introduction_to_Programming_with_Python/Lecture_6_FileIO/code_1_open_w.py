name = input("What's your name? ")

file = open("names.txt", "w") 
# open names.txt and 
#   i want to do write operation in it
# NOTE: "w" opens the file and recreates the file. old content gets lost

file.write(name) # writing name in the file(names.txt)

file.close() # closing the file(names.txt)