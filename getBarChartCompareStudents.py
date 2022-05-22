# Get Bar Chart - Compare Students

# Imports
import csv
import pandas as pd
import sys
import matplotlib.pyplot as plt
import numpy as np

# Bar Chart
def barChartCompareStudens(studentId1, studentId2, semester):
    reader = pd.read_csv("Data/Student Performance.csv")
    reader.set_index("Semester_Name", inplace=True)
    
    reader2 = reader.loc[semester]
    reader2.set_index("Student_ID", inplace=True)
    reader4 = reader2.loc[studentId1]

    reader5 = reader.loc[semester]
    reader5.set_index("Student_ID", inplace=True)
    reader6 = reader5.loc[studentId2]

    x_axis = ["Paper 1", "Paper 2", "Paper 3", "Paper 4", "Paper 5", "Paper 6", "Paper 7"]
    student1 = [reader4.loc[:, "Marks"][0], reader4.loc[:, "Marks"][1], reader4.loc[:, "Marks"][2], reader4.loc[:, "Marks"][3], reader4.loc[:, "Marks"][4], reader4.loc[:, "Marks"][5], reader4.loc[:, "Marks"][6]]
    student2 = [reader6.loc[:, "Marks"][0], reader6.loc[:, "Marks"][1], reader6.loc[:, "Marks"][2], reader6.loc[:, "Marks"][3], reader6.loc[:, "Marks"][4], reader6.loc[:, "Marks"][5], reader6.loc[:, "Marks"][6]]

    x_x_axis = np.arange(len(x_axis))

    fig = plt.figure(figsize = (10, 5))

    plt.bar(x_x_axis - 0.2, student1, 0.4, label = "Student - 1", color = "blue")
    plt.bar(x_x_axis + 0.2, student2, 0.4, label = "Student - 2", color = "maroon")

    plt.xlabel("Both the Students")
    plt.ylabel("Marks")
    plt.title("Student Performance - Bar Chart (Comparision)")
    plt.legend()
    plt.show()