name = input("What's your name? ")

file = open("names.txt","a")
# open names.txt
# i want to append in that file

file.write(name)
# write name in file by appending with previous value

file.close()