import json
import os

#ToDos
#   1.Limit the grades
#   2.Order the list
#   3.Grade should be a number
#   4.
if os.path.isfile('./gc_grades.json')==True:
        with open('gc_grades.json') as data_file2:
            course2 = json.load(data_file2)
        grades2 = course2["mygrades"]
        print(grades2)

with open('gc_setup.json') as data_file:
    course = json.load(data_file)

grades = course["course_setup"]["grade_breakdown"]

current_grades = {"mygrades": {}}

for key in grades:
    print(grades[key])
    current_grades["mygrades"][key] = input("What is your Current Grade for: " + key + " . Please insert -1 if you don't have a grade yet")

print (json.dumps(current_grades))
file = open("gc_grades.json", "w")
file.write(json.dumps(current_grades))
file.close()

curr_grade = 0
for key in current_grades["mygrades"]:
    if current_grades["mygrades"][key] != -1:
        calc_grade = int(current_grades["mygrades"][key]) * grades[key] / 100
        curr_grade = curr_grade + calc_grade

print (curr_grade)

