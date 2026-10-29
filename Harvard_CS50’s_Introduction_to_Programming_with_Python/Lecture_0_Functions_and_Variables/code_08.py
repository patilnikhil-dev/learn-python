# ask use for their name
name = input("What's your name? ").strip().title()

first, last = name.split(" ") # returns array of strings

print(f"Hello, {first}")