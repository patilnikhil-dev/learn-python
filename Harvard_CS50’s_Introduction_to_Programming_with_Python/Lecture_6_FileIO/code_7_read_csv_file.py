# In students.csv file on each line there can be more than 2 words seperated by ,
# if we use same approach like code_6 then we get 
#   ValueError : too many values to unpack (expected 2, got 3)
# So for that we need to use csv library/ module to read 

import csv

students = []

with open("students.csv") as file:
    # we used skipinitialspace = True to show python quotes marks in csv file
    # helpful for 1st line in csv file where multiple values/words are seperated by , and those words are enclosed in ""
    reader = csv.reader(file, skipinitialspace = True) # reads the file

    for name, home in reader:
        students.append(
                {
                    "name": name, 
                    "home": home
                }
            )

for student in sorted(students, key = lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")
