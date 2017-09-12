#!/bin/python3

import sys
import math

def roundup(x):
    return int(math.ceil(x / 5.0) * 5)

def solve(grades):
    # Complete this function
    for i in range(n):
        grade = grades[i]
        roundGrade = roundup(grades[i])
        if (roundGrade - grade) < 3 and grade > 37: grades[i] = roundGrade
    return(grades)

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
