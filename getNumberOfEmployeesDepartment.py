# Get Number of Employees in a Department

# Imports
import csv
import pandas as pd
import sys

# Number of Employees
def employeesInDepartment(departmentId):
    reader = pd.read_csv("Data/Employees.csv")
    reader.set_index("Department_ID", inplace=True)

    reader2 = reader.loc[departmentId]

    if (reader2.empty):
        print("Please enter a valid department ID!")
    else:
        print("\033[1m" + "Employees in Department: " + "\033[0m" + str(len(reader2.index)))