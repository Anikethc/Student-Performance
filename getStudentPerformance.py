# Get Student Councelling Information

# Imports
import csv
import pandas as pd
import sys

# Choice 1
def choice1(studentId):
    reader = pd.read_csv("Data/Student Performance.csv")
    reader.set_index("Student_ID", inplace=True)

    reader2 = reader.loc[studentId]

    if (reader2.empty):
        print("Enter valid details!")
    else:
        print(reader2)

# Choice 2
def choice2(studentId, semester):
    reader = pd.read_csv("Data/Student Performance.csv")
    reader.set_index("Student_ID", inplace=True)

    reader2 = reader.loc[studentId]
    reader2.set_index("Semester_Name", inplace=True)
    reader3 = reader2.loc[semester]

    if (reader3.empty):
        print("Enter valid details!")
    else:
        print(reader3)

# Choice 3
def choice3(studentId, semester, paper):
    reader = pd.read_csv("Data/Student Performance.csv")
    reader.set_index("Student_ID", inplace=True)

    reader2 = reader.loc[studentId]
    reader2.set_index("Semester_Name", inplace=True)
    reader3 = reader2.loc[semester]
    reader3.set_index("Paper_ID", inplace=True)
    reader4 = reader3.loc[paper]

    if (reader4.empty):
        print("Enter valid details!")
    else:
        print(reader4)