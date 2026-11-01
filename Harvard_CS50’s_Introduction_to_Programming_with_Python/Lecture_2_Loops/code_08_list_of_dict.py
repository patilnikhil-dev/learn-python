# list of dictiories
students = [
    {
        "name": "Harmione",
        "house": "Gryffindor",
        "patronus": "Otter"
    },
    {
        "name": "Harry",
        "house": "Gryffindor",
        "patronus": "Stag"
    },
    {
        "name": "Ron",
        "house": "Gryffindor",
        "patronus": "Jack Russell Terrier"
    },
    {
        "name": "Draco",
        "house": "Slytherin",
        "patronus": None # No value for patronus
    }
]

# iterating students
for student in students:
    print(student) # prints current indexth student dict
