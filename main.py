list = [1, 2, 3]
new_list = [item + 1 for item in list]
print(new_list)
new_cal = [item * 2 for item in range(1, 5)]
print(new_cal)


#DICT COMPREHENSION:

names = ['Alex', 'Beth', 'Caro', 'Dave', 'Fred']
import random

student_grade = {item: random.randint(1, 100) for item in names}
print(student_grade)

passed = {name: score for (name, score) in student_grade.items() if score >= 60}
print(passed)

#DICT COMPREHENSION: with panda

import pandas

student_dict = {"students": ['angela', 'james', 'lilly'], "grades": [55, 78, 99]}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)