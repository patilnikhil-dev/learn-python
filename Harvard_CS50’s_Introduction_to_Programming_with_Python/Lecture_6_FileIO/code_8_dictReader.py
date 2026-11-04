# reading csv file with headers/ columns
import csv

students = []

with open("students_with_column.csv") as file:
    reader = csv.DictReader(file, skipinitialspace = True) # reads the file

    for row in reader:
        students.append(
                {
                    "name": row["name"], 
                    "home": row["home"]
                }
            )

for student in sorted(students, key = lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")
