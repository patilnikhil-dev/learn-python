# ask use for their name
name = input("What's your name? ")

# remove whitespaces from str - starting and ending spaces removed
name = name.strip()

# say hello to user
print(f"Hello, {name}")

# Capatalize user's name --> First letter of word convert into capital letter
name = name.capitalize()

# say hello to user
print(f"Hello, {name}")

# Capatalizing each word's first character 
name = name.title()

# say hello to user
print(f"Hello, {name}")


# we can combile all string function in one line at time of taking input
# eg. name = input("What's your name? ").strip().title()
