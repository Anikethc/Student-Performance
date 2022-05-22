# Get Department Information

# Imports
import csv
import pandas as pd
import sys

# Variables
departmentId = sys.argv[1]

# Read CSV File
def readCSV(departmentId):
    reader = pd.read_csv("Data/Departments.csv")
    reader.set_index("Department_ID", inplace=True)

    reader2 = reader.loc[departmentId]

    if (reader2.empty):
        print("Enter a valid department ID!")
    else:
        departmentName = str(reader2[0])
        dateOfEntry = str(reader2[1])

        # Print the Information
        print("\033[1m" + "\nDepartment ID: " + "\033[0m" + departmentId)
        print("\033[1m" + "Department Name: " + "\033[0m" + departmentName)
        print("\033[1m" + "Date of Entry: " + "\033[0m" + dateOfEntry)

readCSV(departmentId)