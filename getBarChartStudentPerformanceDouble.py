# Get Bar Chart from Student Performance - Double

# Imports
import csv
import pandas as pd
import sys
import matplotlib.pyplot as plt
import numpy as np

# Bar Chart
def barChartStudentPerformanceDouble(studentId, semester1, semester2):
    reader = pd.read_csv("Data/Student Performance.csv")
    reader.set_index("Student_ID", inplace=True)

    reader2 = reader.loc[studentId]
    reader2.set_index("Semester_Name", inplace=True)

    reader3 = reader2.loc[semester1]
    reader4 = reader2.loc[semester2]

    x_axis = ["Paper 1", "Paper 2", "Paper 3", "Paper 4", "Paper 5", "Paper 6", "Paper 7"]
    sem1 = [reader3.loc[:, "Marks"][0], reader3.loc[:, "Marks"][1], reader3.loc[:, "Marks"][2], reader3.loc[:, "Marks"][3], reader3.loc[:, "Marks"][4], reader3.loc[:, "Marks"][5], reader3.loc[:, "Marks"][6]]
    sem2 = [reader4.loc[:, "Marks"][0], reader4.loc[:, "Marks"][1], reader4.loc[:, "Marks"][2], reader4.loc[:, "Marks"][3], reader4.loc[:, "Marks"][4], reader4.loc[:, "Marks"][5], reader4.loc[:, "Marks"][6]]

    x_x_axis = np.arange(len(x_axis))

    fig = plt.figure(figsize = (10, 5))

    plt.bar(x_x_axis - 0.2, sem1, 0.4, label = "First Semester You Selected", color = "blue")
    plt.bar(x_x_axis + 0.2, sem2, 0.4, label = "Second Semester You Selected", color = "maroon")

    plt.xlabel("Both the Semesters")
    plt.ylabel("Marks")
    plt.title("Student Performance - Bar Chart (Double)")
    plt.legend()
    plt.show()