import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students_inputed_file.csv", "a", newline="") as file:
    #writer = csv.writer(file) # here ordering of column matters
    #writer.writerow([name, home])
    
    # using DictWriter
    writer = csv.DictWriter(file, fieldnames=["name","home"])
    writer.writerow(
        {
            "name" : name,
            "home" : home
        }
    )
