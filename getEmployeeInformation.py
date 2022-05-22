# Get Employee Information

# Imports
import csv
import pandas as pd
import sys

# Variables
employeeId = sys.argv[1]

# Read CSV File
def readCSV(employeeId):
    reader = pd.read_csv("Data/Employees.csv")
    reader.set_index("Employee ID", inplace=True)

    reader2 = reader.loc[str(employeeId)]

    if (reader2.empty):
        print("Enter a valid employee ID!")
    else:
        dateOfBirth = str(reader2[0])
        dateOfJoining = str(reader2[1])
        departmentId = str(reader2[2])

        # Print the Information
        print("\033[1m" + "\nEmployee ID: " + "\033[0m" + employeeId)
        print("\033[1m" + "Date of Birth: " + "\033[0m" + dateOfBirth)
        print("\033[1m" + "Date of Joining: " + "\033[0m" + dateOfJoining)
        print("\033[1m" + "Department ID: " + "\033[0m" + departmentId)

readCSV(employeeId)