# dictionary of students
students = {
    "Herminoe" : "Gryffindor",
    "Harry" : "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco" : "Slytherin"
}

# printing dict of students
print(students)


# printing using key
print(f"Data present at key Don : {students["Ron"]}")

print()

# iterating dict by using for loop
for student in students:
    print(student, students[student], sep=" - ") # prints current key with its associated value