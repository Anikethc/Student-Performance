# Main Python

# Imports
import os
import getStudentPerformance
import getNumberOfEmployeesDepartment
import getBarChartStudentPerformance
import getBarChartStudentPerformanceDouble
import getBarChartCompareStudents

# Ask User What Operation
print("Hello, welcome to Student Performance!\n")
print("What would you like to do today?\n1) Employee Information\n2) Department Information\n3) Student Councelling Information\n4) Student Performance\n5) Number of Employees in a Department\n6) Pie Chart of a Student in a Semester (Visualization)\n7) Compare 2 Semesters of a Student (Visualization)\n8) Compare 2 Students in a Semester\n")

userChoice = int(input("Enter your choice: "))

# Choices
if (userChoice == 1):
    employeeIdInput = input("\nWhat is the employee's ID? ")

    os.system("python getEmployeeInformation.py " + str(employeeIdInput))
elif (userChoice == 2):
    departmentId = input("\nWhat is the department ID? ")

    os.system("python getDepartmentInformation.py " + str(departmentId))
elif (userChoice == 3):
    studentId = input("\nWhat is the student ID? ")

    os.system("python getStudentCounsellingInformation.py " + str(studentId))
elif (userChoice == 4):
    print("\nWhat would you like to do now?\n1) View the whole performance of a student.\n2) View one semester's performance.\n3) View specific performance in a paper in a semester.\n")

    userChoice2 = int(input("Enter your choice: "))

    if (userChoice2 == 1):
        studentId = input("\nWhat is the student ID? ")

        getStudentPerformance.choice1(str(studentId))
    elif (userChoice2 == 2):
        studentId = input("\nWhat is the student ID? ")
        semester = input("Which semester (1, 2, 3, 4, 5, 6, 7, 8): ")

        getStudentPerformance.choice2(studentId, semester)
    elif (userChoice2 == 3):
        studentId = input("\nWhat is the student ID? ")
        semester = input("Which semester (1, 2, 3, 4, 5, 6, 7, 8): ")
        paper = input("What is the paper ID? ")

        getStudentPerformance.choice3(studentId, semester, paper)
    else:
        print("Enter a valid choice.")
elif (userChoice == 5):
    departmentId = input("\nEnter the department ID: ")

    getNumberOfEmployeesDepartment.employeesInDepartment(departmentId)
elif (userChoice == 6):
    studentId = input("\nEnter the student ID: ")
    semester = input("Enter the semester (1, 2, 3, 4, 5, 6, 7, 8): ")

    getBarChartStudentPerformance.barChartStudentPerformance(studentId, semester)
elif (userChoice == 7):
    studentId = input("\nEnter the student ID: ")
    semester1 = input("Enter the first semester (1, 2, 3, 4, 5, 6, 7, 8): ")
    semester2 = input("Enter the second semester (1, 2, 3, 4, 5, 6, 7, 8): ")

    getBarChartStudentPerformanceDouble.barChartStudentPerformanceDouble(studentId, semester1, semester2)
elif (userChoice == 8):
    studentId1 = input("\nEnter the first student ID: ")
    studentId2 = input("Enter the second student ID: ")
    semester = input("Enter the semester (1, 2, 3, 4, 5, 6, 7, 8): ")

    getBarChartCompareStudents.barChartCompareStudens(studentId1, studentId2, semester)
else:
    print("Enter a valid choice.")