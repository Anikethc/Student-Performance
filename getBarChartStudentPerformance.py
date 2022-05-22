# Get Bar Chart from Student Performance

# Imports
import csv
import pandas as pd
import sys
import matplotlib.pyplot as plt

# Bar Chart
def barChartStudentPerformance(studentId, semester):
    reader = pd.read_csv("Data/Student Performance.csv")
    reader.set_index("Student_ID", inplace=True)

    reader2 = reader.loc[studentId]
    reader2.set_index("Semester_Name", inplace=True)
    reader3 = reader2.loc[semester]

    marks1 = reader3.loc[:, "Marks"][0]
    marks2 = reader3.loc[:, "Marks"][1]
    marks3 = reader3.loc[:, "Marks"][2]
    marks4 = reader3.loc[:, "Marks"][3]
    marks5 = reader3.loc[:, "Marks"][4]
    marks6 = reader3.loc[:, "Marks"][5]
    marks7 = reader3.loc[:, "Marks"][6]

    data = {
        "Paper 1": marks1,
        "Paper 2": marks2,
        "Paper 3": marks3,
        "Paper 4": marks4,
        "Paper 5": marks5,
        "Paper 6": marks6,
        "Paper 7": marks7
    }

    paper = list(data.keys())
    marks = list(data.values())

    fig = plt.figure(figsize = (10, 5))

    plt.bar(paper, marks, color = 'blue', width = 0.4)

    plt.xlabel("The List of Papers")
    plt.ylabel("Marks")
    plt.title("Student Performance - Bar Diagram")
    plt.show()