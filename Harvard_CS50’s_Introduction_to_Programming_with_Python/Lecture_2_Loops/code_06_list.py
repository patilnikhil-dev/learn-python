# list of students
students = ["Hermione", "Harry", "Ron"] # list of  strings

print(students) # printing list

print(students[0]) # printing first element - 0th index element of list
print(students[1]) # printing second element - 1st index element of list
print(students[2]) # printing third element - 2nd element of list

print()

# we can use for loop to iterate through list
for student in students:
    print(student, end=" ")

# using length
print(f"Length of students list : {len(students)}")

# iterating using length
for i in range(len(students)):
    print(students[i])